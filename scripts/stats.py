from elasticsearch import Elasticsearch;

es = Elasticsearch(['localhost'])

index = 'wiating'
log_indices = 'wiating_*'
tester_user = "some_sub"

added_locations = es.search(index=log_indices, body={
    "query": {
        "bool": {
            "filter": [
                {"range": {"timestamp": {"gt": "2020/09/16"}}},
                {"term": {"changes.action": "created"}}
            ],
            "must_not": [
                {"term": {"modified_by.keyword": tester_user}}
            ]
        }
    }
})['hits']['total']['value']

all_locations = es.search(index=index)['hits']['total']['value']

locations_without_photos = es.search(index=index, body={
    "query": {
        "bool": {
            "must_not": [
                {"exists":{"field": "images"}}
            ]
        }
    }
})['hits']['total']['value']

added_photos = es.search(index=log_indices, body={
    "query": {
        "bool": {
            "filter": [
                {"range": {"timestamp": {"gt": "2020/09/16"}}},
                {"exists": {"field": "changes.images"}},
            ],
            "must_not": [
                {"term": {"modified_by.keyword": tester_user}},
                {"exists": {"field":"changes.images.old_value"}}
            ]
        }
    }
})['hits']['total']['value']

all_photos = es.search(index=index, body={
    "aggs" : {
        "all_photos" : { "value_count" : { "field" : "images.name" } }
    }
})['aggregations']['all_photos']['value']

changed_locations = es.search(index=log_indices, body={
    "query": {
        "bool": {
            "filter": [
                {"range": {"timestamp": {"gt": "2020/09/16"}}}
            ],
            "must_not": [
                {"term": {"modified_by.keyword": tester_user}},
                {"exists": {"field": "changes.images"}},
                {"exists": {"field":"changes.images.old_value"}},
                {"term": {"changes.action": "created"}}
            ]
        }
    }
})['hits']['total']['value']

print(
    "Nowe lokacje:", added_locations,
    "\nWszystkie lokacje:", all_locations,
    "\nLokacje bez zdjęć", locations_without_photos,
    "\nNowe zdjęcia:", added_photos,
    "\nWszystkie zdjęcia:", all_photos,
    "\nWprowadzone zmiany:", changed_locations
)