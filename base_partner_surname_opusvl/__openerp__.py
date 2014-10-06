# -*- encoding: utf-8 -*-
##############################################################################
#    
# OpenERP, Open Source Management Solution
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
{
    "name" : "Partner Surname OpusVL",
    'version' : '1.1',
    "author" : "OpusVL",
    "website" : "http://opusvl.com",
    "category" : "Generic Modules/Base",
    "description": """
This module use for seperate surname from contact name of partner. Now You can give first name & last name on contact Name.
This module is deprecated, it is highly recommended to use base_contact instead.

    """,
    "depends" : ["base"],
    "init_xml" : [ ],
    "demo_xml" : [ ],
    "update_xml" : [ "partner_view.xml" ],
    "installable": True,
    "auto_install": False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

