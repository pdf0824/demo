# coding=utf-8
from common import utils
from faceID import GetFaceID as getToken
import re

BaseUrl = 'https://api-cn.faceplusplus.com/facepp/v3/search'

'''
传入图片的路径，将图片上传detect API获取face token，
将获取的face token传至face set中查询，返回可信度最高的face token
'''


def who_is(path):
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
            -F "api_secret=''' + utils.api_secret + '''" \\
            -F "outer_id=''' + utils.outer_id + '''" \\
            -F "face_token=''' + getToken.getFaceID(path) + '''"'''
    result = utils.do_shell(command)
    errmsg = utils.get_errmsg(result)
    confidence = re.search('(?<=("confidence":(\s)))[^",]*', result)
    face_token = re.search('(?<=("face_token":(\s)"))[^"]*', result)
    if errmsg:
        return errmsg.group()
    elif float(confidence.group()) > 75:
        return face_token.group()
    else:
        return "Please try again"


# print who_is(utils.img_path + "test.jpg")
