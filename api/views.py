from api.permissions import is_permissible
from revproxy.views import ProxyView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class ScidProxyView(UserPassesTestMixin, ProxyView):
    def test_func(self):
        return is_permissible(self.request.user)

    def handle_no_permission(self):
        raise PermissionDenied()
    
    upstream = 'http://localhost:3001/scid'