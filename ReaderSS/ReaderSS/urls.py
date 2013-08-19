from django.conf.urls import patterns, include, url
from homepage.views import HomeIndexView, HomeLogoutView, HomeRegisterView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url( r'^$', HomeIndexView.as_view(), name='index'),
    url( r'^logout/', HomeLogoutView.as_view(), name='logout_page' ),
    url( r'^register/', HomeRegisterView.as_view(), name='register_page' ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
