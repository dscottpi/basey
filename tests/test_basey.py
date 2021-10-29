from basey import __version__
from basey.lib import decode, encode

def test_version():
    assert __version__ == '0.1.0'

def test_base62_encoding():
    result = encode(11157)
    assert result == '2TX'

def test_base62_decode():
    result = decode('2TX')
    assert result == 11157

def test_encode_decode():
    to_encode = 23472938
    encoded = encode(to_encode)
    decoded = decode(encoded)

    assert decoded == to_encode
