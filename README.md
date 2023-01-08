
# 上应小风筝 gRPC 约定

本仓库下的 protobuf3 协议定义，适用于上应小风筝 [kite-server](https://github.com/SIT-kite/kite-server) 与 [kite-app](https://github.com/SIT-kite/kite-app) 之间的 gRPC 通信。

详细说明请参考 server 与 app 的代码，以及仓库内 proto 文件的说明。

**为什么使用 gRPC？**

1. 与之前的 REST API 相比，通用性不太弱，便利性增加。可以很方便地看到接口定义以及前后端沟通的过程；
2. 与同类相比，其基于 HTTPS 协议，相对于 thrift, 无需额外考虑 web 平台及传输过程中的加密等等；
3. 生态较为丰富。

尽管好处不少，但在初识 gRPC 时免不了很多疑问，只待日后理解。
