
def image_directory_path(instance, filename):
    return f'images/{instance.id}/{filename}'


def video_file_directory_path(instance, filename):
    return f'videos/{instance.id}/{filename}'
