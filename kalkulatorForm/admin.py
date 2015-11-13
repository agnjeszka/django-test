from django.contrib import admin

# Register your models here.
from .forms import ZamowienieForm
from .models import Zamowienie

class ZamowienieAdmin(admin.ModelAdmin):
    list_display = ["__str__" ]
    form = ZamowienieForm
   # class Meta:
       # model = Zamowienie

admin.site.register(Zamowienie, ZamowienieAdmin)
