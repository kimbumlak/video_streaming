from django.contrib import admin
from .models import Video, Comment
# from .models import MyAwesomeModelWithFiles
# Register your models here.

# class MyAwesomeModelWithFiles(admin.ModelAdmin):
#     change_form_template = 'progressbarupload/change_form.html'
#     add_form_template = 'progressbarupload/chage_form.html'

# admin.site.register(MyAwesomeModelWithFiles, UploadFileModelAdmin)
admin.site.register([Video, Comment])
