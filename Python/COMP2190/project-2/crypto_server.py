# Server to implement the simplified RSA algorithm and receive encrypted
# integers from a client.
# The server waits for the client to say Hello. Once the client says hello,
# the server sends the client a public key. The client uses the public key to
# send a session key with confidentiality to the server.

import socket
import random
import math
import hashlib
import time
import sys
import simplified_AES
from NumTheory import NumTheory


class RSAServer(object):
    
    def __init__(self, port, p, q):
         # Create TCP socket
        self.socket = socket.socket()
        # The option below is to permit reuse of a socket in less than an MSL
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("", int(port)))
        self.socket.listen(5)
        
        # Store primes for RSA key generation
        self.p = p
        self.q = q
    
    
        self.lastRcvdMsg = None
        self.sessionKey = None		#For storing the symmetric key
        self.modulus = None		#For storing the server's n in the public/private key
        self.pubExponent = None	#For storing the server's e in the public key
        self.privExponent = None	#For storing the server's d in the private key
        self.nonce = None
        # Call the methods to compute the public private/key pairs
        

    def send(self, conn, message):
        """Send UTF-8 encoded message to client."""
        conn.send(bytes(message,'utf-8'))

    def read(self):
        try:
            data = self.socket.recv(4096).decode('utf-8')
        except BlockingIOError:
            pass
        else:
            if data:
                self.lastRcvdMsg = data
            else:
                raise RuntimeError("Client is unavailable")

    def close(self, conn):
        print("closing server side of connection")
        try:
            conn.close()
        except OSError as e:
            print(
                "error: socket.close() exception for",
                f" {repr(e)}",
            )
        finally:
            # Delete reference to socket object
            conn = None    

    def RSAencrypt(self, msg):
        """RSA encryption: c = m^e mod n"""
        if msg >= self.modulus:
            raise ValueError("Message must be < n")
        return NumTheory.expMod(msg, self.pubExponent, self.modulus)

    def RSAdecrypt(self, cText):
        """RSA decryption: m = c^d mod n"""
        return NumTheory.expMod(cText, self.privExponent, self.modulus)

    def AESdecrypt(self, cText):
        """Decryption side of AES"""
        simplified_AES.keyExp(self.sessionKey)
        return simplified_AES.decrypt(cText)

    def AESencrypt(self, plaintext):
        """Computes the simplified AES encryption of some plaintext"""
        simplified_AES.keyExp(self.sessionKey) # Generating round keys for AES.
        ciphertext = simplified_AES.encrypt(plaintext) # Running simplified AES.
        return ciphertext

    def generateNonce(self):
        """This method returns a 16-bit random integer derived from hashing the
            current time. This is used to test for liveness"""
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        self.nonce = int.from_bytes(hash.digest()[:2], byteorder=sys.byteorder)

    def findE(self, phi):
        """Select a random e such that gcd(e,phi)=1."""
        while True:
            e = random.randint(3, phi-1)
            if NumTheory.gcd_iter(e, phi) == 1:
                return e

    def genKeys(self, p, q):
        """Generate RSA modulus n, phi(n), e, and private key d."""
        self.modulus = p * q
        phi = (p - 1) * (q - 1)

        self.pubExponent = self.findE(phi)
        self.privExponent = NumTheory.ext_Euclid(phi, self.pubExponent)

        print("n =", self.modulus)
        print("phi(n) =", phi)
        print("e =", self.pubExponent)
        print("d =", self.privExponent)

    def clientHelloResp(self):
        """Generates response string to client's hello message"""
        self.generateNonce()
        status = "102 Hello AES, RSA16, " + str(self.modulus) + ", " + \
         str(self.pubExponent) + ", " + str(self.nonce)
        return status

    def nonceVerification(self, decryptedNonce):
        """Check if client-returned nonce matches original."""
        return decryptedNonce == self.nonce


    def start(self):
        self.genKeys(self.p, self.q)
        
        print("Server started...")

        while True:
            connSocket, addr = self.socket.accept()
            print("Connection from:", addr)

            msg = connSocket.recv(4096).decode('utf-8')
            print("Client:", msg)

            # send hello + pubkey + nonce
            self.send(connSocket, self.clientHelloResp())

            # receive session key msg
            sessionMsg = connSocket.recv(4096).decode('utf-8')
            print("Client:", sessionMsg)

            parts = sessionMsg.split()
            # Expected: "103 SessionKey encKey encNonce"
            encKey = int(parts[2])
            encNonce = int(parts[3])

            # Decrypt session key using RSA
            sessionKey = self.RSAdecrypt(encKey)
            
            self.sessionKey = sessionKey

            decryptedNonce = self.AESdecrypt(encNonce)

            # Validate nonce
            if not self.nonceVerification(decryptedNonce):
                self.send(connSocket, "400 Error")
                self.close(connSocket)
                break

            self.send(connSocket, "104 Nonce Verified")

            # Receive encrypted integers
            encInts = connSocket.recv(4096).decode('utf-8').split()
            print("Client:", encInts)

            a_enc = int(encInts[2])
            b_enc = int(encInts[3])

            a = self.AESdecrypt(a_enc)
            b = self.AESdecrypt(b_enc)

            result = a + b
            result_enc = self.AESencrypt(result)

            self.send(connSocket, f"114 CompositeEncrypted {result_enc}")

            connSocket.close()
            break

def main():
    args = sys.argv
    if len(args) != 2:
        print ("Please supply a server port.")
        sys.exit()
        
    HOST = ''		# Symbolic name meaning all available interfaces
    PORT = int(args[1])     # The port on which the server is listening
    if PORT < 1023 or PORT > 65535:
        print("Invalid port specified.")
        sys.exit()
    print("Server of Cajaun")
    print ("""Enter prime numbers. One should be between 211 and 281,
    and the other between 229 and 307. The product of your numbers should
    be less than 65536""")
    p = int(input('Enter P: '))
    q = int(input('Enter Q: '))
    
    server = RSAServer(PORT, p, q)
    server.start()

if __name__ == "__main__":
    main()
