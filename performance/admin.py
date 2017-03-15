from django.contrib import admin

from .models import Algorithm, Cluster, Performance

admin.site.register(Algorithm)
admin.site.register(Cluster)
admin.site.register(Performance)