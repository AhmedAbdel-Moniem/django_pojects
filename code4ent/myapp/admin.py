from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.site_header = 'Code For Ent'
admin.site.site_title = 'code for ent'


class MyappAdmin(admin.ModelAdmin):
    fields = ['title', 'hint', 'description']
    list_display = ['title', 'hint', 'summary', 'price', 'description', 'title_price']
    list_display_links = ['hint']
    list_editable = ['title']
    list_filter = ['price', 'hint']
    search_fields = ['title', 'hint']

    def title_price(self, obj):
        return "{} - {}".format(obj.title, obj.price)


admin.site.register(Product, MyappAdmin)
