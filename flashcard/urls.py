from django.conf.urls import patterns, url
from flashcard import views


urlpatterns = patterns('',
                       url(r'^tags/$', views.tags, name='tags'),
                       url(r'^words/$', views.words, name='words'),
                       url(r'^deck/$', views.deck, name='deck'),
                       url(r'^play/$', views.play, name='play'),
                       url(r'^load/$', views.load, name='load'),
                       # url(r'^deck/(.*)$', name='deck'),
                       # url(r'^%splay/(.*)$' % prefix, name='play'),
                       # url(r'^%stag/(.*)$' % prefix, name='tag'),
                       # url(r'^%sword/(.*)$' % prefix, name='word'),
                       # url(r'^gdata/$', views.gdata,
                       #     name='import_from_google'),
                       url(r'^cleardb/$', views.cleardb, name='cleardb'),
                       )
