from django.contrib import admin
from Jeapedu.models import *

class Course_admin(admin.ModelAdmin):
    list_display =('photo_tag','title','startdate',)
	
class Teachers_admin(admin.ModelAdmin):
    list_display =('photo_tag','name','kw',)
	
class Students_admin(admin.ModelAdmin):
    list_display =('photo_tag','name','kw',)
	
class News_admin(admin.ModelAdmin):
    list_display =('photo_tag','title',)
	
class Enterprise_admin(admin.ModelAdmin):
    list_display =('photo_tag','name',)

admin.site.register(Course,Course_admin)
admin.site.register(Teachers,Teachers_admin)
admin.site.register(Students,Students_admin)
admin.site.register(News,News_admin)
admin.site.register(Enterprise,Enterprise_admin)