from gendiff import generate_diff as gd


d1 = 'file1.json'
d2 = 'file2.json'

def test_generate():
    assert type(gd(d1, d2)) == str
    assert gd(d1, d2) == '-1follow: False\n host: hexlet.io\n-proxy: 123.234.53.22\n-timeout: 50\n+timeout: 20\n+verbose: True'






