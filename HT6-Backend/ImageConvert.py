import os, io
from PIL import Image

directory = 'images'
ConvertedImages = []
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        f = os.path.join(directory, filename)
        im = Image.open(f)

        image_bytes = io.BytesIO()
        im.save(image_bytes, format='JPEG')

        image = {
            'data': image_bytes.getvalue()
        }
        ConvertedImages.append(image)
