import pytest

from LocAndEur import LocAndEur



def test_loc():
    mes = 'A ver si hacemos una barbacoa por Barcelona'
    res = LocAndEur(mes).matcher_loc()

    assert 'Madrid' in res