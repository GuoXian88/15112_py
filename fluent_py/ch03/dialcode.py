# BEGIN DIALCODES
# dial codes of the top 10 most populous countries
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)  # <1>
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))  # <2>
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))  # <3> 根据value重排
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3  # <4>

country_code = {code: country for code, country in DIAL_CODES}
country_code
{code: country.upper() for code, country in DIAL_CODES}

# END DIALCODES
"""
# BEGIN DIALCODES_OUTPUT
d1: dict_keys([880, 1, 86, 55, 7, 234, 91, 92, 62, 81])
d2: dict_keys([880, 1, 91, 86, 81, 55, 234, 7, 92, 62])
d3: dict_keys([880, 81, 1, 86, 55, 7, 234, 91, 92, 62])
# END DIALCODES_OUTPUT
"""