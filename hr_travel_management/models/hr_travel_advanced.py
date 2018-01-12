# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp import tools
from openerp.osv import osv
from datetime import date, datetime

import openerp.addons.decimal_precision as dp
import time

class hr_travel_advanced(models.Model):
	_name = 'hr.travel.advanced'
	
	#@api.multi
	#@api.depends('unit_amount','unit_quantity')
	def _amount(self):
		for advance in self:
			advance.total_amount = advance.unit_amount * advance.unit_quantity
	
	def _get_uom_id(self, cr, uid, context=None):
		result = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'product', 'product_uom_unit')
		return result and result[1] or False
	
	name = fields.Char('Advanced Note', required=True)
	travel_id = fields.Many2one('hr.travel.management', 'Travel', ondelete='cascade', select=True)
	date_value = fields.Date('Date', required=True)
	total_amount = fields.Float(compute='_amount', string='Total', digits_compute=dp.get_precision('Account'))
	unit_amount = fields.Float('Unit Price', digits_compute=dp.get_precision('Product Price'))
	unit_quantity = fields.Float('Quantities', digits_compute= dp.get_precision('Product Unit of Measure'))
	product_id = fields.Many2one('product.product', 'Product', domain=[('hr_expense_ok','=',True)])
	uom_id = fields.Many2one('product.uom', 'Unit of Measure', required=True)
	description = fields.Text('Description')
	sequence = fields.Integer('Sequence', select=True, help="Gives the sequence order when displaying a list of expense lines.")
	
	_defaults = {
        'unit_quantity': 1,
        'date_value': lambda *a: time.strftime('%Y-%m-%d'),
        'uom_id': _get_uom_id,
    }
	
	def onchange_product_id(self, cr, uid, ids, product_id, context=None):
		res = {}
		if product_id:
			product = self.pool.get('product.product').browse(cr, uid, product_id, context=context)
			res['name'] = product.name
			amount_unit = product.price_get('standard_price')[product.id]
			res['unit_amount'] = amount_unit
			res['uom_id'] = product.uom_id.id
		return {'value': res}
	
	def onchange_uom(self, cr, uid, ids, product_id, uom_id, context=None):
		res = {'value':{}}
		if not uom_id or not product_id:
			return res
		product = self.pool.get('product.product').browse(cr, uid, product_id, context=context)
		uom = self.pool.get('product.uom').browse(cr, uid, uom_id, context=context)
		if uom.category_id.id != product.uom_id.category_id.id:
			res['warning'] = {'title': ('Warning'), 'message': ('Selected Unit of Measure does not belong to the same category as the product Unit of Measure')}
			res['value'].update({'uom_id': product.uom_id.id})
		return res
