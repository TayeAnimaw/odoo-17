from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Full Name', required=True)
    specialization = fields.Char(string='Specialization')
    license_number = fields.Char(string='License Number')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    department_id = fields.Many2one('hospital.department', string='Department')
    user_id = fields.Many2one('res.users', string='Related User')
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')