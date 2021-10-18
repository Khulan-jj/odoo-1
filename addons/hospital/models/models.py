# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields, api


class hospital(models.Model):
    _name = 'medical.test'
    _description = 'Medical test'

    partner_id = fields.Many2one('res.partner', 'Partner', ondelete = 'restrict', required = True)
    partner_id = fields.Many2one('product.product', 'Test Product', ondelete = 'restrict', required = True)
    date_test = fields.Datetime('Datetime Test', required = True)
    doctor = fields.Many2one('hr.employee', 'Doctor', Required = True)
    state = fields.selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('tested', 'Tested')], 'State', Required=True)

class hospital(models.Model):
    _name = 'medical.test'
    _description = 'Medical test'

    test_id = fields.Many2one('res.partner', 'Partner', ondelete = 'restrict', required = True)
    partner_id = fields.Many2one('product.product', 'Test Product', ondelete = 'restrict', required = True)
    date_test = fields.Datetime('Datetime Test', required = True)
