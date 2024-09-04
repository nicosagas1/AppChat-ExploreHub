from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Cambia esto si quieres que otra página sea la principal.

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/programas')
def programas():
    return render_template('programas.html')

@app.route('/tecnologia')
def tecnologia():
    return render_template('tecnolog.html')

if __name__ == '__main__':
    app.run(debug=True)
