from flask import Flask, render_template, request, session, redirect, url_for
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import io
import base64

app = Flask(__name__)
app.secret_key = "super_secret_key"

def generate_captcha_text(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_captcha_image(text):
    width, height = 250, 100
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # Draw characters with rotation
    for i, char in enumerate(text):
        char_image = Image.new('RGBA', (50, 60), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)

        color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))
        char_draw.text((10, 10), char, font=font, fill=color)

        rotated = char_image.rotate(random.randint(-30, 30), expand=1)
        image.paste(rotated, (20 + i * 35, random.randint(10, 30)), rotated)

    # Add noise dots
    for _ in range(1000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(random.randint(0,255),
                                  random.randint(0,255),
                                  random.randint(0,255)))

    # Add random lines
    for _ in range(8):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2),
                  fill=(random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255)),
                  width=2)

    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('captcha')
        if user_input and user_input.upper() == session.get('captcha_text'):
            return "<h2>CAPTCHA Verified ✅</h2>"
        else:
            return redirect(url_for('index'))

    captcha_text = generate_captcha_text()
    session['captcha_text'] = captcha_text

    image = generate_captcha_image(captcha_text)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render_template("index.html", captcha_image=image_base64)

if __name__ == "__main__":
    app.run(debug=True)