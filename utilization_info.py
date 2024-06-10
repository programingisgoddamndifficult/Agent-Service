#负责采集主机利用率信息的模块
import psutil
import logging

def collect_utilization_info():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_traffic = psutil.net_io_counters()

    # 将采集到的信息保存在全局变量中
    global utilization_data
    utilization_data = {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage,
        'network_traffic': network_traffic,
    }

    # 记录utilization_info信息到日志
    logging.info('Utilization Info: %s', utilization_data)