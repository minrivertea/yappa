from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from products import views


urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^games/$', views.games, name="games"),
    #url(r'^add/$', views.add_question, name="add_question"),
    #url(r'^answer/([\w+])/$', views.answer_vote, name="answer_vote"),
    url(r'^games/(?P<slug>[\w-]+)/$', views.game, name="game"),
)

