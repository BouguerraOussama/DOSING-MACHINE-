🚨 DOSING-MACHINE

Simulateur SYN Flood Éducatif - Comprendre les vulnérabilités TCP/IP

Afficher l'image
Afficher l'image
Afficher l'image
📋 Description
DOSING-MACHINE est un outil éducatif conçu pour comprendre les attaques SYN Flood et l'impact sur les protocoles TCP/IP. Il simule une attaque par déni de service (DoS) dans un environnement contrôlé.
🎯 Objectifs pédagogiques

Comprendre le fonctionnement du three-way handshake TCP
Analyser l'impact des attaques SYN Flood sur les ressources serveur
Explorer les techniques de spoofing d'adresses IP
Sensibiliser aux vulnérabilités des protocoles réseau

⚠️ Usage Éthique UNIQUEMENT
🛑 AVERTISSEMENT CRITIQUE 🛑
Cet outil est destiné EXCLUSIVEMENT à des fins éducatives :
✅ Tests sur VOS propres systèmes
✅ Environnements de laboratoire/simulation  
✅ Recherche académique en sécurité
❌ AUCUN usage malveillant autorisé
🛠️ Installation
Prérequis
bash# Python 3.7+
python3 --version

# Privilèges administrateur (pour Scapy)
sudo -v
Dépendances
bash# Installation de Scapy
pip3 install scapy

# Ou avec requirements.txt
pip3 install -r requirements.txt
🚀 Usage
Syntaxe de base
bashsudo python3 dosing_machine.py <TARGET_IP> <TARGET_PORT> [OPTIONS]
Exemples d'utilisation
Test local basique
bash# Test sur localhost
sudo python3 dosing_machine.py 127.0.0.1 80
Configuration avancée
bash# 20 threads avec méthode Scapy
sudo python3 dosing_machine.py 192.168.1.100 8080 -t 20 -m scapy

# Méthode socket (sans privilèges root)
python3 dosing_machine.py 192.168.1.100 8080 -m socket
Options disponibles
OptionDescriptionDéfaut-t, --threadsNombre de threads10-m, --methodMéthode (scapy/socket)scapy-h, --helpAide-
🔧 Fonctionnalités
🎯 Deux méthodes d'attaque

Scapy : Contrôle total des paquets TCP/IP
Socket : Approche plus simple, pas de privilèges requis

📊 Monitoring temps réel
[DOSING] Paquets envoyés: 15847 | Taux: 1584.7 pkt/s | Durée: 10.0s
🧵 Multi-threading

Simulation de charge distribuée
Contrôle du nombre de threads
Synchronisation thread-safe

🛡️ Safeguards intégrés

Confirmation d'usage éthique
Validation des paramètres
Gestion propre des interruptions

🔬 Analyse Technique
Fonctionnement SYN Flood

Génération d'IPs sources aléatoires (spoofing)
Envoi massif de paquets SYN
Épuisement de la table de connexions du serveur
Déni de service pour les clients légitimes

Structure des paquets
python# Paquet SYN avec Scapy
ip_layer = IP(src=random_ip, dst=target_ip)
tcp_layer = TCP(sport=random_port, dport=target_port, flags="S")
packet = ip_layer / tcp_layer
📈 Métriques et Rapport
