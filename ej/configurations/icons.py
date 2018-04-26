FONT_AWESOME_ICONS = {'bars', 'fa-facebook', 'fa-telegram', 'fa-whatsapp', 'fa-twitter'}
MATERIAL_ICONS = {'menu'}

# A list of pairs of {social network: (fa icon, material icon)}
NETWORK_ICONS = {
    'facebook': ('fa-facebook', 'facebook'),
}


def default_icon_name(network, lib='fa'):
    fa, material = NETWORK_ICONS.get(network.lower(), (None, None))
    return fa if lib == 'fa' else material