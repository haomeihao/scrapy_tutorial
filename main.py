# coding=utf-8

import sys
import os
from scrapy.cmdline import execute

# 注意这行代码必须加上 否则配置的输出文件路径有问题
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute(['scrapy', 'crawl', 'lagou'])
# execute(['scrapy', 'crawl', 'woaiwojia'])
# execute(['scrapy', 'crawl', 'woaiwojia', '-o', 'output/data/woaiwojia.json'])
execute(['scrapy', 'crawl', 'woaiwojia', '-o', 'output/data/woaiwojia.json', '--logfile=output/logs/woaiwojia.log'])
# execute(['scrapy', 'crawl', '5i5j'])
# execute(['scrapy', 'crawl', 'imooc'])
