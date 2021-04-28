from tkinter import *
from tkinter import messagebox
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Model functions
def CreateDataset(frame2,frame3, frame4,frame5):
    try:
        def testResult():
            i = 0
            resultList.insert(0,'Experience(years)        Result(by machine)         Result(original)')
            while i< len(X_test):
                resultList.insert(i+1,f'{X_test[i]}                        {Y_predict[i]}            {Y_test[i]}')
                i += 1

        def graphResult():
            plt.scatter(X_train,Y_train, color = 'red', label = 'training data')
            plt.plot(X_train, regressionObject.predict(X_train), color = 'blue', label = 'best fit')
            plt.scatter(X_test, Y_test, color = 'green', label = 'test data')
            plt.scatter(X_test,Y_predict, color= "black", label = 'predicted test data')
            plt.title("Salary vs Experience")
            plt.xlabel('years of experience')
            plt.ylabel('salary')
            plt.legend()
            plt.show()

        def show():
            try:
                def showsalgraph():
                    plt.scatter(experience, salaries,color = 'black')
                    plt.xlabel('Years of experiences')
                    plt.ylabel('Salaries')
                    plt.show()

                r = resultentry.get().split(',')
                ex = []
                exp = []
                for i in r:
                    i = float(i)
                    exp.append(i)
                    ex.append([i])
                experience = np.array(ex)
                salaries = regressionObject.predict(experience)
                # d = pd.DataFrame({'experience': exp, 'salaries': salaries})
                b['command'] = showsalgraph
                showlist.insert(0,'    experience      salary')
                for i in range(len(ex)):
                    showlist.insert(i+1,f'{i}     {exp[i]}       {salaries[i]}')
            except:
                showlist.insert(0,'Invalid Input')

        def clearl():
            showlist.delete(0,END)

        dataset = pd.read_csv(file)
        X = dataset.iloc[:,:-1].values   # taking all the values of all rows of first column
        Y = dataset.iloc[:,-1].values
        s = 0.15
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = s)
        regressionObject = LinearRegression()
        regressionObject.fit(X_train, Y_train)    # this function will create the regression line of best fit with x and y values

        Y_predict = regressionObject.predict(X_test)    # this will return the predict data
        Label(frame2, text = 'Model created and tested successfully',font = 'calibri 18 bold', bg= 'brown', fg = 'white',padx = 40).pack()
        
        r2 = r2_score(Y_test, Y_predict)                                              # showing accuracy in percentage
        result = "Our model is %2.2f%% accurate" %(r2*100)
        Label(frame2,text = result, font = 'calibri 16 bold', bg = 'sky blue',padx = 3, pady = 3,relief = SUNKEN).pack(side = LEFT,pady = 15, padx = 10)
        
        resultList = Listbox(frame3, bg = 'skyblue', relief = SUNKEN,width = 50, height = 8,font = 'calibri 13 bold')
        
        Button(frame2, text = 'CLICK to view tested result', font = 'calibri 13 bold' , bg = 'grey',command = testResult).pack(side = LEFT, pady = 15, padx = 45)
        resultList.pack(side = 'right')

        Button(frame3, text = "view result \n(Graph form)", font = 'calibri 13 bold', bg ='dark grey',command = graphResult).pack(side = RIGHT, padx = 35, pady = 30)

        # main prediction
        Label(frame4, text = 'Predict salary of different employees',font = 'calibri 18 bold', bg= 'brown', fg = 'white').pack( side = TOP,padx = 30,pady = 10)
        Label(frame4, text = 'Enter year of experiences(Separated by comma)',font = 'calibri 13 bold', bg= 'white', fg = 'blue').pack( side = LEFT,padx = 3)
        scvalue = StringVar()
        scvalue.set('')
        resultentry = Entry(frame4,textvariable = scvalue,relief = SUNKEN, bg = 'sky blue', font = 'calibri 15 bold',width= 28)
        resultentry.pack(side = LEFT,padx = 5)
        
        showlist = Listbox(frame5,bg = 'sky blue',width = 35, height = 8,relief = SUNKEN, font = 'calibri 13 bold')
        showlist.pack(side = RIGHT, padx = 10,pady = 10)
        b = Button(frame5, text = "show salary(in graph)", font = 'calibri 13 bold', bg ='dark grey')    
        
        Button(frame5, text = "show salary", font = 'calibri 13 bold', bg ='dark grey',command = show).pack(side = RIGHT,pady = 40,padx = 5)
        b.pack(side = RIGHT,pady = 40,padx = 5)
        Button(frame5, text = "clear", font = 'calibri 13 bold', bg ='dark grey',command = clearl).pack(side = RIGHT,pady = 40,padx = 5)
        b.pack(side = RIGHT,pady = 10,padx = 5)
    except:
        pass


def findCsv():
    csv_files = []
    cur_dir = os.getcwd()                   # returns the current working directory
    cur_list = os.listdir(cur_dir)          # returns the list of files 
    for x in cur_list:
        if x.split('.')[-1] == 'csv':
            csv_files.append(x)
    if len(csv_files) != 0:
        return csv_files


# creating new window and model analysing
def analysis(event):
    try:
        global root
        if file != 'k':
            root.destroy()
            top = Tk()
            top.geometry('690x565+400+100')
            top.minsize(690,565)
            top.maxsize(690,565)
            top.title('Model analysis')
            top.configure(background = 'aquamarine')
            frame2 = Frame(top, bg= 'aquamarine')
            frame3 = Frame(top, bg = 'aquamarine')
            frame4 = Frame(top, bg = 'aquamarine')
            frame5 = Frame(top, bg = 'aquamarine')
        
            CreateDataset(frame2,frame3, frame4,frame5)
            frame2.pack( fill = X, padx = 10,pady = 10)
            frame3.pack( fill = X,padx = 10)
            frame4.pack( fill = X,padx = 10)
            frame5.pack( fill = X,padx = 10)    
            top.mainloop()
            root = Tk()
            main(root)
    except:
        pass
    


# gui functions 
def setdimension():
    root.geometry('650x565+400+100')
    root.minsize(650,565)
    root.maxsize(650,565)
    root.title("Kishan's major project")
    root.config(background = 'grey')

# selecting csv (left side)
def selectCsv():
    def get(event):
        global file
        file = listbox.get(ACTIVE)
        messagebox.showinfo('CSV files',f'You have selected {file}')

    frame = Frame(root,bg = 'aquamarine2')
    csv_files = findCsv()

    Label(frame, text = 'Select your Csv file', fg = 'blue', font = 'calibri 16 bold').pack(padx = 20, pady =10)

    listbox = Listbox(frame, bg = 'sky blue', font = 'calibri 14 bold',height = 6)
    for i in range(len(csv_files)):
        listbox.insert(i,csv_files[i])
    listbox.pack(padx= 20)

    button = Button(frame, text = 'SELECT',bg = 'grey', font = 'calibri 15 bold')
    button.pack(pady = 10)
    button.bind('<Button-1>',get)
    frame.pack(side = 'left', padx = 25)
    

# Right side three button

def modelAnalysis(f):
    b3 = Button(f,text = 'Predict Salary\nModel Analysis(working)',font = 'calibri 18 bold',bg = 'light grey',padx = 4,pady = 4)
    b3.pack(padx = 20, pady = 15)
    b3.bind('<Button-1>', analysis)
    
    
def endapp():
    exit()


def end(f):
    b4 = Button(f,text = 'Exit',font = 'calibri 18 bold',bg = 'light grey',padx = 110,pady = 4, command = endapp)
    b4.pack(padx = 20, pady = 15)

# describing model 
def describe():
    f2 = Frame(root,bg = 'aquamarine2')
    Label(f2, text= 'DESCRIPTION', font = 'calibri 18 bold',bg = 'light grey').pack(fill = X)
    Label(f2, text= 'This is a Machine Learning project, which predict  Salaries of job applicants', fg = 'dark blue',bg = 'aquamarine2', font = 'calibri 14 bold').pack(fill = X)
    Label(f2, text= ' on the basis of their year of experiences', fg = 'dark blue', bg = 'aquamarine2', font = 'calibri 14 bold').pack(fill = X)
    Label(f2, text= 'This model will takes the previous records of the company and train itself', fg = 'dark blue', bg = 'aquamarine2', font = 'calibri 14 bold').pack(fill = X)
    Label(f2, text= 'This will automatically test itself and give you the accuracy of this model', fg = 'dark blue', bg = 'aquamarine2', font = 'calibri 14 bold').pack(fill = X)
    f2.pack(side = 'bottom',pady = 15,padx = 25,fill = X,anchor = 'se')


def main(root):
    try:
        setdimension() 
        Label(root,text='Salary Prediction System', bg = 'black',fg = 'white',pady = 5, font = 'calibri 24 bold').pack(fill = X,padx= 20, pady = 15)   
        f1 = Frame(root,bg = 'aquamarine2')
        modelAnalysis(f1)
        end(f1)
        describe()
        f1.pack(side = 'right', padx = 25)
        selectCsv()
        
        
        root.mainloop()
    except:
        pass

if __name__ == "__main__":
    file = 'k'
    root = Tk()
    main(root)
    
    