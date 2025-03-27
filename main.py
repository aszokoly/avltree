from friendsbalt.acs import OrderedMap, StringDiff
from fsspec import filesystem
from datetime import datetime



class filesystem:
    def time(timestamp):
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        version = {diff1: 'version1', diff2: 'version2', diff3: "version3"}
        return timestamp
    

class VersionFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.versions = OrderedMap()
        file_string = self.read_from_file()
        initial_diff = StringDiff("", file_string)
        timestamp = int(round(curr_dt.timestamp()))
        curr_dt = datetime.now()
        self.versions[timestamp] = initial_diff
        return timestamp
    
    def save(self):
        previous_version = self.build_latest()
        current_version = self.read_from_file()

    def read_from_file(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        return (content)
    def build_latest(self):
        current = ""
        for _, diff in self.versions:
            StringDiff.apply_diff(current, diff)

        return current
        


 
        # 4. add the diff to version_map
   

x = VersionFile("example.txt")
print(x.read_from_file())