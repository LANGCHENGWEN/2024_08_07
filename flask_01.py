from flask import Flask #flask是工具箱(module模組)，Flask是工具(class類別)
from flask import redirect, url_for, render_template

app = Flask(__name__) #製作出一個由Flask類別生成的物件(object)

@app.route("/") #裝飾器:根目錄要做什麼事
@app.route("/<string:username>")
def say_hello_world(username=""):
    return render_template("hello.html",name=username)

@app.route("/tell_me_a_joke")
def tell_me_a_joke():
    return "<h1>ha ha ha ha</h1>"

@app.route("/eat/<string:what_fruit>")
def eat_fruit(what_fruit):
    return redirect(url_for('say_fruit_is_gone',fruit=what_fruit))


@app.route("/eat/<string:fruit>")
def say_fruit_is_gone(fruit):
    return "<h1>" + fruit + "is gone.</h1>"


#打flask --app flask_01.py run 執行程式
#flask --app flask_01.py --debug run 執行程式
#python flask_01.py 執行程式
#.\AI_env\Scripts\Activate.ps1 執行虛擬環境
#deactivate 退出虛擬環境

#如果我直接執行這個檔案，那__name__就等於__main__
if __name__ == '__main__':
    #或打flask --app flask_01.py run
    app.run(debug=True)