import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","p11get_post")

import django
django.setup()

from django.core.files.storage import FileSystemStorage

def storage_image(image):
    fs=FileSystemStorage()
    file=fs.save(image.name,image)
    file_url=fs.url(file)
    return file_url
    