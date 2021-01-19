# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class visitas_model(models.Model):
    _name = 'pacientes_app.visitas_model'
    _description = 'pacientes_app.visitas_model'

    fecha = fields.Datetime(string="Fecha", help="Añade la fecha y la hora", required=True, index=True, default=datetime.now())
    detalle = fields.Html(string="Detalle", help="Añade el motivo de la visita", required=True)

    paciente = fields.Many2one("pacientes_app.pacientes_model", string="Paciente")
