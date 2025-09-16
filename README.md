# 🚨 DOSING-MACHINE

> **Simulateur SYN Flood Éducatif** - Comprendre les vulnérabilités TCP/IP

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](#)
[![Ethical](https://img.shields.io/badge/Usage-Ethical%20Only-red.svg)](#)

## 📋 Description

DOSING-MACHINE est un outil éducatif conçu pour **comprendre les attaques SYN Flood** et l'impact sur les protocoles TCP/IP. Il simule une attaque par déni de service (DoS) dans un environnement contrôlé.

### 🎯 Objectifs pédagogiques
- Comprendre le fonctionnement du **three-way handshake TCP**
- Analyser l'impact des attaques SYN Flood sur les ressources serveur
- Explorer les techniques de **spoofing d'adresses IP**
- Sensibiliser aux vulnérabilités des protocoles réseau

## ⚠️ Usage Éthique UNIQUEMENT

```
🛑 AVERTISSEMENT CRITIQUE 🛑
Cet outil est destiné EXCLUSIVEMENT à des fins éducatives :
✅ Tests sur VOS propres systèmes
✅ Environnements de laboratoire/simulation  
✅ Recherche académique en sécurité
❌ AUCUN usage malveillant autorisé
```

## 🛠️ Installation

### Prérequis
```bash
# Python 3.7+
python3 --version

# Privilèges administrateur (pour Scapy)
sudo -v
```

### Dépendances
```bash
# Installation de Scapy
pip3 install scapy

# Ou avec requirements.txt
pip3 install -r requirements.txt
```

## 🚀 Usage

### Syntaxe de base
```bash
sudo python3 dosing_machine.py <TARGET_IP> <TARGET_PORT> [OPTIONS]
```

### Exemples d'utilisation

#### Test local basique
```bash
# Test sur localhost
sudo python3 dosing_machine.py 127.0.0.1 80
```

#### Configuration avancée
```bash
# 20 threads avec méthode Scapy
sudo python3 dosing_machine.py 192.168.1.100 8080 -t 20 -m scapy

# Méthode socket (sans privilèges root)
python3 dosing_machine.py 192.168.1.100 8080 -m socket
```

### Options disponibles
| Option | Description | Défaut |
|--------|-------------|---------|
| `-t, --threads` | Nombre de threads | 10 |
| `-m, --method` | Méthode (scapy/socket) | scapy |
| `-h, --help` | Aide | - |

## 🔧 Fonctionnalités

### 🎯 Deux méthodes d'attaque
- **Scapy** : Contrôle total des paquets TCP/IP
- **Socket** : Approche plus simple, pas de privilèges requis

### 📊 Monitoring temps réel
```
[DOSING] Paquets envoyés: 15847 | Taux: 1584.7 pkt/s | Durée: 10.0s
```

### 🧵 Multi-threading
- Simulation de charge distribuée
- Contrôle du nombre de threads
- Synchronisation thread-safe

### 🛡️ Safeguards intégrés
- Confirmation d'usage éthique
- Validation des paramètres
- Gestion propre des interruptions

## 🔬 Analyse Technique

### Fonctionnement SYN Flood
1. **Génération d'IPs sources aléatoires** (spoofing)
2. **Envoi massif de paquets SYN**
3. **Épuisement de la table de connexions** du serveur
4. **Déni de service** pour les clients légitimes

### Structure des paquets
```python
# Paquet SYN avec Scapy
ip_layer = IP(src=random_ip, dst=target_ip)
tcp_layer = TCP(sport=random_port, dport=target_port, flags="S")
packet = ip_layer / tcp_layer
```

## 📈 Métriques et Rapport

Le tool génère un rapport détaillé à l'arrêt :
```
╔══════════════════════════════════════════════════════════════╗
║                    RAPPORT D'ATTAQUE                        ║
╠══════════════════════════════════════════════════════════════╣
║ Paquets envoyés: 25000     Durée: 15.8s                    ║
║ Taux moyen: 1582.28 pkt/s                                   ║
║ Cible: 192.168.1.100:80                                     ║
╚══════════════════════════════════════════════════════════════╝
```

## 🎓 Contexte Éducatif

### Utilisations pédagogiques
- **Cours de sécurité réseau** : Démonstration pratique
- **Labs de cybersécurité** : Analyse du trafic avec Wireshark
- **Projets étudiants** : Compréhension des protocoles TCP/IP
- **Recherche** : Tests de résilience sur infrastructures contrôlées

### Analyses complémentaires
```bash
# Monitoring réseau pendant l'attaque
sudo tcpdump -i eth0 host <target_ip>

# Analyse avec Wireshark
wireshark -i eth0 -f "host <target_ip>"

# Monitoring système côté cible
netstat -an | grep SYN_RECV | wc -l
```

## ⚖️ Aspects Légaux

### ✅ Usages autorisés
- Tests sur vos propres systèmes
- Environnements de lab isolés
- Recherche académique encadrée
- Formation en cybersécurité

### ❌ Usages interdits
- Attaque de systèmes tiers
- Perturbation de services
- Tests sans autorisation explicite
- Usage commercial malveillant

## 🤝 Contribution

Les contributions sont bienvenues pour :
- Amélioration du code
- Nouvelles fonctionnalités éducatives
- Documentation technique
- Cas d'usage pédagogiques

## 📚 Ressources Complémentaires

### Documentation technique
- [RFC 793 - TCP Protocol](https://tools.ietf.org/html/rfc793)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [SYN Flood Attack Analysis](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)

### Défenses contre SYN Flood
- **SYN Cookies** : Validation sans état
- **Rate Limiting** : Limitation du taux de connexions
- **Firewall Rules** : Filtrage du trafic malveillant

## 👨‍💻 Auteur

**Oussama Bouguerra**  
Étudiant Ingénieur Cybersécurité - EPITA  
📧 oussama.bouguerra@epita.fr  
🔗 [GitHub](https://github.com/BouguerraOussama) | [LinkedIn](https://www.linkedin.com/in/bouguerraoussama/)

---

> *"La cybersécurité commence par la compréhension des vulnérabilités"*

## 📄 License

Usage éducatif uniquement. Toute utilisation malveillante est strictement interdite et de la responsabilité de l'utilisateu
