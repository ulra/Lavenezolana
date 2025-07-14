from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'vzla.vehiculo'
    _description = 'Vehículo Asegurado'

    poliza_id = fields.Many2one('vzla.poliza', string='Póliza', required=True)
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    puestos = fields.Integer(string='Puestos')
    version = fields.Char(string='Versión')
    ano = fields.Integer(string='Año')
    tipo = fields.Selection([
        ('particular', 'Particular'),
        ('comercial', 'Comercial'),
        ('carga', 'Carga'),
        ('otro', 'Otro')
    ], string='Tipo')
    placa = fields.Char(string='Placa', required=True)
    serial_motor = fields.Char(string='Serial de Motor')
    uso = fields.Selection([
        ('privado', 'Privado'),
        ('publico', 'Público'),
        ('comercial', 'Comercial')
    ], string='Uso')
    color = fields.Char(string='Color')
    serial_carroceria = fields.Char(string='Serial de Carrocería')
    otros = fields.Text(string='Otros Detalles')