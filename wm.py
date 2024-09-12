from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from env import WM_TEXT

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def draw_rotated_text(image, font, text, angle, x, y):
    txt = Image.new(image.mode, (x, y))
    d = ImageDraw.Draw(txt)
    d.text((0, 0), text, font=font, fill=(255, 0, 0))
    txt = txt.rotate(angle)
    image.paste(txt, (int(x - txt.width/2), int(y - txt.height/2)), txt)

def font_getsize(font: ImageFont.FreeTypeFont, text):
    left, top, right, bottom = font.getbbox(text)
    width = right - left
    height = bottom - top

    return (width, height)

class Wm:
    def generate(self, image_path: str, text=WM_TEXT):
        image = Image.open(image_path).convert('RGBA')
        image_name = Path(image_path).stem
        image_width, image_height = image.size
        fontsize = 1
        font_fraction = 98 / 100
        font = ImageFont.truetype('./fonts/static/Quicksand-Bold.ttf', fontsize) 

        while font_getsize(font, text)[0] < image_width * font_fraction:
            fontsize += 1
            font = ImageFont.truetype('./fonts/static/Quicksand-Bold.ttf', fontsize) 

        txt = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)
        _, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)
        draw.text(((image_width-text_width)/2, (image_height-text_height)/2), text, font=font, fill=(255, 0, 67, 255))
        rotated_txt = txt.rotate(25, center=(0, image.width - 5))
        result = Image.alpha_composite(image, rotated_txt)
        result_path = f'./downloads/{image_name}-result.png'
        result.save(result_path)

        return result_path
 

wm = Wm()
