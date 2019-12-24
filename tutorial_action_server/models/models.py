# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class SalesTarget(models.Model):
    _name = 'ng.sale.target'

    name = fields.Char(default='Sales Target')
    target_line_id = fields.One2many('ng.sale.target.line', 'target_id')

    def open_sales_target(self):
        # cek sudah ada data sales target atau belum
        existed_data = self.env['ng.sale.target'].search([],limit=1)

        # jika belum ada buat sales target baru
        if not existed_data:
            existed_data = self.create({})        
        
        # tampilkan data sales target ke user dengan Action Window
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ng.sale.target',
            'res_id': existed_data.id,
        }
    

class SalesTargetLine(models.Model):
    _name = 'ng.sale.target.line'

    user_id = fields.Many2one('res.users', string='Sales Person')
    total_target = fields.Float(string='Total Target', default=0)
    target_id = fields.Many2one('ng.sale.target')


    