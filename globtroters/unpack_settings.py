import yaml


def load_and_unpack_settings_yaml():
    # globtroters/
    path = 'globtroters/settings/config_file.yaml'
    settings = {}
    try:
        with open(path, 'r') as handle:
            settings = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        print(exc)
    for color in settings['colors']:
        settings['colors'][color] = eval(settings['colors'][color])
    settings['WIDTHOFBOARD'] = int(settings['WIDTHOFBOARD'])
    settings['MULTIPLIEDSIZE'] = int(settings['MULTIPLIEDSIZE'])
    settings['RESOLUTION'] = eval(settings['RESOLUTION'])
    return settings['colors'], settings
