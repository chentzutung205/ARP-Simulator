import socket

# network dictionary
NETWORK = {
    '192.168.0.1': 'E4:CF:FA:4F:C9:CD',
    '192.168.0.2': 'EB:87:79:1B:BC:DB',
    '192.168.0.3': 'C2:E0:21:7E:C0:90',
    '192.168.0.4': '00:0A:74:6D:93:18',
    '192.168.0.5': '88:4F:7C:79:0A:85'
}

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen()
    print("ARP server is running...")

    # Keep the server running
    while True:
        conn, addr = s.accept()
        with conn:
            # print('Connected by', addr)
            while True:
                ip = conn.recv(1024).decode('utf-8')
                if not ip: break
                mac = NETWORK.get(ip, None)
                response = mac if mac else 'Not Found'
                print(f"Received ARP request for IP: {ip}. Responded with: {response}")
                conn.sendall(response.encode('utf-8'))