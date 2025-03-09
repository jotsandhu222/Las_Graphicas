from .models import TShirt, Polo, PoloImage

from django.contrib import admin

class PoloImageInline(admin.TabularInline):
    model = PoloImage
    extra = 1  # Number of empty forms to display

class PoloAdmin(admin.ModelAdmin):
    inlines = [PoloImageInline]
    
admin.site.register(TShirt)
#admin.site.register(Polo)




admin.site.register(Polo, PoloAdmin)
admin.site.register(PoloImage)