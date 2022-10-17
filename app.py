from flask import Flask

app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "Bulbasaur, Charmander, pikachu, eevee, diglet"


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is bulbasaur, a generation 1 pokemon who looks like a little dinosaur"


@app.get("/diglet")
def diglet_data():
    return "This is diglet, a generation 1 pokemon who looks like a tiny mole"


@app.get("/charmander")
def charmander_data():
    return "This is charmander, a generation 1 pokemon who looks like a little reptile"


@app.get("/pikachu")
def pikachu_data():
    return "This is pikachu, a generation 1 pokemon who looks like a little rodent"


@app.get("/eevee")
def eeve_data():
    return "This is eevee, a generation 1 pokemon who looks like a tiny fox"


if __name__ == "__main__":
    app.run()
