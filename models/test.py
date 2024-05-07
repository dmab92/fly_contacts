from datetime import datetime

from PIL import Image, ImageDraw,ImageFont

# Open the desired Image you want to add text on
#i = Image.open('sample2.jpg')
img = Image.open("/opt/odoo16/odoo16/addons/contacts/models/flystore.png", "r")
# To add 2D graphics in an image call draw Method
# Custom font style and font siz
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Custom font style and font size
myFont = ImageFont.truetype('DejaVuSans-Bold.ttf', 35)
#myFont = ImageFont.load_default()

 
# Add Text to an image
I1.text((214, 498), "Boris MENI", font=myFont, fill =(17, 30, 126))
 
# Display edited image
img.show()
 
# Save the edited image
img.save("/opt/odoo16/odoo16/addons/contacts/models/flystore2.png")