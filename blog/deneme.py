def a(t,z):
    z=str(z)
    if t=="p":
        a="listphone"
    if t=="c":
        a="listcomputer"
    if t=="e":
        a="listelectronic"


    
    exec(price=eval("%s[%s][Product_price]"%(a,z)))
    
    plist=str(price).split(".")
    try:
        plist[0]= plist[0][:-3]+"."+plist[0][-3:] 
    except:
        pass
    
    price=",".join(plist)+"TL"
    return price