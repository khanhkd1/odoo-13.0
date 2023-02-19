from odoo import models, fields


class Demo(models.Model):
    _name = 'khanhkd1.demo'
    _description = "Demo model"
    
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
