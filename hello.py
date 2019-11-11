# coding=utf-8
import time
from flask import Flask, render_template
from test.spider_entry import SpiderEntry
from test.re_entry import re_test

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    # app.debug = True
    # app.run(host='127.0.0.1', port=5011, debug=True)

    entry_url = 'https://baike.baidu.com/item/github/10145341?fr=aladdin'
    # entry_url = 'https://bbs.hupu.com/30452896.html'
    print('entry url: {}'.format(entry_url))
    print('开始爬取数据')
    _st = time.time()
    spe = SpiderEntry()
    spe.dispatch(entry_url)
    print('爬取结束')

    # re_test()

    # yield
    # def get_square(n):
    #     for i in range(n):
    #         yield pow(i, 2)
    #
    # a = get_square(5)
    # print(a)
    # print(next(a))
    # print(next(a))
    # print(next(a))

    # my_g = (x*x+1 for x in range(3))
    # for gi in my_g:
    #     print(gi)
    #
    # print(my_g)
    # for k in my_g:
    #     print(k)
    # for i in a:
    #     print(i, end=', ')
