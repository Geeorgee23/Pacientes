# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from odoo.exceptions import ValidationError
import re


class pacientes_model(models.Model):
    _name = 'pacientes_app.pacientes_model'
    _description = 'pacientes_app.pacientes_model'

    name = fields.Char(string="Nombre",help="Añade el nombre del Paciente",required=True, index=True, size=25)
    dni = fields.Char(string="Dni",help="Añade el dni del Paciente",required=True, index=True, size=9)
    apellidos = fields.Char(string="Apellidos",help="Añade los apellidos del Paciente",required=True, index=True, size=50)
    telefono = fields.Char(string="Telefono",help="Añade el telefono del Paciente",required=True, index=True, size=9)
    fechaNac = fields.Date(string="Fecha de Nacimiento",help="Añade la fecha de nacimiento del Paciente",required=True, index=True, default=datetime.today())
    email = fields.Char(string="Email",help="Añade el email del Paciente",required=False, size=100)
    foto = fields.Binary()

    visitas = fields.One2many("pacientes_app.visitas_model", "paciente", string="Visitas")
    numVisitas = fields.Integer(string="Numero Visitas: ", compute="_calcVisitas", store=True) 
    

    @api.constrains("dni")
    def _validarDni(self):
        letras="TRWAGMYFDPXBNJZSQVHLCKE"

        letra =self.dni[-1]
        num=int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError ("DNI Invalido!")

    @api.depends("visitas")
    def _calcVisitas(self):
        self.numVisitas = len(self.visitas)


    @api.constrains("fechaNac")
    def _checkEdad(self):
        edad = date.today().year - self.fechaNac.year

        if edad<18:
            raise ValidationError ("Fecha de nacimiento Invalida! El paciente tiene que se mayor de edad!")



    @api.constrains("email")
    def is_valid_email(self):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if re.match(expresion_regular, self.email) is None:
            raise ValidationError ("Email Invalido!")