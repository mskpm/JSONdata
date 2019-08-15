from pygal_maps_world.maps import World

wm = World()
wm.force_url_protocl = 'http'
wm.title = 'Ameryka Północna, Środkowa i Południowa'

wm.add('Ameryka Połnocna', ['ca', 'mx', 'us'])
wm.add('Ameryka Środkowa', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Ameryka Południowa', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
