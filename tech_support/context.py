# -*- coding: utf-8 -*-
from django.template import RequestContext

def menu_processor(request):
    path = request.path.split('/')[1]
    return {
        'path': path,
    }
