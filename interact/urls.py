from django.conf.urls import url
from . import views
from .views import IndexView, CreateTest, AddClass, PracticeLandingView, AboutView, SignUpView
# from django.views.generic.edit import CreateView
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', SignUpView.as_view(), name='register'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^create_test/$', CreateTest.as_view(), name='create_test'),
    url(r'^add_class/$', AddClass.as_view(), name='add_class'),
    url(r'^student/(?P<id>\d+)/$', views.student, name='student'),
    url(r'^tutorial/([0-9]+)/$', views.test_tutorial, name='question_detail'),
    url(r'^practice_dashboard/$', PracticeLandingView.as_view(), name='practice'),
    url(r'^practice/(?P<difficulty_level>[0-9]+)/$', views.get_queryset_by_level, name='level'),
    url(r'^practice/choice/$', views.TestMultiChoiceView.as_view(), name='multiple_choice'),
    url(r'^practice/fraction/$', views.TestFractionView.as_view(), name='fraction_fill_in'),
    url(r'^practice/select/$', views.multiple_select, name='multiple_select'),
    url(r'^practice/drag/$', views.drag_and_drop, name='drag_and_drop'),
    url(r'^practice/fill/$', views.fill_blank, name='fill_blank'),
    url(r'^practice/bar/$', views.graph, name="graph"),
    url(r'^home/$', views.home, name='home')
    ]
