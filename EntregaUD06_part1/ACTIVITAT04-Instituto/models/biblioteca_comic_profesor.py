from odoo import models, fields

class BibliotecaProfesor(models.Model):
    _name = 'biblioteca.comic.profesor'
    _description = 'Profesor de la Biblioteca'
    
    nombre = fields.Char('Nom')
    apellido = fields.Char('Cognom')
    