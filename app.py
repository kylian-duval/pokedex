from flask import Flask, render_template
from requests import get

app = Flask (__name__)


@app.route('/')
def index():
    content = get ('https://studies.delpech.info/pbi/pokemons/dataset/json')
    pokemons = content.json()
    #pokemon = get ('https://tmare.ndelpech.fr/tps/pokemons/{}'.format(pokemons[0]['id'])).json()
    #pokemons = pokemon = get ('https://tmare.ndelpech.fr/tps/pokemons'.format()).json()
    #return pokemon['name']['fr'] + pokemon['name']['en']
    #pokemons = pokemons[0]
    return render_template('index.jinja', allPokemon = pokemons)

@app.route('/pokedex/<string:id>')
def pokedex(id):
    pokemon = get ('https://studies.delpech.info/pbi/pokemons/dataset/'+id+'/json').json()
    return render_template ('pokedex.jinja', pokemon = pokemon) 



#('https://studies.delpech.info/pbi/pokemons/dataset/'+id +'/json').json()
#pokemon = get ('https://tmare.ndelpech.fr/tps/pokemons/{}'.format(pokemons[id]['id'])).json()