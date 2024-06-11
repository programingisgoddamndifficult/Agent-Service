# views.py
from django.http import HttpResponse
from django.shortcuts import render
import requests
def home_view(request):
    return HttpResponse("Welcome to the Monitor Platform")  # 根路径的响应内容可以根据需要进行修改
def monitor_view(request):
    # 从服务器获取监控数据
    response = requests.get('http://localhost:8000/api/monitor')
    monitor_data = response.json()  # 将响应解析为JSON格式数据

    # 将数据传递给模板
    return render(request, 'monitor.html', {'monitor_data': monitor_data})
