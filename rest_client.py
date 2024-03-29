import argparse
import json
import random
import urllib2
import uuid

BEER = [ 'blue moon', 'budweiser', 'coors light', 'corona', 'guinness',
         'heineken', 'miller lite', 'molson dry', 'pabst blue ribbon', 'rickards' ]

CEREALS = [ 'capn crunch', 'cheerios', 'cinnamon toast crunch', 'froot loops', 'frosted flakes', 
            'lucky charms', 'mini wheats', 'raisin bran', 'rice krispies', 'special k']

FRUITS = [ 'ananas', 'banane', 'bleuet', 'fraise', 'framboise',
           'mangue', 'orange', 'peche', 'pomme', 'raisin' ]

PASTA = [  'farfalle', 'fettuccine', 'gnocchi', 'linguine', 'pappardelle',
           'penne rigate', 'ravioli', 'rigatoni', 'spaghetti', 'tortellini']

SPICES = [ 'aneth', 'basilic', 'cumin', 'origan', 'paprika',
           'persil', 'poivre', 'moutarde', 'sel', 'thym' ]

VEGETABLES = [ 'aubergine', 'broccoli', 'carotte', 'choux', 'concombre', 
               'courge', 'laitue', 'patate', 'poivron', 'radis' ]

ALL_PRODUCTS = BEER + CEREALS + FRUITS + PASTA + SPICES + VEGETABLES

PRODUCTS_DICT = { 'beer': BEER, 'cereals': CEREALS, 'fruits': FRUITS, 
                  'pasta': PASTA, 'spices': SPICES, 'vegetables': VEGETABLES }

def add_receipt(receipt):
    url = 'http://localhost:3000'
    headers = {'Content-Type': 'application/json'}
    body = json.dumps(receipt)
    req = urllib2.Request(url, body, headers)
    res = urllib2.urlopen(req)

def clear_database():
    url = 'http://localhost:3000/clear'
    req = urllib2.Request(url, '')
    res = urllib2.urlopen(req)

def get_receipts():
    url = 'http://localhost:3000'
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    return res.read()
        
def get_frequent_products():
    url = 'http://localhost:3000/frequent'
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    return res.read()

def gen_receipt(nb_products, freq_type=None):
    products = []
    if freq_type is not None:
        nb_freq_products = nb_products // 2
        products += random.sample(PRODUCTS_DICT[freq_type], nb_freq_products)
        nb_products -= nb_freq_products

    products += random.sample(ALL_PRODUCTS, nb_products)
    products_dict = { product: random.randint(1, 100) for product in products }
    return { 'id': str(uuid.uuid4()), 'products': products_dict }

def populate_database(nb_receipts, max_nb_products, freq_type=None):
    clear_database()

    if freq_type is None:
        freq_type = random.choice(PRODUCTS_DICT.keys())

    for _ in range(nb_receipts):
        nb_products = random.randint(2, max_nb_products)
        receipt = gen_receipt(nb_products, freq_type)
        add_receipt(receipt)


parser = argparse.ArgumentParser()
parser.add_argument('action', choices=[ 'clear', 'frequent', 'populate', 'receipts'],
                    help='The action to perform.')
parser.add_argument('--type', choices=PRODUCTS_DICT.keys(),
                    help='The procuct type that should be more frequent.')
parser.add_argument('--nb_receipts', type=int, default=100,
                    help='The number of receipts to generate when populating the database.')
args = parser.parse_args()

if args.action == 'clear':
    print 'Clearing database...'
    clear_database()
    print 'Database cleared!'
elif args.action == 'frequent':
    print 'Getting frequent products...'
    print get_frequent_products()
elif args.action == 'populate':
    print 'Populating database...'
    populate_database(args.nb_receipts, 10, args.type)
    print 'Database populated!'
elif args.action == 'receipts':
    print 'Getting all receipts...'
    print get_receipts()

