from django.contrib import admin
from .models import post
from .models import user
from .models import comments
from .models import topic
from .models import audienceuser
# Register your models here.

class datadisplay(admin.ModelAdmin):
    search_fields = ('name','email')
    list_display=('name', 'email', 'mobile', 'profile')
    #list_display
    
admin.site.register(post)
admin.site.register(user)
admin.site.register(comments)
admin.site.register(topic)
admin.site.register(audienceuser,datadisplay)
