# Socket Client Server Demo

A Python project exploring TCP socket communication between a client and server.

The project demonstrates how Python can create network sockets, establish connections, exchange messages, and use threads to handle communication.

## Features

* TCP socket communication
* Client/server architecture
* Multi-threaded communication
* Command-line arguments with `argparse`
* Message sending and receiving
* Python socket programming

## Requirements

* Python 3
* Windows, Linux, or macOS

No external Python packages are required.

## Run

Start the server:

```bash
python socket_demo.py --listen
```

In another terminal, connect to the server:

```bash
python socket_demo.py --connect 127.0.0.1
```

Type messages in the client terminal and the server will receive them and send a response.

Type:

```text
exit
```

to close the client connection.

## Project Structure

```text
socket-client-server-demo/
├── socket_demo.py
├── .gitignore
└── README.md
```

## Notes

This project is an educational demonstration of TCP socket programming and client/server communication.

It does not execute commands on the remote system or provide remote shell functionality.
