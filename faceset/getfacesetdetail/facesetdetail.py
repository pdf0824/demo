# coding=utf-8
from common import utils
import re
import json

BaseUrl = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'


def get_face_set_detail(outer_id=utils.outer_id):
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
                -F "api_secret=''' + utils.api_secret + '''" \\
                -F "outer_id=''' + outer_id + '''" '''
    result = utils.do_shell(command)
    errmsg = utils.get_errmsg(result)
    if errmsg:
        return errmsg.group()
    else:
        return json.loads(result)

# print get_face_set_detail('das')
