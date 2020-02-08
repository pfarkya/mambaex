import mambaex
import pytest

class TestMambaex:
    @pytest.mark.parametrize(
        'name', (
            ('hiwpefhipowhefopw'),
            ('localhost:3128'),
            ('localhost.localdomain:3128/'),
            ('10.122.1.1:3128/'),
            ('http://'),
        ))
    def test_invalid_url(self, name):
        value = mambaex.getServer(name)
        assert value == name
