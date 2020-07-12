from PIL import Image
import os, sys
from os.path import isfile, join

# Gif handling from https://gist.github.com/BigglesZX/4016539
def analyseImage(path):
    '''
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    '''
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results

def processImage(path):
    '''
    Iterate the GIF, extracting each frame.
    '''
    mode = analyseImage(path)['mode']
    
    im = Image.open(path)

    p = im.getpalette()
    last_frame = im.convert('RGBA')

    '''
    If the GIF uses local colour tables, each frame will have its own palette.
    If not, we need to apply the global palette to the new frame.
    '''
    if not im.getpalette():
        im.putpalette(p)
    
    new_frame = Image.new('RGBA', im.size)
    
    '''
    Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
    If so, we need to construct the new frame by pasting it on top of the preceding frames.
    '''
    if mode == 'partial':
        new_frame.paste(last_frame)
    
    new_frame.paste(im, (0,0), im.convert('RGBA'))
    return new_frame

def gifHead(width):
    img = Image.open('gifhead.png')
    baseheight = int(width * 0.2)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)
    return img

directories = [
    'fanart',
    'official',
    'edits',
    'fancomics',
    'LN_v2',
    'LN_v4.0',
    'LN_v4.5',
    'LN_v5',
    'LN_v6',
    'LN_v7.0',
    'LN_v7.5',
    'LN_v8',
    'LN_v9',
    'LN_v11.0',
    'LN_v11.5',
    'LN_v11.75',
    'LN_v12'
]
prev = 0

redo = True

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
        #print('No files to convert in "%s" folder.' % directory)
        continue
    print('Begin work on "%s" folder.' % directory)

    for filename in filesToDo:
        if filename[:1] == '.':
            continue

        if False and ('.jpg' in filename.lower() or '.png' in filename.lower()):
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
                orig = orig.convert('RGBA')
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
            img.save(join("./thumbnails/" + directory, filename.replace('.png', '.jpg')), optimize=True, quality=50)
        elif '.gif' in filename.lower():
            ost = '\rWorking on ' + filename
            sys.stdout.write('\r' + prev * ' ')
            sys.stdout.flush()
            sys.stdout.write(ost)
            sys.stdout.flush()
            prev = len(ost)
            orig = processImage(join(directory, filename))
            img = Image.new("RGBA", orig.size, "WHITE")
            orig = orig.convert('RGBA')
            img.paste(orig, (0, 0), orig)
            showGif = gifHead(orig.size[0])
            img.paste(showGif, (0, 0), showGif)
            img = img.convert('RGB')
            basewidth = 400
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            if not os.path.exists("./thumbnails/" + directory):
                os.makedirs("./thumbnails/" + directory)
            img.save(join("./thumbnails/" + directory, filename.replace('.gif', '.jpg')), optimize=True, quality=50)

    print('\n')