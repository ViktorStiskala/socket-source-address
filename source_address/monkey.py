import socket
real_create_conn = socket.create_connection


class MonkeySocket:
    _source_address = ('', 0)

    def patch_socket(self):
        def _create_connection(address, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, *args):
            return real_create_conn(address, timeout, self._source_address)
        socket.create_connection = _create_connection

    def switch_source_address(self, *source_address):
        self._source_address = source_address