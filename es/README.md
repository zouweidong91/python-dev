
安装
docker pull elasticsearch:latest

dev 模式
docker run --rm  -p 9200:9200 -e "discovery.type=single-node" elasticsearch:6.6.2 
docker run --rm -p 5601:5601  kibana:6.6.2 

# 启动服务
启动服务: `docker-compose up -d`  
关闭服务: `docker-compose down`  
查看日志: `docker-compose logs -f --tail=20 kibana`  

curl 127.0.0.1:9200
输出:
```
{
  "name" : "TdziJct",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "TM-i0xrLRmSRdffiZoAtHg",
  "version" : {
    "number" : "5.6.12",
    "build_hash" : "cfe3d9f",
    "build_date" : "2018-09-10T20:12:43.732Z",
    "build_snapshot" : false,
    "lucene_version" : "6.6.1"
  },
  "tagline" : "You Know, for Search"
}
```

# 运维命令
服务健康状态: `curl http://es.dev.phbs.wezuzhi.com/_cat/health?v`  
集群节点: `curl http://es.dev.phbs.wezuzhi.com/_cat/nodes?v`  
查看索引: `http://es.dev.phbs.wezuzhi.com/_cat/indices?v`

[其它命令](https://www.elastic.co/guide/en/elasticsearch/reference/6.6/cat.html)



**进入节点容器**:
```
docker exec -it elasticsearch bash
```
查看容器端口映射: `docker port elasticsearch`