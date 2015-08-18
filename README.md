# PyPeer - Best way to send files

A simple professional file transfer for sending files across lan. 

## what is PyPeer?

PyPeer is a personal project developed by [*Venkata Ramana*](https://venkata-ramana.github.io/) inspired by BitTorrentSync.

Installation
---------------
	git clone https://github.com/venkata-ramana/PyPeer.git

For File Sharing:
-----------
    python shareFiles.py

	-> click add files icon at top left most corner
	
	-> add files that you want
	
	-> share with connected peers
	
	
## How PyPeer works?
	
	-> I've implemented a concept called seeding & peering.
	
Peering
---------------
    -> which is a thread it checks for peers to connect

    -> whenever a peer is add get connected it updates peer count and as well as peer list.

Seeding
---------------
    -> Seeding is the technique when a file needed to download by multiple peers 
       then each reciever(download-peer) acts like a sender(upload-peer).





