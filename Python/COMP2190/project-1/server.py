

import socket
import sys
import random
from numTheory import NumTheory

randomGenerator = random.SystemRandom()

def PrimeCollect():
    """Accepts a prime number to send to the client"""
    primeNbr = int(input("Enter a prime number between 257 and 4093: "))
    while not NumTheory.IsPrime(primeNbr):
        print("Number is not prime.")
        primeNbr = int(input("Enter a prime number between 257 and 4093: "))
    return primeNbr

def GeneratorCollect(p):
    """Accepts a generator for the prime"""
    generator = int(input("Enter a generator for the prime number: "))
    while not NumTheory.IsValidGenerator(generator, p):
        print("Invalid generator for prime.")
        generator = int(input("Enter a generator for the prime number: "))
    return generator

def clientHello(g, p):
    """Generates an acknowledgement for the client's hello message"""
    return f"105 Generator + Prime {g} {p}"

def computePublicKey(g, p, s):
    """Computes node's public key"""
    return NumTheory.expMod(g, s, p)

def computeSecretKey(g, p):
    """Computes this node's secret key"""
    return randomGenerator.randint(1, p - 1)

def sendPublicKey(g, p, s):
    """Sends node's public key"""
    return "121 PubKey " + str(computePublicKey(g, p, s))

def generateNonce(p):
    """This method returns a 16-bit random integer derived from hashing the
		current time. This is used to test for liveness"""
    return randomGenerator.randint(6, p - 1)

def AllGood():
    """Generates 220 Verified"""
    return "220 Verified"

def ErrorCondition():
    """Generates 400 Error"""
    return "400 Error"

#s      = socket
#msg    = message being processed
#state  = dictionary containing state variables
def processMsgs(conn, msg, state):
    """This function processes messages that are read through the socket. It returns
     a status, which is an integer indicating whether the operation was successful."""
    while msg:
        print("Received:", msg)
        parts = msg.strip().split()

        # Client Hello 
        if parts[0] == "100": 
            conn.sendall(clientHello(state['g'], state['p']).encode('utf-8'))

        # Client public key received
        elif parts[0] == "120":  
            state['client_pub'] = int(parts[-1])
             # Compute shared secret
            state['shared'] = NumTheory.expMod(state['client_pub'], state['x'], state['p'])
            
            
            # Send server's public key back to client
            conn.sendall(sendPublicKey(state['g'], state['p'], state['x']).encode('utf-8'))
            
            # Generate nonce challenge and send to client
            state['nonce'] = generateNonce(state['p'])
            conn.sendall(f"130 Nonce {state['nonce']}".encode('utf-8'))

     # Client's transformed nonce received
        elif parts[0] == "131": 
            transformed = int(parts[-1])
             # Verify that the transformed value differs by exactly 5
            if abs(transformed - state['nonce']) == 5:
                conn.sendall(AllGood().encode('utf-8'))
            else:
                conn.sendall(ErrorCondition().encode('utf-8'))
            return  

        try:
            msg = conn.recv(1024).decode('utf-8')
        except:
            break
        
def main():
    """
    Main entry point for the server.
    - Accepts server name input.
    - Accepts port as command line argument.
    - Waits for client connections and processes messages.
    """
    if len(sys.argv) != 2:
        print("Please supply a server port.")
        sys.exit()
    HOST = ''
    PORT = int(sys.argv[1])
    if (PORT < 1023 or PORT > 65535):
        print("Invalid port specified.")
        sys.exit()


    server_name = input("Enter server name: ")
    print(f"Server of {server_name}")


    p = PrimeCollect()
    g = GeneratorCollect(p)


    x = computeSecretKey(g, p)

    # Save state variables
    state = {'p': p, 'g': g, 'x': x}

    # Create TCP socket and listen for one connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Listening on port {PORT}...")
        conn, addr = s.accept()
        with conn:
            print("Connected from:", addr)
            msg = conn.recv(1024).decode('utf-8')
            processMsgs(conn, msg, state)

   
    print("\n--- SERVER SUMMARY ---")
    print(f"Server Name = {server_name}")
    print(f"g = {g}")
    print(f"p = {p}")
    print(f"Server private key (x) = {x}")
    print(f"Server public key = {computePublicKey(g, p, x)}")
    print(f"Client public key = {state.get('client_pub')}")
    print(f"Shared secret = {state.get('shared')}")
    print(f"Nonce = {state.get('nonce')}")
    print("---------------------")

if __name__ == "__main__":
    main()