# 🛡️ IDS/IPS Intelligent Hybride

Système de détection et prévention d'intrusions combinant **Suricata** et **Intelligence Artificielle** pour identifier et bloquer automatiquement les attaques réseau en temps réel.

## 🏗️ Architecture
Kali (Attaquant)
↓
Scapy (Packet Analyzer)
↓
Suricata (Signature Engine) + Random Forest IA
↓
IPS Blocker (iptables)
↓
Logstash → Elasticsearch → Grafana Dashboard

## 🔧 Technologies utilisées

| Outil | Rôle |
|---|---|
| **Suricata** | IDS/IPS - Détection par signatures |
| **Python / Scapy** | Capture et analyse de paquets |
| **Random Forest** | Détection comportementale par IA |
| **Elasticsearch** | Stockage des alertes |
| **Logstash** | Transport des logs |
| **Grafana** | Dashboard SOC temps réel |
| **Kali Linux** | Simulation d'attaques |

## 📊 Résultats

- ✅ **50,185 règles** Suricata chargées
- ✅ **77.27% accuracy** du modèle IA
- ✅ **97% précision** sur la détection d'attaques
- ✅ Blocage automatique des IPs attaquantes

## 🚨 Attaques détectées

- Scan Nmap
- SSH Brute Force
- Ping Flood / ICMP
- Analyse comportementale anormale

## 📸 Screenshots

### Dashboard Grafana SOC
![Dashboard](screenshots/dashboardGrafana1.png)

### Alertes Suricata en temps réel
![Alertes](screenshots/alertesucricata2.png)

### Packet Analyzer (Scapy)
![Scapy](screenshots/Packet_Analyzer3.png)

### Détection et Blocage automatique
![Blocage](screenshots/attaque_detectee4.png)

### Modèle IA - Random Forest
![IA](screenshots/Modele_IA5.png)

## 🚀 Lancement du projet

### 1. Démarrer les services
```bash
sudo systemctl start elasticsearch logstash grafana-server
sudo suricata -c /etc/suricata/suricata.yaml -i ens33
```

### 2. Lancer le Packet Analyzer + IA
```bash
sudo python3 -W ignore packet_analyzer.py
```

### 3. Lancer l'IPS Blocker
```bash
sudo python3 ips_blocker.py
```

### 4. Entraîner le modèle IA
```bash
python3 model.py
```

## 👩‍💻 Auteur

**Lembahej Manal & Kamali Chaimae** — 4CIR-G3-EMSI ANFA
