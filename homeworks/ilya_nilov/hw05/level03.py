def good_phone(phnnmbr): 
    if phnnmbr == None:
        return False 
    pref = "+375"
    if (len(phnnmbr) == 13) and (phnnmbr[1:].isdigit()):
        if phnnmbr.index(pref,0,4):
            return True        
    else:    
        return False
    

