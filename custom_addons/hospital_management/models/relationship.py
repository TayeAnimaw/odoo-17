from odoo import models, fields

class HospitalRelationship(models.Model):
    _name = 'hospital.relationship'
    _description = 'Patient Relationship'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    related_patient_id = fields.Many2one('hospital.patient', string='Related Patient', required=True)
    relationship_type = fields.Selection([
        ('parent', 'Parent'),
        ('child', 'Child'),
        ('spouse', 'Spouse'),
        ('sibling', 'Sibling'),
        ('guardian', 'Guardian'),
        ('other', 'Other')
    ], string='Relationship Type', required=True)
    notes = fields.Text(string='Notes')