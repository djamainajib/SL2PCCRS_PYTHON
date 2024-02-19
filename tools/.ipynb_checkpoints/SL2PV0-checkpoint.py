import pickle


def s2_createFeatureCollection_domains():
    with open('nets/SL2PCCRS-DOMAIN.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_Network_Ind():
    with open('nets/Parameter_file_SL2PCCRS.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file
   
 # --------------------
 # SL2P for DBF: 
 # --------------------
def s2_createFeatureCollection_estimates():
    print('SL2PCCRS for DBF\nTo switch to SL2PCCRS for ENF use the appropriate function in tools\SL2PV0.py')
    with open('nets/SL2PCCRS-DBF.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_errors():
    with open('nets/SL2PCCRS-DBF-errors.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file


 # --------------------
 # SL2P for ENF: 
 # --------------------
# def s2_createFeatureCollection_estimates():
#     print('SL2PCCRS for ENF \nTo switch to SL2PCCRS for DBF use the appropriate function in tools\SL2PV0.py')
#     with open('nets/SL2PCCRS-ENF.pkl', "rb") as fp:   #Pickling
#         file = pickle.load(fp)
#     fp.close()    
#     return file

# def s2_createFeatureCollection_errors():
#     with open('nets/SL2PCCRS-ENF-errors.pkl', "rb") as fp:   #Pickling
#         file = pickle.load(fp)
#     fp.close()    
#     return file

 


 


