import streamlit as stl 
from Product_Init import Product_Init

def productParameters(product) :

    GeneralDict = {"CLX":{"Name":"CLX","Components":["MB","AP"],"Insertions":["MAIN"], "Flavors":["LCC","HCC","XCC"]},
                        "CPX":{"Name":"CPX","Components":["MB","AP"],"Insertions":["MAIN"], "Flavors":["XCP"]}, 
                        "ICX":{"Name":"ICX","Components":["MB","AP"],"Insertions":["MAIN","SDE"], "Flavors":["XCP"]},
                        "SPR":{"Name":"SPR","Components":["MB","AP"],"Insertions":["MAIN","CXL","SDE"], "Flavors":["XCC","MCC","112L","WMCC"]},
                        "EMR":{"Name":"EMR","Components":["MB","AP"],"Insertions":["MAIN","SDE"], "Flavors":["XCP"]},       #PENDING TO CONFIRM
                        "GNR":{"Name":"GNR","Components":["MB","AP"],"Insertions":["MAIN","SDE"], "Flavors":["XCP"]},       #PENDING TO CONFIRM
                        "SRF":{"Name":"SRF","Components":["MB","AP"],"Insertions":["MAIN","CXL","SDE"], "Flavors":["XCP"]}} #PENDING TO CONFIRM

    return GeneralDict[product]

stl.set_page_config(page_title = "PPV Collateral Fungibility Matrix Generator",
                    page_icon = "https://upload.wikimedia.org/wikipedia/commons/6/64/Intel-logo-2022.png", 
                    menu_items= {
                        'Get Help' : 'mailto:crat.sthi.eng@intel.com',
                        'Report a Bug' : 'mailto:gabriel.alba.romero@intel.com'
                    })
stl.image("https://upload.wikimedia.org/wikipedia/commons/6/64/Intel-logo-2022.png")
stl.title("PPV Collateral Fungibility Matrix Generator")


Continue = False        
__ProductList__ = ["CLX", "CPX", "ICX", "SPR", "EMR", "GNR" ,"SRF"]

productSelection = stl.multiselect('Please select one or more products', __ProductList__)
if len(productSelection) == 1 :
    flavorSelection = stl.multiselect('Please select one or more flavors', productParameters(productSelection[0])["Flavors"])
    componentSelection = stl.multiselect('Please select one or more components', productParameters(productSelection[0])["Components"])
    insertionSelection = stl.multiselect('Please select one or more insertions', productParameters(productSelection[0])["Insertions"])
    Continue = True #Defining to continue since product is populated
    ProdObj = Product_Init(productSelection, flavorSelection, componentSelection, insertionSelection)

elif len(productSelection) > 1 :
    flavorsList = []
    insertionsList = []
    for product in productSelection:
        for flavor in productParameters(product)["Flavors"] :
            flavorsList.append(product + "_" + flavor)
    for product in productSelection:
        for insertion in productParameters(product)["Insertions"] :
            insertionsList.append(product + "_" + insertion)
    flavorSelection = stl.multiselect('Please select one or more flavors', flavorsList)
    componentSelection = stl.multiselect('Please select one or more components', productParameters(productSelection[0])["Components"])
    insertionSelection = stl.multiselect('Please select one or more insertions', insertionsList)
    Continue = True #Defining to continue since product is populated
    ProdObj = Product_Init(productSelection, flavorSelection, componentSelection, insertionSelection)

else :
    Continue = False
    pass

if len(productSelection) >= 1 and len(flavorSelection) >= 1 and len(componentSelection) >= 1 and len(insertionSelection) >= 1:

    ObjectList = ProdObj.CreateObjects()
    #print(ObjectList)
    if len(ObjectList) > 0 :
        col1,col2,col3,col4 = stl.columns([1,1,1,1])
        df = ProdObj.CreateDFs(1)
        df = ProdObj.FungMatrix(df)
        stl.header("Fungibility Matrix")
        with col1 :
            add_CSV_button = stl.button("Generate CSV")
        if add_CSV_button :
            CSV = ProdObj.to_CSV(df)
            with col2:
                if CSV == "ERROR: File is open" :
                    stl.text("ERROR: File is open")
                elif CSV == "ERROR: Dataframe is inexistent":
                    stl.text("ERROR: Dataframe is inexistent")
                else :
                    stl.text("CSV Generated")
        else :
            pass
        stl.dataframe(df,800)
    else :
        print("Object List is empty")