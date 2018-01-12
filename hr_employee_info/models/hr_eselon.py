# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_eselon(models.Model):
	_name = 'hr.eselon'
	_rec_name = 'eselon'
	
	eselon = fields.Char('Eselon', size=128, required=True)