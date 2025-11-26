from odoo import models, fields

class HospitalBed(models.Model):
    _name = 'hospital.bed'
    _description = 'Hospital Bed'

    name = fields.Char(string='Bed Number', required=True)
    location_id = fields.Many2one('hospital.location', string='Location')
    status = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance')
    ], string='Status', default='available')
    patient_id = fields.Many2one('hospital.patient', string='Current Patient')