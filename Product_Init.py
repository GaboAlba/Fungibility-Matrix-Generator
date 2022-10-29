from Product_File import Product_File

class Product_Init :

    def __init__(self, prodList, flavList, comList, insList):
        self.prodList = prodList
        self.flavList = flavList
        self.comList = comList
        self.insList = insList
        self.ObjList = []
        self.Fung = Product_File("FUNG","FUNG","FUNG","FUNG")

    def __getitem__(self,key) :
        return self.ObjList[key]

    def __len__(self) :
        return len(self.ObjList)

    def CreateObjects(self) :
        self.ObjList = []
        def MultipleProductFlavor(product, flavor) :
            for component in self.comList:
                        for insertion in self.insList:
                            match product :
                                case "CLX" :
                                    match flavor[4:] :
                                        case "LCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CLX_LCC_MB_MAIN = Product_File("CLX","MAIN","LCC","MB")
                                                            self.ObjList.append(CLX_LCC_MB_MAIN)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CLX_LCC_AP_MAIN = Product_File("CLX","MAIN","LCC","AP")
                                                            self.ObjList.append(CLX_LCC_AP_MAIN)
                                        case "HCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CLX_HCC_MB_MAIN = Product_File("CLX","MAIN","HCC","MB")
                                                            self.ObjList.append(CLX_HCC_MB_MAIN)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CLX_HCC_AP_MAIN = Product_File("CLX","MAIN","HCC","AP")
                                                            self.ObjList.append(CLX_HCC_AP_MAIN)
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CLX_XCC_MB_MAIN = Product_File("CLX","MAIN","XCC","MB")
                                                            self.ObjList.append(CLX_XCC_MB_MAIN)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CLX_XCC_AP_MAIN = Product_File("CLX","MAIN","XCC","AP")
                                                            self.ObjList.append(CLX_XCC_AP_MAIN)
                                case "CPX" :
                                    match flavor[4:] :
                                        case "XCP" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CPX_XCP_MB_MAIN = Product_File("CPX","MAIN","XCP","MB")
                                                            self.ObjList.append(CPX_XCP_MB_MAIN)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            CPX_XCP_AP_MAIN = Product_File("CPX","MAIN","XCP","AP")
                                                            self.ObjList.append(CPX_XCP_AP_MAIN)
                                case "ICX" :  #Verify other flavors
                                    match flavor[4:] :
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            ICX_XCC_MB_MAIN = Product_File("ICX","MAIN","XCC","MB")
                                                            self.ObjList.append(ICX_XCC_MB_MAIN)
                                                        case "SDE" :
                                                            ICX_XCC_MB_SDE = Product_File("ICX","SDE","XCC","MB")
                                                            self.ObjList.append(ICX_XCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            ICX_XCC_AP_MAIN = Product_File("ICX","MAIN","XCC","AP")
                                                            self.ObjList.append(ICX_XCC_AP_MAIN)
                                                        case "SDE" :
                                                            ICX_XCC_AP_SDE = Product_File("ICX","SDE","XCC","AP")
                                                            self.ObjList.append(ICX_XCC_AP_SDE)
                                case "SPR" :
                                    match flavor[4:] :
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_XCC_MB_MAIN = Product_File("SPR","MAIN","XCC","MB")
                                                            self.ObjList.append(SPR_XCC_MB_MAIN)
                                                        case "CXL" :
                                                            SPR_XCC_MB_CXL = Product_File("SPR","CXL","XCC","MB")
                                                            self.ObjList.append(SPR_XCC_MB_CXL)
                                                        case "SDE" :
                                                            SPR_XCC_MB_SDE = Product_File("SPR","SDE","XCC","MB")
                                                            self.ObjList.append(SPR_XCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_XCC_AP_MAIN = Product_File("SPR","MAIN","XCC","AP")
                                                            self.ObjList.append(SPR_XCC_AP_MAIN)
                                                        case "CXL" :
                                                            SPR_XCC_AP_CXL = Product_File("SPR","CXL","XCC","AP")
                                                            self.ObjList.append(SPR_XCC_AP_CXL)
                                                        case "SDE" :
                                                            SPR_XCC_AP_SDE = Product_File("SPR","SDE","XCC","AP")
                                                            self.ObjList.append(SPR_XCC_AP_SDE)
                                        case "MCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_MCC_MB_MAIN = Product_File("SPR","MAIN","MCC","MB")
                                                            self.ObjList.append(SPR_MCC_MB_MAIN)
                                                        case "CXL" :
                                                            SPR_MCC_MB_CXL = Product_File("SPR","CXL","MCC","MB")
                                                            self.ObjList.append(SPR_MCC_MB_CXL)
                                                        case "SDE" :
                                                            SPR_MCC_MB_SDE = Product_File("SPR","SDE","MCC","MB")
                                                            self.ObjList.append(SPR_MCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_MCC_AP_MAIN = Product_File("SPR","MAIN","MCC","AP")
                                                            self.ObjList.append(SPR_MCC_AP_MAIN)
                                                        case "CXL" :
                                                            SPR_MCC_AP_CXL = Product_File("SPR","CXL","MCC","AP")
                                                            self.ObjList.append(SPR_MCC_AP_CXL)
                                                        case "SDE" :
                                                            SPR_MCC_AP_SDE = Product_File("SPR","SDE","MCC","AP")
                                                            self.ObjList.append(SPR_MCC_AP_SDE)
                                        case "112L" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_112L_MB_MAIN = Product_File("SPR","MAIN","112L","MB")
                                                            self.ObjList.append(SPR_112L_MB_MAIN)
                                                        case "CXL" :
                                                            SPR_112L_MB_CXL = Product_File("SPR","CXL","112L","MB")
                                                            self.ObjList.append(SPR_112L_MB_CXL)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_112L_AP_MAIN = Product_File("SPR","MAIN","112L","AP")
                                                            self.ObjList.append(SPR_112L_AP_MAIN)
                                                        case "CXL" :
                                                            SPR_112L_AP_CXL = Product_File("SPR","CXL","112L","AP")
                                                            self.ObjList.append(SPR_112L_AP_CXL)
                                        case "WMCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_WMCC_MB_MAIN = Product_File("SPR","MAIN","WMCC","MB")
                                                            self.ObjList.append(SPR_WMCC_MB_MAIN)
                                                        case "CXL" :
                                                            SPR_WMCC_MB_CXL = Product_File("SPR","CXL","WMCC","MB")
                                                            self.ObjList.append(SPR_WMCC_MB_CXL)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SPR_WMCC_AP_MAIN = Product_File("SPR","MAIN","WMCC","AP")
                                                            self.ObjList.append(SPR_WMCC_AP_MAIN)
                                                        case "CXL" :
                                                            SPR_WMCC_AP_CXL = Product_File("SPR","CXL","WMCC","AP")
                                                            self.ObjList.append(SPR_WMCC_AP_CXL)
                                case "EMR" : #Verify other flavors UCC y XCC
                                     match flavor[4:] :
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            EMR_XCC_MB_MAIN = Product_File("EMR","MAIN","XCC","MB")
                                                            self.ObjList.append(EMR_XCC_MB_MAIN)
                                                        case "SDE" :
                                                            EMR_XCC_MB_SDE = Product_File("EMR","SDE","XCC","MB")
                                                            self.ObjList.append(EMR_XCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            EMR_XCC_AP_MAIN = Product_File("EMR","MAIN","XCC","AP")
                                                            self.ObjList.append(EMR_XCC_AP_MAIN)
                                                        case "SDE" :
                                                            EMR_XCC_AP_SDE = Product_File("EMR","SDE","XCC","AP")
                                                            self.ObjList.append(EMR_XCC_AP_SDE)
                                        case "MCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            EMR_MCC_MB_MAIN = Product_File("EMR","MAIN","MCC","MB")
                                                            self.ObjList.append(EMR_MCC_MB_MAIN)
                                                        case "SDE" :
                                                            EMR_MCC_MB_SDE = Product_File("EMR","SDE","MCC","MB")
                                                            self.ObjList.append(EMR_MCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            EMR_MCC_AP_MAIN = Product_File("EMR","MAIN","MCC","AP")
                                                            self.ObjList.append(EMR_MCC_AP_MAIN)
                                                        case "SDE" :
                                                            EMR_MCC_AP_SDE = Product_File("EMR","SDE","MCC","AP")
                                                            self.ObjList.append(EMR_MCC_AP_SDE)
                                case "GNR" : #Verify other flavors UCC y XCC
                                    match flavor[4:] :
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            GNR_XCC_MB_MAIN = Product_File("GNR","MAIN","XCC","MB")
                                                            self.ObjList.append(GNR_XCC_MB_MAIN)
                                                        case "SDE" :
                                                            GNR_XCC_MB_SDE = Product_File("GNR","SDE","XCC","MB")
                                                            self.ObjList.append(GNR_XCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            GNR_XCC_AP_MAIN = Product_File("GNR","MAIN","XCC","AP")
                                                            self.ObjList.append(GNR_XCC_AP_MAIN)
                                                        case "SDE" :
                                                            GNR_XCC_AP_SDE = Product_File("GNR","SDE","XCC","AP")
                                                            self.ObjList.append(GNR_XCC_AP_SDE)
                                        case "UCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            GNR_UCC_MB_MAIN = Product_File("GNR","MAIN","UCC","MB")
                                                            self.ObjList.append(GNR_UCC_MB_MAIN)
                                                        case "SDE" :
                                                            GNR_UCC_MB_SDE = Product_File("GNR","SDE","UCC","MB")
                                                            self.ObjList.append(GNR_UCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            GNR_UCC_AP_MAIN = Product_File("GNR","MAIN","UCC","AP")
                                                            self.ObjList.append(GNR_UCC_AP_MAIN)
                                                        case "SDE" :
                                                            GNR_UCC_AP_SDE = Product_File("GNR","SDE","UCC","AP")
                                                            self.ObjList.append(GNR_UCC_AP_SDE)
                                        case "DE" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            GNR_DE_MB_MAIN = Product_File("GNR","MAIN","DE","MB")
                                                            self.ObjList.append(GNR_DE_MB_MAIN)
                                                        case "SDE" :
                                                            GNR_DE_MB_SDE = Product_File("GNR","SDE","DE","MB")
                                                            self.ObjList.append(GNR_DE_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            GNR_DE_AP_MAIN = Product_File("GNR","MAIN","DE","AP")
                                                            self.ObjList.append(GNR_DE_AP_MAIN)
                                                        case "SDE" :
                                                            GNR_DE_AP_SDE = Product_File("GNR","SDE","DE","AP")
                                                            self.ObjList.append(GNR_DE_AP_SDE)
                                case "SRF" : #Verify other flavors
                                    match flavor[4:] :
                                        case "LCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SRF_LCC_MB_MAIN = Product_File("SRF","MAIN","LCC","MB")
                                                            self.ObjList.append(SRF_LCC_MB_MAIN)
                                                        case "CXL" :
                                                            SRF_LCC_MB_CXL = Product_File("SRF","CXL","LCC","MB")
                                                            self.ObjList.append(SRF_LCC_MB_CXL)
                                                        case "SDE" :
                                                            SRF_LCC_MB_SDE = Product_File("SRF","SDE","LCC","MB")
                                                            self.ObjList.append(SRF_LCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            SRF_LCC_AP_MAIN = Product_File("SRF","MAIN","LCC","AP")
                                                            self.ObjList.append(SRF_LCC_AP_MAIN)
                                                        case "CXL" :
                                                            SRF_LCC_AP_CXL = Product_File("SRF","CXL","LCC","AP")
                                                            self.ObjList.append(SRF_LCC_AP_CXL)
                                                        case "SDE" :
                                                            SRF_LCC_AP_SDE = Product_File("SRF","SDE","LCC","AP")
                                                            self.ObjList.append(SRF_LCC_AP_SDE)
        def SingleProductFlavor(product, flavor) :
            for component in self.comList:
                #print(component)
                for insertion in self.insList:
                    #print(insertion)
                    match product :
                        case "CLX" :
                            match flavor :
                                case "LCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    CLX_LCC_MB_MAIN = Product_File("CLX","MAIN","LCC","MB")
                                                    self.ObjList.append(CLX_LCC_MB_MAIN)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    CLX_LCC_AP_MAIN = Product_File("CLX","MAIN","LCC","AP")
                                                    self.ObjList.append(CLX_LCC_AP_MAIN)
                                case "HCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    CLX_HCC_MB_MAIN = Product_File("CLX","MAIN","HCC","MB")
                                                    self.ObjList.append(CLX_HCC_MB_MAIN)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    CLX_HCC_AP_MAIN = Product_File("CLX","MAIN","HCC","AP")
                                                    self.ObjList.append(CLX_HCC_AP_MAIN)
                                case "XCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    CLX_XCC_MB_MAIN = Product_File("CLX","MAIN","XCC","MB")
                                                    self.ObjList.append(CLX_XCC_MB_MAIN)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    CLX_XCC_AP_MAIN = Product_File("CLX","MAIN","XCC","AP")
                                                    self.ObjList.append(CLX_XCC_AP_MAIN)
                        case "CPX" :
                            match flavor :
                                case "XCP" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    CPX_XCP_MB_MAIN = Product_File("CPX","MAIN","XCP","MB")
                                                    self.ObjList.append(CPX_XCP_MB_MAIN)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    CPX_XCP_AP_MAIN = Product_File("CPX","MAIN","XCP","AP")
                                                    self.ObjList.append(CPX_XCP_AP_MAIN)
                        case "ICX" :  #Verify other flavors
                            match flavor :
                                case "XCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    ICX_XCC_MB_MAIN = Product_File("ICX","MAIN","XCC","MB")
                                                    self.ObjList.append(ICX_XCC_MB_MAIN)
                                                case "SDE" :
                                                    ICX_XCC_MB_SDE = Product_File("ICX","SDE","XCC","MB")
                                                    self.ObjList.append(ICX_XCC_MB_SDE)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    ICX_XCC_AP_MAIN = Product_File("ICX","MAIN","XCC","AP")
                                                    self.ObjList.append(ICX_XCC_AP_MAIN)
                                                case "SDE" :
                                                    ICX_XCC_AP_SDE = Product_File("ICX","SDE","XCC","AP")
                                                    self.ObjList.append(ICX_XCC_AP_SDE)
                        case "SPR" :
                            match flavor :
                                case "XCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_XCC_MB_MAIN = Product_File("SPR","MAIN","XCC","MB")
                                                    self.ObjList.append(SPR_XCC_MB_MAIN)
                                                case "CXL" :
                                                    SPR_XCC_MB_CXL = Product_File("SPR","CXL","XCC","MB")
                                                    self.ObjList.append(SPR_XCC_MB_CXL)
                                                case "SDE" :
                                                    SPR_XCC_MB_SDE = Product_File("SPR","SDE","XCC","MB")
                                                    self.ObjList.append(SPR_XCC_MB_SDE)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_XCC_AP_MAIN = Product_File("SPR","MAIN","XCC","AP")
                                                    self.ObjList.append(SPR_XCC_AP_MAIN)
                                                case "CXL" :
                                                    SPR_XCC_AP_CXL = Product_File("SPR","CXL","XCC","AP")
                                                    self.ObjList.append(SPR_XCC_AP_CXL)
                                                case "SDE" :
                                                    SPR_XCC_AP_SDE = Product_File("SPR","SDE","XCC","AP")
                                                    self.ObjList.append(SPR_XCC_AP_SDE)
                                case "MCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_MCC_MB_MAIN = Product_File("SPR","MAIN","MCC","MB")
                                                    self.ObjList.append(SPR_MCC_MB_MAIN)
                                                case "CXL" :
                                                    SPR_MCC_MB_CXL = Product_File("SPR","CXL","MCC","MB")
                                                    self.ObjList.append(SPR_MCC_MB_CXL)
                                                case "SDE" :
                                                    SPR_MCC_MB_SDE = Product_File("SPR","SDE","MCC","MB")
                                                    self.ObjList.append(SPR_MCC_MB_SDE)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_MCC_AP_MAIN = Product_File("SPR","MAIN","MCC","AP")
                                                    self.ObjList.append(SPR_MCC_AP_MAIN)
                                                case "CXL" :
                                                    SPR_MCC_AP_CXL = Product_File("SPR","CXL","MCC","AP")
                                                    self.ObjList.append(SPR_MCC_AP_CXL)
                                                case "SDE" :
                                                    SPR_MCC_AP_SDE = Product_File("SPR","SDE","MCC","AP")
                                                    self.ObjList.append(SPR_MCC_AP_SDE)
                                case "112L" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_112L_MB_MAIN = Product_File("SPR","MAIN","112L","MB")
                                                    self.ObjList.append(SPR_112L_MB_MAIN)
                                                case "CXL" :
                                                    SPR_112L_MB_CXL = Product_File("SPR","CXL","112L","MB")
                                                    self.ObjList.append(SPR_112L_MB_CXL)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_112L_AP_MAIN = Product_File("SPR","MAIN","112L","AP")
                                                    self.ObjList.append(SPR_112L_AP_MAIN)
                                                case "CXL" :
                                                    SPR_112L_AP_CXL = Product_File("SPR","CXL","112L","AP")
                                                    self.ObjList.append(SPR_112L_AP_CXL)
                                case "WMCC" :
                                    match component :
                                        case  "MB" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_WMCC_MB_MAIN = Product_File("SPR","MAIN","WMCC","MB")
                                                    self.ObjList.append(SPR_WMCC_MB_MAIN)
                                                case "CXL" :
                                                    SPR_WMCC_MB_CXL = Product_File("SPR","CXL","WMCC","MB")
                                                    self.ObjList.append(SPR_WMCC_MB_CXL)
                                        case "AP" :
                                            match insertion :
                                                case "MAIN" :
                                                    SPR_WMCC_AP_MAIN = Product_File("SPR","MAIN","WMCC","AP")
                                                    self.ObjList.append(SPR_WMCC_AP_MAIN)
                                                case "CXL" :
                                                    SPR_WMCC_AP_CXL = Product_File("SPR","CXL","WMCC","AP")
                                                    self.ObjList.append(SPR_WMCC_AP_CXL)
                        case "EMR" : #Verify other flavors UCC y XCC
                                     match flavor :
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            EMR_XCC_MB_MAIN = Product_File("EMR","MAIN","XCC","MB")
                                                            self.ObjList.append(EMR_XCC_MB_MAIN)
                                                        case "SDE" :
                                                            EMR_XCC_MB_SDE = Product_File("EMR","SDE","XCC","MB")
                                                            self.ObjList.append(EMR_XCC_MB_SDE)
                                                case "AP" :
                                                    match insertion[4:] :
                                                        case "MAIN" :
                                                            EMR_XCC_AP_MAIN = Product_File("EMR","MAIN","XCC","AP")
                                                            self.ObjList.append(EMR_XCC_AP_MAIN)
                                                        case "SDE" :
                                                            EMR_XCC_AP_SDE = Product_File("EMR","SDE","XCC","AP")
                                                            self.ObjList.append(EMR_XCC_AP_SDE)
                                        case "MCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            EMR_MCC_MB_MAIN = Product_File("EMR","MAIN","MCC","MB")
                                                            self.ObjList.append(EMR_MCC_MB_MAIN)
                                                        case "SDE" :
                                                            EMR_MCC_MB_SDE = Product_File("EMR","SDE","MCC","MB")
                                                            self.ObjList.append(EMR_MCC_MB_SDE)
                                                case "AP" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            EMR_MCC_AP_MAIN = Product_File("EMR","MAIN","MCC","AP")
                                                            self.ObjList.append(EMR_MCC_AP_MAIN)
                                                        case "SDE" :
                                                            EMR_MCC_AP_SDE = Product_File("EMR","SDE","MCC","AP")
                                                            self.ObjList.append(EMR_MCC_AP_SDE)
                        case "GNR" : #Verify other flavors
                            match flavor :
                                        case "XCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            GNR_XCC_MB_MAIN = Product_File("GNR","MAIN","XCC","MB")
                                                            self.ObjList.append(GNR_XCC_MB_MAIN)
                                                        case "SDE" :
                                                            GNR_XCC_MB_SDE = Product_File("GNR","SDE","XCC","MB")
                                                            self.ObjList.append(GNR_XCC_MB_SDE)
                                                case "AP" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            GNR_XCC_AP_MAIN = Product_File("GNR","MAIN","XCC","AP")
                                                            self.ObjList.append(GNR_XCC_AP_MAIN)
                                                        case "SDE" :
                                                            GNR_XCC_AP_SDE = Product_File("GNR","SDE","XCC","AP")
                                                            self.ObjList.append(GNR_XCC_AP_SDE)
                                        case "UCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            GNR_UCC_MB_MAIN = Product_File("GNR","MAIN","UCC","MB")
                                                            self.ObjList.append(GNR_UCC_MB_MAIN)
                                                        case "SDE" :
                                                            GNR_UCC_MB_SDE = Product_File("GNR","SDE","UCC","MB")
                                                            self.ObjList.append(GNR_UCC_MB_SDE)
                                                case "AP" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            GNR_UCC_AP_MAIN = Product_File("GNR","MAIN","UCC","AP")
                                                            self.ObjList.append(GNR_UCC_AP_MAIN)
                                                        case "SDE" :
                                                            GNR_UCC_AP_SDE = Product_File("GNR","SDE","UCC","AP")
                                                            self.ObjList.append(GNR_UCC_AP_SDE)
                                        case "DE" :
                                            match component :
                                                case  "MB" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            GNR_DE_MB_MAIN = Product_File("GNR","MAIN","DE","MB")
                                                            self.ObjList.append(GNR_DE_MB_MAIN)
                                                        case "SDE" :
                                                            GNR_DE_MB_SDE = Product_File("GNR","SDE","DE","MB")
                                                            self.ObjList.append(GNR_DE_MB_SDE)
                                                case "AP" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            GNR_DE_AP_MAIN = Product_File("GNR","MAIN","DE","AP")
                                                            self.ObjList.append(GNR_DE_AP_MAIN)
                                                        case "SDE" :
                                                            GNR_DE_AP_SDE = Product_File("GNR","SDE","DE","AP")
                                                            self.ObjList.append(GNR_DE_AP_SDE)
                        case "SRF" : #Verify other flavors
                            match flavor :
                                        case "LCC" :
                                            match component :
                                                case  "MB" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            SRF_LCC_MB_MAIN = Product_File("SRF","MAIN","LCC","MB")
                                                            self.ObjList.append(SRF_LCC_MB_MAIN)
                                                        case "CXL" :
                                                            SRF_LCC_MB_CXL = Product_File("SRF","CXL","LCC","MB")
                                                            self.ObjList.append(SRF_LCC_MB_CXL)
                                                        case "SDE" :
                                                            SRF_LCC_MB_SDE = Product_File("SRF","SDE","LCC","MB")
                                                            self.ObjList.append(SRF_LCC_MB_SDE)
                                                case "AP" :
                                                    match insertion :
                                                        case "MAIN" :
                                                            SRF_LCC_AP_MAIN = Product_File("SRF","MAIN","LCC","AP")
                                                            self.ObjList.append(SRF_LCC_AP_MAIN)
                                                        case "CXL" :
                                                            SRF_LCC_AP_CXL = Product_File("SRF","CXL","LCC","AP")
                                                            self.ObjList.append(SRF_LCC_AP_CXL)
                                                        case "SDE" :
                                                            SRF_LCC_AP_SDE = Product_File("SRF","SDE","LCC","AP")
                                                            self.ObjList.append(SRF_LCC_AP_SDE)
        for product in self.prodList :
            #print(product)
            for flavor in self.flavList :
                #print(flavor)
                if len(flavor) > 4:
                    MultipleProductFlavor(product, flavor)
                else :
                    SingleProductFlavor(product, flavor)
        return self.ObjList

    def CreateDFs(self, counter = 1) :
        #print(self.ObjList)
        if len(self.ObjList) > 1 :
            Obj0 = self.ObjList[0]
            df0 = Obj0.create_DF()
            Obj1 = self.ObjList[counter]
            df1 = Obj1.create_DF()
            dfFung = self.Fung.append_File(df0,df1)
            while counter <= len(self.ObjList)-1 : 
                if counter > 0:
                    Obj1 = self.ObjList[counter]
                    df1 = Obj1.create_DF()
                    dfFung = self.Fung.append_File(dfFung,df1)
                else :
                    raise Exception ("Counter must equal equal or greater than 0")
                counter += 1
        elif len(self.ObjList) == 1 :
            Obj0 = self.ObjList[0]
            dfFung = Obj0.create_DF()
        else :
            dfFung = []
            print("Object List is empty")
        return dfFung

    def FungMatrix(self, DF) :
        DF = self.Fung.CreateFungTable(DF)
        for columns in DF.columns :
            x = ["X" if DF[columns].values[i] > 0 else "" for i in range(len(DF[columns].values))]
            DF[columns] = x
        return DF

    def to_CSV(self,DF):
        return self.Fung.CreateCSV(DF)
