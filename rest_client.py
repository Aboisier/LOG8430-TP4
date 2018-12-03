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


def gen_receipt(nb_products, freq_type=None):
    products = []
    if freq_type is not None:
        nb_freq_products = nb_products // 2
        products += random.sample(PRODUCTS_DICT[freq_type], nb_freq_products)
        nb_products -= nb_freq_products

    products += random.sample(ALL_PRODUCTS, nb_products)
    products_dict = { product: random.randint(1, 100) for product in products }
    return { 'id': str(uuid.uuid4()), 'products': products_dict }

def add_receipt(receipt):
    url = 'http://localhost:3000'
    headers = {'Content-Type': 'application/json'}
    body = json.dumps(receipt)
    req = urllib2.Request(url, body, headers)
    res = urllib2.urlopen(req)

def populate_database(nb_receipts, max_nb_products, freq_type=None):
    for _ in range(nb_receipts):
        nb_products = random.randint(2, max_nb_products)
        receipt = gen_receipt(nb_products, freq_type)
        add_receipt(receipt)

def clear_database():
    url = 'http://localhost:3000/clear'
    req = urllib2.Request(url, '')
    res = urllib2.urlopen(req)

def get_all_products():
    url = 'http://localhost:3000'
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    print res.read()
        
def get_frequent_products():
    url = 'http://localhost:3000/frequent'
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    print res.read()



