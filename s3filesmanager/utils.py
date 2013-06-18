from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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