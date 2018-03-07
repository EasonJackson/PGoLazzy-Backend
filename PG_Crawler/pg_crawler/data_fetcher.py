import logging
import json
import sys
import os
from pymongo import MongoClient

def fetch(cell_ids):
    try:
        data = json.loads(request.body) 
        # If this is a raw event, 
        # break down to smaller request and send back to queue
        if isinstance(data, dict):
            result = break_down_request(data)
            return HttpResponse(result)
        else:
            cell_ids = data
    except:
        logging.getLogger('worker').error("Fail to parse cellid from {0}".format(request.body))
        logging.getLogger('worker').error(str(sys.exc_info()))
        return HttpResponseBadRequest("Fail to parse cellid from {0}".format(request.body))

    
    fail_count = worker.query_cell_ids(cell_ids)
    if fail_count > 0:
        return HttpResponseBadRequest("Some cell failed. Total fail count: {0}".format(fail_count))
    