# coding: utf-8
from pathlib import Path
from flask import Flask, render_template, Markup, request, jsonify
from mailsend import mailsend
import os.path
import csv

app = Flask(__name__)

#common consts
__COMMON_CONSTS = {}
__COMMON_CONSTS.setdefault("siteTitle","PyMiniMailer")
__COMMON_CONSTS.setdefault("defautEncoding","utf-8")
__COMMON_CONSTS.setdefault("addrSep",",")

#common setting file name with relative path
__COMMON_PATH = {}
__COMMON_PATH.setdefault("envLogin","./env/lg")
__COMMON_PATH.setdefault("envToList","./env/to")
__COMMON_PATH.setdefault("envEncode","./env/encoding")
__COMMON_PATH.setdefault("envLogger","./env/logger")

#logininfo
__frUser = None
__frPw = None
__toAddrs = None

@app.route("/")
@app.route("/index.htm")
@app.route("/index.html")
def firstDisp():
    return render_template("views/index.html", common=__COMMON_CONSTS, user=__frUser, pw=__frPw, toAddrs=__toAddrs)

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        smtpAddr = request.form['smtpSelect']
        smtpPort = request.form['portText']
        frAddr = request.form['frAddrText']
        passwd = request.form['frPwText']
        toAddrs = request.form['toAddrsText']
        subject = request.form['subjectText']
        msg = request.form['messageText']
        
        try:
            mailsend(smtpAddr,int(smtpPort),frAddr,passwd,toAddrs,subject,msg)
            return render_template("views/index.html", common=__COMMON_CONSTS,  user=frAddr, pw=passwd, toAddrs=toAddrs, errorMsg='success')
        except Exception as ex:
            return render_template("views/index.html", common=__COMMON_CONSTS,  user=frAddr, pw=passwd, toAddrs=toAddrs, errorMsg=str(ex))
        finally:
            pass

def __initialize__():
    if os.path.isfile(__COMMON_PATH["envLogin"]) == True:
        lg = open(__COMMON_PATH["envLogin"])
        lst = list(csv.reader(lg))
        global __frUser
        global __frPw
        __frUser = lst[0][0]
        __frPw = lst[0][1]
        
    else:
        raise Exception("missing Login File")
    
    if os.path.isfile(__COMMON_PATH["envEncode"]) == True:
        en = open(__COMMON_PATH["envEncode"], "r")
        global __COMMON_CONSTS
        __COMMON_CONSTS['defautEncoding'] = en.readline()
    
    if os.path.isfile(__COMMON_PATH["envToList"]) == True:
        lst = open(__COMMON_PATH["envToList"], "r")
        global __toAddrs
        __toAddrs = lst.read()

__initialize__()
if __name__ == '__main__':
    try:
        #app.run()
        app.run(host='0.0.0.0', debug=True, port=5002)
    except Exception as ex:
        print(ex)
    finally:
        pass
