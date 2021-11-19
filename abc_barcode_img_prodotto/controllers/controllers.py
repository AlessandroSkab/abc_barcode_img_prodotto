# -*- coding: utf-8 -*-
# from odoo import http


# class AbcBarcodeImgProdotto(http.Controller):
#     @http.route('/abc_barcode_img_prodotto/abc_barcode_img_prodotto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_barcode_img_prodotto/abc_barcode_img_prodotto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_barcode_img_prodotto.listing', {
#             'root': '/abc_barcode_img_prodotto/abc_barcode_img_prodotto',
#             'objects': http.request.env['abc_barcode_img_prodotto.abc_barcode_img_prodotto'].search([]),
#         })

#     @http.route('/abc_barcode_img_prodotto/abc_barcode_img_prodotto/objects/<model("abc_barcode_img_prodotto.abc_barcode_img_prodotto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_barcode_img_prodotto.object', {
#             'object': obj
#         })
