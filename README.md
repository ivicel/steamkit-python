title: A Simple SteamKit implement with using Python(一)
date: 2018-07-18
tags: python, steam, steamkit



#### 1. 连接握手

1. 与 steam 客户端进行通信的称为 CM Server, Steam 客户端首先要向发送一个连接请求, 然后服务器会返回一个 `CHANNEL_ENCRYPT_REQUEST`, 这个消息包会带有一个 16 字节的 质询 `challenge`

2. 我们随机生生成一个 256 位长度的密钥 `session_key`,  使用 steam 的公钥对密钥加密后再发回给服务器, 加密方法为 `RSA`, padding 为 `OAEP(mgf=MGF1(algorithm=SHA1), algorithm=SHA1)` 

   > 这里可里选择只发送回 `session_key`(legacy mode), 或者回应质询 `session_key + challenge`, 发回后者表示在以后的通信中使用每次会生成一个 `SHA1-HMAC`. 

3. 收到服务的 `session_key` 确认, 结果为 `EResult.OK` 时, 连接成功. 以后的通信会基于 `session_key` 加密

   > 如果我们启用了 `SHA1-HMAC` 消息认证, 那么在 `CBC` 模式使用的初始向量 `iv` 会有不同, 不是通过直接随机生成, 而是对明文生成 HMAC 后, 取其前 13 bytes, 再加上随机生成 3 bytes. 下面是发送 `HMAC` 时的步骤
   >
   > 1. 随机生成 3 bytes `prefix`, 把这三个字节加到明文的前面, hash key 是 `session_key` 的前 16 bytes, 即 `hash_key = session_key[:16]`. 使用 `HMAC(hash_key=session[:16], hash_function=SHA1, message=prefix + need_to_encrypt_text)`, 生成的 `hmac_msg` 后, `iv = hmac_msg[:13] + prefix`
   > 2. 使用 `AES-256-ECB`, 加密 `iv`, 分组长度为 128 bits. 得到 `enc_iv`, 一共是 16个字节
   > 3. 使用 `AES-256-CBC`, 加密 `need_to_encrypt_text`, 分组长度为 `128 bits`, 填充模式为 `PKCS7`.  得到 `enc_msg`
   > 4. 返回的 `enc_iv + env_msg` 即是加密完成的的消息体
   >
   > 如果没有启用 `HMAC`, 即不发送 `challenge`, 在第一步中把 `iv` 换成随机生成的 16 字节即可.
   >
   > 解密过程就是反向过程, 消息包的前 16 个字节是 `env_iv`, 剩下的是加密后 message 本体. 使用对应的加密方法进行解密即可

4. 初始的 CM Server IP 地址和端口 可以在 `steam_installed_directory/config/config.vdf` 找到, 在通信的过程, 服务器会发回新 CM IP 地址和端口

5. steam 客户端保持一个 TCP/UDP 长连接, 用来与 CM Server 通信, 并且要定时发送一个 **"heartbeat"** 用来告诉 CM 不要断开连接

6. 通信的数据结构主要为 [Protocol Buffer v2](https://developers.google.com/protocol-buffers/), 在 proto 外包了一层 header, header 里指明了是否为 proto buffer

#### 2. 了解 Protocol Bufffer

根据 protobuf 的 [文档](https://github.com/google/protobuf), 使用 protobuf 要三步走

1.  定义 `.proto` 文件原型, steamdb 已经收集好了, 从 [SteamDB github](https://github.com/SteamDatabase/SteamTracking) 下载, 另外这些都是定义都依赖 Google 定义的 `descriptor.proto`, 在 [这里](https://github.com/google/protobuf/blob/master/src/google/protobuf/descriptor.proto) 可以下载到这个文件, 打包的编译器也带了这个

   > 花 [5 分钟](https://space.bilibili.com/423895/) 了解一下 protobufs 是如何 [定义](https://developers.google.com/protocol-buffers/docs/proto)

2. 使用 `protobuf` 编译器把 `.proto` 文件编译成对应语言文件, 编译器在 [这里](https://github.com/google/protobuf/releases) 下载, 下载对应系统的版本即可, 带语言标签的是使用特定语言的实现源代码

   > 花几分钟读下 [python tutorial](https://developers.google.com/protocol-buffers/docs/pythontutorial)

3. 使用 Python protocol buffer API 读写, API 文档在 [这里](https://developers.google.com/protocol-buffers/docs/reference/python/)

#### 3. 编译 protobuf

```shell
# project 目录
mkdir python-steamkit && cd python-steamkit
python3 -m venv venv
# 用于加密和 protobuf 的依赖包
pip install cryptography protobuf

# Protobufs 目录定义主要的通信格式
# 其他目录是对应的游戏通信格式
git clone https://github.com/SteamDatabase/SteamTracking
cd SteamTracking/Protobufs
mv renderer/rendermessages.proto .
# 删掉重复定义
rm -R steamdatagram_auth_messages.proto renderer
# 在每个 proto 文件的第一行加上 syntax = "proto2"; 语法定义避免编译警告
sed -s -i '1isyntax = "proto2";' *.proto
# optinal 查看来是否所有 .proto 文件都有 proto2 语法定义了, 0 表示成功
test $(find . -type f -name '*.proto' | wc -l) -eq \
	$(grep -E '^syntax\s?=\s?"proto2";$' -R . | wc -l); echo $?
	
# 新建目录来存放编译后的 .py 文件
mkdir protobufs
# 如果文件名了带有点号, 比如 a.b.proto, 编译后会生成 a/b_pb.py, 我们不需要独立的目录
# 把文件的中点号换成下划线 "_", 文件内的依赖路径相应的也需要更改
for n in `ls`; do; name=$(echo $n | sed -E 's/\./_/g; s/_proto$/\.proto/g'); mv $n $name; done
sed -E -i '/^import/s/\./_/; /^import/s/_proto/\.proto/' *.proto

# 下载的 protoc 编译包里包含了 descriptor.proto, 指定依赖路径即可
protoc --python_out=./protobufs -I. -I protoc/include *.proto
# 将 steam_proto 打包成 python package
touch protobufs/__init__.py
mv protobuf ../../
sed -E '/^import\s+"[^\/]*$/s/"(.*)";$/"steam\/protobufs\/\1";/' steam/protobufs/*.proto -i
```

#### 4. 通信消息的格式

通信是按 **Little endian** 传输的, 通信包的定义主要有三种情况:

1. 前三个握手包, 用来生成加密的通信, 有自己特定的定义
2. protobuf 包, 包含一个 protobuf 消息
3. multi message, (1) 根据 `CMsgMulti.size_unzipped` 是否 **大于 0** 来判断 `CMsgMulti.message_body` 是否启用了  gzip 压缩. (2) 如果是则要先先把 `message_body` 解压, 然后再解读里面的消息

这三种包都会包含以下三个字段: 

* 4 bytes 的 包长度 
* 固定的 4 bytes magic number, 为 `0x31305456`
* 4 bytes 的 消息类型, 消息的最高位为 protobuf 消息掩码位, `0` 表示非 protobuf, `1` 为 protobuf

```
1. handshake packet: <ChannelEncryptRequest>, <ChannelEncryptResponse>, <ChannelEncryptResult>
+ + + + + + + + + + + + + + +
|   4 bytes msg_len         |
+ - - - - - - - - - - - - - +
|   4 bytes magic_number    |
+ - - - - - - - - - - - - - +
|   4 bytes msg_type        |
+ - - - - - - - - - - - - - +
|   8 bytes target_job_id   |
+ - - - - - - - - - - - - - +
|   8 bytes source_job_id   |
+ - - - - - - - - - - - - - +             
|                           |       
|   body(msg_len - 20 bytes)| 
|                           |
+ + + + + + + + + + + + + + +

body 详细说明
I. recv <ChannelEncryptRequest>
    + - - - - - - - - - - - - - - - + 
    | (msg_len - 20)bytes challenge |
    + - - - - - - - - - - - - - - - + 

II. send <ChannelEncryptResponse>
    + - - - - - - - - - - - - - - - + 
    | 4 bytes protocol_version (1)  |
    + - - - - - - - - - - - - - - - + 
    | 4 bytes key_size (128)        |
    + - - - - - - - - - - - - - - - + 
    | 128 bytes session_key         |
    + - - - - - - - - - - - - - - - +  
    | 4 bytes crc32(session_key)    |       
    + - - - - - - - - - - - - - - - +  
    | 4 bytes end_flag (0)          |
    + + + + + + + + + + + + + + + + +

III. recv <ChannelEncryptResult>
    + - - - - - - - - - - - - - - - + 
    | 4 bytes EResult               |
    + - - - - - - - - - - - - - - - + 

2. Protobuf packet
+ + + + + + + + + + + + + + +
|   4 bytes msg_len         |
+ - - - - - - - - - - - - - +
|   4 bytes magic_number    |
+ - - - - - - - - - - - - - +
|   4 bytes msg_type        |
+ - - - - - - - - - - - - - +
|   4 bytes protobuf_len    |
+ - - - - - - - - - - - - - +          
|                           |       
|   Protobuf Message        |
|                           |
+ + + + + + + + + + + + + + +


3. mutil packet
+ + + + + + + + + + + + + + +
| 4 bytes msg_len           |
+ - - - - - - - - - - - - - +
| 4 bytes magic_number      |
+ - - - - - - - - - - - - - +
| 4 bytes msg_type          |
+ - - - - - - - - - - - - - +
| 1 byte header_size (32)   |
+ - - - - - - - - - - - - - +
| 2 bytes header_version (1)|
+ - - - - - - - - - - - - - +
| 8 bytes target_job_id     |
+ - - - - - - - - - - - - - +
| 8 bytes source_job_id     |
+ - - - - - - - - - - - - - +  
| 1 byte header_canary      |
+ - - - - - - - - - - - - - +
| 8 bytes steam_id          |
+ - - - - - - - - - - - - - + 
| 8 bytes source_job_id     |
+ - - - - - - - - - - - - - +   
| 8 bytes session_id        |
+ - - - - - - - - - - - - - +             
|                           |       
|Protobuf message<CMsgMulti>|
|                           |
+ + + + + + + + + + + + + + +

Multi 包含一个或多个 message, 每个结构为, 前 4 个字节为消息长度 + message
+ - - - - - - - - - - - - - + 
| 4 bytes message_len       |
+ - - - - - - - - - - - - - +   
| message_len bytes message |
+ - - - - - - - - - - - - - +  
| 4 bytes message_len       |
+ - - - - - - - - - - - - - +   
| message_len bytes message |
+ - - - - - - - - - - - - - +


4. send protobuf message
+ + + + + + + + + + + + + + + + + + + +
|   4 bytes msg_len                   |
+ - - - - - - - - - - - - - - - - - - + 
|   4 bytes magic_number              |
+ - - - - - - - - - - - - - - - - - - + 
|   encrypted mesasge body            |
+ - - - - - - - - - - - - - - - - - - +

需要发送的 protobuf message 包含 message header 和 message body 主体
1> 如果已经登录的情况下, 把 header 里的 steamid, client_sessionid 改成对应的值
2> 将这两个序列化生成字节串
3> 使用 session_key 加密, 根据前面的握手过程, 依需要生成 hash message
4> 组合成上面的包. 注意的是包的主体消息长度是指加密后的字节数
+ - - - - - - - - - - - - - - - - - - +  
| Protobuf header<CMsgProtoBufHeader> |
+ - - - - - - - - - - - - - - - - - - +  
| Protobuf message                    |
+ - - - - - - - - - - - - - - - - - - +  
```





#### Reference

1. https://github.com/ValvePython/steam/issues/79
2. https://github.com/ValvePython/steam
3. https://github.com/SteamRE/SteamKit/issues/555