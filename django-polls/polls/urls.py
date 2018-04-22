from django.urls import path

from . import views

# 添加命名空间
app_name = 'polls'

# 子项目的路由要在项目入口 mysite 中引用

# urlpatterns = [
# 	path('', views.index, name="index"),
# 	path('<int:question_id>/', views.detail, name="detail"),
# 	path('<int:question_id>/results/', views.results, name="results"),
# 	path('<int:question_id>/vote/', views.vote, name="vote"),
# ]

urlpatterns = [
	
	path('', views.IndexView.as_view(), name="index"),
	path('<int:pk>/', views.DetailView.as_view(), name="detail"),
	path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
	path('<int:question_id>/vote/', views.vote, name="vote"),
]