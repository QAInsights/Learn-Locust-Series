import re
import random
import requests

# import random
# status_codes = [100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305,
#                         307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416,
#                         417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 444, 451, 499, 500, 501, 502, 503, 504, 505,
#                         506, 507, 508, 510, 511, 599]
# print(random.choice(status_codes))
#
response = '''
<area alt="Birds" coords="72,2,280,250"
                href="Catalog.action?viewCategory=&categoryId=BIRDS" shape="RECT" />
        <area alt="Fish" coords="2,180,72,250"
                href="Catalog.action?viewCategory=&categoryId=FISH" shape="RECT" />
        <area alt="Dogs" coords="60,250,130,320"
                href="Catalog.action?viewCategory=&categoryId=DOGS" shape="RECT" />
        <area alt="Reptiles" coords="140,270,210,340"
                href="Catalog.action?viewCategory=&categoryId=REPTILES" shape="RECT" />
        <area alt="Cats" coords="225,240,295,310"
                href="Catalog.action?viewCategory=&categoryId=CATS" shape="RECT" />
        <area alt="Birds" coords="280,180,350,250"
                href="Catalog.action?viewCategory=&categoryId=BIRDS" shape="RECT" />

'''
r = re.findall("href=\"Catalog.action\?viewCategory=&categoryId=(.*?)\"", response)
print(r)
print(random.choice(r))
# print(r.group(1))
# print(len(r.groups()))
# print(r.groups())
#
# r = requests.session()
#
# r.cookies.cl

# print("Hello "future "python!")

# print("Hello future python!")
