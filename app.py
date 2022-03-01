import json
from pickle import TRUE
from flask import Flask, request, jsonify, make_response, send_file, send_from_directory
import pandas as pd
import os




#Intialize app
app = Flask(__name__)


POKEMON_PICTURE_DIR = 'C:/Users/Chartres/Documents/workspace-Api/PokemonFile/Pictures-names'
POKEMON_FILE = "./PokemonFile/pokemon.csv"
# Read the pokemon csv table
pokemon_csv = pd.read_csv(POKEMON_FILE)
# dictionary that will hold the indexed data
pokemon_dictionary = {}

# The absolute path of the directory containing images for users to download
app.config["CLIENT_IMAGES"] = POKEMON_PICTURE_DIR


# build the dictionary in the form of 
# {
#   "pikachu": {number: , type1: ,}
# }
# changed the csv into more of a dictionary to allow for quick lookup
# by having a dictionary where the key is the name of the pokemon, it would
# allow me to find all the information i need just using the name
# other wise i would have had to go through the csv every time in order to find an entry



for _,row in pokemon_csv.iterrows():
    # made the name lower case to make sure there is consistency in all the pokemon names
    name = row["name"].lower()
    pokemon_dictionary[name] = {"number":row["pokedex_number"],"type1": row["type1"],"type2": row["type2"],"japanese_name":row["japanese_name"]}



# custom error message
def custom_error(message, status_code): 
    return make_response(jsonify(message), status_code)



# localhost:5000/pokemon
@app.route('/pokemon', methods=['GET'])
def get_all():
    # returns all the pokemons 
    return jsonify(pokemon_dictionary)



# localhost:5000/pokemon/<pokemon_name>
@app.route('/pokemon/<pokemon_name>', methods=['GET'])
def get_pokemon(pokemon_name):
    # made the provided name lowercase to match my dictionary
    pokemon_name = pokemon_name.lower()
    
    if pokemon_name in pokemon_dictionary:
        return jsonify(pokemon_dictionary[pokemon_name])
    else:
        return custom_error("Pokemon not found", 404)

#localhost:5000/pokemon/picture/<pokemon_name>   
# GET /pokemon/picture/cyndaquil
# pokemon_name = cyndaquil
@app.route('/pokemon/picture/<pokemon_name>', methods=['GET'])
def get_pokemon_picture(pokemon_name):
    pokemon_name = pokemon_name.lower()

    # if non letters 
    if (pokemon_name.isalpha() == False) or (pokemon_name == ''):
        return custom_error("bad input", 400)
    elif pokemon_name not in pokemon_dictionary:
        return custom_error("Pokemon not found", 404)
    else:
        pokemon_file_name = pokemon_name + '.jpeg'
        pokemon_file_list = os.listdir(app.config["CLIENT_IMAGES"])

        if (pokemon_file_name in pokemon_file_list ):
           return send_from_directory(app.config["CLIENT_IMAGES"], pokemon_file_name, as_attachment=True)
        else:
            return custom_error("Pokemon image not found", 404)





#Run Server
if __name__ == '__main__':
    app.run(debug=True)
