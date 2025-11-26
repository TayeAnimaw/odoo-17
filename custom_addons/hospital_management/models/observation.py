from odoo import models, fields

class HospitalObservation(models.Model):
    _name = 'hospital.observation'
    _description = 'Clinical Observation'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    medical_record_id = fields.Many2one('hospital.medical_record', string='Medical Record')
    observation_date = fields.Datetime(string='Observation Date', default=fields.Datetime.now, required=True)
    concept = fields.Char(string='Concept', required=True)  # e.g., 'Blood Pressure', 'Temperature'
    value = fields.Char(string='Value', required=True)  # Could be text, number, etc.
    unit = fields.Char(string='Unit')  # e.g., 'mmHg', 'Celsius'
    notes = fields.Text(string='Notes')