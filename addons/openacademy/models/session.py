from odoo import models, fields, api
from datetime import timedelta

class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'Session de formation'

    name = fields.Char(string='Titre', required=True)
    course_id = fields.Many2one('openacademy.course', string='Cours', required=True)
    instructor_id = fields.Many2one('res.partner', string='Formateur')
    attendee_ids = fields.Many2many('res.partner', string='Participants')
    start_date = fields.Date(string='Date de début', default=fields.Date.today)
    duration = fields.Float(string='Durée (jours)', default=1)
    seats = fields.Integer(string='Nombre de places', default=10)
    
    # Champ calculé : pourcentage de places prises
    taken_seats = fields.Float(string='Places prises', compute='_compute_taken_seats')
    
    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for session in self:
            if session.seats > 0:
                session.taken_seats = 100.0 * len(session.attendee_ids) / session.seats
            else:
                session.taken_seats = 0.0
