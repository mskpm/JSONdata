import json
from country_codes import get_country_code 
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal_maps_world.maps import World

# Wczytanie danych i umieszczenie ich na liście
filename = 'json/population_data.json'
with open(filename) as file:
    pop_data = json.load(file)

# Utworzenie słownika danych dotyczących populacji
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Podzieleniw państw na trzy grupy według liczebności populacji
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {} 
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# Przygotowanie wykresu

wm_style = RS('#336699', base_style = LCS)
wm = World(style=wm_style)

wm.force_url_protocol = 'http'
wm.title = 'Populacja na świecie w 2010 roku. (dane dla poszczególnych państw)'
wm.add('0 - 10 mln', cc_pops_1)
wm.add('10 mln - 1 mld', cc_pops_2)
wm.add('> 1 mld', cc_pops_3)


wm.render_to_file('world_population.svg')