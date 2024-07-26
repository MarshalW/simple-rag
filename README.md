# simple rag

一个简易的rag，用于旅游信息对话。

## server

```bash
# 直接访问服务器端
curl -N -X POST  \
 -H "Content-Type: application/json" \
 -H "accept: text/event-stream" \
 -d '{"query":"八达岭旺季是啥时候？几点开门？\n"}' \
 http://monkey:10999/query

#  重新索引
sudo rm -rf ./server/src/storage
docker compose restart simple-rag-server
 ```

 ## client


 ![](./files/Kapture%202024-07-27%20at%2006.40.36.gif)