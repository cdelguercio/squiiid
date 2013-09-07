from django.conf.urls import patterns, include, url

from userena import views as userena_views
from userena.forms import SignupFormOnlyEmail
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.contrib.auth.forms import AdminPasswordChangeForm

urlpatterns = patterns('',
    url(r'^$', 'squiiid.views.index', name='index'),

### userena

    url(r'^accounts/', include('userena.urls')),
    url(r'^signout/$',
        userena_views.signout,
        {'template_name': 'signout.html',
         'next_page': '/'}),
    url(r'^signin/$',
        userena_views.signin,
        {'template_name': 'signin.html'}),
    url(r'^signup/$',
        userena_views.signup,
        {
            'signup_form': SignupFormOnlyEmail,
            'template_name': 'signup.html',
            'success_url': '/dashboard/',
        }),

    url(r'^password/reset$',
        auth_views.password_reset,
        {'template_name': 'userena/password_reset_form.html',
         'email_template_name': 'userena/emails/password_reset_message.txt'},
        name='userena_password_reset'),
    url(r'^password/reset/done/$',
       auth_views.password_reset_done,
       {'template_name': 'userena/password_reset_done.html'},
       name='userena_password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
       auth_views.password_reset_confirm,
       {'template_name': 'userena/password_reset_confirm_form.html'},
       name='userena_password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
       auth_views.password_reset_complete,
       {'template_name': 'userena/password_reset_complete.html'}),

### squiiid

    url(r'^dashboard/$', 'squiiid.views.dashboard', name='dashboard'),
    url(r'^dashboard/settings/$', 'squiiid.views.dashboard_settings', name='dashboard_settings'),
    url(r'^get_exif/$', 'squiiid.views.get_exif', name='get_exif'),
    url(r'^upload/$', 'squiiid.views.dashboard_upload', name='dashboard_upload'),
    url(r'^upload_complete/$', 'squiiid.views.upload_complete', name='upload_complete'),
    url(r'^image/(?P<image_id>\d+)/$', 'squiiid.views.image', name='image'),
    url(r'^image/details/(?P<image_id>\d+)/$', 'squiiid.views.image_details', name='image_details'),
    url(r'^edit/(?P<image_id>\d+)/$', 'squiiid.views.edit', name='edit'),
    url(r'^delete/(?P<image_id>\d+)/$', 'squiiid.views.delete', name='delete'),
    url(r'^like/(?P<image_id>\d+)/$', 'squiiid.views.like', name='like'),
    url(r'^click/(?P<image_id>\d+)/$', 'squiiid.views.click', name='click'),
    url(r'^hover/(?P<image_id>\d+)/$', 'squiiid.views.hover', name='hover'),
    url(r'^reblog/(?P<image_id>\d+)/$', 'squiiid.views.reblog', name='reblog'),
    url(r'^first_intro/$', 'squiiid.views.first_intro', name='first_intro'),
    url(r'^first_upload/$', 'squiiid.views.first_upload', name='first_upload'),
    url(r'^first_settings/$', 'squiiid.views.first_settings', name='first_settings'),
    url(r'^terms_of_use/$', 'squiiid.views.terms_of_use', name='terms_of_use'),
    url(r'^landing/$', 'squiiid.views.landing', name='landing'),
    url(r'^request_invite/$', 'squiiid.views.invite', name='invite'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)