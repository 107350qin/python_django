from django.conf.urls import url
from . import views
app_name='polls'


urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^polls/(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^polls/(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	url(r'^polls/(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote')
	
]