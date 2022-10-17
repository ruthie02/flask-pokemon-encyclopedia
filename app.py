from flask import Flask
from helpers import get_pokemon_by_name

app = Flask(__name__)

pokemon_data = {
    "bulbasaur": "dinosaur",
    "charmander": "reptile",
    "pikachu": "rodent",
    "eeve": "fox",
    "diglett": "mole"
}


@app.get("/")
def pokemon_list():
    return "Bulbasaur, Charmander, pikachu, eevee, diglet"


@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    pokemon = get_pokemon_by_name(pokemon_name)
    return f"This is {pokemon['name']}.\n" \
           f"Height: {pokemon['height']}.\n" \
           f"Weight: {pokemon['weight']}.\n" \
           f"Base experience: {pokemon['base_experience']}.\n" \
           f"Type(s): {' and '.join(type_info['type']['name'] for type_info in pokemon['types'])}"


if __name__ == "__main__":
    app.run()
