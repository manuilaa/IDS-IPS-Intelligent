import json
import subprocess
import time

LOG_FILE = "/var/log/suricata/eve.json"
blocked_ips = set()

def block_ip(ip):
    if ip not in blocked_ips:
        print(f"🚨 Blocage de l'IP: {ip}")
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])
        blocked_ips.add(ip)
        print(f"✅ IP {ip} bloquée !")

def monitor():
    print("🔍 IPS Blocker démarré - surveillance en cours...")
    with open(LOG_FILE, 'r') as f:
        f.seek(0, 2)  # Va à la fin du fichier
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            try:
                event = json.loads(line)
                if event.get('event_type') == 'alert':
                    src_ip = event.get('src_ip')
                    alert_msg = event['alert']['signature']
                    print(f"⚠️  Alerte: {alert_msg} depuis {src_ip}")
                    block_ip(src_ip)
            except json.JSONDecodeError:
                continue

if __name__ == "__main__":
    monitor()
