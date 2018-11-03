from django.conf.urls import url
from . import views

app_name='[class_web]'
urlpatterns = [
   url(r'^$',views.index,name='index'),
   url(r'^news/$',views.news,name='news'),
   url(r'^notes/$',views.notes,name='notes'),
   url(r'^actives/$',views.actives,name='actives'),
   url(r'^new/(?P<news_id>\d+)/$',views.new,name='new'),
   url(r'^note/(?P<note_id>\d+)/$',views.note,name='note'),
   url(r'^active/(?P<active_id>\d+)/$',views.active,name='active'),
   url(r'^download/$',views.download,name='download'),
   url(r'^messge/$',views.messge,name='messge'),
   url(r'^login/$', views.acc_login,name='acc_login'),
   url(r'^logout/$',views.acc_logout,name='acc_logout'),
   url('^login/edito/$',views.adminindex,name='adminindex')
]