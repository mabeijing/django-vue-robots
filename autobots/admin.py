from django.contrib import admin
from .models import Question, Choice, TbMenus, TbRules, TbUsers

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TbUsers)
admin.site.register(TbRules)
admin.site.register(TbMenus)
