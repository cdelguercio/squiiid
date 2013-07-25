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
        
        c = RequestContext(request, {
            'csrf': get_token(request),
            'images': images,
        })
        return render_to_response('dashboard.html', c)
    else:
        return HttpResponseRedirect(reverse('squiiid.views.index'))

def get_exif(request):
    pass

def upload(request):
    if request.user.is_authenticated():
        profile = request.user.get_profile()
        #image = request.FILES.get('image', None)
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
                                         image=None,
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

        return HttpResponseRedirect(reverse('squiiid.views.upload_complete'))
    
    return HttpResponseRedirect(reverse('squiiid.views.index'))
        

def upload_complete(request):
    return render_to_response('upload_complete.html')

def image(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    c = RequestContext(request, {
            'csrf': get_token(request),
            'image_url': image.url,
        })
    return render_to_response('image.html', c)

def invite(blog_urlrequest):
    email = request.POST['email']
    blog_url = request.POST['blog_url']
    
    invite = Invite(email=email,blog_url=blog_url)
    invite.save()
    return ''