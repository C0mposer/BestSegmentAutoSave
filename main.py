import time
from livesplit_wss import *
from obs_wss import *
from rename_replay import *

while True:

    request_livesplit_data() # Request livesplit data every 1s

    if livesplit_data.is_connected:
        if livesplit_data.GetCurrentRunningTimeFloat() > 0: # If the timer is running
            if livesplit_data.previous_best_possible_time != None: # If has saved previous best possible time at least once
                print(f"Current BPT: {livesplit_data.GetCurrentBestPossibleTimeFloat()}\nPrevious BPT: {livesplit_data.GetPreviousBestPossibleTimeFloat()}\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                if livesplit_data.GetCurrentBestPossibleTimeFloat() < livesplit_data.GetPreviousBestPossibleTimeFloat():
                    save_replay()
                    
                    # Optional code to rename replay to segment name after it has saved (10s). Still needs work.
                    #time.sleep(10)
                    #rename_replay()
            
    # Set the previous best possible time to the current best possible time at the end of each check
    livesplit_data.SetPreviousBestPossibleTime(livesplit_data.current_best_possible_time)
    
    time.sleep(1)