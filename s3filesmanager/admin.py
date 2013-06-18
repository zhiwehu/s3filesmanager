from django.contrib import admin

from .s3filesmanager.models import S3File


class S3FileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'file_name', 'file_size', 's3_file', 'thumbnail_url', 'created', 'modified')


admin.site.register(S3File, S3FileAdmin)