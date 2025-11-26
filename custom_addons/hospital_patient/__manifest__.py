{
    'name': 'Hospital Patient',
    'version': '1.0',
    'summary': 'Manage hospital patients',
    'description': 'Patient registration and management module for hospital',
    'category': 'Hospital',
    'author': 'Taye Animaw',
    'depends': ['base'],  # Only depends on base module for now
    'data': [
        'views/patient_view.xml',
    ],
    'installable': True,
    'application': True,
}
