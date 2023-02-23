from PIL import Image
im = Image.open("without-metadata/IMG20230222085746.jpg")
exif = im.getexif()
exif[37511] = ["{\"object_name\": \"Escritorio C48CWEc7741\", \"object_price\": \"18,000\"}"]
im.save("out.jpg", exif=exif)