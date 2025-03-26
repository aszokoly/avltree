from friendsbalt.acs import OrderedMap, StringDiff
from fsspec import filesystem
from datetime import datetime
# make a version control system
#store the verison history
#do previous for multiple files
#restore any previous verison
#show  a log of any file
# figure out ordered map, figure out how to do this with one file, save a version, compute difference between versions and store that vallue in a map, value will be the string diff
# built in function on time class, how many seconds time stamp, order by time

x = OrderedMap()
a = "Hello\napple"
b = "Hello\napple!" #updated version

#Compute diff of a and b.
diff = StringDiff(a,b)

# Show changes
print(StringDiff.raw_diff(a,b))

# Construct b from a and the diff.
print(StringDiff.apply_diff(a, diff))

a = 'Hello\nWorld'
b = 'Hello\nWorld!'
c = "Hello\nWorld!!"
d = "Hello\nWorld!!!"
diff1= StringDiff(a,b)
diff2  = StringDiff(b, c)
diff3 = StringDiff(c,d)
print(StringDiff.raw_diff(a,b))

class filesystem:
    def time(timestamp):
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        version = {diff1: 'version1', diff2: 'version2', diff3: "version3"}
        return timestamp
    

class VersionFile(filepath, Version_map):
    def save():
        # 1. read the file from the disc (google - Mr.Hammer said we could search it up)
        diffs = []
        file = #something
        a = original.read()
        
        # 2. compute the latest version from the map
        b = current_version.read()
        # 3. compute the diff between 1 and 2
        diff1 = StringDiff(a,b)
        # 4. add the diff to version_map
        diffs.append(diff1)

    def build_latest():
        # starting from empty string, succesively apply diffs in version_map
        version_map = ''
        version



    def save(timestamp, versions, diff1, diff2, diff3):
        om = OrderedMap
        om.append(versions)
        while True:
            input("diff1")
            if input == 'save':
                om.append(diff1)
            elif input == 'restore':
                om.append(diff2)
            elif input 


