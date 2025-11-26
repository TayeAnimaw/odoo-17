from odoo import models, fields

class HospitalProgram(models.Model):
    _name = 'hospital.program'
    _description = 'Hospital Program'

    name = fields.Char(string='Program Name', required=True)
    description = fields.Text(string='Description')
    patient_ids = fields.Many2many('hospital.patient', string='Patients')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='active')