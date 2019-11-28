from odoo import api,fields,models

class sale_order(models.Model):
    _inherit = "sale.order"

    @api.multi
    def print_ticket(self):
        return self.env.ref('salereport_jss.action_report_sale_order_ticket')\
            .report_action(self)