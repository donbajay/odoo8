# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_jenispeg(models.Model):
	_name = 'hr.jenispeg'
	_rec_name = 'jenispeg'
	
	kodejenispeg = fields.Char('Kode Jenis Pegawai', size=10, required=True)
	jenispeg = fields.Char('Jenis Pegawai', size=128, required=True)