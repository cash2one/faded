from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group, Permission
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class MyAdminSite(AdminSite):
    site_title = _('JOYOTIME')
    site_header = _('JOYOTIME administration')
    index_title = _('JOYOTIME administration')


site = MyAdminSite(name='myadmin')

site.register(User)
site.register(Group)
site.register(Permission)
site.register(Site)
site.register(FlatPage)

