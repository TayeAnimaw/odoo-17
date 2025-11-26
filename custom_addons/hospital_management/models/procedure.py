from odoo import models, fields

class HospitalProcedure(models.Model):
    _name = 'hospital.procedure'
    _description = 'Medical Procedure'

    name = fields.Char(string='Procedure Name', required=True)
    code = fields.Char(string='Procedure Code')
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')
    duration = fields.Integer(string='Duration (minutes)')
    medical_record_id = fields.Many2one('hospital.medical_record', string='Medical Record')
    procedure_date = fields.Datetime(string='Procedure Date', default=fields.Datetime.now)
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='scheduled')
    notes = fields.Text(string='Notes')