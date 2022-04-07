from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder= "template");
host = "0.0.0.0";
port = 5050;


def fetch_api(url):
    response = requests.get(url);
    return response.json();


@app.route("/")
def index():
    limit = "20";
    All_POKEMON = fetch_api("https://pokeapi.co/api/v2/pokemon/?limit=" + limit);

    POKEMON = [];

    for pokemon_data in All_POKEMON["results"]:
        pokedata = fetch_api(pokemon_data["url"]);
        
        sprites = pokedata["sprites"];
        types = pokedata["types"];

        print(types[0]);

        pokemon = {
            "name": pokedata["name"],
            "sprite_front": sprites["front_default"],
            "sprite_back": sprites["back_default"],
            "type": types[0]["type"]["name"],
        }

        POKEMON.append(pokemon);

    return render_template("index.html", all_pokemon = POKEMON);


if __name__ == "__main__":
    app.run(host, port, debug = True);