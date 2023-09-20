# -*- coding: utf-8 -*-

{
    'name': 'GES2 Logistics',
    'summary': """
        GES2 Logistics
    """,
    'version': '1.6',
    'author': 'GES Logistics',
    'category': 'freight',
    'company': 'GES Logistics',
    'maintainer': 'GES Logistics',
    'website': "https://www.geslogistics.com",
    'depends': ['crm'],
    'data': [
        # Views
        'views/crm_views.xml',
        # Security
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
    'license': 'OPL-1',
}
