from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world1():
    return """
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <a href='/cat/'>🐱котики тут</a><br>
    <a href='/dog/'>🐶собаки тут</a><br>
    <a href='/parrot/'>🐦попугаи тут</a><br>
"""


@app.route('/cat/')
def hello_cat():
    return """
    <link rel="stylesheet" type="text/css" href="/static/styles2.css">
    тут обитают котики =З<br>
    <img src='/static/cat-cats.gif' alt='Кот' style='width:500px;'><br>
    <a href='/'>'←вернуться на главную'</a>
"""

@app.route('/dog/')
def hello_dog():
    return """
    <link rel="stylesheet" type="text/css" href="/static/styles2.css">
    тут флексят собачки =)<br>
    <img src='/static/dogdance.gif' alt='Собака' style='width:500px;'><br>
    <a href='/'>'←вернуться на главную'</a>
"""


@app.route('/parrot/')
def hello_parrot():
    return """
    <link rel="stylesheet" type="text/css" href="/static/styles2.css">
    тут чилят попугаи =><br> 
    <img src='/static/party-parrot.gif' alt='Попугай' style='width:500px;'><br>
    <a href='/'>'←вернуться на главную'</a>
"""


app.run(debug=True, host="0.0.0.0", port=5000)
