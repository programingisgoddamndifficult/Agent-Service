#负责获取主机硬件信息和操作系统信息的模块
import psutil
import platform
import logging

# 配置日志记录
logging.basicConfig(filename='app.log', level=logging.INFO)
def get_host_info():
    cpu_info = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    network_info = psutil.net_if_addrs()

    # 获取操作系统信息
    os_info = {
        'system': platform.system(),  # 操作系统名称
        'release': platform.release(),  # 操作系统版本
        'architecture': platform.machine()  # 操作系统架构
    }

    host_info = {
        'cpu_percent': cpu_info,
        'memory': memory_info,
        'network': network_info,
        # 操作系统信息
    }

    # 记录host_info信息到日志
    logging.info('Host Info: %s', host_info)

    return host_info