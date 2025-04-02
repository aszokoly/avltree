from friendsbalt.acs import OrderedMap, StringDiff
from fsspec import filesystem
from datetime import datetime

#to test: create an infinite loop at bottom and use input command. print out a menu of things you cna do (current veriosn, previous version press2, save current version. then go into file and make a change. pushb 3 to end the loop and print out previous version)

class filesystem:
    def time(timestamp):
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        return timestamp
    

class VersionFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.versions = OrderedMap()
        file_string = self.read_from_file()
        initial_diff = StringDiff("", file_string)
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        self.versions[timestamp] = initial_diff
    
    def save(self):
        previous_version = self.build_latest()
        current_version = self.read_from_file()
        updated = StringDiff(previous_version, current_version)
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        self.versions[timestamp] = updated
        
    def read_from_file(self):
        with open(self.file_path, 'r') as file:
            content = file.read()  
        return (content)
    
    def build_latest(self):
        current = ""
        for _, diff in self.versions:
            current = StringDiff.apply_diff(current, diff)

        return current
        


 
        # 4. add the diff to version_map
   

x = VersionFile("example.txt")
print(x.read_from_file())