from django.contrib import admin

from .models import Usuario

#from .models import Figurinha, Troca

# class FigurinhaAdmin(admin.ModelAdmin):
#    ...

# class TrocaAdmin(admin.ModelAdmin):
#    ...


#admin.site.register(Figurinha, Troca)

admin.site.register(Usuario)
