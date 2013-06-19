from squiiid.models import SquiiidImage
from squiiid.models import Invite

def index(request):
    if request.user.is_authenticated():
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('index.php', c)
    else:
        c = RequestContext(request, {
            'csrf': get_token(request),
        })
        return render_to_response('index.php', c)

def image(request, image_id):
    image = SquiiidImage.objects.get(pk=image_id)
    c = RequestContext(request, {
            'csrf': get_token(request),
            'image_url': image.url,
        })
    return render_to_response('image.html', c)

def invite(request):
    invite = Invite(email=request.POST['email'],blog_url=request.POST['blog_url'])
    invite.save()
    return ''