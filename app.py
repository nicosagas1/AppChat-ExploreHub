import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = 'tu_api_key'
url = 'https://api.leonardo.ai/generate'  # Reemplaza con la URL correcta de la API de Leonardo


def generar_imagen(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': prompt,
        'model': 'Leonardo-v1',  # Asegúrate de usar el modelo correcto
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get('image_url')  # URL de la imagen generada
    return None


@app.route('/')
def home():
    # Genera una imagen para la página de login o registro
    prompt = "A futuristic city skyline at night"  # Cambia este prompt a lo que desees
    imagen_url = generar_imagen(prompt)
    return render_template('login.html', imagen_url=imagen_url)  # Pasa la URL de la imagen a la plantilla

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
    return render_template('tecnologia.html')


if __name__ == '__main__':
    app.run(debug=True)
