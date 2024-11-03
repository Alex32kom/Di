from django.contrib import admin

from .models import Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

    class Media:
        css = {
            "all": ("css/style2.css",)
        }


admin.site.register(Skill, SkillAdmin)
