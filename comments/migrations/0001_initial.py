# Generated by Django 4.2 on 2024-06-20 14:41

import comments.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=-1,
                        scale=None,
                        size=[320, 240],
                        upload_to=comments.models.image_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "gif", "png"]
                            )
                        ],
                    ),
                ),
                (
                    "text_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=comments.models.file_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["txt"]
                            ),
                            comments.models.validate_file_size,
                        ],
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="comments.comment",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
