# coding=utf-8
from common import utils
import os
import re

BaseUrl = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'


def del_face_token(*tokens):
    if len(tokens) < 1:
        pass
    elif len(tokens) == 1:
        tokens = "".join(tokens)
    else:
        tokens = ",".join(tokens)
        print(tokens)
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
            -F "api_secret=''' + utils.api_secret + '''" \\
            -F "outer_id=''' + utils.outer_id + '''" \\
            -F "face_tokens=''' + tokens + '''"'''
    result = os.popen(command).read()
    errmsg = utils.get_errmsg(result)
    num = re.search('(?<=("face_removed":\s))[^",]*', result)
    if errmsg:
        return errmsg.group()
    elif int(num.group()) > 0:
        return '已经移除' + num.group() + '张人脸'
    else:
        return '可能此人脸不存在'

# print del_face_token("88c2b9d533737581bc4ae1e481d824e2", "faabc1cc21dada9fbb695d1f64d51cd8")
