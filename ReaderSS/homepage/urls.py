from django.conf.urls import patterns, include, url
from homepage.views import HomeIndexView, HomeLoginView, HomeLogoutView, HomeRegisterView

urlpatterns = patterns('',
    url( r'^$', HomeIndexView.as_view(), name='index'),
    url( r'^logout/', HomeLogoutView.as_view(), name='logout_page' ),
    url( r'^login/', HomeLoginView.as_view(), name='login_page' ),
    url( r'^register/', HomeRegisterView.as_view(), name='register_page' ),
)
