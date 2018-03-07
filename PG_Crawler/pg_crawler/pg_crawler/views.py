import logging
import json
import sys
import time
import os
import s2sphere
import redis
import boto3
from django.http import HttpResponse, HttpResponseBadRequest
from pymongo import MongoClient
import data_fatcher

COMMON_TIME_LAG = 10000
mongodb_client = MongoClient('localhost', 27017)

def test(request):
    return HttpResponse("Test: Hello, world.")

def search_map(request):
    print(request)
    params = {}
    params["north"] = 1
    params["south"] = 1
    params["east"] = 1
    params["west"] = 1
    json_result = []

    # 1. Check redis results
    # redis_cached = check_redis(params)
    # if len(redis_cached) != 0:
    #     json_result.append(redis_cached)

    tic = time.gmtime(0) # 
    
    # 2. Check database results
    region = s2sphere.RegionCoverer()
    p1 = s2sphere.LatLng.from_degrees(params["north"], params["west"])
    p2 = s2sphere.LatLng.from_degrees(params["south"], params["east"])
    cell_ids = region.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))
    
    db_result = search_database(cell_ids)

    toc = time.gmtime(0)

    # if toc - tic > COMMON_TIME_LAG:
    #     return json_result

    if len(db_result) == 0:
        data_fetcher.fetch(cell_ids)
        db_result =search_database(cell_ids)
    else:
        return HttpResponse(json.dupms(json_result))

def check_redis(params):
    return {[]}

def search_database(cell_ids):
    db = mongodb_client.pokemon_go
    result = []
    for cell_id in cell_ids:
        query_temp = db.posts.find('cell_id': cell_id)
        result.append(json.loads(query_temp))
    return result

