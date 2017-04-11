from flask import Flask , request , render_template
import bs
app = Flask(__name__)

@app.route("/")
def home():

	#print( bs.getBirds())
	return render_template("home.html")

# @app.route("/)
# def hpage():
# 	return render_template("HOME PAGE.HTML")

# @app.route("/add")
# def addpage():
# 	return render_template("add.html")

# @app.route("/login")
# def log ():
# 	return  render_template("login.html")

# @app.route("/sign up")
# def sign():
# 	return  render_template("sign up.html")
#

@app.route("/add", methods= ["post","get"])
def put_bird():
	if(request.method =="POST"):
		name = request.form["name_bird"]
		video= request.form["video_bird"]
		information=request.form["information_bird"]
		img=request.form["image"]
		bs.insertBird(name,img ,video,information)
		return  render_template("home.html"  , data =  bs.getBirds())

	else:
		return render_template("add.html")

#@app.route('/<birdname>')
#def Individual(birdname):
	#return render_template("birdtest.html"  , data = bs.GetBird(birdname))

@app.route('/bird/<birdname>')
def Ind(birdname):
	return render_template("birdtest.html"  , data = bs.GetBird(birdname))

if __name__ == "__main__":
    app.run( port=8080)
