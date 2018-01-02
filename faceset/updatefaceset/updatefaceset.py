# coding=utf-8
from common import utils
import re

BaseUrl = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/update'


def update(new_outer_id, old_outer_id=utils.outer_id, tag=0):
    command = '''curl -X POST "''' + BaseUrl + '''" -F "api_key=''' + utils.api_key + '''" \\
            -F "api_secret=''' + utils.api_secret + '''" \\
            -F "outer_id=''' + old_outer_id + '''" \\
            -F "new_outer_id=''' + new_outer_id + '''"'''
    result = utils.do_shell(command)
    errmsg = utils.get_errmsg(result)
    succ = re.search('(?<=("outer_id":\s"))[^"]*', result)
    if errmsg:
        return errmsg.group()
    elif succ:
        try:
            operation = open('/root/PycharmProjects/demo/common/utils.py', 'r+')
            all = operation.readlines()
            all[6] = "outer_id = '" + new_outer_id + "'\n"
            operation = open('/root/PycharmProjects/demo/common/utils.py', 'w+')
            operation.writelines(all)
            operation.close()
        except Exception:
            if tag == 0:
                update(old_outer_id, new_outer_id, tag + 1)
            else:
                return "请稍后再试!"
        else:
            return '"' + old_outer_id + '"已经替换成"' + new_outer_id + '"'
    else:
        return '请稍后再试!'


print update('pdf')
