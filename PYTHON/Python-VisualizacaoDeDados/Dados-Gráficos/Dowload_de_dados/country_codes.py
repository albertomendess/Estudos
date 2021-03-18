from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Devolve o código de duas letras da Pygal país, dado o seu nome."""
    for code, name in COUNTRIES.items():
        if name == country_name.title():
            return code
        elif country_name.title() == 'Bolivia':
            return 'bo'
        elif country_name.title() == 'Congo, Rep.':
            return 'cd'
        elif country_name.title() == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name.title() == 'Gambia, The':
            return 'gm'
        elif country_name.title() == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name.title() == 'Korea, Rep.':
            return 'kp'
        elif country_name.title() == 'Libya':
            return 'ly'
        elif country_name.title() == 'Slovak Republic':
            return 'sk'
        elif country_name.title() == 'Tanzania':
            return 'tz'
        elif country_name.title() == 'Venezuela, RB':
            return 've'
        elif country_name.title() == 'Vietnam':
            return 'vt'
        elif country_name.title() == 'Yemen, Rep.':
            return 'ye'
    # Se o país não for encontrado, devolve None.
    return None
