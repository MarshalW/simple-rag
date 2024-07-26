from llama_index.readers.web import TrafilaturaWebReader
import os

items = [
    "颐和园",
    "恭王府",
    "国家博物馆",
    "八达岭长城",
    "故宫",
    "北海公园",
    "景山公园",
    "天坛公园",
]

data_path = "./data"


def init():
    if len(os.listdir(data_path)) == 0:
        # 下载文档
        documents = TrafilaturaWebReader().load_data(
            [f"https://baike.baidu.com/item/{item}" for item in items]
        )

        # 文档保存到目录
        documents_data = [[items[index], documents[index].text]
                          for index, item in enumerate(items)]
        for data in documents_data:
            with open(os.path.join(data_path, f"{data[0]}.txt"), "w", encoding="utf-8") as file:
                file.write(data[1])
