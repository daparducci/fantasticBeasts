from django.contrib import admin
from .models import Beast, Feeding, Toy
# Register your models here.

admin.site.register(Beast)
admin.site.register(Feeding)
admin.site.register(Toy)