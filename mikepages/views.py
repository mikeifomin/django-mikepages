from django.shortcuts import render
import os
from models import Page
from django.template import loader, RequestContext
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.conf import settings

DEFAULT_TEMPLATE = "default.html"
DEFAULT_TEMPLATE_DIR = "smartpages"


def page(request, url):

    if not url.startswith('/'):
        url = '/' + url
    try:
        page_object = get_object_or_404(Page, slug__exact=url)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            page_object = get_object_or_404(Page, slug__exact=url)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise

    return render_page(request, page_object)


def render_page(request, page_object):


    po = page_object
    if po.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)

    wrp = lambda file: "%s/%s" % (DEFAULT_TEMPLATE_DIR, file)
    if po.template_name:
        tpl = loader.select_template((wrp(po.template_name), wrp(DEFAULT_TEMPLATE)))
    else:
        tpl = loader.get_template(wrp(DEFAULT_TEMPLATE))

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    po.title = mark_safe(po.title)
    po.content = mark_safe(po.content)
    po.h1 = mark_safe(po.h1)
    po.description = mark_safe(po.description)


    c = RequestContext(request, {
        'page': po,
    })

    response = HttpResponse(po.render(c))
    # populate_xheaders(request, response, FlatPage, f.id)
    return response

