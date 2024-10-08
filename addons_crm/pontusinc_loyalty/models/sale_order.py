from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    loyalty_customer_id = fields.Many2one('loyalty.customer', string='Loyalty')

    @api.model_create_multi
    def create(self, vals_list):
        loyalty = self.env['loyalty.customer']
        for vals in vals_list:
            loyalty_card = loyalty.sudo().search([('partner_id', '=', vals.get('partner_id'))], limit=1)
            if loyalty_card:
                vals['loyalty_customer_id'] = loyalty_card.id
        res = super().create(vals_list)
        return res