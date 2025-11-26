from odoo import models, fields

class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical_record'
    _description = 'Medical Record'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    visit_date = fields.Datetime(string='Visit Date', required=True)
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment')
    prescription_ids = fields.One2many('hospital.prescription', 'medical_record_id', string='Prescriptions')
    lab_test_ids = fields.One2many('hospital.lab_test', 'medical_record_id', string='Lab Tests')
    notes = fields.Text(string='Notes')