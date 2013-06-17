from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import filesizeformat
from django.utils import simplejson

from sorl.thumbnail import get_thumbnail

from .models import S3File


def get_page(request, items, count_per_page):
    paginator = Paginator(items, count_per_page)
    page = request.GET.get('page')
    try:
        paginator.object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator.object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator.object_list = paginator.page(paginator.num_pages)
    return paginator


@login_required
def file_list(request, template='s3filemanage/index.html', extra_context=None):
    paginator = get_page(request, S3File.objects.filter(owner=request.user).order_by('-created'), 10)
    context = {
        'paginator': paginator,
    }
    if extra_context:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))


@login_required
def upload_file(request):
    '''
    Upload file
    :param request:
    :return:
    '''
    if request.method == 'POST':
        # Get the file obj from request.FILES
        s3_file = request.FILES['file']

        # Create a new S3File object
        s3_file_obj = S3File(owner=request.user, file_name=s3_file.name, file_size=s3_file.size)

        # Save the file to storage
        s3_file_obj.s3_file.save(s3_file.name, s3_file)

        # Generate the thumbnail
        im = get_thumbnail(s3_file_obj.s3_file, '80x80', crop='center', quality=99)
        im_url = im.url.split('?')[0]
        s3_file_obj.thumbnail_url = im_url

        # Save the S3File object into db
        s3_file_obj.save()

        result_dict = {
            'file_id': s3_file_obj.id,
            'file_name': s3_file_obj.file_name,
            'file_size': filesizeformat(s3_file_obj.file_size),
            's3_file_url': s3_file_obj.s3_file.url,
            'thumbnail_url': s3_file_obj.thumbnail_url,
            'created': datetime.strftime(s3_file_obj.created, '%Y-%m-%d %H:%M:%S'),
            'modified': datetime.strftime(s3_file_obj.modified, '%Y-%m-%d %H:%M:%S')
        }

        return HttpResponse(simplejson.dumps(result_dict), mimetype='application/json')
    return HttpResponseNotAllowed(['POST', ])


@login_required
def delete_files(request):
    '''
    Delete files
    :param request:
    :return:
    '''
    if request.method == 'POST':
        file_id_list = request.POST.getlist('file_id', [])
        for file_id in file_id_list:
            try:
                file = S3File.objects.get(id=file_id, owner=request.user)
                file.s3_file.delete()
                file.delete()
            except S3File.DoesNotExist:
                pass
        return HttpResponseRedirect(reverse('file_list'))
    return HttpResponseNotAllowed(['POST', ])
