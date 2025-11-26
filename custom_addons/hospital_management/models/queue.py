from odoo import models, fields

class HospitalQueue(models.Model):
    _name = 'hospital.queue'
    _description = 'Patient Queue'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    queue_number = fields.Integer(string='Queue Number', required=True)
    status = fields.Selection([
        ('waiting', 'Waiting'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='waiting')
    check_in_time = fields.Datetime(string='Check-in Time', default=fields.Datetime.now)
    called_time = fields.Datetime(string='Called Time')
    notes = fields.Text(string='Notes')