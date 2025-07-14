from odoo import models, fields, api

class Cobertura(models.Model):
    _name = 'vzla.cobertura'
    _description = 'Coberturas de la Póliza'

    poliza_id = fields.Many2one('vzla.poliza', string='Póliza', required=True)
    name = fields.Selection([
        ('datos_personal', 'Datos Personales'),
        ('exceso_limite', 'Exceso Límite'),
        ('muerte_invalidez', 'Muerte e Invalidez'),
        ('danos_cosas', 'Daños a Cosas'),
        ('defensa_penal', 'Defensa Penal'),
        ('gastos_medicos', 'Gastos Médicos'),
        ('gastos_funerarios', 'Gastos Funerarios')
    ], string='Tipo de Cobertura', required=True)
    suma_asegurada = fields.Float(string='Suma Asegurada')
    prima = fields.Float(string='Prima')
    deducible = fields.Float(string='Deducible')
    activa = fields.Boolean(string='Activa', default=True)