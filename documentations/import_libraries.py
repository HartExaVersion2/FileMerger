import pip

libraries = ['deep_translator', 'PySimpleGUI', 'Pillow']


def install():
    for libra in libraries:
        pip.main(['install', libra])


install()