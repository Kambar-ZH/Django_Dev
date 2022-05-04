import os
from django.core.exceptions import ValidationError

from main.utils.constants import DOCUMENT_TEMPLATE_FILE_ALLOWED_EXTENSIONS, DOCUMENT_TEMPLATE_MAX_FILE_SIZE, \
    IMAGE_MAX_FILE_SIZE, IMAGE_ALLOWED_EXTENSIONS


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() in DOCUMENT_TEMPLATE_FILE_ALLOWED_EXTENSIONS:
        raise ValidationError('Unsupported file extension.')


def validate_file_size(value):
    if value.size > DOCUMENT_TEMPLATE_MAX_FILE_SIZE:  # 10 MB
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    else:
        return value


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() in IMAGE_ALLOWED_EXTENSIONS:
        raise ValidationError('Unsupported file extension.')


def validate_image_size(value):
    if value.size > IMAGE_MAX_FILE_SIZE:  # 10 MB
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    else:
        return value
