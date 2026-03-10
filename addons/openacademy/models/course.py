from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', string='Responsible')
