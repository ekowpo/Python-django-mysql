from django.conf.urls import url
from .import views
from views import SemesterView,semester_createview,SemesterView,SemesterUpdateView,SemesterDeleteView

app_name='students'

urlpatterns = [
    # /students
    url(r'^$', views.SemesterView.as_view()),
    url(r'^/create/$', views.SemesterView.as_view()),

    url(r'^semester/(?P<pk>[0-9]+)/$', views.SemeterDetailView.as_view()),

    url(r'^semester/create/$', views.semester_createview),

    url(r'^semester/(?P<pk>[0-9]+)/update/$', views.SemesterUpdateView.as_view()),
    url(r'^semester/(?P<pk>[0-9]+)/delete/$', views.SemesterDeleteView.as_view()),

]