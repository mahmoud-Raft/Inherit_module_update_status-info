# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from odoo import fields, models

class saleorder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection([
        ('draft', 'Request'),
        ('sent', 'Request Sent'),
        ('sale', 'Request to Approved'),
        ('done', 'Approved'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')


# from odoo import models, fields, api


# class tahrircompanysales(models.Model):
#     _name = 'tahrircompanysales.tahrircompanysales'
#     _description = 'tahrircompanysales.tahrircompanysales'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
