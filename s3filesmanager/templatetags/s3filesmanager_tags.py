from django import template

from s3filesmanager.utils import get_page
from s3filesmanager.models import S3File

register = template.Library()


@register.inclusion_tag('s3filesmanager/s3filesmanager.html', takes_context=True)
def s3filesmanager(context, *args, **kwargs):
    request = context['request']
    if request.user.is_authenticated():
        paginator = get_page(request, S3File.objects.filter(owner=request.user).order_by('-created'), 10)
        context = {
            'paginator': paginator,
        }
        return context
    return {'paginator': None}


@register.inclusion_tag('s3filesmanager/s3filesmanager_js.html', takes_context=True)
def s3filesmanager_js(context, *args, **kwargs):
    return {}