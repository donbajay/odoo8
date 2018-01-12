# -*- coding: utf-8 -*-
# © 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class hr_employee(models.Model):
	_inherit = 'hr.employee'

	jabfung_ids = fields.Many2one('hr.jabfung',
                                   string='Jabatan Fungsional',
                                   help="Jabatan Fungsional")
	jabstruktur_ids = fields.Many2one('hr.jabstruktur',
                                   string='Jabatan Struktural',
                                   help="Jabatan Struktural")
	jenispeg_ids = fields.Many2one('hr.jenispeg',
                                   string='Jenis Pegawai',
                                   help="Jenis Pegawai")
	golpangkat_ids = fields.Many2one('hr.golpangkat',
                                   string='Golongan',
                                   help="Golongan")
	agama_ids = fields.Many2one('hr.agama',
                                   string='Agama',
                                   help="Agama")
	nip = fields.Char('Nomer Induk Pegawai', 
						size=10)
	gelardepan = fields.Char('Gelar Depan', 
						size=20)
	gelarbelakang = fields.Char('Gelar Belakang', 
						size=20)
	nup = fields.Char('NUP', 
						size=10)
	nidk = fields.Char('NIDK', 
						size=10)
	nidn = fields.Char('NIDN', 
						size=10)