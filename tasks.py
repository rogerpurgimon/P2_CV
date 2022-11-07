import os

class Tasks:

    def parse_info(self):
        '''
        1) Create a python script able to parse the ‘ffmpeg
        –i BBB.mp4’ file, which can mark at least 3 relevant
        data from the container
        '''
        c1 = 'ffmpeg -i bbb.mp4 2> info.txt'
        os.system(c1)
        with open('info.txt', 'r') as f:
            for line in f.readlines():
                if "Duration" in line:
                    print(line)



    def new_container(self):
        '''
        2) You’re going to create a script in order to create
        a new BBB container:
            · Cut BBB into 1 minute only video.
            · Export BBB(1min) audio as MP3 stereo track.
            · Export BBB(1min) audio in AAC w/ lower bitrate
        Now package everything in a .mp4 with FFMPEG!
        '''
        c1 = 'ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:01:00 BBB.mp4'
        c2 = 'ffmpeg -i BBB.mp4 -ac 2 BBB.mp3'
        #convert an audio file to ACC in mp4 container
        c3 = 'ffmpeg -i BBB.mp4 -c:a libfdk_aac -b:a 60k BBB_newc.mp4'  ## -b:a (chosen bit rate)
        os.system(c1)
        os.system(c2)
        os.system(c3)

    def resize(self):
        '''
        3) Create a python script able to resize (resolution
        change) of any input given
        '''
        w = int(input("Entra l'amplada (width) de resolució: (ha de ser un enter) "))
        h = int(input("Entra l'amplada (height) de resolució: (ha de ser un enter): "))
        c = "ffmpeg -i BBB_newc.mp4 -vf scale={0}:{1} -c:a copy BBB_res.mp4".format(w,h)
        os.system(c)

    def checl_track(self):
        '''
        4) Create a python script which will check the
        audio tracks of the video. Then, with this
        information, it will explain in which broadcasting
        standard the video can fit. I.e.: one AC-3 audio, that
        means it can be ATSC.
        '''
        c1 = 'ffmpeg -i BBB_res.mp4 2> info.txt'
        os.system(c1)
        with open('info.txt', 'r') as f:
            for line in f.readlines():
                if ("Audio: ac3" or "Audio: ac3") in line:
                    print('DVB/ATSC/DTMB broadcast standard')

                if "Audio: aac" in line:
                    print('ISDB/DVB/DTMB broadcast standard')

                if "Audio: mp2"  in line:
                    print('DTMB broadcast standard')

                if "Audio: mp3"  in line:
                    print('DVB/DTMB broadcast standard')

                if "Audio: dra"  in line:
                    print('DTMB broadcast standard')
