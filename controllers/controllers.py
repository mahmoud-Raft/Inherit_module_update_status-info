# -*- coding: utf-8 -*-
# from odoo import http


# class Tahrircompanysales(http.Controller):
#     @http.route('/tahrircompanysales/tahrircompanysales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tahrircompanysales/tahrircompanysales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tahrircompanysales.listing', {
#             'root': '/tahrircompanysales/tahrircompanysales',
#             'objects': http.request.env['tahrircompanysales.tahrircompanysales'].search([]),
#         })

#     @http.route('/tahrircompanysales/tahrircompanysales/objects/<model("tahrircompanysales.tahrircompanysales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tahrircompanysales.object', {
#             'object': obj
#         })
