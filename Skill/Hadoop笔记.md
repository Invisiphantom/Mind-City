
## Hadoop环境配置

https://hadoop.apache.org/releases.html
http://localhost:9870/explorer.html#/user/hadoop

```bash
sudo useradd -m -s /bin/bash hadoop
sudo adduser hadoop sudo
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