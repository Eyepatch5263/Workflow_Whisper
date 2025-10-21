import os
from stegano import lsb
from PIL import Image

secret = os.environ.get('HIDDEN_SECRET', 'default_secret')

img = Image.new('RGB', (200, 100), color=(73, 109, 137))
img.save('original.png')

lsb.hide('OIP.jpeg', secret).save('stego.png')

print('Image generated with hidden secret.')
