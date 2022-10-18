from django.contrib import admin
from blog.models import Post,Contact,Kor
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','text','date']
admin.site.register(Post)
admin.site.register(Kor)
admin.site.register(Contact,ContactAdmin)