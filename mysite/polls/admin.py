from django.contrib import admin
# 导入Question的模型
from .models import Question, Choice

# Register your models here.


# 在admin页面注册Question模型,可以让我们在admin页面管理模型
# admin.site.register(Question)
# admin.site.register(Choice)


# 将choice选择的行数增加至三行(StackedInline表示行数分散显示,TabularInline表示紧凑显示)
class ChoiceInline(admin.StackedInline):
    # 设置模型
    model = Choice
    # 设置行数
    extra = 3


# 自定义Admin页面,继承ModelAdmin
class QuestionAdmin(admin.ModelAdmin):
    # 调换默认的时间和问题的位置.默认是问题在前,时间在后
    # fields = ['pub_date', 'question_text']

    # 添加说明栏,此处在'pub_date'上添加'Date information'一栏显示在admin页面作为介绍,classes能够隐藏说明的内容
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    # inlines将choice的行数设置添加
    inlines = [ChoiceInline]
    # list_display详细显示问题的内容,时间,是否现在创建等等
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter按照问题创建时间创造一个过滤器
    list_filter = ['pub_date']
    # search_fields增加一个搜索栏用来搜索question_text的内容
    search_fields = ['question_text']
    # 其他还有change list pagination; search boxes; filters, date-hierarchies; column-header-ordering等功能


# 注册模型和自定义模型的更改
admin.site.register(Question, QuestionAdmin)