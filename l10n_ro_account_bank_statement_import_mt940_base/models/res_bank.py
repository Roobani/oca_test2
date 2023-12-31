# Copyright 2018 NextERP Romania
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ResPartnerBank(models.Model):
    _name = "res.partner.bank"
    _inherit = ["res.partner.bank", "l10n.ro.mixin"]

    l10n_ro_unstructured_tag86 = fields.Text(
        string="Romania - MT940 Unstructured Tag 86 Pattern"
    )
