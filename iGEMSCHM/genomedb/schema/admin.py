from django.contrib import admin



# Register your models here.from django.contrib import admin



# Register your models here.


from .models import HMM_profile

from .models import HMM_Output

from .models import Operon_Database

from .models import Gene

from .models import Accession

from .models import Species


admin.site.register(HMM_profile)

admin.site.register(HMM_Output)

admin.site.register(Operon_Database)

admin.site.register(Gene)

admin.site.register(Accession)

admin.site.register(Species)













