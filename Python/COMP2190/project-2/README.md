# COMP2190 Project 2

Project 2 combines RSA key exchange with simplified AES. The client sends an encrypted session key and nonce, then sends encrypted integers. The server decrypts the integers, computes their sum, and returns an encrypted result.

## Entry Points

| File | Role |
| --- | --- |
| `crypto_server.py` | Generates RSA keys and serves one client |
| `crypto_client.py` | Negotiates the session key and sends encrypted values |
| `NumTheory.py` | RSA number-theory helpers |
| `simplified_AES.py` | Symmetric encryption implementation |
| `*.asc` and `message.txt*` | Public-key, encrypted-message, and message artifacts |

## Run

Start the server in one terminal:

~~~bash
cd Python/COMP2190/project-2
python3 crypto_server.py 5001
~~~

Enter the required prime values when prompted. Start the client in another terminal:

~~~bash
cd Python/COMP2190/project-2
python3 crypto_client.py 127.0.0.1 5001
~~~

Use the same port in both commands. The protocol expects one client exchange per server run.
