'''from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("scream_cat.jpg")
draw = ImageDraw.Draw(img)

# font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("sans-serif.ttf", 16)
font = ImageFont.load_default()

# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(255,255,255),font=font)

#img.save('sample-out.jpg')
img.show()'''

from PIL import ImageFont, ImageDraw, Image
from io import BytesIO
import requests

image = Image.open(BytesIO(requests.get('https://i.imgur.com/fYe7MrH.jpg').content))
draw = ImageDraw.Draw(image)
txt = "測試中文字啊啊啊"
fontsize = 80
ttf = 'https://www.dropbox.com/s/cq2bainz70cpbu4/ArialUnicodeMS.ttf?dl=1'
color = 'red' #default

W, H = image.size

blank = Image.new('RGB',(1000, 300))
font = ImageFont.truetype(requests.get(ttf, stream=True).raw, fontsize)

w, h = draw.textsize(txt, font=font)

print('{} {} {} {}'.format((H-h), (H-h)/10, (H-h)/5, (H-h)/2))

draw.text(((W-w)/2,(H-h)/50), txt, font=font, fill=color) #up
draw.text(((W-w)/2,(H-h)/2), txt, font=font, fill=color) #center
draw.text(((W-w)/2,(H-h)-((H-h)/50)), txt, font=font, fill=color) #down
#image.save('sample-out.png') # save it
image.show()