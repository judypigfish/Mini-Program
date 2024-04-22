from moviepy.editor import VideoFileClip
from PyQt5 import QtWidgets
import sys

class VideoToMp3:
    def __init__(self):
        super().__init__()
        self.filePath = []
        self.get_path()

    def get_path(self):
        if len(sys.argv) <= 1:
            self.filePath , _ = QtWidgets.QFileDialog.getOpenFileNames(caption='Open video file',
                                                                       filter='Video(*.mp4 *.mov *.mkv *.avi *.wmv *.flv)')
        else:
            for i in sys.argv[1:]:
                self.filePath.append(i.replace("\\",'/'))
            
        self.dir = QtWidgets.QFileDialog().getExistingDirectory(caption='Storage location')
        self.convert()
        
    def convert(self):
        for i in self.filePath:
            file = i.split('/')
            file = file[-1].split('.')
            
            try:
                video = VideoFileClip(i)
                video.audio.write_audiofile("{0}/{1}.mp3".format(self.dir, file[0]))
            except Exception as e:
                print(e)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    VideoToMp3()
    sys.exit()
