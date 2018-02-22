from ui import ProgressDialog
from scanner import DirectoryScanner

# here is main function
if __name__ == '__main__':
    progressDialog = ProgressDialog()  # init GUI
    controller = DirectoryScanner(progressDialog) #init Controller

    controller.startCrawler()
    progressDialog.startGui()
