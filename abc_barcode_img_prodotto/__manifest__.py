# -*- coding: utf-8 -*-
{
    'name': "Img Prodotto in Barcode",

    'summary': """
        Modulo che estende la vista dove vengono visualizzati i prodotti nell'app Barcode
        affinchè possa essere mostrata l'immagine del prodotto stesso.""",

    'description': """
        Modulo che estende la vista dove vengono visualizzati i prodotti nell'app Barcode
        affinchè possa essere mostrata l'immagine del prodotto stesso.
    """,

    'author': "A.B.C. Strategie ",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'stock_barcode'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_adjustments.xml',
        'views/operations.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
