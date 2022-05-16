from PIL import ImageFont, ImageDraw, Image
from io import BytesIO
import requests

def generate_meme(url:str, txt:str, color:str, fontsize:int):
    """Generate and display meme

    Args:
        url (str): Image url
        txt (str): Text to display on the image
    """
    
    image = Image.open(BytesIO(requests.get(url).content))
    draw = ImageDraw.Draw(image)
    ttf = 'https://www.dropbox.com/s/cq2bainz70cpbu4/ArialUnicodeMS.ttf?dl=1'

    W, H = image.size

    #blank = Image.new('RGB',(1000, 300))
    font = ImageFont.truetype(requests.get(ttf, stream=True).raw, fontsize)

    w, h = draw.textsize(txt, font=font)

    print('{} {} {} {}'.format((H-h), (H-h)/10, (H-h)/5, (H-h)/2))

    draw.text(((W-w)/2,(H-h)/50), txt, font=font, fill=color) #up
    draw.text(((W-w)/2,(H-h)/2), txt, font=font, fill=color) #center
    draw.text(((W-w)/2,(H-h)-((H-h)/50)), txt, font=font, fill=color) #down
    #image.save('sample-out.png') #save
    image.show() #display
    
def main():
    generate_meme("https://i.imgur.com/fYe7MrH.jpg", "測試中文字啊啊啊", 'red', 80)

if __name__ == '__main__':
    main()