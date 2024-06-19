import psutil
import os
import multiprocessing

def get_cpu_info():
    result = {}
    cpu_count = multiprocessing.cpu_count()
    result["cpu_count"] = cpu_count

    cpu_percent = psutil.cpu_percent(interval=1)  # 采样间隔1秒
    result["cpu_percent"] = str(round(cpu_percent,2))+"%"
    result["cpu_list_info"] = []
    # 获取每个CPU核心的使用情况
    cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=True)
    for i, cpustat in enumerate(cpu_times_percent):
        result["cpu_list_info"].append({"all":str(round(cpustat.user,2)+round(cpustat.system,2))+"%"})
    return result

def get_memory_info():
    # 获取内存信息
    memory = psutil.virtual_memory()
    result = {}
    result["total"] = str(round(memory.total / (1024.0 ** 3),2))+"GB"
    result["used"] = str(round(memory.used / (1024.0 ** 3),2))+"GB"
    result["percent"]=str(round(memory.used/memory.total*100,2))+"%"
    return result

def get_network_interface_info():
    network_interface_info=[]
    net_io_counters = psutil.net_io_counters(pernic=True)
    for interface, stats in net_io_counters.items():
        network_interface_info.append({"interface_name":interface,"recv_bytes":str(round(stats.bytes_recv,2))+"B","sent_bytes":str(round(stats.bytes_sent,2))+"B"})
    return network_interface_info

def get_disk_info():
    disk_info = []
    disk_usage = psutil.disk_usage("C:")
    disk_info.append({"partition":"C:","disk_total":str(round(disk_usage.total / (1024.0 ** 3),2))+"GB","disk_used":str(round(disk_usage.used / (1024.0 ** 3),2))+"GB",
                                    "disk_free":str(round((disk_usage.total -disk_usage.used)/(1024.0 ** 3),2))+"GB","disk_percent":str(round(disk_usage.used/disk_usage.total,2))+"%"})
    return disk_info

def merge_all_info():
    result = {}
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    network_interface_info = get_network_interface_info()
    disk_info = get_disk_info()

    result["cpu_info"] = cpu_info
    result["memory_info"] = memory_info
    result["interface_info"] = network_interface_info
    result["disk_info"] = disk_info

    return result

if __name__ == "__main__":
    print(merge_all_info())
