import pytest
import socket as s


@pytest.fixture
def socket(request):
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    def socket_teardown():
        _socket.close()
    request.addfinalizer(socket_teardown)
    return _socket


def test_server_connect(socket):
    socket.connect(('localhost', 5000))
    assert socket

@pytest.fixture(scope='module')
def Server():
    class Dummy:
        host_port = 'localhost', 5000
        uri = 'http://%s:%s/' % host_port
    return Dummy


def test_server_connect(socket, Server):
    socket.connect(Server.host_port)
    assert socket

