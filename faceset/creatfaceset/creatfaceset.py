# coding=utf-8
from common import utils
import re
import os

BaseUrl = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'


def create_face_set(name=None, description=None):
    if name is None:
        name = utils.outer_id
    if description is None:
        description = utils.display_name
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
    -F "api_secret=''' + utils.api_secret + '''" \\
    -F "display_name=''' + description + '''" \\
    -F "outer_id=''' + name + '''"'''
    result = utils.do_shell(command)
    succ = re.search('(?<=("outer_id":\s"))[^"]*', result)
    errmsg = utils.get_errmsg(result)
    if succ:
        return "face set '" + succ.group() + "' already succ create"
    elif errmsg:
        return errmsg.group()
    else:
        return "create face set error"


# print create_face_set('ghj', "a test outer_id")
'''
{"faceset_token": "7293d22a21c6350af2999de01aed0dcb", "time_used": 126,
 "face_count": 0, "face_added": 0, "request_id": "1513346011,2cc30ff1-ce21-4ef8-be8e-75f7716f9ef8", 
 "outer_id": "pdf", "failure_detail": []}


'''
