from odoo import models, fields

class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Prescription'

    medical_record_id = fields.Many2one('hospital.medical_record', string='Medical Record', required=True)
    drug_id = fields.Many2one('hospital.drug', string='Drug', required=True)
    dosage = fields.Char(string='Dosage')
    frequency = fields.Char(string='Frequency')
    duration = fields.Char(string='Duration')
    quantity = fields.Integer(string='Quantity')
    instructions = fields.Text(string='Instructions')
    dispensed = fields.Boolean(string='Dispensed', default=False)