from odoo import models, fields, api

class HospitalInvoice(models.Model):
    _name = 'hospital.invoice'
    _description = 'Hospital Invoice'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    invoice_date = fields.Date(string='Invoice Date', default=fields.Date.today, required=True)
    total_amount = fields.Float(string='Total Amount', required=True)
    paid_amount = fields.Float(string='Paid Amount', default=0.0)
    balance = fields.Float(string='Balance', compute='_compute_balance', store=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    description = fields.Text(string='Description')
    line_ids = fields.One2many('hospital.invoice.line', 'invoice_id', string='Invoice Lines')

    @api.depends('total_amount', 'paid_amount')
    def _compute_balance(self):
        for record in self:
            record.balance = record.total_amount - record.paid_amount

class HospitalInvoiceLine(models.Model):
    _name = 'hospital.invoice.line'
    _description = 'Invoice Line'

    invoice_id = fields.Many2one('hospital.invoice', string='Invoice', required=True)
    description = fields.Char(string='Description', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    unit_price = fields.Float(string='Unit Price', required=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.depends('quantity', 'unit_price')
    def _compute_total(self):
        for record in self:
            record.total = record.quantity * record.unit_price