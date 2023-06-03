import psutil
import socket

print("www.github.com/hyzle\n")
def get_active_connections():
    connections = psutil.net_connections(kind='inet')
    active_connections = []

    for conn in connections:
        if conn.status == 'ESTABLISHED':
            local_ip = conn.laddr.ip
            local_port = conn.laddr.port
            remote_ip = conn.raddr.ip
            remote_port = conn.raddr.port
            process_name = psutil.Process(conn.pid).name()

            connection_info = {
                'local_ip': local_ip,
                'local_port': local_port,
                'remote_ip': remote_ip,
                'remote_port': remote_port,
                'process_name': process_name
            }

            active_connections.append(connection_info)

    return active_connections

def main():
    active_connections = get_active_connections()

    for connection in active_connections:
        local_ip = connection['local_ip']
        local_port = connection['local_port']
        remote_ip = connection['remote_ip']
        remote_port = connection['remote_port']
        process_name = connection['process_name']

        try:
            remote_host = socket.gethostbyaddr(remote_ip)[0]
        except socket.herror:
            remote_host = "Unknown"

        print(f"Local IP: {local_ip}")
        print(f"Local Port: {local_port}")
        print(f"Remote IP: {remote_ip}")
        print(f"Remote Port: {remote_port}")
        print(f"Remote Host: {remote_host}")
        print(f"Process Name: {process_name}")
        print()

    input("Press any key to exit...")

if __name__ == '__main__':
    main()
