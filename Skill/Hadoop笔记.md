

https://hadoop.apache.org/releases.html
http://localhost:9870/explorer.html#/user/hadoop


# Hadoop-WSL单机配置

https://hadoop.apache.org/releases.html
http://localhost:9870/explorer.html#/user/hadoop

```bash
sudo useradd -m -s /bin/bash hadoop
sudo usermod -aG sudo hadoop
sudo passwd hadoop
su hadoop && cd

ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
sudo apt install -y openssh-server
ssh localhost

wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz
tar -xvf hadoop*.tar.gz && rm hadoop*.tar.gz
mv hadoop-* hadoop && sudo mv hadoop/ /usr/local/
sudo chown -R hadoop:hadoop /usr/local/hadoop


sudo apt install -y openjdk-11-jre-headless openjdk-11-jdk-headless

vi ~/.bashrc && source ~/.bashrc
export HADOOP_HOME=/usr/local/hadoop
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=HADOOP_HOME/bin/:$PATH
export PATH=HADOOP_HOME/sbin/:$PATH

rm -f $HADOOP_HOME/bin/*.cmd
rm -f $HADOOP_HOME/sbin/*.cmd
vi $HADOOP_HOME/etc/hadoop/hadoop-env.sh
vi $HADOOP_HOME/etc/hadoop/core-site.xml
vi $HADOOP_HOME/etc/hadoop/hdfs-site.xml

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

core-site.xml
```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

hdfs-site.xml
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>
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

spark-shell
val fs = org.apache.hadoop.fs.FileSystem.get(spark.sparkContext.hadoopConfiguration)
println(fs)
```





# Hadoop-Docker集群配置


```dockerfile
FROM ubuntu:24.04

# 安装必要的软件
RUN apt update && apt upgrade -y
RUN apt install -y net-tools iputils-ping curl vim sudo openssh-server openjdk-11-jre-headless openjdk-11-jdk-headless

# 创建 hadoop 用户
RUN useradd -m -s /bin/bash hadoop
RUN usermod -aG sudo hadoop
RUN echo 'hadoop:123456' | chpasswd

# 切换到 hadoop 用户
USER hadoop
WORKDIR /home/hadoop

# 配置 .bashrc
RUN echo "alias ps='ps axuc --forest'" >> .bashrc
RUN echo "alias update='sudo apt update && sudo apt upgrade -y'" >> .bashrc
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' .bashrc

# 配置 .ssh
RUN mkdir .ssh
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -N ""
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

CMD ["bash"]
```


```shell
# 构建镜像
docker build -t hadoop_img .
docker rmi hadoop_img

# 创建数据卷, 并下载 hadoop 文件
docker volume create hadoop_volume
docker run --rm -v hadoop_volume:/mnt/hadoop_volume ubuntu:24.04 bash -c "apt update && apt install -y wget && cd /mnt/hadoop_volume && wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz && tar -xvf hadoop*.tar.gz && rm hadoop*.tar.gz"

# 创建网络
docker network create --subnet=192.168.0.0/16 --gateway=192.168.0.1 hadoop_net
docker network rm hadoop_net

# 创建容器
docker run --name master_con --net hadoop_net --ip 192.168.1.1 -it -h master -w /home/hadoop -v hadoop_volume:/mnt/hadoop_volume hadoop_img
docker run --name slave1_con --net hadoop_net --ip 192.168.1.2 -it -h salve1 -w /home/hadoop -v hadoop_volume:/mnt/hadoop_volume hadoop_img
docker run --name slave2_con --net hadoop_net --ip 192.168.1.3 -it -h salve2 -w /home/hadoop -v hadoop_volume:/mnt/hadoop_volume hadoop_img

# 启动所有容器
docker start master_con slave1_con slave2_con

# 停止所有容器
docker stop master_con slave1_con slave2_con

# 删除所有容器
docker rm master_con slave1_con slave2_con

# 进入容器终端
docker exec -it master_con bash
docker exec -it slave1_con bash
docker exec -it slave2_con bash
```


```bash
# 移动 hadoop 文件到 /usr/local
sudo mv /mnt/hadoop_volume/hadoop-* /usr/local/
sudo chown -R hadoop:hadoop /usr/local/hadoop

# 配置环境变量
echo "export HADOOP_HOME=/usr/local/hadoop" >> ~/.bashrc
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> ~/.bashrc
echo "export PATH=$HADOOP_HOME/bin/:$PATH" >> ~/.bashrc
echo "export PATH=$HADOOP_HOME/sbin/:$PATH" >> ~/.bashrc

# 移除 windows 脚本防止干扰
rm -f $HADOOP_HOME/bin/*.cmd
rm -f $HADOOP_HOME/sbin/*.cmd

# 修改 hadoop 配置文件
vi $HADOOP_HOME/etc/hadoop/hadoop-env.sh
vi $HADOOP_HOME/etc/hadoop/core-site.xml
vi $HADOOP_HOME/etc/hadoop/hdfs-site.xml

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

core-site.xml
```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

hdfs-site.xml
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>
```

