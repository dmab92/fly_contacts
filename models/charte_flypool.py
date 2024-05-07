# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime

from odoo import api, fields, models, _
from PIL import Image, ImageDraw,ImageFont


class CharteFlypool(models.Model):
    _name = 'charte.flypool'
    _description = 'Charte Flypool'

    name = fields.Char('I, the undersigned Mr or Mrs', required=True)
    company_id = fields.Many2one("res.company", string="Company")
    sum_of = fields.Integer(string=" paying the sum of:")
    period = fields.Integer(string=" monthly or occasionally for a period of")
    bool = fields.Boolean(string= "Océan Gardener")
    bool1 = fields.Boolean(string ="Apeel")
    nb_employees= fields.Integer(string='Number of employees in the structure ')
    nb_flypool = fields.Integer(string='Number of FlyPoints made available')
    date = fields.Date("Date", default=datetime.today().date())
    signature = fields.Binary(string="Signature")
    state = fields.Selection([('draft', 'Draft'),
                              ('valited', 'Confirm'),
                              ('cancel', 'cancel'),
                              ], default='draft', string="State")



    def print_recu(self):

        return self.env.ref('contacts.action_report_charte_flypool').report_action(self)

    def print_flystore(self):
       # Open the desired Image you want to add text on
        img = Image.open("/opt/odoo16/odoo16/addons/contacts/static/description/flystore.png", "r")

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
         
        # Custom font style and font size
        myFont = ImageFont.truetype('DejaVuSans-Bold.ttf', 35)
         
        # Add Text to an image
        I1.text((214, 498), self.name, font=myFont, fill =(17, 30, 126))
         
        # Display edited image
        img.show()
         
        # Save the edited image
        img.save("/opt/odoo16/odoo16/addons/contacts/static/description/flystore2.png")
        

        return self.env.ref('contacts.action_report_flystore_flypool').report_action(self)

    def print_sponsorship(self):
        return self.env.ref('contacts.action_report_sponsorship_flypool').report_action(self)


    def set_valitaded(self):
        return self.write({'state': 'valited'})