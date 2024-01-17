from .views import *
def site_context(request):
    current_site = get_current_site(request)
    sites = Site.objects.all()
    return {'current_site': current_site, 'sites': sites}