from odoo import models, fields, api

class Recibo(models.Model):
    _name = 'vzla.recibo'
    _description = 'Recibos de Póliza'

    poliza_id = fields.Many2one('vzla.poliza', string='Póliza', required=True)
    name = fields.Char(string='Número de Recibo', required=True)
    fecha_inicio = fields.Datetime(string='Fecha de Inicio')
    fecha_fin = fields.Datetime(string='Fecha de Fin')
    tipo_movimiento = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('renovacion', 'Renovación'),
        ('endoso', 'Endoso')
    ], string='Tipo de Movimiento')
    sucursal = fields.Char(string='Sucursal')
    canal_venta = fields.Char(string='Canal de Venta')
    frecuencia_pago = fields.Selection([
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('semestral', 'Semestral'),
        ('anual', 'Anual')
    ], string='Frecuencia de Pago')
    total_pagar = fields.Float(string='Total a Pagar')
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('emitido', 'Emitido'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='borrador')