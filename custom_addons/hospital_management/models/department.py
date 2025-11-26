from odoo import models, fields

class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Hospital Department'

    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Department Code')
    description = fields.Text(string='Description')
    head_id = fields.Many2one('hospital.doctor', string='Department Head')
    doctor_ids = fields.One2many('hospital.doctor', 'department_id', string='Doctors')