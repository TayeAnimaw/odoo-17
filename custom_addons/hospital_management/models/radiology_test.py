from odoo import models, fields

class HospitalRadiologyTest(models.Model):
    _name = 'hospital.radiology_test'
    _description = 'Radiology Test'

    medical_record_id = fields.Many2one('hospital.medical_record', string='Medical Record', required=True)
    test_name = fields.Char(string='Test Name', required=True)
    test_date = fields.Datetime(string='Test Date', required=True)
    result = fields.Text(string='Result')
    status = fields.Selection([
        ('ordered', 'Ordered'),
        ('completed', 'Completed'),
        ('pending', 'Pending')
    ], string='Status', default='ordered')
    notes = fields.Text(string='Notes')