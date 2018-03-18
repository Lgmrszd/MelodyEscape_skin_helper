import xml.etree.ElementTree
from PIL import Image, ImageDraw, ImageFont


# filenames
image_file = "character_skin.png"
image_save_file = "character_skin_borders.png"
areas_file = "skin_sprites_areas.xml"

# Colors, as (R, G, B, A)
dark_green = (0, 150, 0, 255)
purple = (255, 0, 255, 255)
black = (0, 0, 0, 255)

text_color = black
dor_color = dark_green
rectangle_color = dark_green

# Mode (True -- show image, False -- save with another filename)
SHOW = False


def main():
    im = Image.open(image_file)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 12)

    areas = xml.etree.ElementTree.parse(areas_file).getroot()
    dict_areas = []
    for area in areas:
        dict_area = {k: int(v) for k, v in {
            "x": area.get("X"),
            "y": area.get("Y"),
            "w": area.get("W"),
            "h": area.get("H"),
            "px": area.get("PX"),
            "py": area.get("PY"),
        }.items()}
        dict_area["name"] = area.get("Key")
        dict_areas.append(dict_area)

    for area in dict_areas:
        x, y, w, h, px, py, name = area["x"], area["y"], area["w"], area["h"], area["px"], area["py"], area["name"]
        draw.rectangle([(x, y), (x+w, y+h)], outline=rectangle_color)
        draw.rectangle([(x, y), (x+w, y+h)], outline=rectangle_color)
        draw.ellipse([(x+px-1, y+py-1), (x+px+1, y+py+1)], fill=dor_color)
        draw.text((x+2, y+2), name, font=font, fill=text_color)

    del draw
    if SHOW:
        im.show()
    else:
        im.save(image_save_file, "PNG")


if __name__ == '__main__':
    main()
