from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# L***_123pd,s.c
# P***_123pp,mta
# Register your models here.
# from django.contrib import admin
from .models import Post

admin.site.register(Post)

# Custom

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()