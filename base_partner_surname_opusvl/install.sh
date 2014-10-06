#! /bin/bash

# NMB: Replaces the module in the right place on my dev box.

MYDIR="$(dirname "$(realpath "$0")")"
DESTDIR="/usr/lib/pymodules/python2.6/openerp/addons/base_partner_surname_opusvl"

set -x
rm -r "${DESTDIR}"
cp -r "${MYDIR}" "${DESTDIR}"
