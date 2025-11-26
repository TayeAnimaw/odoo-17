from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    patient_id = fields.Char(string='Patient ID', required=True, copy=False, readonly=True, default=lambda self: self._generate_patient_id())
    name = fields.Char(string='Full Name', required=True)
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    emergency_contact = fields.Char(string='Emergency Contact')
    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ], string='Blood Type')
    allergies = fields.Text(string='Allergies')
    medical_history = fields.Text(string='Medical History')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    medical_record_ids = fields.One2many('hospital.medical_record', 'patient_id', string='Medical Records')
    admission_ids = fields.One2many('hospital.admission', 'patient_id', string='Admissions')
    allergy_ids = fields.One2many('hospital.allergy', 'patient_id', string='Allergies')
    relationship_ids = fields.One2many('hospital.relationship', 'patient_id', string='Relationships')

    def _generate_patient_id(self):
        return self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'

    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                today = fields.Date.today()
                record.age = today.year - record.dob.year - ((today.month, today.day) < (record.dob.month, record.dob.day))
            else:
                record.age = 0
