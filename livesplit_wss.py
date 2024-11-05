import socket
import json
import time

from livesplit_data import LivesplitData

livesplit_socket = None

livesplit_data = LivesplitData()

def connect_to_livesplit(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		print("Connected to LiveSplit server.")
		return s
	except ConnectionRefusedError:
		print("Failed to connect to LiveSplit server. Make sure you turn on the server in livesplit with:\nRight Click -> Control -> Start server ")
		return None
	except Exception as e:
		print(f"Error: {e}")
		return None

def request_livesplit_data():
    global livesplit_socket

    if not livesplit_socket:
        livesplit_socket = connect_to_livesplit("localhost", 16834)
    if livesplit_socket:
        # Send requests to livesplit websocket
        livesplit_data.is_connected = True
        best_possible_time = get_best_possible_time()
        current_time = get_current_time()
        split_index = get_split_index()
        if int(split_index) > 0:
            last_split_name = get_last_split_name()
        print() # \n
        # Set global livesplit data with data retrieved from requests
        livesplit_data.SetBestPossibleTime(best_possible_time)
        livesplit_data.SetCurrentTime(current_time)
        if int(split_index) > 0:
            livesplit_data.SetLastSplitName(last_split_name)

# Send command to LiveSplit server
def send_command(sock, command):
    global livesplit_socket
    sock.send((command + "\r\n").encode())
    response = sock.recv(1024).decode().strip()
    return response

# Commands
def get_best_possible_time():
    bpt = send_command(livesplit_socket, "getbestpossibletime")
    print("Best Possible Time: " + bpt)
    return bpt
def get_split_index():
    split_index = send_command(livesplit_socket, "getsplitindex")
    print("Current Split Index: " + split_index)
    return split_index
def get_last_split_name():
    last_split_name = send_command(livesplit_socket, "getprevioussplitname")
    print("Last Split Name: " + last_split_name)
    return last_split_name
    
def get_current_time():
    current_time = send_command(livesplit_socket, "getcurrenttime")
    print("Current Time: " + current_time)
    return current_time
    

