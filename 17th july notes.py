#create a class called suiiiiii with minimum 5 class properties,6 object properties, 3 objects,print the properties of all objects


class Rm:
    rm="realmadrid"
    lw="karim benzema"
    rw="zizou"
    fwd="david beckam"
    gk="Navas"
    def __init__(self,pos,name,st="Cristiano Ronaldo",cb="roberto carlos",lb="marcelo",rb="sergio ramos"):
        self.pos=name
        self.st=st
        self.cb=cb
        self.lb=lb
        self.rb=rb
p1=Rm("lw","vini jr")
p2=Rm("rw","rodrigo")
p3=Rm("mf","tony kroos")
print(p1.cb,p1.gk,p1.rb,p1.pos,p1.fwd,sep="\n")


        
        
    
    
    
    