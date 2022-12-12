
from django.contrib import admin
from .models import Label
from .models import Recipe

# Register your models here.
admin.site.register(Label)
admin.site.register(Recipe)
