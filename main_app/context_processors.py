from .models import Membership

def memberships(request):
    return {'membership': Membership.objects.all()}