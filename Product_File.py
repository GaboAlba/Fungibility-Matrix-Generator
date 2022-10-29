import pandas as pd
import numpy as np

class Product_File :

    __speedEnable__ = False
    global dfColumns
    dfColumns = ["Find", "Item Code", "Qty", "BOM Type", "Description", "Rev", 
                "Item Class", "Status", "Design Group", "Product", "Flavor"]

    
    def __init__(self,product, insertion, flavor, component):
        self.product = product
        self.insertion = insertion
        self.flavor = flavor
        self.component = component

    def GetPath(self) :
        BOMMainPath = r"\\CRATSHFS.intel.com\CRATAnalysis$\MAOATM\Engineering\CRAT PPV Engineering\Fungibility Matrix\BOM's"
        Filename = self.product + "_" + self.flavor  + "_" + self.component + "_" + self.insertion + ".csv"
        Path = BOMMainPath + "\\" + str(self.product) + "\\" + Filename
        return Path

    def createVar(self) :
        return open(self.path, "w+")

    def create_DF(self) :
        path = Product_File.GetPath(self)
        if Product_File.__speedEnable__ == True :
            # PLACEHOLDER
            #  Code if data is going to be extracted from SPEED
            pass
        else :
            try :
                df = pd.read_csv(path,header = 0, delimiter= ',')
            except FileNotFoundError:
                print(path)
                print("ERROR: Product file does not exist")
            else :
                if 'Product' in df.columns :
                    pass
                else :
                    df['Product'] = self.product
                
                if 'Flavor' in df.columns :
                    pass
                else :
                    df['Flavor'] = self.flavor
                return df

    def append_File(self,originDF, DFToAppend) :
        try :
            df = pd.concat([originDF,DFToAppend], axis = 0)
            return df
        except ValueError:
            print("ERROR: The Dataframes don't exist")
        

    def CreateFungTable(self, dataframe) :
        dfColumns = ["Find", "Item Code", "Qty", "BOM Type", "Description", "Rev", 
                "Item Class", "Status", "Design Group", "Product", "Flavor"]
        dfColumns.remove("Item Code")
        dfColumns.remove("Description")
        dfColumns.remove("Product")
        dfColumns.remove("Flavor")      
        try :
            dataframe.drop(dfColumns, axis = 1, inplace = True)  
            dataframe = dataframe.pivot_table(index = ['Item Code','Description'], columns = ['Product','Flavor'],
                                                                    aggfunc = len,
                                                                    fill_value = 0)     
            return dataframe
        except AttributeError:
            print("ERROR: Trying to operate on an inexistent dataframe")
                                                        
    def CreateCSV(self, DF) :
        try :
            return DF.to_csv(r'C:\temp\Fungibility_Matrix.csv')
        except PermissionError:
            print("ERROR: The fungibility file is not accesible")
            return "ERROR: File is open"
        except AttributeError :
            print("ERROR: Trying to operate on an inexistent dataframe")
            return "ERROR: Dataframe is inexistent"




# Main_112L = Product_File("SPR","MAIN","112L","MB")
# CXL_WMCC = Product_File("SPR","CXL","WMCC","MB")
# Fung = Product_File("FUNG","FUNG","FUNG","FUNG")
# dfMain = Main_112L.create_DF()
# #dfMain = Main_112L.CreateFungTable(dfMain)
# dfCXL = CXL_WMCC.create_DF()
# #dfCXL = CXL_112L.CreateFungTable(dfCXL)
# dfFung  = Fung.append_File(dfMain,dfCXL)
# dfFung = Fung.CreateFungTable(dfFung)
# Fung.CreateCSV(dfFung)
# print(dfFung)

