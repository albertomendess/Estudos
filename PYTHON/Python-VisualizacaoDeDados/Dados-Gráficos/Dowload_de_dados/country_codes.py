from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Devolve o código de duas letras da Pygal país, dado o seu nome."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Rep.':
            return 'cd'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Rep.':
            return 'kp'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vt'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
    # Se o país não for encontrado, devolve None.
    return None
