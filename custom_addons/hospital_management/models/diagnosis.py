from odoo import models, fields

class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    medical_record_id = fields.Many2one('hospital.medical_record', string='Medical Record', required=True)
    icd_code = fields.Char(string='ICD Code')
    diagnosis_name = fields.Char(string='Diagnosis Name', required=True)
    certainty = fields.Selection([
        ('confirmed', 'Confirmed'),
        ('presumed', 'Presumed'),
        ('rule_out', 'Rule Out')
    ], string='Certainty', default='confirmed')
    notes = fields.Text(string='Notes')