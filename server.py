from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "whatever"
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/routes', methods=['POST'])
def routes():
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['language'] = request.form['language']
  session['comment'] = request.form['comment']
  return render_template("process.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"

   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show')

@app.route('/back')
def back():
  return render_template('index.html')

@app.route('/show')
def show_user():
  return render_template('user.html')

@app.route('/numbergamepage')
def numbergamepage():
  return render_template('numbergame.html')

@app.route('/surveypage')
def surveypage():
  return render_template('index.html')

@app.route('/counterpage')
def counterpage():
  return render_template('counter.html')

@app.route('/counter')
def counter():
	if "counter" in session:
		session['counter'] +=1
	else:
		session['counter'] = 0
	return render_template('counter.html')

@app.route('/plustwo')
def plustwo():
	session['counter'] += 1
	return redirect('/counter')

@app.route('/numbergame')
def numbergame():
	if 'number' in session:
		pass
	else:
		session['number'] = random.randint(0, 101)
	return render_template('numbergame.html')

@app.route('/reset')
def reset():
	if 'counter' in session:
		session['counter'] = 0
	else:
		pass
	return redirect('/counter')

@app.route('/res')
def res():
	if 'number' in session:
		session['number'] = random.randint(0, 101)
		print session['number']
	else:
		pass
	return redirect('/numbergame')

@app.route('/guess', methods=['POST'])
def guess():
	print session['number']
	session['guess'] = int(request.form['guess'])
	#turns the guess into an integer
	if session['guess'] == session['number']:
		session['result'] = "You got it!"
	elif session['guess'] > session['number']:
		session['result'] =  "That's too high!"
	elif session['guess'] < session['number']:
		session['result'] =  "That's too low!"
	return redirect('/numbergame')

app.run(debug=True)

















