from obswebsocket import obsws, requests

# Configure OBS connection details
OBS_HOST = "localhost"   # OBS WebSocket server address
OBS_PORT = 4455          # Default port for OBS WebSocket
OBS_PASSWORD = "123456"  # Password for OBS WebSocket

def save_replay():
    try:
        # Connect to OBS WebSocket server
        ws = obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)
        ws.connect()
        print("Connected to OBS WebSocket server.")

        # Save the replay buffer
        ws.call(requests.SaveReplayBuffer())
        print("Replay buffer saved.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Disconnect from OBS
        ws.disconnect()
        print("Disconnected from OBS WebSocket server.")
