from mambaex.mambaexApp import MambaexApp
from mambaex import MambaexApps
import pytest

class TestMambaexApp:
    @pytest.mark.parametrize(
        'name', (
            ('hiwpefhipowhefopw'),
            ('localhost:3128'),
            ('localhost.localdomain:3128/'),
            ('10.122.1.1:3128/'),
            ('http://'),
        ))
    def test_direct_instance_creation_should_fail(self, name):
        with pytest.raises(Exception):
            assert MambaexApp(name)

    def test_get_function_should_add_appstack(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp()
        appInstance.get('/sss', callback)
        assert len(appInstance.appstack) == 1
    def test_post_function_should_add_appstack(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp()
        appInstance.post('/sss', callback)
        assert len(appInstance.appstack) == 2
    def test_put_function_should_add_appstack(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp()
        appInstance.put('/sss', callback)
        assert len(appInstance.appstack) == 3
    def test_use_function_should_add_appstack(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp()
        appInstance.use('/sss', callback)
        assert len(appInstance.appstack) == 4
    def test_delete_function_should_add_appstack(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp()
        appInstance.delete('/sss', callback)
        assert len(appInstance.appstack) == 5
    def test_patch_function_should_add_appstack(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp()
        appInstance.patch('/sss', callback)
        assert len(appInstance.appstack) == 6

    def test_get_function_check_path_should_be_correct(self):
        def callback(req, res, next):
            pass
        appInstance = MambaexApps.getOrCreateApp('1')
        appInstance.put('sss', callback)
        assert len(appInstance.appstack) == 1
