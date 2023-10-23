## Circuit switching
- Switching technique that **establishes a dedicated path between sender and a receiver**.
- Once the connection is established, then the dedicated path will remain to exist until the connection is terminated.
- Operates in a similar way as the telephone works.
- A **complete end-to-end path must exist before the communication takes place**.
- Ex. Used in public networks, used for voice transmission.
	- Types - 1. Space division switches  2. Time division switches.
## Message switching
- **Message is transferred as a complete unit and routed through intermediate nodes** at which it is stored and forwarded.
- **No establishment of dedicated path** between the sender and receiver. Destination address is appended to the message.
- Provides **dynamic routing**, they are good at providing most efficient routes.

## Packet switching
- **Message is sent in one go, but it is divided into smaller chunks, and they are sent individually**.
- These smaller **chunks are called as "packets"**, and **packets are given unique numbers** to **identify their order at the receiving end**.
- Every packet contains some information in its headers such as **source address**, **destination address and sequence number**.
- Packets will travel across the network, taking the **shortest path** as possible.
- **If any packet is missing or corrupted, then the message will be sent to resend the message.**
- If the correct order of the packets is reached, then the acknowledgment message will be sent.

## Approaches of Packet switching
1. **Datagram packet switching**
	- packet is known as datagram, considered as an independent entity.
	- packets reassembled at the receiving end in correct order.
	- **Path is not fixed**.
	- Also known as **connectionless switching**.
  
2. **Virtual circuit switching**
	- Also known as **connection-oriented switching**.
	- Preplanned route is established before the message is sent.
	- Call request and call accept packets are used to establish the connection between sender and receiver.
	- In this case, the **path is fixed** for the duration of a logical connection