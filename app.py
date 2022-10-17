from flask import Flask

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
def pokemon_data_data(pokemon_name):
    creature = pokemon_data.get(pokemon_name)
    return f"This is {pokemon_name}, a generation 1 pokemon who looks like a tiny {creature}"


if __name__ == "__main__":
    app.run()
