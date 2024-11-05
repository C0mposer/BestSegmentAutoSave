import os
import time
from livesplit_wss import *

REPLAY_FOLDER = "D:/Recordings/"  # Adjust this to where OBS saves your recordings/replays
REPLAY_EXTENSION = ".mp4"  # Or whatever format your replays are saved in

def rename_replay():
    NEW_REPLAY_NAME = livesplit_data.last_split_name + " Gold " + time.strftime("%m-%d-%Y %H-%M-%S") + REPLAY_EXTENSION
    try:
        # Locate the latest saved replay file
        
        #List files ending with "REPLAY_EXTENSION" in replay dir
        files = [f for f in os.listdir(REPLAY_FOLDER) if f.endswith(REPLAY_EXTENSION)]
        if files:
            latest_file = max([os.path.join(REPLAY_FOLDER, f) for f in files], key=os.path.getctime) # Get latest file ending with "REPLAY_EXTENSION"
            print(f"Latest replay file: {latest_file}")

            # Rename the replay file
            new_file_path = os.path.join(REPLAY_FOLDER, NEW_REPLAY_NAME)
            os.rename(latest_file, new_file_path)
            print(f"Replay renamed to: {new_file_path}")
        else:
            print("No replay files found.")

    except Exception as e:
        print(f"Error: {e}")
