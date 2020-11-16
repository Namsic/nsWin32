import socket, threading


class Transfer:
    def __init__(self, _socket):
        self.len_size = 10
        self.set_socket(_socket)
        self.func_dict = {}
    
        
    def set_socket(self, _socket):
        self._socket = _socket


    def send_data(self, header, data):
        if type(data) == str:
            data = data.encode()

        l = format(len(data), '0'+str(self.len_size)).encode()

        self._socket.sendall(header.encode() + l + data)


    def recv_data(self):
        header = self._socket.recv(3).decode()
        if not header:
            return
        l = int(self._socket.recv(self.len_size))
        recv = self._socket.recv(l)
        return header, recv


    def receive(self):
        while True:
            head, data = self.recv_data()
            
            if head == 'txt':
                print('recv: ' + data.decode())
            elif head == 'ech':
                self.send_data('txt', data)
            elif head in self.func_dict:
                self.func_dict[head](data)
            else:
                self.send_data('txt', '[{}] is not defined(data: {}'.format(head, data))


    def receive_on(self):
        thrd = threading.Thread(target=self.receive)
        thrd.daemon = True
        thrd.start()


class Server:
    def __init__(self):
        addr = ('', 3056)

        server_socket = socket.socket()
        server_socket.bind(addr)
        server_socket.listen()
        self.client_socket, c_addr = server_socket.accept()

    def input_cmd(self):
        t = Transfer(self.client_socket)
        t.receive_on()
        print('ok')
        while True:
            h = input('header: ')
            d = input('data: ')
            t.send_data(h, d)


class Client:
    def __init__(self, ip_add='127.0.0.1'):
        _socket = socket.socket()
        _socket.connect((ip_add, 3056))
        self.T = Transfer(_socket)



if __name__ == '__main__':
    Server().input_cmd()
