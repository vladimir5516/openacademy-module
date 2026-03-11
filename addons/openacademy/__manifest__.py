{
    'name': 'Open Academy',
    'version': '1.0',
    'summary': 'Gestion de formations',
    'author': 'Vladimir',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    'installable': True,
    'application': True,
}
