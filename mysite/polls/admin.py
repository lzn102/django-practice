from django.contrib import admin
# 导入Question的模型
from .models import Question, Choice

# Register your models here.


# 在admin页面注册Question模型,可以让我们在admin页面管理模型
admin.site.register(Question)
admin.site.register(Choice)