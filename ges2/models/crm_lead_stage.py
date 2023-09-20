from odoo import models, fields, api, _


class LeadStage(models.Model):
    _name = "crm.lead.stage"
    _description = "CRM Lead Stages"
    _rec_name = 'name'
    _order = "sequence, name, id"

    

    name = fields.Char('Stage Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    color = fields.Integer('Color')
    requirements = fields.Text('Requirements', help="Enter here the internal requirements for this stage (ex: Offer sent to customer). It will appear as a tooltip over the stage's name.")