import contextlib
import netifaces as ni
import os

def get_current_ip():
    interfaces = ni.interfaces()
    
    for interface in interfaces:
        with contextlib.suppress(ValueError, KeyError):
            addresses = ni.ifaddresses(interface)
            ipv4_address = addresses[ni.AF_INET][0]['addr']
            if ipv4_address != '127.0.0.1':
                return ipv4_address

    return None

def update_env_file(ip):
    try:
        if not os.path.isfile('.env'):
            with open('.env', 'w') as new_file:
                new_file.write(f'MY_IP={ip}\n')
        else:
            with open('.env', 'r') as file:
                lines = file.readlines()
            
            with open('.env', 'w') as file:
                for line in lines:
                    if line.startswith('MY_IP='):
                        continue
                    else:
                        file.write(line)
                file.write(f'MY_IP={ip}\n')

        print(f'IP atualizado no arquivo .env: MY_IP={ip}')
    except Exception as e:
        print(f"Erro ao atualizar o arquivo .env: {e}")

def main():
    ip = get_current_ip()
    if ip:
        update_env_file(ip)

if __name__ == "__main__":
    main()