# _*_ coding : UTF-8 _*_
# 开发人员："夏沫丶"
# 开发时间： 2019/12/16 21:35
# 文件名称： app.py
# 开发工具： PyCharm
from flask import Flask

app = Flask(__name__)

@app.route("/greek")
@app.route('/greek/<request>')
def say_hello(request="cc"):
    a = 1
    b = 2
    return f"{a + b} hello {request} 我来啦！!!"


if __name__ == "__main__":
    app=app.run(host='localhost',debug="Ture",port=80)
