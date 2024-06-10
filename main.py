import hardware_info
import utilization_info
import service_info
# import communication

def main():
    # 获取主机信息
    host_info = hardware_info.get_host_info()

    # 获取主机利用率信息
    utilization_info.collect_utilization_info()

    print(host_info)
    print(utilization_info)

    # 获取技术栈和服务信息
    service_info.collect_service_info()
    #
    # # 与服务器通信
    # communication.send_data(host_info, utilization_info.utilization_data, service_info.service_data)

if __name__ == '__main__':
    main()