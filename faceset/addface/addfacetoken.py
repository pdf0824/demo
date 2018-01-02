# coding=utf-8
from common import utils
from faceID import GetFaceID as getToken
import re

BaseUrl = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'


def add_face_token(path):
    token = getToken.getFaceID(path)
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
        -F "api_secret=''' + utils.api_secret + '''" \\
        -F "outer_id=''' + utils.outer_id + '''" \\
        -F "face_tokens=''' + token + '''"'''
    result = utils.do_shell(command)
    errmsg = utils.get_errmsg(result)
    if errmsg:
        return errmsg.group()
    else:
        num = re.search('(?<=("face_added":\s))[^,"]*', result)
        if int(num.group() > 0):
            # 增加taken用户信息并持久化到数据库，关闭摄像头
            name = raw_input("姓名：")
            stu_num = raw_input('学号：')
            pass
            pass
            pass
            pass
            pass
            return '已添加->' + name
        else:
            return '添加失败，请重试'


print add_face_token(utils.img_path + "test.jpg")
'''
{"faceset_token": "7293d22a21c6350af2999de01aed0dcb", "tags": "", "time_used": 70, "user_data": "", "display_name": "", "face_tokens": 
["88c2b9d533737581bc4ae1e481d824e2", "
faabc1cc21dada9fbb695d1f64d51cd8", 
"ea657f69854f0ecd14f9ff0cc8dea1c1", 
"151cb3c11e6805d4f7a67950699eff05",
"255f361d9014f9f2ad049d3fef4ce048", 
"b33189a169bff1d0e669af58e53b9ce3"], 
"face_count": 6, "request_id": "1513352258,70e61490-80d1-4c6b-b6bb-c1dae0c32425", "outer_id": "pdf"}
'''
