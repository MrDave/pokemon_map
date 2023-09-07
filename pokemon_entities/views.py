import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from pokemon_entities.models import Pokemon
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = localtime()
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon.entities.filter(appeared_at__lte=now, disappeared_at__gt=now):
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon.image.url)
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    now = localtime()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.entities.filter(appeared_at__lte=now, disappeared_at__gt=now):
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    if pokemon.previous_evo:
        previous_evo = {
            "title_ru": pokemon.previous_evo.title,
            "pokemon_id": pokemon.previous_evo.id,
            "img_url": request.build_absolute_uri(pokemon.previous_evo.image.url),
        }
    else:
        previous_evo = {}

    next_pokemon = pokemon.next_evo.first()
    if next_pokemon:
        next_evo = {
            "title_ru": next_pokemon.title,
            "pokemon_id": next_pokemon.id,
            "img_url": request.build_absolute_uri(next_pokemon.image.url)
        }
    else:
        next_evo = {}


    pokemon_dict = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'next_evolution': next_evo,
        'previous_evolution': previous_evo
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_dict
    })
