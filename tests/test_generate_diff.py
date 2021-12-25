from gendiff import generate_diff as gd


d1 = 'f1.json'
d2 = 'f2.json'

def test_generate():
    assert type(gd(d1, d2)) == str
    assert gd(d1, d2) == '-follow: False\n host: hexlet.io\n' \
                         '-proxy: 123.234.53.22\n-timeout: 50\n' \
                         '+timeout: 20\n+verbose: True'
