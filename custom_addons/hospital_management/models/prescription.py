from odoo import models, fields

class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Prescription'

    medical_record_id = fields.Many2one('hospital.medical_record', string='Medical Record', required=True)
    medication = fields.Char(string='Medication', required=True)
    dosage = fields.Char(string='Dosage')
    frequency = fields.Char(string='Frequency')
    duration = fields.Char(string='Duration')
    instructions = fields.Text(string='Instructions')