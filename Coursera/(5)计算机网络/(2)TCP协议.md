

# 面向连接的可靠数据传输: TCP


![](https://img.ethancao.cn/202410221058016.png =400x)


| Filed               | Name               |
| ------------------- | ------------------ |
| Source Port         | 源端口号           |
| Dest Port           | 目的端口号         |
|                     | '                  |
| Seq Number          | 数据流的字节编号   |
| Ack Number          | 累积待接收字节编号 |
|                     | '                  |
| Header Len          | 首部长度           |
| Unused              | 保留未用           |
| Flags               | 标志位             |
| Receive Window      | 接收窗口           |
|                     | '                  |
| Checksum            | 校验和             |
| Urgent Data Pointer | 紧急指针           |
|                     | '                  |
| Options             | 选项               |
| Data                | 数据               |


| Flags | Full                                  | Desc                                                               |
| ----- | ------------------------------------- | ------------------------------------------------------------------ |
| CWR   | Congestion Window Reduced             | 指示发送方已接收到拥塞通知, 并已减少拥塞窗口                       |
| ECE   | Explicit Congestion Notification Echo | 用于扩展拥塞通知, 表示接收方检测到网络拥塞                         |
| URG   | Urgent                                | 指示该段数据包含紧急数据, 接收方应尽快处理                         |
| ACK   | Acknowledgment                        | 确认收到的数据段。此标志位为 1 时, 表示该 TCP 段中包含有效的确认号 |
| PSH   | Push                                  | 请求接收方立即将数据推送到应用层, 而不是缓存在接收缓冲区中         |
| RST   | Reset                                 | 用于重置连接。当一方收到无法识别的 TCP 段或需要强制关闭连接时发送  |
| SYN   | Synchronize                           | 用于建立连接, 表示请求同步序列号                                   |
| FIN   | Finish                                | 表示发送方完成数据传输, 请求关闭连接                               |


## 往返时间与超时间隔

| RTT             | Desc         | Param          |
| --------------- | ------------ | -------------- |
| SampleRTT       | 样本往返时间 |                |
| EstimatedRTT    | 期望往返时间 | $\alpha=0.125$ |
| DevRTT          | 往返时间偏差 | $\beta=0.25$   |
| TimeoutInterval | 超时时间间隔 | $1:4$          |

1. $\text{EstimatedRTT}=(1-\alpha)\times\text{EstimatedRTT}+\alpha\times\text{SampleRTT}$
2. $\text{DevRTT}=(1-\beta)\times\text{DevRTT}+\beta\times|\text{SampleRTT}-\text{EstimatedRTT}|$
3. $\text{TimeoutInterval}=\text{EstimatedRTT}+4\times\text{DevRTT}$
4. 如果超时发生: $\text{TimeoutInterval}=2\times\text{TimeoutInterval}$


## 可靠数据传输


```sh
{
    NextSeqNum = InitialSeqNum
    SendBase = InitialSeqNum
}
{
    event=1: 从上层接收到数据e
    {
        生成具有序号NextSeqNum的TCP报文段
        if (定时器当前没有运行)
            启动定时器
        向IP传递报文段
        NextSeqNum = NextSeqNum + length(data)
    }

    event=2: 定时器超时
    {
        重传具有最小序号但仍未应答的报文段
        启动定时器
    }

    event=3: 收到ACK，具有编号ReceiveBase
    {
        if (ReceiveBase > SendBase)
            SendBase = ReceiveBase
            if (当前还有未被应答的报文段)
                启动定时器
    }
}

```

### 冗余ACK与快速重传


![](https://img.ethancao.cn/202410221222780.png)

```sh
    event=3: 收到ACK，具有编号ReceiveBase
    {
        if (ReceiveBase > SendBase)
            SendBase = ReceiveBase
            if (当前还有未被应答的报文段)
                启动定时器
        else
            当前冗余ACK数目++
            if (冗余ACK数目 == 3)
                快速重传报文段SendBase
    }
```


# 流量控制


![](https://img.ethancao.cn/202410291016260.png =400x)

|                                              |                        |
| -------------------------------------------- | ---------------------- |
| RcvBuffer                                    | 接收缓存大小           |
| LastByteRevd                                 | 接收方收到的字节编号   |
| LastByteRead                                 | 接收方读出的字节编号   |
| ASSERT(LastByteRevd-LastByteRead<=RevBuffer) | 不允许缓存溢出         |
| rwnd=RevBuffer-[LastByteRevd-LastByteRead]   | 接收窗口大小           |
|                                              | '                      |
| LastByteSend                                 | 发送方发送的字节编号   |
| LastByteAcked                                | 发送方确认的字节编号   |
| ASSERT(LastByteSend-LastByteAcked<=rwnd)     | 不允许发送超出接收窗口 |

> 当接收窗口为0时, 发送方将会继续发送1个字节的报文段, 直到缓存开始清空


# 连接管理


![](https://img.ethancao.cn/202410291044296.png =400x)

![](https://img.ethancao.cn/202410291050575.png =400x)

![](https://img.ethancao.cn/202410291051360.png =400x)

![](https://img.ethancao.cn/202410291055015.png =400x)


# 拥塞控制

![](https://img.ethancao.cn/202410291211587.png)

![](https://img.ethancao.cn/202411050900085.png)