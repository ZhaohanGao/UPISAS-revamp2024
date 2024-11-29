# 使用官方的 Python 基础镜像
FROM python:3.9.12

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到容器内的 /app 目录
COPY . /app

# 安装所需的 Python 依赖
RUN pip install --no-cache-dir flask requests

# 暴露服务的端口
EXPOSE 50000

# 定义运行容器时的启动命令
CMD ["python", "api.py"]
