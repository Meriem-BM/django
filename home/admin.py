from django.contrib import admin

from .models import Tutorial
from .forms import TutorialForm


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published')
    Serializer = TutorialForm


admin.site.register(Tutorial, TutorialAdmin)
