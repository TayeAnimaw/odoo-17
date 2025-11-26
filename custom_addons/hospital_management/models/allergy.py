from odoo import models, fields

class HospitalAllergy(models.Model):
    _name = 'hospital.allergy'
    _description = 'Patient Allergy'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    allergen = fields.Char(string='Allergen', required=True)
    reaction = fields.Text(string='Reaction')
    severity = fields.Selection([
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe')
    ], string='Severity', default='mild')
    notes = fields.Text(string='Notes')