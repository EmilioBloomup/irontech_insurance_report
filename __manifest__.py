{
    'name': "irontech_insurance_report",
    'depends': ['base', 'insurance_app'],
    'application': False,
    'description': """
        Aggiunge stampa di rapporto danni assicurazione   
    """,
    'data': [
        'security/ir.model.access.csv',
        'report/insurance_report_menu.xml',
        'report/insurance_report_template.xml'
    ]
}