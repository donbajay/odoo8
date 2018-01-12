# -*- coding: utf-8 -*-

from openerp import models, fields

class hr_pangkat(models.Model):
	_name = 'hr.pangkat'
	_rec_name = 'pangkat'
	
	pangkat = fields.Char('Pangkat', size=128, required=True)
	ruang = fields.Char('Golongan/Ruang')
	kredit = fields.Integer('Angka Kredit')
	jabfung_ids = fields.Many2one('hr.jabfung',string='Jabatan Fungsional',help="Jabatan Fungsional")