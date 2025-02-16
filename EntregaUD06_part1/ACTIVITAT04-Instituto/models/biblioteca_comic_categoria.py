# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class BookCategory(models.Model):
    #Nombre y descripcion del modelo
    _name = 'biblioteca.comic.categoria'
    _description = 'Categoria de comics de la biblioteca'

    #Para guardar lo del padre y acelerar consultas
    # https://www.odoo.com/documentation/17.0/es/developer/reference/addons/orm.html#odoo.models.BaseModel._comic_store
    _comic_store = True
    #ID que indica el padre de este modelo
    _comic_name = "comic_id"

    #Atributos del modelo


    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR LOS Many2One en Vistas
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'

    #Nombre categoria
    nombre = fields.Char('Nombre')


    #ID de la categoría padre (relación muchos a uno con este mismo modelo)
    modulo_ids = fields.Many2many(
        'biblioteca.comic.socio',
        string='Módulo',
        required=True
    )
    
    
    #socio_id = fields.One2many(
    #    'biblioteca.comic.socio', 'comic_id',
    #    string='Categorias hijas',
    #    ondelete='set null')
    #Necesario para comprobar la recursion
    data_prestec = fields.Date(string="Data de Préstec", default=fields.Date.today)
    data_retorn = fields.Date(string="Data Prevista de Retorn")

    #Decorador para introducir "constraints" https://odoo-development.readthedocs.io/en/latest/dev/py/constraints.html
      
    @api.constrains('data_prestec', 'data_retorn')
    def _check_dates(self):
        today = date.today()
        for record in self:
            if record.data_prestec and record.data_prestec > today:
                raise ValidationError("La data de préstec no pot ser posterior al dia de hui.")
            if record.data_retorn and record.data_retorn < today:
                raise ValidationError("La data prevista de tornada no pot ser anterior al dia de hui.")


