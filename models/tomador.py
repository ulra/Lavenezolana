from odoo import models, fields, api

class TomadorSeguro(models.Model):
    _name = 'vzla.tomador'
    _description = 'Tomador de Seguro'

    name = fields.Char(string='Tomador', required=True)
    cedula_rif = fields.Char(string='Cédula/RIF', required=True)
    asegurado = fields.Char(string='Asegurado')
    asegurado_cedula_rif = fields.Char(string='Cédula/RIF Asegurado')
    direccion = fields.Text(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    
    poliza_ids = fields.One2many('vzla.poliza', 'tomador_id', string='Pólizas')