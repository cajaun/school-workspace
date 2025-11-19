

import socket
import sys
from random import SystemRandom
from numTheory import NumTheory


randomGenerator = SystemRandom()

def serverHello():
    """Generates client hello message"""
    return "100 Hello"

def computeSecretKey(g, p):
    """Computes this node's secret key"""
    return randomGenerator.randint(1, int(p) - 1)

def computePublicKey(g, p, s):
    """Computes a node's public key"""
    return NumTheory.expMod(int(g), int(s), int(p))

def sendPublicKey(g, p, s):
    """Sends node's public key"""
    return "120 PubKey " + str(computePublicKey(g, p, s))

def processMsgs(s, msg, state):
    """
    This function processes messages that are read through the socket. It
     returns a status, which is an integer indicating whether the operation
     was successful.
    """
    while msg:
        print("Received:", msg)
        parts = msg.strip().split()

        # Server sends generator and prime
        if parts[0] == "105":  
            g, p = parts[-2], parts[-1]
            state['g'] = int(g)
            state['p'] = int(p)
            # Generate client's secret key
            state['y'] = computeSecretKey(state['g'], state['p'])
            
            # Send client's public key to server
            pubkey_msg = sendPublicKey(state['g'], state['p'], state['y'])
            s.sendall(pubkey_msg.encode('utf-8'))

         # Server sends its public key
        elif parts[0] == "121":  
            state['server_pub'] = int(parts[-1])
        
            state['shared'] = NumTheory.expMod(state['server_pub'], state['y'], state['p'])
            print("Shared secret computed.")

        # Server sends nonce challenge
        elif parts[0] == "130":  
            state['nonce'] = int(parts[-1])
            transformed = state['nonce'] - 5
            state['transformed'] = transformed
            send_msg = "131 Transformed Nonce " + str(transformed)
            s.sendall(send_msg.encode('utf-8'))

        # Server verifies and responds
        elif parts[0] == "220":
            print("Verification successful!")
            return 0
        elif parts[0] == "400":
            print("Error received from server.")
            return 1

       
        try:
            msg = s.recv(1024).decode('utf-8')
        except:
            break

    return 0

def main():
    """
    Main entry point for the client.
    - Accepts client name as input
    - Accepts server host and port from command line args
    - Initiates handshake with the server
    - Runs the full message exchange
    """
    if len(sys.argv) != 3:
        print("Please supply a server address and port.")
        sys.exit()
    serverHost = str(sys.argv[1])
    serverPort = int(sys.argv[2])

   
    client_name = input("Enter client name: ")
    print(f"Client of {client_name}")
    print("""
  The purpose of this program is to implement a simple program that will carry
  out an exchange of messages that contains elements of a zero knowledge proof.
  The client sends a hello message to the server. The server responds with a
  message containing a generator, a prime, some public information, and
  a commitment message. The client will respond with a challenge message that
  contains an integer. The server transforms that received integer and then
  sends a response message to the client. The client checks that this
  transformed integer shows that the server knows the secret (without the
  secret being revealed).""")

    # Open TCP socket and connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((serverHost, serverPort))
        state = {}

    
        hello = serverHello()
        sock.sendall(hello.encode('utf-8'))

 
        msg = sock.recv(1024).decode('utf-8')
        processMsgs(sock, msg, state)

   
        print("\n--- CLIENT SUMMARY ---")
        print(f"Client Name = {client_name}")
        print(f"g = {state.get('g')}")
        print(f"p = {state.get('p')}")
        print(f"Client private key (y) = {state.get('y')}")
        print(f"Client public key = {computePublicKey(state['g'], state['p'], state['y'])}")
        print(f"Server public key = {state.get('server_pub')}")
        print(f"Shared secret = {state.get('shared')}")
        print(f"Nonce = {state.get('nonce')} | Transformed = {state.get('transformed')}")
        print("---------------------")

if __name__ == "__main__":
    main()