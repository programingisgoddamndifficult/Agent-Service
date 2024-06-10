#负责与服务器通信的模块
import requests

def send_data(host_info, utilization_data, service_data):
    # 将采集到的信息打包成JSON格式
    data = {
        'host_info': host_info,
        'utilization_data': utilization_data,
        'service_data': service_data,
    }

    # 发送HTTP请求将数据传递给服务器
    response = requests.post('http://server-url/api/monitor', json=data)
    # 处理服务器的响应