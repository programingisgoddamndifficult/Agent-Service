#负责采集技术栈和服务信息的模块
import logging

service_data={}
def collect_service_info():
    # 遍历已安装的服务和组件，识别技术栈并采集相应的信息
    installed_services = get_installed_services()
    global service_data
    for service in installed_services:
        tech_stack = identify_tech_stack(service)
        service_metrics = collect_metrics(service)

        service_data[service] = {
            'tech_stack': tech_stack,
            'metrics': service_metrics,
            # 其他信息
        }

    # 将采集到的信息保存在全局变量中
    # global service_data
    logging.info('Service Info: %s', service_data)

    service_data = service_data


def identify_tech_stack(service):
    # 根据服务的名称或其他信息来识别服务的技术栈
    # 返回技术栈信息
    if service == 'SpringBoot':
        return 'Java'
    elif service == 'Flask':
        return 'Python'
    else:
        return 'Unknown'

def collect_metrics(service):
    if service == 'SpringBoot':
        # 采集SpringBoot服务的指标数据和调用链信息的代码
        metrics = {
            'active_sessions': 100,
            'requests': 500,
            'http_sessions': 50
        }
        call_chain = ['ServiceA', 'ServiceB', 'ServiceC']
        return {
            'metrics': metrics,
            'call_chain': call_chain
        }
    elif service == 'Flask':
        # 采集Flask服务的指标数据和调用链信息的代码
        metrics = {
            'active_sessions': 50,
            'requests': 200,
            'http_sessions': 20
        }
        call_chain = ['ServiceX', 'ServiceY']
        return {
            'metrics': metrics,
            'call_chain': call_chain
        }
    else:
        return {
            'metrics': {},
            'call_chain': []
        }

def get_installed_services():
    # 获取已安装的服务和组件列表
    # 返回已安装的服务和组件列表
    installed_services = ['SpringBoot', 'Flask', 'ServiceA', 'ServiceB']
    return installed_services