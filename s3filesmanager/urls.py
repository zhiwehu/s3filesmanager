from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^files/$', 's3filesmanager.views.file_list', name='file_list'),
                       url(r'^files/upload/$', 's3filesmanager.views.upload_file', name='file_upload'),
                       url(r'^files/delete/$', 's3filesmanager.views.delete_files', name='delete_files'),
)