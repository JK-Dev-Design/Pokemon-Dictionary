import flask
import json
database = json.load(open("db.json"))
# print(database["pikachu"])
app = flask.Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def start():
  if flask.request.method == "POST":
    pokemon = flask.request.form["pokemon"]
   if pokemon in list(database.keys()):
      abilities = []
      for i in database[pokemon]["abilities"]:
        abilities.append(i ["name"])
      return flask.render_template(
        "result.html",
        idvalue = database[pokemon]["id"],
        namevalue = database[pokemon]["name"], 
        heightvalue = database[pokemon]["height"],   
        weightvalue = database[pokemon]["weight"],      
        imgvalue = database[pokemon]["image_url"],    
        xpvalue = database[pokemon]["xp"],    
        urlvalue = database[pokemon]["pokemon_url"],
        abilities = ", ".join(abilities),  
        hp = database[pokemon]["stats"][0]["base_stat"],
        data = database[pokemon]
        )
  return flask.render_template("index.html")
app.run("0.0.0.0") 
# {'id': 25, 'name': 'pikachu', 'height': 40, 'weight': 60, 'xp': 112, 'image_url': 
# 'https://pokeres.bastionbot.org/images/pokemon/25.png', 'pokemon_url':
#  'https://www.pokemon.com/us/pokedex/pikachu', 'abilities': [{'name':
#  'static', 'is_hidden': False}, {'name': 'lightning-rod', 'is_hidden':
#  True}], 'stats': [{'name': 'hp', 'base_stat': 35}, {'name': 'attack',
#  'base_stat': 55}, {'name': 'defense', 'base_stat': 40}, {'name': 
# 'special-attack', 'base_stat': 50}, {'name': 'special-defense', 
# 'base_stat': 50}, {'name': 'speed', 'base_stat': 90}], 'types': 
# [{'name': 'electric'}]}
