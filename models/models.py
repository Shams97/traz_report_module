# -*- coding: utf-8 -*-

# MODULE FOR REPORTS CREATED AND EDIT BY SHAMS@INTEGRATED PATH

from odoo import models, fields, api
import datetime

class report_module(models.Model):
    _name = 'traz_report_module.traz_report_module'
    _description = 'traz_report_module.traz_report_module'


class AccountMoveExt(models.Model):
    _inherit="account.move"
    invoice_type = fields.Selection([('monetory', 'نقدي'), ('themem','آجل')] , string="نوع الفاتورة" , default="themem")
    warehouse_location_id = fields.Many2one('stock.picking',compute='calc_warehouse_location_id')
    invoice_time = fields.Char(compute='compute_invoice_time', readonly = True, string='الوقت')
    recievable = fields.Float(string="الواصل") 
    payable = fields.Float()
    
    # new customer information
    cus_name = fields.Char(string="اسم الزبون")
    address = fields.Char(string="العنوان")
    phone_num = fields.Char(string="رقم الهاتف")


    

    @api.depends("partner_id")
    def calc_warehouse_location_id(self):
        if self.invoice_origin:
            transfers=self.env["stock.picking"].search([("origin","=",self.invoice_origin)], limit=1)
            if transfers:
                self.warehouse_location_id = transfers.id
            else:
                self.warehouse_location_id = False
        else:
            self.warehouse_location_id = False 
            print("transfers",transfers)       
    

    def compute_invoice_time(self):
        now = datetime.datetime.now()
        self.invoice_time = now.time().strftime('%H:%M')

