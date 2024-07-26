FROM ubuntu:22.04

RUN sed -i s@/archive.ubuntu.com/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install \
    iputils-ping \
    nano \
    curl \
    python3 \
    pip \
    -y

# 设置时区环境变量
ENV TZ=Asia/Shanghai

# 设置时区和pip镜像
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && pip config --user set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装项目依赖
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    sse-starlette \
    openai \
    llama-index \
    llama-index-llms-openai-like \
    llama-index-embeddings-ollama \
    trafilatura \
    llama-index-readers-web

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY ./src /app

# 为容器指定要运行的命令
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "10999"]

EXPOSE 10999