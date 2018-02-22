from ui import ProgressDialog
from scanner import DirectoryScanner

if __name__ == '__main__':
    #initialize progress GUI
    progressDialog = ProgressDialog()
    #initialize directory scanner
    controller = DirectoryScanner(progressDialog)

    controller.startCrawler()
    progressDialog.startGui()
