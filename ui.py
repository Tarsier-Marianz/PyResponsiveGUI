from tkinter import *
from tkinter import ttk

class ProgressDialog:
    def __init__(self):
        self._root = Tk()  # set up the main window
        self._root.title("Py File Scanner")
        self._root.resizable(width=False, height=False)
        self.progress = IntVar()
        self.progress_max = IntVar()
        self.file_count = IntVar()
        self.dir_count = IntVar()
        self.progress_status = StringVar()
        self.lbl_status = StringVar()
        self.current_file = StringVar()

        self._mainframe = ttk.Frame(self._root, padding="3 3 12 12")
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._mainframe.columnconfigure(0, weight=1)
        self._mainframe.rowconfigure(0, weight=1)
        


        self.lbl_company_id = Label(self._mainframe, text="Current file:")
        self.lbl_company_id.grid(row=0, column=0, sticky='W', padx=5, pady=10)
        self.txt_company_id = Entry(self._mainframe, textvariable=self.current_file, width=60, state="readonly")
        self.txt_company_id.grid(row=0, column=1, columnspan=4 ,sticky="W", padx=4, pady=2)
        
        self.lbl_dispatcher_id = Label(self._mainframe, text="Scanned Files:")
        self.lbl_dispatcher_id.grid(row=1, column=0, sticky='W', padx=5, pady=2)
        self.txt_dispatcher_id = Entry(self._mainframe, textvariable=self.file_count, width=60, state="readonly")
        self.txt_dispatcher_id.grid(row=1, column=1,columnspan=4 , sticky="W", padx=4, pady=2)

        self.lbl_appt_status = Label(self._mainframe, text="Scanned Directories:")
        self.lbl_appt_status.grid(row=2, column=0, sticky='W', padx=5, pady=2)
        self.txt_appt_status = Entry(self._mainframe, textvariable=self.dir_count, width=60, state="readonly")
        self.txt_appt_status.grid(row=2, column=1, columnspan=4 ,sticky="W", padx=4, pady=2)

        self.lbl_progress = Label(self._mainframe, textvariable=self.progress_status)
        self.lbl_progress.grid(row=3, column=0, sticky='W', padx=5, pady=2)
        self.progress_status.set('Progress:')

        self.progressbar = ttk.Progressbar(self._mainframe, orient='horizontal',  variable=self.progress,length=300)
        self.progressbar.grid(row=3, column=1, columnspan=3 ,sticky="W", padx=4, pady=2)
        self.progressbar.start()

        self.btn_cancel = Button(self._mainframe, text="Cancel",  compound =LEFT, command= self.cancel)
        self.btn_cancel.grid(row=3, column=4, sticky="E", padx=4, pady=2)

        
        self.lbl_crawlStat = Label(self._mainframe, textvariable=self.lbl_status, fg = 'blue')
        self.lbl_crawlStat.grid(row=4, column=1, columnspan=3, sticky='W', padx=5, pady=2)
        self.lbl_status.set('A simple demo of responsive GUI...')

        self._root.bind("<Return>", self.ok)
        self._root.bind("<Escape>", self.cancel)

        self._mainframe.pack()

        # padding a little space so that all entries won't be scrunched
        #for child in self._mainframe.winfo_children():
        #    child.grid_configure(padx=2, pady=2)

    def ok(self):
        pass
    def cancel(self):
        pass
    
    def startGui(self):
        # This final line tells Tk to enter its event loop, which is needed to make everything run.
        self._root.mainloop()
   
    def setMaximum(self, maximum):
        self.progress_max.set(maximum)
        #self.progress_status.set('Progress: %s' % maximum)
        
    def updateDetails(self, file, file_count, dir_count, progress):
        self.current_file.set(file)
        self.file_count.set(file_count)
        self.dir_count.set(dir_count)
        self.progress.set(progress)
        pass

