from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE


from .models import Category_3D, Info_Modul_3D, Modul_Format_3D
# Register your models here.

class InLineInfo_Modul_3D(admin.TabularInline):
    model = Info_Modul_3D
    extra = 1
    max_num = 10

class Category_3D_Admin(admin.ModelAdmin):
    inlines = [InLineInfo_Modul_3D]
    
    list_display=(
        'category_name',     
    )
    ordering=(
        'category_name',      
    )
    # list_editable=(
    #     'category_name',
    # )
    list_display_links=(
        'category_name',      
    )
    search_fields=(
        'category_name',       
    )
    list_filter=(
        'category_name',       
    )


    fieldsets =(
        ( 'Kategoriya: ', {
            'fields' : [
                'category_name',
            ]
        }),
    )


class Modul_Format_3D_Admin(admin.ModelAdmin):
    list_display=(
        'modul_constructor',
        'modul_extension',    
    )
    ordering=(
        'modul_constructor',
        'modul_extension',      
    )
    # list_editable=(
    #     'modul_constructor',
    # )
    list_display_links=(
        'modul_constructor',
        'modul_extension',      
    )
    search_fields=(
        'modul_constructor',
        'modul_extension',       
    )
    list_filter=(
        'modul_constructor',
        'modul_extension',       
    )


    fieldsets =(
        ( 'Modul Format: ', {
            'fields' : [
                'modul_constructor',
                'modul_extension',
            ]
        }),
    )

class Info_Modul_3D_Admin(admin.ModelAdmin):
    list_display=(
        'modul_file', 
        'modul_images', 
        'modul_name', 
        'modul_description', 
        'modul_price', 
        'price_currency', 
        # 'modul_format', 
        'state_active', 
        'modul_animated', 
        'modul_printable', 
        'modul_primary_category', 
        # 'modul_secondary_categories', 
        'modul_author_name', 
        'modul_published', 
        'modul_updated',    
    )
    ordering=(
        # 'modul_file', 
        # 'modul_images', 
        # 'modul_name', 
        # 'modul_description', 
        'modul_price', 
        # 'price_currency', 
        # 'modul_format', 
        # 'state_active', 
        # 'modul_animated', 
        # 'modul_printable', 
        # 'modul_primary_category', 
        # 'modul_secondary_categories', 
        # 'modul_author_name', 
        'modul_published', 
        'modul_updated',        
    )
    list_editable=(
        # 'modul_file', 
        # 'modul_images', 
        'modul_name', 
        # 'modul_description', 
        'modul_price', 
        'price_currency', 
        # 'modul_format', 
        'state_active', 
        'modul_animated', 
        'modul_printable', 
        'modul_primary_category', 
        # 'modul_secondary_categories', 
        'modul_author_name', 
        # 'modul_published', 
        # 'modul_updated',  
    )
    list_display_links=(
        'modul_file', 
        'modul_images', 
        # 'modul_name', 
        'modul_description', 
        # 'modul_price', 
        # 'price_currency', 
        # 'modul_format', 
        # 'state_active', 
        # 'modul_animated', 
        # 'modul_printable', 
        # 'modul_primary_category', 
        # 'modul_secondary_categories', 
        # 'modul_author_name', 
        'modul_published', 
        'modul_updated',        
    )
    search_fields=(
        # 'modul_file', 
        # 'modul_images', 
        'modul_name', 
        'modul_description', 
        'modul_price', 
        'price_currency', 
        'modul_format', 
        'state_active', 
        'modul_animated', 
        'modul_printable', 
        'modul_primary_category', 
        'modul_secondary_categories', 
        'modul_author_name', 
        # 'modul_published', 
        # 'modul_updated',        
    )
    list_filter=(
        'modul_file', 
        'modul_images', 
        'modul_name', 
        # 'modul_description', 
        'modul_price', 
        'price_currency', 
        'modul_format', 
        'state_active', 
        'modul_animated', 
        'modul_printable', 
        'modul_primary_category', 
        'modul_secondary_categories', 
        'modul_author_name', 
        'modul_published', 
        'modul_updated',        
    )
    fieldsets = (
        ('3D Model Info', {
            "fields": (
                'modul_file', 
                'modul_images', 
                'modul_name', 
                'modul_description', 
                'modul_price', 
                'price_currency', 
                'modul_format', 
                'state_active', 
                'modul_animated', 
                'modul_printable', 
                'modul_primary_category', 
                'modul_secondary_categories', 
                'modul_author_name', 
                # 'modul_published', 
                # 'modul_updated',  
            ),
        }),
    )
    formfield_overrides={
        models.TextField : {'widget' : TinyMCE},
    }


admin.site.register(Category_3D, Category_3D_Admin)
admin.site.register(Modul_Format_3D, Modul_Format_3D_Admin)
admin.site.register(Info_Modul_3D, Info_Modul_3D_Admin)
