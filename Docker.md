# Docker教程
## Docker
### 简介：
 - 基于Go 语言
 - 沙箱机制
 - 应用容器引擎
 - Apache2.0协议开源
### 用途：
 - 打包应用以及依赖包到一个轻量的、可移植的容器当中，以发布到任何机器上
 - 实现虚拟化
## Docker使用
 - Docker容器是独立运行的一个或一组应用
 - 根据Docker镜像创建Docker容器
 - Docker 仓库用来保存镜像，可以理解为代码控制中的代码仓库
 - C/S 架构，远程API来与 Docker daemon通信，以管理和创建Docker容器
### Docker安装

安装 Docker：
```
yum -y install docker
```
启动 Docker 后台服务：
```
systemctl start docker
systemctl enable docker
```
查看docker版本
```
docker version
```
从registry.docker-cn.com镜像源下载Hello-World并测试运行：
```
docker run registry.docker-cn.com/library/hello-world:latest
```
### Docker镜像源
#### 本地：

docker images 列出本地主机上的镜像
```
docker images 
REPOSITORY                                   TAG                 IMAGE ID            CREATED             SIZE
centos/test1                                 helloworld          7888e4154dbc        3 hours ago         195.7 MB
```
删除本地镜像
```
docker rmi [OPTIONS] IMAGE [IMAGE...]
docker rmi registry.docker-cn.com/library/hello-world
```
```
docker save命令将镜像存出到本地文件
```
docker save [OPTIONS] IMAGE [IMAGE...]
docker save --output /data/testimage.tar testimage:latest
```
docker load命令将镜像载入
```
docker load [OPTIONS]
docker load --input testimage.tar
```
#### 仓库：
1. 本地私有仓库：Harbor
2. 远程官方仓库：Docker Hub

设置仓库后不需要完整指定路径，具体为修改/etc/docker/daemon.json
```
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
```
从仓库查找镜像httpd
```
docker search httpd
```
本地镜像与仓库中镜像进行链接
```
docker tag image:tag ip:port/harbor-project-name/image:tag
docker tag nginx:latest 10.217.248.21/test1/nginx:latest
```
推送本地镜像至仓库
```
docker push ip:port/harbor-project-name/image:tag
docker push 10.217.248.21/test1/nginx:latest
```
从仓库拉取镜像
```
docker pull ip:port/harbor-project-name/image:tag
docker pull 10.217.248.21/test1/nginx:latest
```
### Docker镜像制作

docker commit更新镜像
```
docker commit -m="mention" -a="author" Container_ID image:tag
```
Dockerfile 文件：
 - 每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的
 - 第一条FROM，指定使用哪个镜像源
 - RUN 指令告诉docker 在镜像内执行命令，安装了什么
 - EXPOSE 指定监听哪个端口

docker build构建镜像
```
docker build -t(tag) image:tag $DOCKFILE_DIR
```
docker tag 命令，为镜像添加一个新的标签
```
docker tag IMAGE_ID image:tag
```
Dockerfile
```
cat Dockerfile
FROM    centos:6.7
MAINTAINER      name "email"
RUN     /bin/echo 'root:123456' |chpasswd
RUN     useradd test1
RUN     /bin/echo 'test1:123456' |chpasswd
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
CMD     /bin/bash -c "while true; do echo hello world; sleep 3; done"
```
### Docker容器使用

docker run 命令来在容器内运行一个应用程序
```
docker run image:tag command
docker run ubantu:15.10 /bin/echo "Hello World"
```
交互式的容器-i(interaction) -t（terminal)
```
docker run -i -t ubuntu:15.10 /bin/bash
```
后台启动容器-d(detach）
```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
```
进入后台容器
```
docker attach [OPTIONS] CONTAINER
```
docker info 查看当前系统Docker信息
docker ps 来查看有哪些容器在运行，以及其他信息
docker ps -l 查询最后一次创建的容器
docker restart *Container_ID* 来重启容器
docker logs *Container_ID* 查看指定容器日志信息
docker stop *Container_ID* 命令来停止指定容器
docker rm *Container_ID* 删除不需要的容器
docker inspect *Container_ID* 来查看指定容器的底层信息
docker top *Container_ID* 来查看容器内部运行的进程
### Docker 容器连接

docker port *Container_ID* 5000 命令可以快捷地查看容器的5000端口绑定情况

docker run中使用端口映射
 - -P :是容器内部端口随机映射到主机的高端口
 - -p :是容器内部端口绑定到指定的主机端口

设置后通过访问127.0.0.1:5001来访问容器的TCP5000端口
```
docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py
95c6ceef88ca3e71eaf303c2833fd6701d8d1b2572b5613b5a932dfdfe8a857c
```
设置后通过访问127.0.0.1:5000来访问容器的UDP5000端口
```
docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
6779686f06f6204579c1d655dd8b2b31e8e809b245a97b2d3a8e35abe9dcd22a
```

## Docker实例
### Docker安装Nginx
### #创建Dockerfile

 1. 创建Dockerfile
 2. 通过Dockerfile创建一个镜像

### #使用nginx镜像
### Docker安装Python
### Docker安装MySQL
