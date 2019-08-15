#16.7

import csv
filename = 'csv/API_TX.VAL.MRCH.XD.WD_DS2_en_csv_v2_46748.csv'
from country_codes import get_country_code 
from pygal.style import LightGreenStyle as LCS, RotateStyle as RS
from pygal_maps_world.maps import World

with open(filename) as file:
    reader = csv.DictReader(file)
    #for row in reader:
    #    print(row)
    tx_dic = {}
    for row in reader:
    #    print(row['Country Code'][0:2])
        if '2018' in row:
            country_name = row['ď»ż"Country Name"']
            country_code = row['Country Code']
            try:
                export_value_index = float(row['2017'])
            except ValueError:
                continue
            code = get_country_code(country_name)
            if code:
                tmp={code:export_value_index}
                tx_dic.update(tmp)
            else:
                print("Błąd - " + country_name)
    #print(tx_dic)

# Podzielenie państw na trzy grupy według wielkości indexu
tx_dic_100, tx_dic_300, tx_dic_more = {}, {}, {} 
for cc, pop in tx_dic.items():
    if pop < 100:
        tx_dic_100[cc] = pop
    elif pop < 300:
        tx_dic_300[cc] = pop
    else:
        tx_dic_more[cc] = pop


# Przygotowanie wykresu

wm_style = RS('#336699', base_style = LCS)
wm = World(style=wm_style)

wm.force_url_protocol = 'http'
wm.title = 'Export value index w 2017 roku. (dane dla poszczególnych państw)'
wm.add('< 100', tx_dic_100)
wm.add('100 < 300', tx_dic_300)
wm.add('< 300', tx_dic_more)


wm.render_to_file('Export_value_index_2017.svg')

