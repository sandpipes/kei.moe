from PIL import Image
import os, sys
from os.path import isfile, join

directories = ['fanart', 'official', 'edits']
prev = 0

redo = False

for directory in directories:
    filesToDo = []
    if not redo:
        currentFiles = [f for f in os.listdir(directory) if isfile(join(directory, f))]
        tnFiles = [f for f in os.listdir('./thumbnails/' + directory) if isfile(join('./thumbnails/' + directory, f))]

        temp = []
        for fi in tnFiles:
            for f2 in currentFiles:
                if fi[:len(fi)-3] == f2[:len(f2)-3]:
                    temp.append(f2)
        for t in temp:
            currentFiles.remove(t)

        filesToDo = currentFiles
    else:
        filesToDo = [f for f in os.listdir(directory) if isfile(join(directory, f))]

    if len(filesToDo) == 0:
        print('No files to convert in "%s" folder.' % directory)
        continue
    print('Begin work on "%s" folder.' % directory)

    for filename in filesToDo:
        if filename[:1] == '.':
            continue

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