"""11-24: R'String Practice"""

# Use r'strings for Windows paths
win_path = r'C:\Files\Code\Practice\rstrings.txt'

with open (win_path, 'w') as fp:
    fp.write("Hello R'Strings")