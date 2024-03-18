## Scala配置

https://github.com/scala/scala3/releases/tag/3.3.3
https://www.scala-sbt.org/download

```bash
sudo apt install default-jdk
wget https://github.com/scala/scala3/releases/download/3.3.3/scala3-3.3.3.tar.gz
sudo mv scala3-3.3.3 /usr/local/scala

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export SCALA_HOME=/usr/local/scala
export PATH=$PATH:$SCALA_HOME/bin

echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install sbt
sbt

```

VSCode插件
Scala (Metals)
Scala Snippets
Scala Syntax (official)