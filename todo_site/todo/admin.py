from django.contrib import admin
from .models import Todo  # Replace Todo with the actual name of your model
# Register the model with the admin site
admin.site.register(Todo)
