
def video_image_directory_path(instance, filename):
    return f'videos//{instance.id}/images/{filename}'


def video_file_directory_path(instance, filename):
    return f'videos//{instance.id}/files/{filename}'
