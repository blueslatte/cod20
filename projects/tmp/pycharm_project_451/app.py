# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

# coding: utf-8
from flask import Flask, render_template, url_for, request, json, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/form_data', methods=['GET', 'POST'])
def form_data():
    if request.method=='GET':
        username = request.args.get("username")
        #dumps和loads方法，来自json模块，而json模块是python中的，可以直接导入：
        #而jsonify是flask封装的扩展包
        return jsonify({'status': '0', 'username': username, 'errmsg': '登录成功!'})
    else:
        username = request.form['username']
        return jsonify({'status': '0', 'username': username, 'errmsg': '登录成功!'})



@app.route('/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)

