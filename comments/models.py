import os
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.core.exceptions import ValidationError


def validate_file_size(value):
    limit = 102 * 1024
    if value.size > limit:
        raise ValidationError(f"The file must not exceed 100 KB")


def generate_unique_filename(instance, filename, subdirectory):
    _, extension = os.path.splitext(filename)
    unique_filename = f"{slugify(instance.user_name)}-{uuid.uuid4()}.{extension}"
    return os.path.join(f"uploads/{subdirectory}", unique_filename)


def image_path(instance, filename):
    return generate_unique_filename(instance, filename, 'images')


def file_path(instance, filename):
    return generate_unique_filename(instance, filename, 'files')


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )

    image = ResizedImageField(
        upload_to=image_path,
        null=True,
        blank=True,
        size=[320, 240],
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "gif", "png"]
            ),
        ]
    )

    text_file = models.FileField(
        null=True,
        blank=True,
        upload_to=file_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["txt"],
            ),
            validate_file_size
        ]
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text
