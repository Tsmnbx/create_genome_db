from django.contrib import admin



# Register your models here.

from .models import Species

from .models import Accession

admin.site.register(Species)

admin.site.register(Accession)




