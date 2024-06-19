课题方向：一体化监控平台开发

课题背景介绍:
随着企业数字化转型开展，IT系统逐步上云，系统架构变得复杂，主机设备指数级增长，全栈使用PaaS组件、应用微服务化，运维对象数量急剧增加，日常运维工作压力大。为提升监控运维智能化程度，企业需要开发一套对云环境下的IT系统进行监控的工具，协助运维人员快速发现和定位问题。
开发Agent并部署在每台主机设备上，Agent部署后可以自动扫描、发现和识别此主机上安装的所有服务和组件。识别到服务和组件的技术栈后，Agent可以对不同组件采取不同的信息采集方式，Agent采集到信息后再与服务器通信传递采集到的信息，并通过监控台展示出来。

展示信息包括:
1、主机信息：包含主机CPU、内存、网卡等硬件信息以及操作系统等。
2、主机利用率：包括CPU使用率、内存使用率、磁盘使用情况、网卡传输情况、TCP连接信息等。
3、技术栈和服务信息：服务对应技术栈的metric监控信息（如SpringBoot信息的活动会话数、请求数、HTTP会话数）、服务的指标、调用链等信息。

参考资料推荐：
监控、上云

硬件要求：
PC机 2台：4C 8GB 内存 20GB硬盘

数据要求：
无
测试环境：
网络连通

功能实现：
- [x] 输出信息
1、主机信息：包含主机CPU、内存、网卡等硬件信息以及操作系统等。
2、主机利用率：包括CPU使用率、内存使用率、磁盘使用情况、网卡传输情况、TCP连接信息等。
3、技术栈和服务信息：服务对应技术栈的metric监控信息（如SpringBoot信息的活动会话数、请求数、HTTP会话数）、服务的指标、调用链等信息。
- [ ] Agent采集到信息后再与服务器通信传递采集到的信息
- [x] （选做）前端
