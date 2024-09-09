
## 环境配置

```bash

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64

HADOOP_DIR=$(ls /opt | grep -oP 'hadoop-[0-9]+\.[0-9]+\.[0-9]')
export HADOOP_HOME=/opt/$HADOOP_DIR
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"

```