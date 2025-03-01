from PIL import Image
from ImageTiler import image_bytes
from ImageUtils import write_data, append_palette
import os


def get_mask(img):
    mask = Image.new(mode="L", size=img.size)
    w, h = img.size
    for y in range(h):
        for x in range(w):
            p = img.getpixel((x, y))
            if p == 0:
                mask.putpixel((x, y), 0)
            else:
                mask.putpixel((x, y), 255)
    return mask


def grab_tiles(img):
    positions = ((5, 5), (1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (3, 3))

    tiles = Image.new(mode="P", size=(16, 16 * 7), color=0)
    tiles.putpalette(img.getpalette())

    for i, (x, y) in enumerate(positions):
        tiles.paste(img.crop((x * 16, y * 16, x * 16 + 16, y * 16 + 16)), (0, i * 16))

    return tiles


def build_image(wall, pill=None):
    lab = [[1, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 0, 1, 1, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]
           ]

    wm = get_mask(wall)

    if pill is not None:
        pm = get_mask(pill)

    tiled = Image.new(mode="P", size=(16 * 6, 16 * 8), color=6)
    tiled.putpalette(wall.getpalette())

    tiled.paste(Image.new(mode="P", size=(16 * 6, 16 * 2), color=0), (0, 16 * 6))

    for y in range(8):
        for x in range(6):
            entry = lab[y][x]

            if entry == 1:
                tiled.paste(wall, (16 * x, 16 * y), mask=wm)
            elif (entry == 0) and (pill is not None) and y < 7:
                tiled.paste(pill, (16 * x, 16 * y), mask=pm)

    # tiled.show()

    return tiled


"""

Purpose: generate the tile data needed to draw the level

Loads the various level graphics sets (7 of them) and generates the 7 tiles needed for displaying pills on the floor:
0: empty (no wall touching)
1: wall corner upper left corner
2: wall above, but only one
3: wall above, both
4: wall to the left, only one
6: wall to the left, both

the numbers are corresponding to the bits where the neighboring walls are:
1 top left, 2 top, 4 left

  1            2 
         +------------+
         |\  |        |
         |__\|        | 
  4      |            |  
         |            |
         +------------+
         
Image above shows the cell for the 1 configuration

for 2 it looks like this:

         +------------+
         |\           |
         |  \_________| 
         |            |  
         |            |
         +------------+


for 3 like this:

         +------------+
         |\           |
         |__\_________| 
         |            |  
         |            |
         +------------+

and so on..

these 7 tiles are then combined with the 6 pill states (no pill, size 1, 2, 3, 4, 5)

"""


def write_game_tiles(input_dir, output_dir):
    img = Image.open(os.path.join(input_dir, "level1.png"))

    pills = (None, img.crop((81, 77, 97, 93)), img.crop((81, 60, 97, 76)), img.crop((81, 43, 97, 59)),
             img.crop((81, 26, 97, 42)), img.crop((81, 9, 97, 25)))

    for n in range(1, 8):
        img = Image.open(os.path.join(input_dir, "level%d.png" % n))
        wall = img.crop((21, 5, 42, 26))

        tiled = Image.new(mode="P", size=(16, 16 * 47), color=0)
        tiled.putpalette(wall.getpalette())

        for i, p in enumerate(pills):
            lab_img = build_image(wall, p)
            tiled.paste(grab_tiles(lab_img), (0, 7 * 16 * i))
            if i == 0:
                w1 = lab_img.crop((2 * 16, 6 * 16, 3 * 16, 7 * 16))
                w2 = lab_img.crop((16, 7 * 16, 33, 8 * 16))
                w3 = lab_img.crop((2 * 16, 7 * 16, 3 * 16, 8 * 16))

        tiled.paste(wall, (0, 16 * 42))

        empty = Image.new(mode="P", size=(16, 16), color=0)
        tiled.paste(empty, (0, 16 * 43))

        tiled.paste(w1, (0, 16 * 44))
        tiled.paste(w2, (0, 16 * 45))
        tiled.paste(w3, (0, 16 * 46))

        # tiled.show() # to debug

        write_data(bytearray(image_bytes(bytearray(tiled.getdata()), 4)),
                   os.path.join(output_dir, "wall_gfx_set_%d" % n))

        pal = wall.getpalette()
        pal = [pal[i:i + 3] for i in range(3, 16 * 3, 3)]
        pb = bytearray()
        append_palette(pal, pb)

        write_data(pb, os.path.join(output_dir, "palette_gfx_set_%d" % n))
