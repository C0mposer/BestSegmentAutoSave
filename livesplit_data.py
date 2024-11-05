from time_helper import *

class LivesplitData:
    is_connected = None
    last_split_name = None
    current_best_possible_time = None
    previous_best_possible_time = None
    current_time = None
    
    # Setters
    def SetLastSplitName(self, lsn):
        self.last_split_name = lsn
        
    def SetCurrentTime(self, ct):
        self.current_time = ct
        
    def SetBestPossibleTime(self, bpt):
        self.current_best_possible_time = bpt
        
    def SetPreviousBestPossibleTime(self, bpt):
        self.previous_best_possible_time = bpt
        
    # Float Representation of times
    def GetCurrentBestPossibleTimeFloat(self):
        return time_string_to_seconds(self.current_best_possible_time)
    
    def GetPreviousBestPossibleTimeFloat(self):
        return time_string_to_seconds(self.previous_best_possible_time)
    
    def GetCurrentRunningTimeFloat(self):
        return time_string_to_seconds(self.current_time)
    