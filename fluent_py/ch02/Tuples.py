city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA','31195855'), ('BRA', 'CE34323223'),('ESP', 'XDA211212')]
# unpacking tuples
for passport in sorted(traveler_ids):
    print('%s %s' % passport)

print(divmod(20,8))
t = (20,8)
# tuples unpacking
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)


a, b, *rest = range(5)
print(a, b, rest)


# nested unpacking
metro_areas = [("Tokyo", "JP", 36.933, (35.689722, 139.648566)),
               ("Delhi NCR", "IN", 21.935, (28.244565, 77.02213214)),
               ("Shenzhen", "CN", 100.042, (19.124455, -99.3244445)),
               ("Mexico City", "MX", 20.104, (40.012462, -74.2654789)),
               ("Sao Paulo", "BR", 19.649, (-23.256456, -46.2554789))
               ]

print("{:15} | {:^9} | {:^9}".format('', 'lat.', 'long.'))
fmt = "{:15} | {:9.4f} | {:9.4f}"
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.878954, 139.254455))
print(tokyo.coordinates)

print(City._fields)


LatLong = namedtuple('LatLong','lat long')
delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.244565, 77.02213214))
delhi = City._make(delhi_data)
print(delhi, delhi._asdict())


for key, value in delhi._asdict().items():
    print(key+':', value)

s = "bicycle"
print(s[::3], s[::-1], s[::-2])

