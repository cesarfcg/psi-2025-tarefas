from django.contrib import admin
from . models import Postagem,Header,Footer
# Register your models here.
admin.site.register(Postagem)
admin.site.register(Header)
admin.site.register(Footer)