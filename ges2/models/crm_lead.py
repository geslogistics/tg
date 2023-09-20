from odoo import models, fields, api, _


class Lead(models.Model):
    _inherit = "crm.lead"

    lead_stage_id = fields.Many2one('crm.lead.stage', string='Status', index=True, tracking=True, readonly=False, store=True, copy=False, ondelete='restrict')

   