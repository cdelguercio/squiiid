from django.conf.urls import patterns, include, url

from userena import views as userena_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    url(r'^$', 'squiiid.views.index', name='index'),

### userena

    url(r'^accounts/', include('userena.urls')),

#    url(r'^signout/$',
#        userena_views.signout,
#        {'template_name': 'index.html',
#         'next_page': '/'}),
#    url(r'^modal_login/$',
#        userena_views.signin,
#        {'template_name': 'modal/modal_login.html'}),
#    url(r'^modal_signup/$', 'taggle.views.modal_signup', name='modal_signup'),
#    url(r'^try_again/$',
#        userena_views.signin,
#        {'template_name': 'try_again.html'}),
#    url(r'^first_login/$',
#        userena_views.signin,
#        {'template_name': 'first_login.html'}),
#    url(r'^printer/signup/$',
#        userena_views.signup,
#        {'signup_form': SignupFormPrinter,
#        'template_name': 'printer/printer_signup.html',
#        'success_url': '/first_login/',
#        }),
#    url(r'^club/signup/$',
#        userena_views.signup,
#        {'signup_form': SignupFormConsumer,
#        'template_name': 'consumer/consumer_signup.html',
#        'success_url': '/first_login/',
#        }),
                       
        url(r'^image/(?P<image_id>\d+)/$', 'squiiid.views.image', name='image'),
    # Examples:
    # url(r'^$', 'squiiid_com.views.home', name='home'),
    # url(r'^squiiid_com/', include('squiiid2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
