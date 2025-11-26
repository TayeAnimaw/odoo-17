from odoo import models, fields

class HospitalLocation(models.Model):
    _name = 'hospital.location'
    _description = 'Hospital Location'

    name = fields.Char(string='Location Name', required=True)
    type = fields.Selection([
        ('ward', 'Ward'),
        ('room', 'Room'),
        ('department', 'Department'),
        ('clinic', 'Clinic')
    ], string='Type', required=True)
    parent_id = fields.Many2one('hospital.location', string='Parent Location')
    description = fields.Text(string='Description')
    beds_ids = fields.One2many('hospital.bed', 'location_id', string='Beds')