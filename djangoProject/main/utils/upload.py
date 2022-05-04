
def image_directory_path(instance, filename):
    return f'images/{instance.id}/{filename}'


def file_directory_path(instance, filename):
    return f'files/{instance.id}/{filename}'
