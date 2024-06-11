from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home_view),  # 添加根路径的视图函数
    path('monitor_view/',views.monitor_view)
]