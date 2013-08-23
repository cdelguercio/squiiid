import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.middleware.csrf import get_token

from squiiid.models import SquiiidImage
from squiiid.models import Invite

def index(request):
    if request.user.is_authenticated():
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('index.html', c)
    else:
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('index.html', c)

def dashboard(request):
    if request.user.is_authenticated():
        images = SquiiidImage.objects.filter(profile_id=request.user.get_profile().id)
        
        if images.count() == 0:
            return HttpResponseRedirect(reverse('squiiid.views.first_intro'))
        else:
            c = RequestContext(request, {
                'csrf': get_token(request),
                'images': images,
            })
            return render_to_response('dashboard.html', c)
    else:
        return HttpResponseRedirect(reverse('squiiid.views.index'))

def first_intro(request):
    if request.user.is_authenticated():
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('first_intro.html', c)
    else:
        return HttpResponseRedirect(reverse('squiiid.views.index'))

def first_upload(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            upload(request)
            # TODO need to check if upload is legit
            return HttpResponseRedirect(reverse('squiiid.views.first_settings'))

        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('first_upload.html', c)
    else:
        return HttpResponseRedirect(reverse('squiiid.views.index'))

def first_settings(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            settings(request)
            # TODO need to check if settings legit
            return HttpResponseRedirect(reverse('squiiid.views.dashboard'))
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('first_settings.html', c)
    else:
        return HttpResponseRedirect(reverse('squiiid.views.index'))

def dashboard_settings(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            settings(request)
            # TODO need to check if settings legit
            return HttpResponseRedirect(reverse('squiiid.views.dashboard'))
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('dashboard.html', c)
    else:
        return HttpResponseRedirect(reverse('squiiid.views.index'))

def settings(request):
    request.user.first_name = request.POST.get('first_name', '')
    request.user.last_name = request.POST.get('last_name', '')
    request.user.get_profile().website = request.POST.get('website', '')
    
    request.user.save()
    request.user.get_profile().save()

def get_exif(request):
    pass

def upload_image(request):
    handle_uploaded_file(request.FILES.get('file', None))
    return render_to_response('dashboard.html')

def handle_uploaded_file(f):
    with open('/home/chris/workspace/squiiid/squiiid_com/media/images/test.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def dashboard_upload(request):
    if request.user.is_authenticated():
        upload(request)

        return HttpResponseRedirect(reverse('squiiid.views.upload_complete'))
    
    return HttpResponseRedirect(reverse('squiiid.views.index'))

def upload(request):
    profile = request.user.get_profile()
    image = request.FILES.get('file', None)
    title = request.POST.get('title', 'Title')
    tags = request.POST.get('tags', '')
    contributor_type_1 = request.POST.get('contributor_type_1', '')
    contributor_type_2 = request.POST.get('contributor_type_2', '')
    contributor_type_3 = request.POST.get('contributor_type_3', '')
    contributor_type_4 = request.POST.get('contributor_type_4', '')
    contributor_type_5 = request.POST.get('contributor_type_5', '')
    contributor_name_1 = request.POST.get('contributor_name_1', '')
    contributor_name_2 = request.POST.get('contributor_name_2', '')
    contributor_name_3 = request.POST.get('contributor_name_3', '')
    contributor_name_4 = request.POST.get('contributor_name_4', '')
    contributor_name_5 = request.POST.get('contributor_name_5', '')
    street_address_1 = request.POST.get('street_address_1', '')
    street_address_2 = request.POST.get('street_address_2', '')
    city = request.POST.get('city', '')
    state = request.POST.get('state', '')
    zip_code = request.POST.get('zip_code', '')
    place = request.POST.get('place', '')
    tool = request.POST.get('tool', '')
    iso = request.POST.get('iso', '')
    aperture = request.POST.get('aperture', '')
    exposure = request.POST.get('exposure', '')
    focal_length = request.POST.get('focal_length', '')
    private = request.POST.get('private', '')
    brand_1 = request.POST.get('brand_1', '')
    brand_2 = request.POST.get('brand_2', '')
    brand_3 = request.POST.get('brand_3', '')
    brand_4 = request.POST.get('brand_4', '')
    brand_5 = request.POST.get('brand_5', '')
    product_1 = request.POST.get('product_1', '')
    product_2 = request.POST.get('product_2', '')
    product_3 = request.POST.get('product_3', '')
    product_4 = request.POST.get('product_4', '')
    product_5 = request.POST.get('product_5', '')
    product_url_1 = request.POST.get('product_url_1', '')
    product_url_2 = request.POST.get('product_url_2', '')
    product_url_3 = request.POST.get('product_url_3', '')
    product_url_4 = request.POST.get('product_url_4', '')
    product_url_5 = request.POST.get('product_url_5', '')
    date = datetime.datetime.now()

    new_squiiid_image = SquiiidImage(profile=profile,
                                     image=image,
                                     title=title,
                                     tags=tags,
                                     contributor_type_1=contributor_type_1,
                                     contributor_type_2=contributor_type_2,
                                     contributor_type_3=contributor_type_3,
                                     contributor_type_4=contributor_type_4,
                                     contributor_type_5=contributor_type_5,
                                     contributor_name_1=contributor_name_1,
                                     contributor_name_2=contributor_name_2,
                                     contributor_name_3=contributor_name_3,
                                     contributor_name_4=contributor_name_4,
                                     contributor_name_5=contributor_name_5,
                                     street_address_1=street_address_1,
                                     street_address_2=street_address_2,
                                     city=city,
                                     state=state,
                                     zip_code=zip_code,
                                     place=place,
                                     tool=tool,
                                     iso=iso,
                                     aperture=aperture,
                                     exposure=exposure,
                                     focal_length=focal_length,
                                     private=private,
                                     brand_1=brand_1,
                                     brand_2=brand_2,
                                     brand_3=brand_3,
                                     brand_4=brand_4,
                                     brand_5=brand_5,
                                     product_1=product_1,
                                     product_2=product_2,
                                     product_3=product_3,
                                     product_4=product_4,
                                     product_5=product_5,
                                     product_url_1=product_url_1,
                                     product_url_2=product_url_2,
                                     product_url_3=product_url_3,
                                     product_url_4=product_url_4,
                                     product_url_5=product_url_5,
                                     date=date,
                                     )
    new_squiiid_image.save()

def upload_complete(request):
    return render_to_response('upload_complete.html')

def image(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    c = RequestContext(request, {
            'csrf': get_token(request),
            'image': image,
        })
    return render_to_response('image.html', c)

def image_details(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    c = RequestContext(request, {
            'csrf': get_token(request),
            'image': image,
        })
    return render_to_response('image_details.html', c)

def edit(request, image_id):
    if request.user.is_authenticated():
        image = SquiiidImage.objects.get(pk=image_id)
        if request.user.get_profile() == image.profile:
            if request.method == 'POST':
                image.title = request.POST.get('title', 'Title')
                image.tags = request.POST.get('tags', '')
                image.contributor_type_1 = request.POST.get('contributor_type_1', '')
                image.contributor_type_2 = request.POST.get('contributor_type_2', '')
                image.contributor_type_3 = request.POST.get('contributor_type_3', '')
                image.contributor_type_4 = request.POST.get('contributor_type_4', '')
                image.contributor_type_5 = request.POST.get('contributor_type_5', '')
                image.contributor_name_1 = request.POST.get('contributor_name_1', '')
                image.contributor_name_2 = request.POST.get('contributor_name_2', '')
                image.contributor_name_3 = request.POST.get('contributor_name_3', '')
                image.contributor_name_4 = request.POST.get('contributor_name_4', '')
                image.contributor_name_5 = request.POST.get('contributor_name_5', '')
                image.street_address_1 = request.POST.get('street_address_1', '')
                image.street_address_2 = request.POST.get('street_address_2', '')
                image.city = request.POST.get('city', '')
                image.state = request.POST.get('state', '')
                image.zip_code = request.POST.get('zip_code', '')
                image.place = request.POST.get('place', '')
                image.tool = request.POST.get('tool', '')
                image.iso = request.POST.get('iso', '')
                image.aperture = request.POST.get('aperture', '')
                image.exposure = request.POST.get('exposure', '')
                image.focal_length = request.POST.get('focal_length', '')
                image.private = request.POST.get('private', '')
                image.brand_1 = request.POST.get('brand_1', '')
                image.brand_2 = request.POST.get('brand_2', '')
                image.brand_3 = request.POST.get('brand_3', '')
                image.brand_4 = request.POST.get('brand_4', '')
                image.brand_5 = request.POST.get('brand_5', '')
                image.product_1 = request.POST.get('product_1', '')
                image.product_2 = request.POST.get('product_2', '')
                image.product_3 = request.POST.get('product_3', '')
                image.product_4 = request.POST.get('product_4', '')
                image.product_5 = request.POST.get('product_5', '')
                image.product_url_1 = request.POST.get('product_url_1', '')
                image.product_url_2 = request.POST.get('product_url_2', '')
                image.product_url_3 = request.POST.get('product_url_3', '')
                image.product_url_4 = request.POST.get('product_url_4', '')
                image.product_url_5 = request.POST.get('product_url_5', '')
                image.save()
                
                c = RequestContext(request, {
                    'csrf': get_token(request),
                    'image': image,
                })
                return render_to_response('edit_complete.html', c)
            c = RequestContext(request, {
                    'csrf': get_token(request),
                    'image': image,
                })
            return render_to_response('edit.html', c)
        return HttpResponseRedirect(reverse('squiiid.views.dashboard'))
    return HttpResponseRedirect(reverse('squiiid.views.dashboard'))

def delete(request, image_id):
    if request.user.is_authenticated():
        image = SquiiidImage.objects.get(pk=image_id)
        if request.user.get_profile() == image.profile:
            image.delete()
    return HttpResponseRedirect(reverse('squiiid.views.dashboard'))

def like(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    image.likes = image.likes + 1

def click(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    image.clicks = image.clicks + 1

def hover(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    image.hovers = image.hovers + 1

def reblog(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    image.reblogs = image.reblogs + 1

def invite(blog_urlrequest):
    email = request.POST['email']
    blog_url = request.POST['blog_url']
    
    invite = Invite(email=email,blog_url=blog_url)
    invite.save()
    return ''