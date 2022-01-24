import yaml
from exceptions import (
    ConfigFileError,
    ColorInConfigIsNotATuple,
    MissingArgumentsConfigFile,
    ConfigResolutionError
)


def check_if_settings_are_correct(settings):
    correct = True
    for color in settings['colors']:
        try:
            if not isinstance(eval(settings['colors'][color]), tuple):
                correct = color
        except(TypeError):
            raise ColorInConfigIsNotATuple(color)
    try:
        if not isinstance(settings['FONT'], str):
            correct = 'FONT'
        if not isinstance(settings['FONTSIZE'], int):
            correct = 'FONTSIZE'
        if not isinstance(settings['WIDTHOFBOARD'], int):
            correct = 'WIDTHOFBOARD'
        if not isinstance(settings['MULTIPLIEDSIZE'], int):
            correct = 'MULTIPLIEDSIZE'
        if not isinstance(settings['NUMBERINROWTOWIN'], int):
            correct = 'NUMBERINROWTOWIN'
        if not isinstance(settings['NUMBEROFPAWNS'], int):
            correct = 'NUMBEROFPAWNS'
        if not isinstance(settings['BOARDSIZE'], int):
            correct = 'BOARDSIZE'
    except(KeyError):
        raise MissingArgumentsConfigFile
    resolution = eval(settings['RESOLUTION'])
    if not isinstance(resolution, tuple) or len(resolution) != 2:
        correct = 'RESOLUTION'
    return correct


def load_and_unpack_settings_yaml():
    path = 'globtroters/settings/config_file.yaml'
    settings = {}
    try:
        with open(path, 'r') as handle:
            settings = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        print(exc)
    setting_status = check_if_settings_are_correct(settings)
    if setting_status is True:
        for color in settings['colors']:
            settings['colors'][color] = eval(settings['colors'][color])
        settings['WIDTHOFBOARD'] = int(settings['WIDTHOFBOARD'])
        settings['MULTIPLIEDSIZE'] = int(settings['MULTIPLIEDSIZE'])
        settings['RESOLUTION'] = eval(settings['RESOLUTION'])
        return settings['colors'], settings
    else:
        raise ConfigFileError(setting_status)
