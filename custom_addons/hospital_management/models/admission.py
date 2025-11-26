from odoo import models, fields

class HospitalAdmission(models.Model):
    _name = 'hospital.admission'
    _description = 'Hospital Admission'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    bed_id = fields.Many2one('hospital.bed', string='Bed', required=True)
    admission_date = fields.Datetime(string='Admission Date', default=fields.Datetime.now, required=True)
    discharge_date = fields.Datetime(string='Discharge Date')
    status = fields.Selection([
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged')
    ], string='Status', default='admitted')
    reason = fields.Text(string='Reason for Admission')
    notes = fields.Text(string='Notes')