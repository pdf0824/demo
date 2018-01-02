# coding=utf-8

import json
import re
from common import utils

BaseUrl = "https://api-cn.faceplusplus.com/facepp/v3/detect"


def getFaceID(imgpath):
    # 构建获取face_token的命令
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
    -F "api_secret=''' + utils.api_secret + '''" \\
    -F "image_file=@''' + imgpath + '''" \\
    -F "return_landmark=1" \\
    -F "return_attributes=gender,age"'''
    # post调用，返回照片的json信息
    result = utils.do_shell(command)
    # 模式匹配  正则表达式
    pattern = re.compile(r'(?<=("face_token":(\s)"))[^"]*')
    face_token = pattern.search(result)
    errmsg = utils.get_errmsg(result)
    if face_token:
        return face_token.group()
    elif errmsg:
        return errmsg.group()
    else:
        return "获取facetoken错误"

# resultjson = json.loads(result)
# return "".join([item[key] for item in resultjson['faces'] for key in item if key == "face_token"])

# print('----------------------------------------------------------------------------')
# print(result)

# print getFaceID("../img/1.jpg")
