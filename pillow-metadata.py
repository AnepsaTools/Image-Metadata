from PIL import Image as pil
from PIL import ExifTags

images = ["IMG20230222085746.jpg"]

pilTag = [
    315,
    33432,
    0x9286,
]

value_tag = [
    "Escritorio C48CWEc7741",
    "18,000",
    ["{\"object_name\": \"Escritorio C48CWEc7741\", \"object_price\": \"18,000\"}"]
]


for image in images:

    image_path = "origin/{}".format(image)
    pil_tag = pil.open(image_path)
    img_tag = pil_tag.getexif()

    for tag, value in zip(pilTag, value_tag):
        img_tag[tag] = value
    output_fp = image
    pil_tag.save(output_fp, exif=img_tag)
    pil_tag.close()
    print(image)

    pil_tag = pil.open(output_fp)
    img_tag = pil_tag.getexif()
    
    for tag in pilTag:
        try:
            name_tag = ExifTags.TAGS[tag]
            value = img_tag[tag]
        except:
            print("Don´t exist de tag  {} from EXIF data library pillow")
            continue

        print("{}: {}".format(name_tag, value))
