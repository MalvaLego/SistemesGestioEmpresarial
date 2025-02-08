from odoo import models, fields

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.comic.socio'
    _description = 'Socio de la Biblioteca'
    
    nombre = fields.Char('Nom')
    apellido = fields.Char('Cognom')
    identificador = fields.Char('Identificador')

    def name_get(self):
        res = []
        for record in self:
            name = f"{record.nombre} {record.apellido}"  # Format: "Joan Pérez"
            res.append((record.id, name))
        return res
