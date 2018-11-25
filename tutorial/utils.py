# coding=utf-8
import json
import os
import time
import datetime


def get_millisecond_timestamp():
    return int(round(time.time() * 1000))


def get_second_timestamp():
    return int(round(time.time()))


def format_now_datetime(format_str='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(format_str)


def format_now_date(format_str='%Y-%m-%d'):
    return datetime.datetime.now().strftime(format_str)


def format_now_time(format_str='%H:%M:%S'):
    return datetime.datetime.now().strftime(format_str)


def get_project_dir():
    return os.path.dirname(os.path.dirname(__file__))


def format_json(dict):
    jsonstr = json.dumps(dict, ensure_ascii=False, indent=4)
    return jsonstr


if __name__ == '__main__':
    print get_millisecond_timestamp()
    print get_second_timestamp()
    print format_now_datetime()
    print format_now_date()
    print format_now_time()
    print get_project_dir()
