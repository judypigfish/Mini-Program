import sys
import shutil
from PyQt5 import QtWidgets

class merge_files:
    def __init__(self):
        super().__init__()
        self.get_path()
        
    def get_path(self):
        self.file_path1, _ = QtWidgets.QFileDialog.getOpenFileName(caption='The first file')
        if self.file_path1 == "":
            sys.exit()
            
        self.file_path2, _ = QtWidgets.QFileDialog.getOpenFileName(caption='The second file')
        if self.file_path2 == "":
            sys.exit()
            
        self.out_path = QtWidgets.QFileDialog().getExistingDirectory(caption='Storage location')
        if self.out_path == "":
            sys.exit()
            
        print(""Please enter the output name：", end="")
        self.out_name = input()
        
        if self.out_name != "":
            self.merge()
            
    def merge(self):
        with open("{0}/{1}".format(self.out_path, self.out_name), 'wb') as out:
            with open(self.file_path1, 'rb') as f1:
                shutil.copyfileobj(f1, out)
            with open(self.file_path2, 'rb') as f2:
                shutil.copyfileobj(f2, out)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    merge_files()
    sys.exit()
