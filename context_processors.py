from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404


from products.models import *


def common(request):
    from yappa import settings
    context = {}
    try:
        context['shopsettings'] = get_object_or_404(ShopSettings, is_active=True)
    except:
        pass
    context['ga_is_on'] = settings.GA_IS_ON

    return context

