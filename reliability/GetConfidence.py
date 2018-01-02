# coding=utf-8
import os
from faceID import GetFaceID as getToken
from common import utils
import os
import re

BaseUrl = "https://api-cn.faceplusplus.com/facepp/v3/compare"


def getConfidence(path1, path2):
    token1 = getToken.getFaceID(path1)
    # token = 'b33189a169bff1d0e669af58e53b9ce3'
    token2 = getToken.getFaceID(path2)
    if token1 is None or token2 is None:
        return None
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
        -F "api_secret=''' + utils.api_secret + '''" \\
        -F "face_token1=''' + token1 + '''" \\
        -F "face_token2=''' + token2 + '''"'''
    result = os.popen(command).read()
    print(result)
    confidence = re.search('(?<="confidence": )[^,]*', result)
    errmsg = utils.get_errmsg(result)
    if confidence:
        return confidence.group()
    elif errmsg:
        return errmsg.group()
    else:
        return "search err"

# print getConfidence('../img/jt1.jpg', '../img/jt1.jpg')
