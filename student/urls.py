from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.student_list, name='student_list'),
    url(r'^student/(?P<pk>\d+)/$',
        views.student_detail,
        name='student_detail'),
    url(r'^student/new/$', views.student_new, name='student_new'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit'),
]
