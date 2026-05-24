import pickle
import subprocess
from scapy.all import sniff, IP, TCP, UDP
import numpy as np
from collections import defaultdict
import time

packet_count = defaultdict(list)

# Charge le modèle IA
print("🔄 Chargement du modèle IA...")
with open('/home/ubuntu/ids_model.pkl', 'rb') as f:
    model = pickle.load(f)
print("✅ Modèle IA chargé !")

blocked_ips = set()

def block_ip(ip):
    if ip not in blocked_ips:
        print(f"🚨 Attaque détectée ! Blocage de {ip}")
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])
        blocked_ips.add(ip)
        print(f"✅ IP {ip} bloquée !")

def extract_features(packet):
    features = [0] * 41
    if IP in packet:
        features[0] = len(packet)          # duration/size
        features[4] = len(packet)          # src_bytes
        features[5] = 0                    # dst_bytes
        if TCP in packet:
            features[1] = 6               # protocol TCP
            features[23] = packet[TCP].sport  # src port
        elif UDP in packet:
            features[1] = 17              # protocol UDP
    return features

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        if src_ip == '127.0.0.1' or src_ip == '192.168.10.2':
            return
        now = time.time()
        packet_count[src_ip].append(now)
        # Garde seulement les paquets des 5 dernières secondes
        packet_count[src_ip] = [t for t in packet_count[src_ip] if now - t < 5]
        count = len(packet_count[src_ip])
        print(f"📦 {src_ip} → {count} paquets/5sec")
        if count > 50:
            print(f"⚠️  Attaque détectée depuis {src_ip} !")
            block_ip(src_ip)

print("🔍 Packet Analyzer démarré sur ens33...")
print("En attente de paquets suspects...\n")
sniff(iface="ens33", prn=analyze_packet, store=0)
S
