from odoo import models, fields, api
from datetime import datetime

class Poliza(models.Model):
    _name = 'vzla.poliza'
    _description = 'Póliza de Seguro'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Número de Póliza', required=True, tracking=True)
    tomador_id = fields.Many2one('vzla.tomador', string='Tomador', required=True)
    fecha_inicio = fields.Datetime(string='Fecha de Inicio')
    fecha_fin = fields.Datetime(string='Fecha de Fin')
    tipo_pago = fields.Selection([
        ('contado', 'Contado'),
        ('financiado', 'Financiado')
    ], string='Tipo de Pago')
    sucursal = fields.Char(string='Sucursal')
    canal_venta = fields.Char(string='Canal de Venta')
    frecuencia_pago = fields.Selection([
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('semestral', 'Semestral'),
        ('anual', 'Anual')
    ], string='Frecuencia de Pago')
    codigo_intermediario = fields.Char(string='Código de Intermediario')
    participacion = fields.Float(string='Participación')
    moneda = fields.Selection([
        ('VES', 'Bolívares'),
        ('USD', 'Dólares')
    ], string='Moneda')
    
    vehiculo_id = fields.One2many('vzla.vehiculo', 'poliza_id', string='Vehículo')
    cobertura_ids = fields.One2many('vzla.cobertura', 'poliza_id', string='Coberturas')
    recibo_ids = fields.One2many('vzla.recibo', 'poliza_id', string='Recibos')

    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('vigente', 'Vigente'),
        ('vencida', 'Vencida'),
        ('cancelada', 'Cancelada')
    ], string='Estado', default='borrador', tracking=True)
    
    prima_total = fields.Float(string='Prima Total', compute='_compute_prima_total', store=True)
    cantidad_recibos = fields.Integer(string='Cantidad de Recibos', compute='_compute_cantidad_recibos')
    dias_vencimiento = fields.Integer(string='Días para Vencimiento', compute='_compute_dias_vencimiento')
    color = fields.Integer(string='Color', compute='_compute_color')

    @api.depends('recibo_ids')
    def _compute_prima_total(self):
        for record in self:
            record.prima_total = sum(recibo.monto for recibo in record.recibo_ids)

    @api.depends('recibo_ids')
    def _compute_cantidad_recibos(self):
        for record in self:
            record.cantidad_recibos = len(record.recibo_ids)

    @api.depends('fecha_fin')
    def _compute_dias_vencimiento(self):
        for record in self:
            if record.fecha_fin:
                dias = (record.fecha_fin - fields.Datetime.now()).days
                record.dias_vencimiento = dias
            else:
                record.dias_vencimiento = 0

    @api.depends('dias_vencimiento')
    def _compute_color(self):
        for record in self:
            if record.state == 'cancelada':
                record.color = 1  # Rojo
            elif record.state == 'vencida':
                record.color = 2  # Naranja
            elif record.dias_vencimiento <= 30:
                record.color = 3  # Amarillo
            else:
                record.color = 4  # Verde

    def action_confirmar(self):
        self.ensure_one()
        self.state = 'vigente'

    def action_cancelar(self):
        self.ensure_one()
        self.state = 'cancelada'

    def generar_carnet_rc(self):
        self.ensure_one()
        return self.env.ref('vzla.action_report_carnet_rc').report_action(self)

    def generar_poliza_pdf(self):
        self.ensure_one()
        return self.env.ref('vzla.action_report_poliza').report_action(self)

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code('vzla.poliza.sequence')
        return super(Poliza, self).create(vals)