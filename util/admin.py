from django.contrib import admin

from util.models import HfUser, Category, Criterion


admin.site.register(HfUser)
admin.site.register(Category)
admin.site.register(Criterion)
