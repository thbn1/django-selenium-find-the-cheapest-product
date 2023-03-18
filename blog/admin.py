from django.contrib import admin
from .models import *

def run(self, request, queryset):
    id=request.POST.get('_selected_action')
    siteObj=self.model.objects.get(pk=id)
    self.message_user(request, "Running: " + siteObj.script)
    exec(open(siteObj.script).read())
run.short_description = "Run the script"

class SiteAdmin(admin.ModelAdmin):
    actions = [run]
    model = Site

# Register your models here.
admin.site.register(Site, SiteAdmin)