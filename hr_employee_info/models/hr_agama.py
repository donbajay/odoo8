# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_agama(models.Model):
	_name = 'hr.agama'
	_rec_name = 'agama'
	
	agama = fields.Char('Agama', size=128, required=True)