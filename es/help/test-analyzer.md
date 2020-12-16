1. Create Index
```
# 创建分析器: 分词, html转文本
PUT /test_ik
{
    "settings": {
        "analysis": {
            "char_filter": {
                "my_url_filter": {
                    "type": "pattern_replace",
                    "pattern": "(ht|f)tp(s?)\\:\\/\\/[0-9a-zA-Z]([-.\\w]*[0-9a-zA-Z])*(:(0-9)*)*(\\/?)([a-zA-Z0-9\\-\\.\\?\\=\\,\\'\\/\\\\\\+&amp;%\\$#_]*)?",
                    "replacement": ""
                }
            },
            "analyzer": {
                "my_html_analyzer": {
                    "type": "custom",
                    "tokenizer": "ik_smart",
                    "char_filter": [
                        "html_strip",
                        "my_url_filter"
                    ]
                },
                "my_html_analyzer_maxWord": {
                    "type": "custom",
                    "tokenizer": "ik_max_word",
                    "char_filter": [
                        "html_strip",
                        "my_url_filter"
                    ]
                }
            }
        }
    }
}

PUT /test_ik/_mapping/_doc
{
    "properties": {
        "content": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            },
            "term_vector": "with_positions_offsets",
            "analyzer": "my_html_analyzer",
            "search_analyzer": "my_html_analyzer"
        },
        "content2": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            },
            "term_vector": "with_positions_offsets",
            "analyzer": "my_html_analyzer_maxWord",
            "search_analyzer": "my_html_analyzer_maxWord"
        },
        "content3": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            },
            "analyzer": "my_html_analyzer",
            "search_analyzer": "my_html_analyzer"
        }
    }
}
```

2. Test Analyzer
```
GET /test_ik/_analyze
{
  "analyzer":"my_html_analyzer",
  "text":"http://a.com?b=c&d=e<p>我<em>爱</em><i>北京天安门</i></p>"
}
```

3. Import Test Data
```
POST /test_ik/_doc/1?pretty
{
  "content": "http://a.com?b=c&d=e<p>我<em>爱</em><i>北京天安门</i></p>",
  "content2": "http://a.com?b=c&d=e<p>我<em>爱</em><i>北京天安门</i></p>",
  "content3": "http://a.com?b=c&d=e<p>我<em>爱</em><i>北京天安门</i></p>"
}

POST /test_ik/_doc/2?pretty
{
  "content": "<p>我<em>love</em><i>北京Tian An Men</i></p>"
}
```

4. Test Search
```
GET /test_ik/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "content": {
              "query": "天安门"
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
      "content": {}
    },
    "boundary_scanner": "word", 
    "pre_tags" : ["<hl>"],
    "post_tags": ["</hl>"]
  }
}
```

```
# 测试不同的搜索词
搜索: em
预期: 无结果 (表示html_strip起作用) 

搜索: 天安门
预期: 结果应高亮<hl>天安门</hl> (表示分词起作用) 

搜索: 天安
预期: 如果使用ik_smart分词，无结果；如果使用ik_max_word分词，有结果

搜索: Tian
预期: 有结果

搜索: Tia
预期: 无结果
```