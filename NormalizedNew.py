import os
currentdirectory = os.path.dirname(os.path.abspath(__file__))


def log_that_line(logWhat):
    with open(currentdirectory + '\\output.csv', 'a') as file1:
        file1.writelines(logWhat)

# This function finds the last comma character index number within a text


def LastCommaPosition(text):
    CommaCount = text.count(',')
    RepNum = 0
    for i in range(CommaCount):
        RepNum = text.find(',', RepNum)
        RepNum += 1
    return RepNum - 1


x = 0
row_complete = True
channel_name = ''
channel_url = ''
channel_directory = 'streams'
for y, filename in enumerate(os.listdir(channel_directory)):
    f = os.path.join(channel_directory, filename)
    with open(currentdirectory + '\\' + f, 'r') as source_file:
        # print(filename + ' Started--------------------')
        for i, line in enumerate(source_file):
            if line.find('#EXTM3U') != -1 or line.find('#EXTVLCOPT') != -1:
                # print(i, ' is omitted', line)
                continue
            elif line.find('tvg-id') != -1 and row_complete == True:
                line = line[LastCommaPosition(line) + 1:]
                channel_name = line.replace('\n', '')
                # print(channel_name)
                row_complete = False
            else:
                channel_url = line.replace('\n', '')
                # print(channel_url)
                row_complete = True
                # insert_that_channel(channel_name, channel_url)
                log_that_line(channel_name + '; ' + channel_url + '\n')
                # print(channel_name, ';', channel_url)
    print(filename)
    x += 1
print(x, 'files completed')
rahaf = input('Press anykey to continue')