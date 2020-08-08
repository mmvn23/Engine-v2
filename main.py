import pandas as pd
import numpy as np

class partNumberClass: #corrigir class name

    def __init__(self,name,category= "", pricePAF = 0):
        self.partnumber = name
        self.category = category
        self.pricePAF = pricePAF # budget ao inves de PAF
        self.priceYTD = [0] * 12 # evitar hardcode numero magico, initial value e months in a year, nao repeat yourself
        self.priceYTG = [0] * 12 # dry coding
        self.volumePAF = [0] * 12
        self.volumeYTD = [0] * 12
        self.volumeYTG = [0] * 12
        self.yhold = ""

    def printPN(self): # montar uma __str__ ao inves de printar
        print("PN: {}".format(self.partnumber))
        print("Category: {}".format(self.category))
        print("pricePAF: {}".format(self.pricePAF))
        print("priceYTD: {}".format(self.priceYTD))
        print("priceYTG: {}".format(self.priceYTG))
        print("volumePAF: {}".format(self.volumePAF))
        print("volumeYTD: {}".format(self.volumeYTD))
        print("volumeYTG: {}".format(self.volumeYTG))    

savingsFile = pd.ExcelFile(r'.\inputs\Test.xlsx') #letra minuscila pra variavel
auxPAF = np.array(pd.read_excel(savingsFile,sheet_name="PAF")) #separate in two steps PAF sheet (evitar aux)
auxYTD = np.array(pd.read_excel(savingsFile,sheet_name="YTD"))
auxYTG = np.array(pd.read_excel(savingsFile,sheet_name="YTG"))

# auxPAF = np.array(pd.read_excel(r'.\inputs\Test.xlsx',sheet_name="PAF"))
# auxYTD = np.array(pd.read_excel(r'.\inputs\Test.xlsx',sheet_name="YTD"))
# auxYTG = np.array(pd.read_excel(r'.\inputs\Test.xlsx',sheet_name="YTG"))

PN_listaux = auxPAF[:,0] #evitar aux e decidir underline ou lower/uper case
Cat_listaux = auxPAF[:,1]
Pr_listaux = auxPAF[:,2]

x = [partNumberClass(PN_listaux[i],Cat_listaux[i],Pr_listaux[i]) for i in range (len(PN_listaux))]

for item in x:
    item.printPN()





