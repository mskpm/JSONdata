from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Zwraca stosowany przez Pygal dwuznakowy kod państwa
    przypisany danemu państwu.
    """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'  
        elif country_name == 'Congo, Rep.':
            return 'cg' 
        elif country_name == 'Tanzania':
            return 'tz'
    return None

def print_all_country_codes(pattern=''):
    if pattern:
        for code, name in COUNTRIES.items():
            if code.startswith(pattern.lower()):
                print(code + ':' + name)
    else:
        for code, name in COUNTRIES.items():
            print(code + ':' + name)