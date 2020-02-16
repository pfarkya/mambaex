from mambaex import MambaexApps
from mambaex.mambaexApps import NameShouldBeString
import pytest

#This file to test only the part of related file test only

class TestMambaexApps:
    @pytest.mark.parametrize(
        'name', (
            ('hiwpefhipowhefopw'),
            ('localhost:3128'),
            ('localhost.localdomain:3128/'),
            ('10.122.1.1:3128/'),
            ('http://'),
            (''),
        ))
    def test_instance_creation(self, name):
        value = MambaexApps.getOrCreateApp(name)
        assert value.name == name
    @pytest.mark.parametrize(
        'name', (
            (15),
            (KeyError),
            (None)
        ))
    def test_instance_creation_failed_with_type_error(self, name):
        with pytest.raises(NameShouldBeString):
            assert MambaexApps.getOrCreateApp(name)

    def test_multiple_instance_creation(self):
        instance1 = MambaexApps.getOrCreateApp('instance1')
        instance2 = MambaexApps.getOrCreateApp('instance1')
        assert instance1 == instance2

    def test_multiple_instance_with_different_name_should_different(self):
        instance1 = MambaexApps.getOrCreateApp('instance1')
        instance2 = MambaexApps.getOrCreateApp('instance2')
        assert instance1 != instance2

    def test_multiple_instance_with_no_name_should_same(self):
        instance1 = MambaexApps.getOrCreateApp()
        instance2 = MambaexApps.getOrCreateApp()
        assert instance1 == instance2
