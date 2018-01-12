# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_jabfung(models.Model):
	_name = 'hr.jabfung'
	_rec_name = 'jabfung'
	
	jabfung = fields.Char('Jabatan Fungsional', size=128, required=True)