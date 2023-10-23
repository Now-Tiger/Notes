- Responsible for node to node delivery of the message/information.
- Main functionality of this layer is to make __error-free transmission of the data from one node to another__, over the physical layer.
- Working - Establishes and terminates a connection between two physically connected nodes on a network.
- The __Packet__ received from the __Network layer__ is further divided into __frames__ depending on the frame size of NIC(Network Interface Card)
- This layer is composed of two parts
	* __Logical Link Control__:
		Performs error checking and synchronizes of frames.
	* **Media Access Control**:
		Uses MAC address to connect devices and define permissions to transmit and receive data.
