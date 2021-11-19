# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_barcode_img_prodotto(models.Model):
    _name = 'abc_barcode_img_prodotto.abc_barcode_img_prodotto'
    _description = 'abc_barcode_img_prodotto'

#Eredito il modulo "StockInventoryLine" per accedere alla vista.    
class StockInventoryLine(models.Model):
     _inherit = "stock.inventory.line"
     image = fields.Binary(related='product_id.image_1920')
        
#Eredito il modulo "StockMoveLine" per accedere alla vista.    
class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    image = fields.Binary(related='product_id.image_1920')

#Eredito il modulo "StockPicking" per accedere alla vista.    
class StockPicking(models.Model):
    _inherit = "stock.picking"
    image = fields.Binary(related='product_id.image_1920')

#Eredito il modulo "StockMove" per accedere alla vista.        
class StockMove(models.Model):
    _inherit = "stock.move"
    image = fields.Binary(related='product_id.image_1920')