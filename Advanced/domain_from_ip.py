import socket

def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]] + result[1]
    except socket.herror:
        return []

print(f'Solution: {reverse_dns("142.250.70.174")}')
