

https://hadoop.apache.org/releases.html
http://localhost:9870/explorer.html#/user/hadoop


# Hadoop-WSL单机配置

etc/hadoop/core-site.xml
```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>暂存根目录</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
        <description>文件系统地址</description>
    </property>
</configuration>
```

etc/hadoop/hdfs-site.xml
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
        <description>副本数</description>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
        <description>namenode 数据目录</description>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/data</value>
        <description>datanode 数据目录</description>
    </property>
</configuration>
```

```bash
hdfs namenode -format

start-dfs.sh
hdfs dfs -mkdir -p /user/hadoop/input
hdfs dfs -put $HADOOP_HOME/etc/hadoop/*.xml input
hdfs dfs -ls input

hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep input output 'dfs[a-z.]+'
hdfs dfs -cat output/*
hdfs dfs -rm -r output
stop-dfs.sh
```


## Spark环境配置

```bash
wget https://dlcdn.apache.org/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz
tar -xvf spark*.tgz && rm spark*.tgz
mv spark-* spark && sudo mv spark/ /usr/local/
sudo chown -R hadoop:hadoop /usr/local/spark

export SPARK_HOME=/usr/local/spark
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)
export PATH=/usr/local/spark/bin/:$PATH

spark-bash
val fs = org.apache.hadoop.fs.FileSystem.get(spark.sparkContext.hadoopConfiguration)
println(fs)
```




# Hadoop-Docker集群配置


```dockerfile
FROM ubuntu:24.04

RUN sed -i 's|archive.ubuntu|mirrors.aliyun|g; s|security.ubuntu|mirrors.aliyun|g' /etc/apt/sources.list.d/ubuntu.sources
RUN apt update && apt upgrade -y
RUN apt install -y net-tools iputils-ping curl vim sudo openssh-server openjdk-11-jre-headless openjdk-11-jdk-headless


# 创建 hadoop 用户
RUN useradd -m -s /bin/bash hadoop
RUN usermod -aG sudo hadoop
RUN echo 'hadoop:123456' | chpasswd

# 配置 .bashrc
WORKDIR /home/hadoop
RUN echo "alias ps='ps axuc --forest'" >> .bashrc
RUN echo "alias update='sudo apt update && sudo apt upgrade -y'" >> .bashrc
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' .bashrc
RUN echo "export HADOOP_HOME=/usr/local/hadoop" >> .bashrc
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> .bashrc
RUN echo "export PATH=\$HADOOP_HOME/sbin/:\$HADOOP_HOME/bin/:\$PATH" >> .bashrc
RUN touch .sudo_as_admin_successful


# 配置 ssh
USER hadoop
RUN mkdir .ssh
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -N ""
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
USER root
RUN service ssh start




# ~ 每次启动容器 需要执行的命令
RUN touch init.sh

RUN echo "if [ -d /mnt/hadoop ]; then" >> init.sh
RUN echo "  if [ ! -d /usr/local/hadoop ]; then" >> init.sh
RUN echo "    cp -r /mnt/hadoop/hadoop-* /usr/local/hadoop" >> init.sh
RUN echo "    chown -R hadoop:hadoop /usr/local/hadoop" >> init.sh
RUN echo "    echo \"\n> Files copied from /mnt/hadoop/hadoop-* to /usr/local/hadoop\n\"" >> init.sh
RUN echo "  fi" >> init.sh
RUN echo "fi" >> init.sh

RUN echo "service ssh start" >> init.sh
RUN echo "su hadoop" >> init.sh

RUN chown -R hadoop:hadoop /home/hadoop
CMD ["/bin/bash", "/home/hadoop/init.sh"]
```


```bash
docker build -t hadoop .

docker network create --subnet=192.168.0.0/16 --gateway=192.168.0.1 hadoopNet

docker run --name main --net subnet --ip 192.168.1.0 -p 16810:22 -it -h main -w /home/hadoop -v hadoop:/mnt/hadoop hadoop
docker run --name node1 --net subnet --ip 192.168.1.1 -p 16811:22 -it -h node1 -w /home/hadoop -v hadoop:/mnt/hadoop hadoop
docker run --name node2 --net subnet --ip 192.168.1.2 -p 16812:22 -it -h node2 -w /home/hadoop -v hadoop:/mnt/hadoop hadoop

docker start main node1 node2

docker stop main node1 node2
docker rm main node1 node2
docker rmi hadoop

docker exec -it -u hadoop main bash
docker exec -it -u hadoop node1 bash
docker exec -it -u hadoop node2 bash
```



```bash
docker volume create hadoop

docker run --name vol -h vol --net subnet --ip 192.168.1.0 -p 16820:22 -it -w /mnt/hadoop -v hadoop:/mnt/hadoop ubuntu:24.04

sed -i 's|archive.ubuntu|mirrors.aliyun|g; s|security.ubuntu|mirrors.aliyun|g' /etc/apt/sources.list.d/ubuntu.sources && apt update && apt install -y wget openssh-server && service ssh start

cd /mnt/hadoop && wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz && tar -xvf hadoop*.tar.gz && rm hadoop*.tar.gz && cd hadoop-* && rm bin/*.cmd sbin/*.cmd

cd /mnt/hadoop/hadoop-*/etc/hadoop

docker start vol
docker exec -it vol bash
docker stop vol
docker rm vol
```

etc/hadoop/workers
```
localhost
node1
node2
```

etc/hadoop/core-site.xml
```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>暂存根目录</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://main:9000</value>
        <description>文件系统地址</description>
    </property>
</configuration>
```

etc/hadoop/hdfs-site.xml
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
        <description>副本数</description>
    </property>
    <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>main:50090</value>
        <description>辅助namenode</description>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
        <description>namenode 数据目录</description>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/data</value>
        <description>datanode 数据目录</description>
    </property>
</configuration>
```

etc/hadoop/apred-site.xml
```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
        <description>框架名称</description>
    </property>
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>main:10020</value>
        <description>历史服务器地址</description>
    </property>
    <property>
        <name>mapreduce.jobhistory.webapp.address</name>
        <value>main:19888</value>
        <description>历史服务器网站地址</description>
    </property>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
        <description>MapReduce 应用管理 环境变量</description>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
        <description>Map 任务 环境变量</description>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
        <description>Reduce 任务 环境变量</description>
    </property>
</configuration>
```


etc/hadoop/yarn-site.xml
```xml
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>main</value>
        <description>资源管理器 主机名</description>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
        <description>节点管理器 辅助服务</description>
    </property>
</configuration>
```