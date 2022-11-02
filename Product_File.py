# Class for generating and operations for specific product, flavor, component and insertion for the system test module

import pandas as pd                                                                                                                         #Importing pandas for matrix creation as dataframe
import numpy as np                                                                                                                          #Importing numpy for numerical operations

class Product_File :                                                                                                                        #Defining the class Product_File

    __speedEnable__ = False                                                                                                                 #SpeedEnable for possible data extraction of SPEED
    global dfColumns                                                                                                                        #Defining the dataframe columns as global variable
    dfColumns = ["Find", "Item Code", "Qty", "BOM Type", "Description", "Rev",                                                              #Defining column headers
                "Item Class", "Status", "Design Group", "Product", "Flavor"]

    
    def __init__(self,product, insertion, flavor, component):                                                                               #Init method definition, With product, insertion, flavor and component as inputs
        self.product = product                                                                                                              #Assigning product to object
        self.insertion = insertion                                                                                                          #Assigning insertion to object
        self.flavor = flavor                                                                                                                #Assigning flavor to object
        self.component = component                                                                                                          #Assigning component to object

    def GetPath(self) :
        BOMMainPath = r"\\CRATSHFS.intel.com\CRATAnalysis$\MAOATM\Engineering\CRAT PPV Engineering\Fungibility Matrix\BOM's"                #GetPath method to get the file path for any object
        Filename = self.product + "_" + self.flavor  + "_" + self.component + "_" + self.insertion + ".csv"
        Path = BOMMainPath + "\\" + str(self.product) + "\\" + Filename                                                                     #Concatenate all variable to a single path
        return Path

    def createVar(self) :
        return open(self.path, "w+")

    def create_DF(self) :                                                                                                                   #create_DF method to create dataframe for any csv file in the object path
        path = Product_File.GetPath(self)                                                                                                   #Getting path for given object
        if Product_File.__speedEnable__ == True :                                                                                           #Method for SPEED enablement
            # PLACEHOLDER
            #  Code if data is going to be extracted from SPEED
            pass
        else :                                                                                                                              #Create DF from a given CSV in a given path
            try :
                df = pd.read_csv(path,header = 0, delimiter= ',')                                                                           #Generate the DF from a CSV
            except FileNotFoundError:                                                                                                       #Exception handling in case file is not found 
                print(path)
                print("ERROR: Product file does not exist")
            else :                                                                                                                          #Method in case DF is generated correctly
                if 'Product' in df.columns :
                    pass
                else :
                    df['Product'] = self.product                                                                                            #Create Product column in DF in case in doesn't exist
                
                if 'Flavor' in df.columns :
                    pass
                else :
                    df['Flavor'] = self.flavor                                                                                              #Create Flavor column in DF in case in doesn't exist
                return df

    def append_File(self,originDF, DFToAppend) :                                                                                            #Method to concatenate generated dataframes
        try :
            df = pd.concat([originDF,DFToAppend], axis = 0)                                                                                 #Concatenate dataframes
            return df
        except ValueError:                                                                                                                  #Exception Handling in case dataframes don't exist
            print("ERROR: The Dataframes don't exist")
        

    def CreateFungTable(self, dataframe) :                                                                                                  #Method for creating Fungibility Matrix
        dfColumns = ["Find", "Item Code", "Qty", "BOM Type", "Description", "Rev",                                                          #Re-defining dataframe columns to be deleted
                "Item Class", "Status", "Design Group", "Product", "Flavor"]
        dfColumns.remove("Item Code")                                                                                                       #Remove Item Code from columns list                                                                                                      
        dfColumns.remove("Description")                                                                                                     #Remove Description from columns list
        dfColumns.remove("Product")                                                                                                         #Remove Product from columns list
        dfColumns.remove("Flavor")                                                                                                          #Remove Flavor from columns list
        try :
            dataframe.drop(dfColumns, axis = 1, inplace = True)                                                                             #Remove remaining values of list from dataframe
            dataframe = dataframe.pivot_table(index = ['Item Code','Description'], columns = ['Product','Flavor'],                          #Pivot dataframe over product flavor to have count of ocurrences
                                                                    aggfunc = len,
                                                                    fill_value = 0)                                                         #Fill value 0 so empty values equals 0      
            return dataframe
        except AttributeError:                                                                                                              #Exception handling in case dataframe is non-existent
            print("ERROR: Trying to operate on an inexistent dataframe")
                                                        
    def CreateCSV(self, DF) :                                                                                                               #Method to generate CSV out of a dataframe
        try :
            return DF.to_csv(r'C:\temp\Fungibility_Matrix.csv')                                                                             #Generate CSV in Temp folder in C drive
        except PermissionError:                                                                                                             #Exception handling in case the file is open
            print("ERROR: The fungibility file is not accesible")
            return "ERROR: File is open"
        except AttributeError :
            print("ERROR: Trying to operate on an inexistent dataframe")
            return "ERROR: Dataframe is inexistent"                                                                                         #Exception handling in case dataframe doesn't exist



#VALIDATION BLOCK
#################################################################################
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
###################################################################################
