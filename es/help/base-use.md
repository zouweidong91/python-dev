```
# 创建索引
PUT /zwd_test

# 写入数据
POST /zwd_test/_doc/123?pretty
{
  "foo": "bar",
  "age": -1
}

# 读取数据
GET /zwd_test/_doc/123?pretty

# 查询数据
GET /zwd_test/_search?pretty
{
  "query": {
    "match": {
      "foo": "bar"
    }
  }
}

# 更新字段
POST /zwd_test/_doc/123/_update
{
  "doc": {
    "age": 18
  }
}

# 删除数据
DELETE /zwd_test/_doc/123
```