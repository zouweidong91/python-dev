es建立索引和字段

# index and mapping

**删除index**:
```
DELETE /test_art
```

**创建index**:
```
PUT /test_art
{}
```

**设置mapping**:
```
PUT /test_art/_mapping/test_art
{
    "properties" : {
        "art_content" : {
            "type" : "text",
            "fields" : {
                "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
                }
            }
        },
        "art_id" : {
            "type" : "long"
        },
        "art_tag_ids" : {
            "type" : "long"
        },
        "art_tags" : {
            "type" : "text",
            "fields" : {
                "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                }
            }
        },
        "art_title" : {
            "type" : "text",
            "fields" : {
                "keyword" : {
                    "type" : "keyword",
                    "ignore_above" : 256
                }
            },
            "term_vector": "with_positions_offsets",
            "analyzer": "ik_max_word",
            "search_analyzer": "ik_max_word"
        },
        "create_time" : {
            "type" : "date"
        }
    }
}
```

**查看mapping**:
```
GET /test_art/_mapping
```


# 参考资料
* [mapping字段说明](https://www.elastic.co/guide/en/elasticsearch/reference/6.6/mapping-params.html)