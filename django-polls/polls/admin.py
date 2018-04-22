

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice

# 注册模型，生成默认的后台管理表单用于展示
# StackedInline[换行显示], TabularInline[内联显示]
class ChoiceInline(admin.TabularInline):
	model = Choice
	# 默认空的插槽数
	extra = 1

# 更改显示数据
class QuestionAdmin(admin.ModelAdmin):
	# 内容信息
	# fields = ['pub_date', 'question_text']
	fieldsets = [
		(None, { 'fields': ['question_text'] }),
		('Date information', {'fields': ['pub_date']  }),
	]
	# 内联其他表
	inlines = [ChoiceInline]
	# 列表展示信息
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# 过滤器
	list_filter = ['pub_date']
	# 搜索
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)



