from PIL import Image
from PIL.ExifTags import TAGS

# Read ours images from current directory
image = Image.open('IMG20230222085746.jpg')

# Get the exif data from the image
exif_data = image._getexif()

# Loop through the exif data and print it
for tagId in exif_data:
    # Get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tagId, tagId)
    data = exif_data.get(tagId)
    # Decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")