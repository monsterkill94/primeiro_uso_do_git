from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon = None

    if request.method == 'POST':
        nome = request.form['pokemon'].lower().strip()
        url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            data = resposta.json()

            # Formata o ID com 3 dígitos para imagem HD do GitHub
            id_formatado = f"{data['id']:03}"
            imagem_hd = f"https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/{id_formatado}.png"
            print("SPRITE:", data["sprites"]["front_default"])
            print("HD:", imagem_hd)

            pokemon = {
                "nome": data["name"].title(),
                "sprite": data["sprites"]["front_default"],
                "imagem_hd": imagem_hd,
                "tipo": [t["type"]["name"].title() for t in data["types"]],
                "altura": data["height"] / 10,
                "peso": data["weight"] / 10
            }
        else:
            pokemon = {'erro': 'Pokémon não encontrado!'}

    return render_template('index.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True)
