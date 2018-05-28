from flask import Flask,render_template,request
class message:
	def __init__(self,name,body):
		self.name=name
		self.body=body
app=Flask(__name__)
messages=[]
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/chat',methods=['POST'])
def chat():
	return render_template("message.html",name=request.form.get("name"),messages=messages)
@app.route('/chatroom/<username>',methods=['POST','GET'])
def chatroom(username):
	if request.method=='GET':
		return render_template("message.html",name=username,messages=messages)
	else:
		x=message(username,request.form.get("msg"))
		messages.append(x)
		return render_template("message.html",name=username,messages=messages)