# COMP2190 Project 1

Project 1 implements a client-server protocol with a Diffie-Hellman-style shared secret, public-key messages, and a transformed nonce challenge.

## Entry Points

| File | Role |
| --- | --- |
| `server.py` | Listens for one client and manages the handshake |
| `client.py` | Connects to the server and responds to the handshake |
| `numTheory.py` | Provides number-theory operations |

## Run

Start the server in one terminal:

~~~bash
cd Python/COMP2190/project-1
python3 server.py 5000
~~~

Start the client in another terminal:

~~~bash
cd Python/COMP2190/project-1
python3 client.py 127.0.0.1 5000
~~~

The server and client each prompt for a name. Use the same port in both commands and stop the server after the one-connection exchange completes.
