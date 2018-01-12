# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_golpangkat(models.Model):
	_name = 'hr.golpangkat'
	_rec_name = 'golpangkat'

	kode_golongan = fields.Char('Kode Golongan', size=1, required=True)
	golpangkat = fields.Char('Golongan', size=128, required=True)