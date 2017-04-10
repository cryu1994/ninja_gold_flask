from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "afk"

@app.route("/")
def main():
    if not "golds" in session:
        session['golds'] = 0
    if not 'log' in session:
        session['log'] = " "

    data = {}
    data['golds'] = session['golds']
    data['log'] = session['log']

    return render_template("index.html", data=data)

@app.route('/process_money', methods = ["POST"])
def process():
    building = request.form['building']

    if building == 'Farm':
        rand = random.randint(10,20)
        message = "<div class='won'>You went to the farm and earned " + str(rand) + " gold!</div>"
        print rand
    elif building == 'Cave':
        rand = random.randint(5,10)
        message = "<div class='won'>You went to the cave and earned " + str(rand) + " gold!</div>"
    elif building == 'House':
        rand = random.randint(2,5)
        message = "<div class='won'>You went to the cave and earned " + str(rand) + " gold!</div>"

    elif building == 'Casino':
        rand = random.randint(-50, 50)
        if rand < 0:
            win_or_lost = 'lost'
        else:
            win_or_lost = 'win'


        message = "<div class='" + win_or_lost + "'>You went to the casino and " + win_or_lost + " " + str(rand) + " gold!</div>"

    log = session['log']
    session['log'] = message + log
    session['golds'] += rand
    print session['log']
    return redirect("/")

@app.route('/reset')
def reset():
	session['golds'] = 0
	session['log'] = ''
	return redirect('/')
app.run(debug=True)
