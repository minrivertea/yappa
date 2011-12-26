from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext

from products.models import *

#render shortcut
def render(request, template, context_dict=None, **kwargs):
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )


def home(request):
    featured_games = Product.objects.all()[:3]
    return render(request, 'products/home2.html', locals())
    

def games(request):
    categories = Category.objects.all().order_by('-order')
    return render(request, 'products/games.html' , locals())
    


def game(request, slug):
    game = get_object_or_404(Product, slug=slug)
    return render(request, 'products/game.html' , locals())