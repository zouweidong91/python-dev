# 插件
```
# ik中文分词
GET /_analyze
{
  "analyzer":"ik_max_word",
  "text":"北京大学汇丰商学院"
}

GET /_analyze
{
  "analyzer":"ik_smart",
  "text":"北京大学汇丰商学院"
}

# smartcn中文分词
GET /_analyze
{
  "analyzer":"smartcn",
  "text":"北京大学汇丰商学院"
}

# strip HTML
GET /_analyze
{
  "tokenizer":      "keyword", 
  "char_filter":  [ "html_strip" ],
  "text": "<p>I&apos;m so <b>happy</b>!</p>"
}
```



POST _analyze
{
  "tokenizer": "keyword",
  "char_filter": ["html_strip"],
  "text":"<p>I&apos;m so <b>happy</b>!</p>"
}

# 创建index,并定义分词器my_analyzer
PUT pattern_test
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer":{
          "tokenizer":"keyword",
          "char_filter":["my_char_filter"]
        }
      },
      "char_filter":{
          "my_char_filter":{
            "type":"mapping",
            "mappings":["苍井空 => 666","武藤兰 => 888"]
          }
        }
    }
  }
}

GET /pattern_test/_analyze
{
  "text": "苍井空热爱武藤兰，可惜后来苍井空结婚了",
  "analyzer": "my_analyzer"
}



# 创建index,并定义分词器
DELETE /cedb_art
PUT /cedb_art
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
                "my_text_analyzer": {
                    "type": "custom",
                    "tokenizer": "ik_smart",
                    "char_filter": [
                        "my_url_filter"
                    ]
                },
                "my_text_analyzer_maxWord": {
                    "type": "custom",
                    "tokenizer": "ik_max_word",
                    "char_filter": [
                        "my_url_filter"
                    ]
                },
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

# 创建字段(需要分词的部分字段)
PUT /cedb_art/_mapping/_doc
{
    "properties": {
        "art_text" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            },
            "term_vector": "with_positions_offsets",
            "analyzer": "my_text_analyzer",
            "search_analyzer": "my_text_analyzer"
        },
        "art_tags" : {
            "properties" : {
                "name" : {
                    "type" : "text",
                    "fields" : {
                        "keyword" : {
                            "type" : "keyword",
                            "ignore_above" : 256
                        }
                    },
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_smart",
                    "search_analyzer": "ik_smart"
                }
            }
        },
        "art_title": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            },
            "term_vector": "with_positions_offsets",
            "analyzer": "ik_smart",
            "search_analyzer": "ik_smart"
        }
    }
}

GET /cedb_art/_mapping


