from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url( r'^$', 'homepage.views.index', name='index'),
    url( r'^logout/', 'homepage.views.logout_page', name='logout_page' ),
    url( r'^login/', 'homepage.views.login_page', name='login_page' ),
    url( r'^register/', 'homepage.views.register_page', name='register_page' ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
