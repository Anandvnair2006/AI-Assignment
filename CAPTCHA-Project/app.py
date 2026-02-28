from flask import Flask, render_template, request, session, redirect, url_for
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import io
import base64

app = Flask(__name__)
app.secret_key = "secret_key"

# Generate random CAPTCHA text
def generate_captcha_text(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Generate CAPTCHA image
def generate_captcha_image(text):
    width, height = 200, 80
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    # Draw text
    for i, char in enumerate(text):
        x = 20 + i * 25
        y = random.randint(10, 30)
        draw.text((x, y), char, fill=(0, 0, 0), font=font)

    # Add noise lines
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0), width=1)

    # Apply blur
    image = image.filter(ImageFilter.BLUR)

    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('captcha')
        if user_input == session.get('captcha_text'):
            return "CAPTCHA Verified Successfully ✅"
        else:
            return "Incorrect CAPTCHA ❌"

    captcha_text = generate_captcha_text()
    session['captcha_text'] = captcha_text

    image = generate_captcha_image(captcha_text)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render_template('index.html', captcha_image=image_base64)

if __name__ == "__main__":
    app.run(debug=True)