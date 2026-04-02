# Client to implement simplified RSA algorithm and then subsequently send
# encrypted prime numbers to a server. The client says hello to the server
# and indicates
# which cryptographic algorithms it can support. The server picks one
# asymmetric key and one symmetric key algorithm and then responds to the
# client with its public key and a nonce. The client generates a symmetric
# key to send to the server, encrypts the symmetric key with the public key,
# and then encrypts the nonce with the symmetric key.
# If the nonce is verified, then the server will send the "104 Nonce Verified"
# message.

import socket
import math
import random
import sys
import simplified_AES
from NumTheory import NumTheory


class RSAClient:
    def __init__(self, address, port):
        self.address = address
        self.port = int(port)
        self.socket = socket.socket()
        self.lastRcvdMsg = None
        self.sessionKey = None		#For storing the symmetric key
        self.modulus = None		    #For storing the server's n in the public key
        self.serverExponent = None	#For storing the server's e in the public key

    def connect(self):
        """Establish TCP connection to server."""
        self.socket.connect((self.address, self.port))


    def send(self, message):
        self.socket.send(bytes(message,'utf-8'))

    def read(self):
        try:
            data = self.socket.recv(4096).decode('utf-8')
        except BlockingIOError:
            pass
        else:
            if data:
                self.lastRcvdMsg = data
            else:
                raise RuntimeError("Server is unavailable")

    def close(self):
        print("closing connection to", self.address)
        try:
            self.socket.close()
        except OSError as e:
            print(
                "error: socket.close() exception for",
                f"{self.address}: {repr(e)}",
            )
        finally:
            # Delete reference to socket object for garbage collection
            self.socket = None

    def RSAencrypt(self, msg):
        """Encrypt session key using server RSA public key."""
        if msg >= self.modulus:
            raise ValueError("Message must be < n")
        return NumTheory.expMod(msg, self.serverExponent, self.modulus)

    def computeSessionKey(self):
        """Generate 15–16 bit random session key."""
        low = 1 << 15      
        high = min(65535, self.modulus - 1)
        self.sessionKey = random.randint(low, high)

    def AESencrypt(self, plaintext):
        """Computes the simplified AES encryption of some plaintext"""
        simplified_AES.keyExp(self.sessionKey) # Generating round keys for AES.
        ciphertext = simplified_AES.encrypt(plaintext) # Running simplified AES.
        return ciphertext
    
    def AESdecrypt(self, cText):
        simplified_AES.keyExp(self.sessionKey)
        return simplified_AES.decrypt(cText)

    def serverHello(self):
        status = "101 Hello 3DES, AES, RSA16, DH16"
        return status

    def sessionKeyMsg(self, nonce):
        self.computeSessionKey()

        encKey = self.RSAencrypt(self.sessionKey)
        encNonce = self.AESencrypt(nonce)

        return f"103 SessionKey {encKey} {encNonce}"

    def start(self):
        self.connect()
        print("Sending:", self.serverHello())
        self.send(self.serverHello())

        self.read()
        print("Received:", self.lastRcvdMsg)

        # Parse modulus, exponent, nonce
        parts = self.lastRcvdMsg.split(", ")
        self.modulus = int(parts[2])
        self.serverExponent = int(parts[3])
        nonce = int(parts[4])

        # Send session key message
        msg = self.sessionKeyMsg(nonce)
        print("Sending:", msg)
        self.send(msg)

        # Receive nonce verification
        self.read()
        print("Received:", self.lastRcvdMsg)

        if "400" in self.lastRcvdMsg:
            print("Server rejected nonce, closing.")
            self.close()
            return

        # Ask user for two integers
        a = int(input("Enter integer a: "))
        b = int(input("Enter integer b: "))

        a_enc = self.AESencrypt(a)
        b_enc = self.AESencrypt(b)

        sendInts = f"113 IntegersEncrypted {a_enc} {b_enc}"
        print("Sending:", sendInts)
        self.send(sendInts)

        # Receive encrypted composite
        self.read()
        print("Received:", self.lastRcvdMsg)

        parts = self.lastRcvdMsg.split()
        compositeEnc = int(parts[2])
        composite = self.AESdecrypt(compositeEnc)

        # Verify correctness
        if composite == a + b:
            print("Sending 200 OK")
            self.send("200 OK")
        else:
            print("Sending 400 Error")
            self.send("400 Error")

        self.close()


def main():
    """Driver function for the project"""
    args = sys.argv
    if len(args) != 3:
        print ("Please supply a server address and port.")
        sys.exit()
    print("Client of Cajaun")
    serverHost = str(args[1])       # The remote host
    serverPort = int(args[2])       # The same port as used by the server

    client = RSAClient(serverHost, serverPort)
    try:
        client.start()
    except (KeyboardInterrupt, SystemExit):
        exit()

if __name__ == "__main__":
    main()
