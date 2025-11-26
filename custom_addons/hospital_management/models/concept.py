from odoo import models, fields

class HospitalConcept(models.Model):
    _name = 'hospital.concept'
    _description = 'Hospital Concept'

    name = fields.Char(string='Concept Name', required=True)
    description = fields.Text(string='Description')
    datatype = fields.Selection([
        ('text', 'Text'),
        ('numeric', 'Numeric'),
        ('coded', 'Coded'),
        ('date', 'Date')
    ], string='Data Type', default='text')
    unit = fields.Char(string='Unit')
    parent_id = fields.Many2one('hospital.concept', string='Parent Concept')
    child_ids = fields.One2many('hospital.concept', 'parent_id', string='Child Concepts')