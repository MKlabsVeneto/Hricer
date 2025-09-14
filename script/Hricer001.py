# IMPORTS
import os

# VARS
usrdistrop = ''

# LOGO AND SIGN
print('Hricer, a dev and community driven python program to automatically install ricing programs and desktop stuff.    Copyright (C) 2025 Kevin De Togni, MKlabs')
print('distribuited on the GNU general public license 3.0v license')
print('          __________     __________')
print('         /         /    /         /')
print('        /         /    /         /')
print('       /         /    /         /')
print('      /         /____/         / __________  _______  _________   _________    __________          by MKlabs developer team')
print('     /                        / /         / /      / /        /  /   _____/   /         /          devs: MrMaxX')
print('    /                        / /         / /      / /   _____/  /   /        /         /')
print('   /          ____          / /    _____/ /      / /   /       /   /_____   /    _____/            official website:')
print('  /          /   /         / / /  |      /      / /   /_____  /    _____/  / /  |                  officialmklabsveneto.netlify.app')
print(' /          /   /         / / ||  |     /      / /         / /    /_____  / ||  |')
print('/__________/   /_________/ /__||__|    /______/ /_________/ /__________/ /__||__|                  version: 0.0.1 ALPHA')
print('')
print('its recommended to run this program as root or it will not work')
print('')
print('select current distro: 1 = ubuntu, 2 = fedora, 3 = arch linux')
print('')
usrdistro = input()
if usrdistro == '1':
    usrdistrop = 'apt'
elif usrdistro == '2':
    usrdistrop = 'dnf'
elif usrdistro == '3':
    usrdistrop = 'pacman'
print('')
print('select theme: MrMaxX')