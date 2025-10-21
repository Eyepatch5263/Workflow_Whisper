import os
from stegano import lsb
from PIL import Image

secret = os.environ.get('HIDDEN_SECRET', '').strip()

if not secret:
	raise ValueError('Secret is empty. Please set the HIDDEN_SECRET environment variable.')

img = Image.new('RGB', (200, 100), color=(73, 109, 137))
img.save('original.png')

lsb.hide('original.png', secret).save('stego.png')

print('Stego image generated as stego.png with hidden secret.')
