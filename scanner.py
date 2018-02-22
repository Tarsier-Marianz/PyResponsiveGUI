import _thread
import time
import os

class DirectoryScanner:
    def __init__(self, progressGUI):
        self._progressGUI = progressGUI        
        self.file_count =0
        self.dir_count =0  
        self.progress =0    
    
    def startCrawler(self):
        try:
            _thread.start_new_thread(self.crawler, ())
        except:
            print("Error: unable to start thread")
            
    def scanned_dir(self, path):        
        try:
            if path.startswith("$")== False:
                list_files = os.listdir(path)
                self.setMaximum(len(list_files))
                self.progress = 0
                for file in list_files:
                    time.sleep(0.1)  # unit = second, delay time UNCOMMENT this line if you want to loop fast
                    filename = os.path.join(path, file)
                    if os.path.isfile(filename):
                        self.file_count+=1
                    if os.path.isdir(filename):
                        self.scanned_dir(filename)
                        self.dir_count+=1
                    self.progress +=1
                    self.updateGuiChange(file, self.file_count, self.dir_count, self.progress)
            else:
                pass
        except:
            pass
        
    def crawler(self):
        #path = "C:\\";
        path = os.path.abspath(os.sep) #make it dynamic
        self.scanned_dir(path)
        
        
    def setMaximum(self,progress):
        self._progressGUI.setMaximum(progress)
                                        
    def updateGuiChange(self,file, file_count, dir_count, progress):
        self._progressGUI.updateDetails(file, file_count, dir_count, progress)
