# Appends all m3u files from streams directory to dump.m3u
import os
currentdirectory = os.path.dirname(os.path.abspath(__file__))

z = open('dump.m3u', 'a')
z.writelines('#EXTM3U\n')
z.close()

def log_that_line(logWhat):
    with open(currentdirectory + '\\dump.m3u', 'a') as file1:
        file1.writelines(logWhat)
channel_directory = 'streams'
for y, filename in enumerate(os.listdir(channel_directory)):
    f = os.path.join(channel_directory, filename)
    with open(currentdirectory + '\\' + f, 'r') as source_file:
        # print(filename + ' Started--------------------')
        for i, line in enumerate(source_file):
            if i != 0:
                if line[0:14] == '#EXTINF:-1 tvg' or line[0:4] == 'http':
                    # print(i, line.replace('\n',''))
                    log_that_line(line)
    print(filename + ' Finished---------------------------')
print('All channels are updated')
x = input('Press any key to continue')