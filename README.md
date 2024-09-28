# Simple ARP Simulator

This project demonstrates a simple implementation of the Address Resolution Protocol (ARP) using a server-client architecture. The server handles ARP requests from clients, allowing them to resolve IP addresses to MAC addresses.

## Overview

The ARP protocol is used to map IP network addresses to the hardware (MAC) addresses used by a data link protocol. This implementation includes:
- A __server__ that listens for ARP requests and responds with the corresponding MAC address.
- A __client__ that sends ARP requests to the server to obtain the MAC address for a specified IP address.

## Requirements
- Python 3.x
- socket module (included with Python)
- Basic knowledge of networking concepts

## Installation
1. Clone this repository:
```
git clone https://github.com/chentzutung205/arp-simulator.git
cd arp-simulator
```
2. No additional dependencies are required, as this implementation relies on Python's built-in libraries.

## Usage
**Running the Server**
1. Open a terminal and navigate to the project directory.
2. Run the server script:
```
python server.py
```
**Running the Client**
1. Open another terminal window.
2. Run the client script:
```
python client.py
```

## How It Works
1. Server: The server listens for incoming ARP requests on a specified port. When a request is received, it checks its mapping of IP addresses to MAC addresses and sends the corresponding MAC address back to the client.
2. Client: The client sends an ARP request containing the target IP address. Upon receiving the response from the server, the client displays the resolved MAC address.
