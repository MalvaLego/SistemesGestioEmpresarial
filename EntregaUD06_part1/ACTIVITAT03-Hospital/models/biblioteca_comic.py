# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"

    #Introducice metodo "archivar" que invierte el estado de "activo"
    def archivar(self):
        for record in self:
            record.activo = not record.activo


#Definimos modelo Biblioteca comic
class BibliotecaComic(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.comic'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Comic de biblioteca'
    

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'


    #Atributo nombre
    nombre = fields.Char('Nombre', required=True, index=True)
    apellidos = fields.Text('Apellidos')
    sintomas = fields.Text('Síntomas')
    #Atributo para seleccionar entre varios
    

    # Relación muchos a muchos de autores utilizando un "partner"
    # de Odoo (Es un elemento que puede ser empresa o individuo)
    autor_ids = fields.Many2many('res.partner', string='Autores')

    # Relación muchos a uno utilizando un "partner"
    # de Odoo (Es un elemento que puede ser empresa o individuo)

    editorial_id = fields.Many2one('res.partner', string='Editorial')

    #Relacion muchos a uno con el modelo de las categorias
    categoria_id = fields.Many2one('biblioteca.comic.categoria')
    

    #Para poder meter referencias a modelos existentes en Odoo (por ejemplo, una factura) como 
    #un dato del modelo. Para saber que documentos, usa "referencable_models"
    ref_doc_id = fields.Reference(selection='_referencable_models', string='Referencia a documento')

    #Funcion usada para obtener que modelos pueden ser referenciados 
    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]


    

    

