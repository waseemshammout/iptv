import os
currentdirectory = os.path.dirname(os.path.abspath(__file__))

z = open('dump.m3u', 'a')
z.writelines('#EXTM3U\n')
z.close()

params = ['MBC 1','MBC 3','MBC 4', 'MBC 5', 'MBC Action','MBC Bollywood', 'MBC Drama', 'MBC Iraq'
        , 'MBC Masr', 'MBC Persia', 'MBC Plus Drama', 'MBC America', 'PMC', 'Syria', 'Jazeera']

channels = ()

def log_that_line(logWhat):
    with open(currentdirectory + '\\dump.m3u', 'a') as file1:
        file1.writelines(logWhat)

channel_directory = 'streams'
for y, filename in enumerate(os.listdir(channel_directory)):
    f = os.path.join(channel_directory, filename)
    with open(currentdirectory + '\\' + f, 'r') as source_file:
        for i, line in enumerate(source_file):
            # if i != 0:
            #     if line[0:14] == '#EXTINF:-1 tvg' or line[0:4] == 'http':
            #         # print(i, line.replace('\n',''))
            #         log_that_line(line)
            for text in params:
                if str(line).find(text,1, 1000) != -1:
                    print(line)
                    # channels   http://www.iptvchannels.somee.com/dump.m3u

    # print(filename + ' Finished---------------------------')
print('All channels are updated')
x = input('Press any key to continue')