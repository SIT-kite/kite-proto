
# 上应小风筝 gRPC 约定

本仓库下的 protobuf3 协议定义，适用于上应小风筝 [kite-server](https://github.com/SIT-kite/kite-server) 与 [kite-app](https://github.com/SIT-kite/kite-app) 之间的 gRPC 通信。

详细说明请参考 server 与 app 的代码，以及仓库内 proto 文件的说明。

**为什么使用 gRPC？**

1. 与之前的 REST API 相比，通用性不太弱，便利性增加。可以很方便地看到接口定义以及前后端沟通的过程；
2. 与同类相比，其基于 HTTPS 协议，相对于 thrift, 无需额外考虑 web 平台及传输过程中的加密等等；
3. 生态较为丰富。

尽管好处不少，但在初识 gRPC 时免不了很多疑问，只待日后理解。


**调试**

一般地，可以使用 grpcurl （命令行工具）和 grpcui （WebUI） 调试。

安装方法：
```shell
yay -S grpcurl grpcui
```

命令的参数主要包括：

1. 调用路径：gRPC 包路径、服务名称和方法名称，格式如 `kite.UserService/Login`。
2. 如本地的 gRPC 服务器采用明文传输（HTTP/2 without TLS），则应添加 `-plaintext` 参数。
3. 服务器程序的地址和端口。
4. 对于 grpcurl, 需要提供请求的参数，用 `-d` 表示。如 `-d '{"text: hello world"}'`，对于 grpcui, 参数值在浏览器上填写。
5. 如果服务端不支持反射，会抛出类似错误：`Error invoking method "/kite.PingService/ping": failed to query for service descriptor "/kite.PingService": server does not support the reflection API`，此时需要通过 `-proto` 指定 .proto 文件。

举例：

```shell
$ grpcurl -plaintext -proto Projects/kite-proto/ping.proto -d '{"text": "hello world"}' 127.0.0.1:8080 kite.ping.PingService/Ping
{
"text": "hello world"
}
$ grpcui -plaintext -proto Projects/kite-proto/ping.proto 127.0.0.1:8080
```

ApiFox、Postman 等工具也支持 gRPC 接口的调试。