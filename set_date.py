#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time
import os

def getNTPTime(host = "pool.ntp.org"):
	success = False
	while not success:
		try: 
			port = 123
			buf = 1024
			address = (host,port)
			msg = '\x1b' + 47 * '\0'

			# reference time (in seconds since 1900-01-01 00:00:00)
			TIME1970 = 2208988800L # 1970-01-01 00:00:00

			# connect to server
			client = socket.socket( AF_INET, SOCK_DGRAM)
			client.sendto(msg, address)
			msg, address = client.recvfrom( buf )

			t = struct.unpack( "!12I", msg )[10]
			t -= TIME1970
			print("Success! Setting date...")
			return time.ctime(t).replace("  "," ")
		except:
			print("Unable to get date, trying again in 1 second")
			time.sleep(1)

if __name__ == "__main__":
        os.system('sudo date -s "' + getNTPTime() + '"')
