# coding=utf-8
import os
import re

api_key = 'Fhekpry0Sum9DctVYaFC4RIV8b1ypgAV'
api_secret = 'eoN0dEvAd0mT7sAeTAjVnAf3XfBvKZot'
outer_id = 'pdf'
test_outer_id = 'ghj'
display_name = 'default_test'
img_path = '/root/PycharmProjects/demo/img/'
'''
one test outer_id is ghj
'''


def do_shell(command):
    return os.popen(command).read()


def get_errmsg(result):
    return re.search('(?<=("error_message":\s"))[^",]*|(?<=("error_message":"))[^",]*', result)
