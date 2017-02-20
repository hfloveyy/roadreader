# -*- coding:utf8 -*-
import time
from flask import Flask, request, make_response
import hashlib
import receive
import reply
import reader

app = Flask(__name__)

app.debug = True


@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = 'iloveyy1314'  # your token
        query = request.args  # GET 方法附上的参数
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s).encode('utf-8')
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
    #xml_recv = ET.fromstring(request.data)
    try:
        recMsg = receive.parse_xml(request.stream.read())
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            print(recMsg.Content)
            content = reader(recMsg.Content)
            print(content)
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            print("暂且不处理")
            return "success"
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run('0.0.0.0',80)