import random


sites = {
    'minecraft': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 12, 'split': True, 'split_symbol': '-',
                  'split_pattern': (4, 4, 4)},
    'amazon': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 12, 'split': True, 'split_symbol': '-',
               'split_pattern': (4, 6, 4)},
    'itunes': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 16, 'split': False, 'split_symbol': '',
               'split_pattern': ()},
    'paypal': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 12, 'split': True, 'split_symbol': '-',
               'split_pattern': (4, 4, 4)},
    'playstation': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 12, 'split': True, 'split_symbol': '-',
                    'split_pattern': (4, 4, 4)},
    'steam': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 15, 'split': True, 'split_symbol': '-',
              'split_pattern': (4, 6, 5)},
    'card_number': {'symbols': '123456789', 'length': 16, 'split': False, 'split_symbol': '',
                    'split_pattern': ()},
    'xbox': {'symbols': 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789', 'length': 25, 'split': True, 'split_symbol': '-',
             'split_pattern': (5, 5, 5, 5, 5)},
    'playstore': {'symbols': 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789', 'length': 20, 'split': True, 'split_symbol': '-',
                  'split_pattern': (4, 4, 4, 4, 4)},
    'pokemontgc': {'symbols': 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789', 'length': 13, 'split': True, 'split_symbol': '-',
                   'split_pattern': (3, 4, 3, 3)},
    'netflix': {'symbols': 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789', 'length': 14, 'split': True, 'split_symbol': '-',
                'split_pattern': (4, 6, 4)},
    'ebay': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 10, 'split': False, 'split_symbol': '',
             'split_pattern': ()},
    'fortnite': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 13, 'split': True, 'split_symbol': '-',
                 'split_pattern': (5, 4, 4)},
    'roblox': {'symbols': '0123456789', 'length': 10, 'split': True, 'split_symbol': '-',
               'split_pattern': (3, 3, 4)},
    'webkinz': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 8, 'split': False, 'split_symbol': '',
                'split_pattern': ()},
    'imvu': {'symbols': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 10, 'split': False, 'split_symbol': '',
             'split_pattern': ()},
}

site_numbers = {"0": "minecraft", "1": "amazon", "2": "itunes", "3": "paypal", "4": "playstation", "5": "steam",
                "6": "card_number", "7": "xbox", "8": "playstore", "9": "pokemontgc", "10": "netflix", "11": "ebay",
                "12": "fortnite", "13": "roblox", "14": "webkinz", "15": "imvu"}

print("Hello to Gift Card Generator\nThis Script Is Just for educational purpose use it at your own risk")
total = int(input("How Many Would You Like To Generate?\n"))

mode = ""
while mode not in site_numbers:
    mode = input('Which Would You Like To Generate?\n' + '\n'.join([str(count) + ". " + x for count, x in enumerate(sites)]) + "\n")

key_list = []

for key in range(total):
    if sites[site_numbers[mode]]['split']:
        key = ''
        for block in sites[site_numbers[mode]]['split_pattern']:
            for char in range(block):
                key += random.choice(sites[site_numbers[mode]]['symbols'])
            key += sites[site_numbers[mode]]['split_symbol']

        key_list.append(key[:-1])

    else:
        key = ''

        for char in range(sites[site_numbers[mode]]['length']):
            key += random.choice(sites[site_numbers[mode]]['symbols'])

        key_list.append(key)

with open('~Developed by @ramy-zemo on GH.txt', 'a+') as file:
    for key in key_list:
        file.write(key + '\n')
