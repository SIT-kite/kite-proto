# 调用示例

> 请在项目主目录 `kite-proto/` 下执行操作。

安装 `grpcio` 依赖：

```shell
pip install grpcio grpcio_tools
```

生成客户端 & 服务器 Python 代码。注意此处 `message` 对应的类可能无法静态生成，并且对应的 IDE 提示将失效：

```shell
mkdir example/gen
python -m  grpc_tools.protoc -I ./ --python_out=example/gen/ --grpc_python_out=example/gen/ *.proto
```
