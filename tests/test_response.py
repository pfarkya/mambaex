from mambaex.response import Response
import pytest

class TestResponse:
    def test_request_initialization(self):
        response = Response()
        assert response != None
