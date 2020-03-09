from PIL import Image
import os, sys
from os.path import isfile, join

directories = ['fanart', 'official']
prev = 0

for directory in directories:
    onlyfiles = [f for f in os.listdir(directory) if isfile(join(directory, f))]
    print('Begin work on ' + directory + ' folder.')

    for filename in onlyfiles:
        if '.jpg' in filename.lower() or '.png' in filename.lower():
            ost = '\rWorking on ' + filename
            sys.stdout.write('\r' + prev * ' ')
            sys.stdout.flush()
            sys.stdout.write(ost)
            sys.stdout.flush()
            prev = len(ost)
            orig = Image.open(join(directory, filename))
            img = None
            if orig.mode in ('RGBA', 'LA') or (orig.mode == 'P' and 'transparency' in orig.info):
                img = Image.new("RGBA", orig.size, "WHITE")
                img.paste(orig, (0, 0), orig)
            else:
                img = Image.new("RGB", orig.size, "WHITE")
                img.paste(orig, (0, 0))
            img = img.convert('RGB')

            basewidth = 400
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            if not os.path.exists("./thumbnails/" + directory):
                os.makedirs("./thumbnails/" + directory)
            img.save(join("./thumbnails/" + directory, filename.replace('png', 'jpg')), optimize=True, quality=50)
    print('\n')