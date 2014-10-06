# -*- encoding: utf-8 -*-
##############################################################################
#
# First Name and Last Name fields for OpenERP.
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# Copyright (C) 2011 SYLEAM (<http://www.syleam.fr>).
# Copyright (C) 2014 OpusVL
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# If you require assistance, support, or further development of this
# software, please contact OpusVL using the details below:
#
# Telephone: +44 (0)1788 298 410
# Email: community@opusvl.com
# Web: http://opusvl.com
#
##############################################################################

from osv import osv
from osv import fields

class res_partner(osv.osv):
    _inherit = 'res.partner'

    def _get_name_calc(self, cr, uid, ids, field_name, unknow_none, context):
        """
        This is for overriding object 'name' property
        """
        ar_ctc = self.read(cr, uid, ids, ['id', 'first_name', 'last_name'], context)
        res = {}
        for record in ar_ctc:
            if not record['first_name'] and not record['last_name']:
                continue
            _name = "%s %s" % (record['first_name'] or '', record['last_name'] or '')
            res[record['id']] = _name
        return res

    def _set_name_calc(self, cr, uid, ids, field_name, value, fnct_inv_arg, context=None):
        """
        Set name of partner if not used first and last name
        """
        if not field_name:
            return False
        ids = isinstance(ids, list) and ids or [ids]
        for partner in self.browse(cr, uid, ids, context):
            cr.execute("""UPDATE res_partner SET
                    name=%s
                WHERE
                    id=%s""", (value or '', partner.id))
        return True


    _columns = {
        'first_name': fields.char('First Name(s)', size=64),
        'last_name': fields.char('Last Name', size=64),
        'name': fields.function(_get_name_calc, fnct_inv=_set_name_calc, type='char', size=128, method=True, string='Name',
                                store={
                                    'res.partner': (lambda self, cr, uid, ids, c={}: ids, ['first_name', 'last_name'], 10),
                                }, select=1,
                               ),
    }

res_partner()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

