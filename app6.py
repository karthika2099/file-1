from flask import Blueprint,Flask

app6 = Blueprint('app6', __name__)
portal=Flask(__name__)

@app6.route('/')
def index():
    return "This is an exam portal app"

portal.register_blueprint(app6)

if __name__=="__main__":
    portal.run()

login=Flask(__name__)

@app6.route('/<int = age>')
def login(age):
    return ("hello") + age 
login.register_blueprint(app6)

if __name__=="__main__":
    login.run(debug=True)


from flask import Flask,request
app5=Flask (__name__)

@app5.route("/enter/<string:number>")
def value(number):
    return "hello" + number 

@app5.route("/login",methods=['POST','GET'])
def portal():
    if request.method=='POST':
        print("successed")
    else:
        print("failed")

if __name__=="__main__":
    app5.run(debug=True)


from flask import Flask,request
app1=Flask(__name__)
@app1.route('/flask')
def program(ready):
    return ready
@app1.route('/login',methods=['POST','GET'])
def login():
    if request=='POST':
        user=request.form("nn")
        password=request.form("kk")
    else:
        print("error")

if __name__=="__main__":
    app1.run()



from flask import Flask,request
app7 = Flask(__name__)  
  
@app7.route('/attendance',methods = ['POST'])  
def attendance():  
      studentname=request.form['studentname']  
      preorabs=request.form['preorabs']  
      if studentname=="karthika" and preorabs=="p":  
          return "attendance " % studentname  
   
if __name__ == '__main__':  
   app7.run(debug = True) 


from flask import Flask ,render_template

app=Flask(__name__)
@app.route ("/flask/<name>")
def function():
    return render_template("welcome frnds")

if __name__ == '__main__':
    app.run(debug=True)


from os import name
from flask import Flask
app2=Flask(__name__)
@app2.route("/data/<name>")
def website(name):
    return "hello"+name
if __name__=="__main__":
    app2.run(debug=True)


from flask import Flask,request
app8 = Flask(__name__)  
  
@app8.route('/shopdetails',methods = ['GET'])  
def attendance():  
      shopname=request.form['shopname']  
      shopnum=request.form['shopnum']  
      if shopname=="karthika" and shopnum=="p":  
          return "attendance " % shopname  
   
if __name__ == '__main__':  
   app8.run(debug = True) 


from flask import Flask
app3=Flask(__name__)
@app3.route('/self/<int:age>')
def data(age):
    return "Age=%d"%age
if __name__=="__main__":
    app3.run(debug=True)


from flask import Blueprint,Flask
# from flask.app import Flask

example_blueprint = Blueprint('example_blueprint', __name__)
app=Flask(__name__)

@example_blueprint.route('/')
def index():
    return "This is an example app"

app.register_blueprint(example_blueprint)

if __name__=="__main__":
    app.run()


