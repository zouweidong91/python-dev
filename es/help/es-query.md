# article
## 查看总数，并打印最后一篇文章
```
GET /cedb_art/_search
{
  "size" : 1,
  "aggs": {
    "art_count": {
      "value_count": {
        "field": "art_id"
      }
    }
  },
  "sort": [
    {
      "art_id": {
        "order": "desc"
      }
    }
  ]
}
```

## 存在标签
```
GET /cedb_art/_search
{
  "size" : 1,
  "aggs": {
    "art_count": {
      "value_count": {
        "field": "art_id"
      }
    }
  },
  "query": {
    "bool": {
      "must": [
        {"exists": {"field": "art_tag_ids"}}
      ]
    }
  }, 
  "sort": [
    {
      "art_id": {
        "order": "desc"
      }
    }
  ]
}
```

## 检索内容
```
GET /cedb_art/_search
{
  "size" : 5,
  "from": 0, 
  "aggs": {
    "art_count": {
      "value_count": {
        "field": "art_id"
      }
    }
  },
  "_source": {
    "excludes": ["art_content", "art_type", "update_time", "delete_flag", "create_time", "art_tag_ids", "art_source"]
  }, 
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "art_title": {
              "query": "商业模式",
              "boost": 5,
              "minimum_should_match": "75%"
            }
          }
        },
        {
          "match": {
            "art_content": {
              "query": "商业模式",
              "boost": 1,
              "minimum_should_match": "75%"
            }
          }
        },
        {
          "term": {
            "art_tags.keyword": {
              "value": "商业",
              "boost": 5
            }
          }
        },
        {
          "term": {
            "art_tags.keyword": {
              "value": "模式",
              "boost": 5
            }
          }
        }
      ]
    }
  }, 
  "sort": [
    "_score",
    {"art_date": {"order": "desc"}}
  ],
  "highlight": {
    "fields": {
      "art_title": {}
    },
    "boundary_scanner": "word", 
    "pre_tags" : ["<em hl>"],
    "post_tags": ["</em>"]
  }
}
```

# article_tag
## 查看总数
```
GET /cedb_tag/_count
```

## 查询近10个标签
```
GET /cedb_tag/_search
{
  "query": {
    "match_all": {}
  },
  "sort": [
    {
      "tag_id": {
        "order": "desc"
      }
    }
  ],
  "size": 10,
  "from": 0
}
```

## 查询总数
```
GET /cedb_tag/_search
{
  "size" : 0,
  "aggs": {
    "tag_count": {
      "value_count": {
        "field": "tag_id"
      }
    },
    "name_count": {
      "cardinality": {
        "field": "tag_name.keyword"
      }
    },
    "parent_count": {
      "cardinality": {
        "field": "parent_id"
      }
    }
  }
}
```

## 检索
```
GET /cedb_tag/_search
{
  "size" : 5,
  "from": 0, 
  "aggs": {
    "tag_count": {
      "value_count": {
        "field": "tag_id"
      }
    }
  },
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "tag_name": {
              "query": "商业模式",
              "boost": 5,
              "minimum_should_match": "1%"
            }
          }
        }
      ]
    }
  }, 
  "sort": [
    "_score"
  ],
  "highlight": {
    "fields": {
      "tag_name": {}
    },
    "boundary_scanner": "word", 
    "pre_tags" : ["<em hl>"],
    "post_tags": ["</em>"]
  }
}
```