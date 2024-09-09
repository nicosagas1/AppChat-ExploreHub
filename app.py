from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de chat
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Ruta para la página de inicio de sesión
@app.route('/login')
def login():
    return render_template('login.html')

# Ruta para la página de programas
@app.route('/programas')
def programas():
    return render_template('programas.html')

# Ruta para la página de tecnología
@app.route('/tecnologia')
def tecnologia():
    return render_template('tecnolog.html')


if __name__ == '__main__':
    app.run(debug=True)
