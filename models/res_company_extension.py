# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import UserError, ValidationError
from odoo.tools import config
from odoo.addons.phone_validation.tools import phone_validation


class InsuranceCompanyExtension(models.Model):
    _inherit="res.partner"
    operative_office = fields.Many2one("res.partner", string="Operative Office", domain=[('type', '!=', 'contact'),('type', '!=', 'private')])
