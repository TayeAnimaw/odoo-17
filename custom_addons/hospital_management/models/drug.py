from odoo import models, fields

class HospitalDrug(models.Model):
    _name = 'hospital.drug'
    _description = 'Hospital Drug'

    name = fields.Char(string='Drug Name', required=True)
    generic_name = fields.Char(string='Generic Name')
    dosage_form = fields.Char(string='Dosage Form')  # e.g., Tablet, Injection
    strength = fields.Char(string='Strength')
    stock_quantity = fields.Integer(string='Stock Quantity', default=0)
    reorder_level = fields.Integer(string='Reorder Level', default=10)
    unit_price = fields.Float(string='Unit Price')
    expiry_date = fields.Date(string='Expiry Date')