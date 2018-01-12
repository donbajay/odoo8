# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp import tools
from openerp.osv import osv
from datetime import date, datetime

import openerp.addons.decimal_precision as dp

class hr_travel_management(models.Model):
	_name = 'hr.travel.management'
	
	def _amount(self):
		res= {}
		for advance in self:
			total = 0.0
			for line in advance.advanced_ids:
				total += line.unit_amount * line.unit_quantity
			#res[advance.id] = total
			advance.advanced_amount = total
		#return res
		
	def _get_user_name(self, cr, uid, *args):
		user_obj = self.pool.get('res.users')
		user_value = user_obj.browse(cr, uid, uid)
		return user_value.login or False
		
	@api.onchange('return_date', 'departure_date')
	def _get_total(self):
		fmt = '%Y-%m-%d'
		if self.departure_date and self.return_date:
			d1 = datetime.strptime(self.departure_date, fmt)
			d2 = datetime.strptime(self.return_date, fmt)
			self.days = str(((d2-d1).days)+1)+' Days'
		else:
			self.days = '0 Days'
		
	def _check_dates(self, cr, uid, ids, context=None):
		for travel in self.read(cr, uid, ids, ['departure_date', 'return_date'], context=context):
			if travel['departure_date'] and travel['return_date']:
				if travel['departure_date'] > travel['return_date']:
					return False
		return True
	
	_constraints = [
		(_check_dates, 'Error! Request Departure Date must be lower than Request Return Date.', ['departure_date', 'return_date'])
	]

	id = fields.Integer('ID', readonly=True)
	name = fields.Char('Travel Agenda', required=True)
	employee_ids = fields.Many2one('hr.employee',string='Employee',help="Employee", required=True)
	job_ids = fields.Many2one('hr.job',string='Job',related='employee_ids.job_id',copy=False, store=True, readonly=True)
	department_ids = fields.Many2one('hr.department',string='Department',related='employee_ids.department_id',copy=False, store=True, readonly=True)
	manager_ids = fields.Many2one('hr.employee',string='Manager',related='department_ids.manager_id',copy=False, store=True, readonly=True)
	user_id = fields.Many2one('res.users','Request by', readonly=True)
	confirm_id = fields.Many2one('res.users','Confirm by', readonly=True)
	approved_id = fields.Many2one('res.users','Approved by', readonly=True)
	request_date = fields.Datetime('Request Date', readonly=True)
	confirm_date = fields.Datetime('Confirm Date', readonly=True)
	approved_date = fields.Datetime('Approved Date', readonly=True)
	travel_type = fields.Selection([('ddn', 'Dinas Dalam Negeri'), ('ddl', 'Dinas Luar Negeri')], string='Travel Type')
	country_ids = fields.Many2one('res.country','Country')
	state_ids = fields.Many2one('res.country.state',string='State', domain="[('country_id', '=', country_ids)]")
	city = fields.Char('City', required=True)
	departure_date = fields.Date('Request Departure Date')
	return_date = fields.Date('Request Return Date')
	days = fields.Char('Days', readonly=True)
	travel_mode  = fields.Selection([('flight', 'Flight'), ('train', 'Train'), ('car', 'Car'), ('ship', 'Ship')], string='Travel Mode')
	advanced_ids = fields.One2many('hr.travel.advanced', 'travel_id', 'Advanced Lines', copy=True, readonly=False)
	state = fields.Selection([
			('draft', 'New'),
			('cancelled', 'Refused'),
			('confirm', 'Waiting Approval'),
			('accepted', 'Approved'),
			('done', 'Waiting Payment'),
			('paid', 'Paid'),
			],
			'Status', readonly=True, track_visibility='onchange', copy=False,
			help='When the expense request is created the status is \'Draft\'.\n It is confirmed by the user and request is sent to admin, the status is \'Waiting Confirmation\'.\
			\nIf the admin accepts it, the status is \'Accepted\'.\n If the accounting entries are made for the expense request, the status is \'Waiting Payment\'.')
	note = fields.Text('Note')
	advanced_amount = fields.Float(compute='_amount', string='Total Amount', digits_compute=dp.get_precision('Account'))
	
	_defaults = {
        'user_id': lambda s, cr, uid, c: uid,
		'state': 'draft',
        'request_date': fields.datetime.now(),
    }