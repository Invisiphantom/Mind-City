
```dockerfile
FROM ubuntu:24.04

RUN sed -i "s@http://.*archive.ubuntu.com@http://mirrors.huaweicloud.com@g" /etc/apt/sources.list.d/ubuntu.sources
RUN sed -i "s@http://.*security.ubuntu.com@http://mirrors.huaweicloud.com@g" /etc/apt/sources.list.d/ubuntu.sources

RUN apt update && apt upgrade -y
RUN apt install -y net-tools iputils-ping curl vim sudo

RUN useradd -m -s /bin/bash hadoop
RUN usermod -aG sudo hadoop
RUN echo 'hadoop:123456' | chpasswd
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /home/hadoop/.bashrc
RUN echo "alias ps='ps axuc --forest'" >> /home/hadoop/.bashrc
RUN echo "alias update='sudo apt update && sudo apt upgrade -y'" >> /home/hadoop/.bashrc

WORKDIR /home/hadoop
USER hadoop
CMD ["bash"]
```



```bash
docker build -t hadoop_image .
docker run -it -h master --name master_con -w /home/hadoop hadoop_img
docker stop master_con

docker start master_con
docker exec -it -u hadoop -w /home/hadoop master_con bash

docker network ls

docker ps -a
docker rm master_con
docker images
docker rmi hadoop_image

```