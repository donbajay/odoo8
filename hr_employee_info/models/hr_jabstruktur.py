# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_jabstruktur(models.Model):
	_name = 'hr.jabstruktur'
	_rec_name = 'jabstruktur'
	
	jabstruktur = fields.Char('Jabatan Struktural', size=128, required=True)
	department_ids = fields.Many2one('hr.department',string='Department',help="Department")
	struktur = fields.Char('Struktural', size=128, required=True,help="Singkatan")
	eselon_ids = fields.Many2one('hr.eselon',string='Eselon',help="Eselon")