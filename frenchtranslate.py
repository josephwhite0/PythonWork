#Program Name: English to French Translator
#Author's Name: Joseph White
#Date: 6.18.2021
#Description of Program: This program has a list of english words and their french counterparts. You can enter an english word and if it is on the list it will display the 
#   french version of it. It as the capability to add words to the dictionary, update the .txt file that the initial data comes from, and show the entire dictionary list.


#importing wxPython
import wx
from wx.core import ID_ANY, LC_REPORT

#creating MyGUI class utilizing wx.Frame
class MyGUI(wx.Frame):
    
    #creating a global class list for the 2D english/french list
    x = []
    
    #constructing MyGUI
    def __init__(self):
        
        #pulling inheritance from wx.Frame
        super().__init__(parent = None, title = "French Translator",)
        
        #setting size of the frame, creating panel, and coloring background
        self.SetSize(600,600)
        self.panel1 = wx.Panel(self)
        self.panel1.SetSize(600,600)
        self.panel1.SetBackgroundColour(wx.Colour(50, 100, 0))
        
        #creating a window that shows the english and french words together
        self.list = wx.ListCtrl(self.panel1, id = ID_ANY, pos = wx.Point(200,0), size = (400,600))
        self.list2 = wx.ListView(parent = self.list, size = (400,540))
        self.list2.InsertColumn(0, "English", width = 200)
        self.list2.InsertColumn(1, "French", width = 200)
        self.index = 0
        
        #creating labels to give explaination on where to put words
        self.enterEng = wx.StaticText(self.panel1, id = ID_ANY, label = "Enter English word here:", pos = wx.Point(25, 25))
        self.enterFre = wx.StaticText(self.panel1, id = ID_ANY, label = "Enter French word here:", pos = wx.Point(25, 85))
        
        #creating text input fields
        self.engInput = wx.TextCtrl(self.panel1, id = ID_ANY, value = "", pos = wx.Point(25, 40))
        self.freInput = wx.TextCtrl(self.panel1, id = ID_ANY, value = "", pos = wx.Point(25, 100))
        
        #creating translate button
        self.enterButton = wx.Button(self.panel1, id = ID_ANY, label = "Translate!", pos = wx.Point(30, 150))
        self.enterButton.Bind(wx.EVT_BUTTON, self.translateToFrench)
        
        #creating menu using menu()
        self.menu()
        
        #filling list with list from file using readFile()
        self.x = readFile()
    
    #creating method to add buttons to drop down menu
    def menu(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        
        #creating menu buttons
        listDictionary = fileButton.Append(wx.ID_ANY, "List Dictionary")
        upDt = fileButton.Append(wx.ID_ANY, "Update")
        addW = fileButton.Append(wx.ID_ANY, "Add Word")
        exitItem = fileButton.Append(wx.ID_EXIT, "EXIT")
    
        #creating menu
        menuBar.Append(fileButton, "File")
        
        self.SetMenuBar(menuBar)
        
        #binding menu buttons to event
        self.Bind(wx.EVT_MENU, self.exit, exitItem)
        self.Bind(wx.EVT_MENU, self.displayAll, listDictionary)
        self.Bind(wx.EVT_MENU, self.addWord, addW)
        self.Bind(wx.EVT_MENU, self.update, upDt)
        self.Show(True)
        
    #closes program when EXIT is selected
    def exit(self, event):
        self.Close()
        
    #displays entire english/french list when List Dictionary is selected
    def displayAll(self, event):
        self.list2.DeleteAllItems()
        self.index = 0
        for word in self.x:
            y = word[0]
            words = y
            english = words[0]
            french = words[1]
            self.list2.InsertItem(self.index, english)
            self.list2.SetItem(self.index, 1, french)
            self.index += 1
            
    #displays french word for inputed english word when translate button is pushed
    def translateToFrench(self, event):
        self.list2.DeleteAllItems()
        english = self.engInput.GetValue()
        index = 0
        for word in self.x:
            y = word[0].upper()
            if english.upper() in y:
                frenchT = y[1]   
                self.list2.InsertItem(index, english)
                self.list2.SetItem(index, 1, frenchT)
    
    #add english and french equivalent to list            
    def addWord(self, event):
        english = self.engInput.GetValue()
        french = self.freInput.GetValue()
        if english.isalpha() and french.isalpha():
            self.x.append([[english,french]])
            
    #writes list to txt file
    def update(self, event):
        file = open("data\english_to_french.txt", "w")
        for word in self.x:
            y = word[0]
            english = y[0].strip()
            french = y[1].strip()
            file.write(english + "\t\t\t" + french + "\n")
    
#creates MainApp
class MainApp(wx.App):
    def OnInit(self):
        frame = MyGUI()
        frame.Show()
        return True

#strips string from txt file of formatting and creates 2D list        
def readFile():
    words = []
     
    file = open("data\english_to_french.txt", "r")
    rows,cols=(0, 1)
    for word in file:
        rows += 1
        wordData = word.split("\t")
        while("" in wordData):
            wordData.remove("")
            french = wordData[1]
            french = french[:-1]
            wordData[1] = french
        for i in range(rows):
            col=[]
            for j in range(cols):
                col.append(wordData)
        words.append(col)
    words.pop()
    file.close()
    return words
        
#runs main loop
def main():
    
    app = MainApp()
    app.MainLoop()
    
#runs main() 
main()