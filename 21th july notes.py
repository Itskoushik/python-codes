#swiggy app full backend -hw


#welcome note:
'''
view search by restaurants or veg or non veg.
have to store the count as well as food name , display them .

cart
buy a product from previous section then we can add that in cart , #inc qualtity 
if needed

'''
class Swiggy:
    compnm="Swiggy"
    @classmethod
    def restaurant(cls):
        ud={"plain dosa":10,"masala dosa":5,"panner tikka masala":3}
        mf={"chicken biriyani":4,"mutton biriyani":6,"chicken tikka biriyani":8,"panner tikka biriyani":4}
        dom={"corn-pizza":12,"chicken-sausage-pizza":2,"vedeshi panner pizza":6}
        bk={"crispy chicken burger":3,"veg makhani burger":5}
        kfc={"chiken strips bk":7,"chicken ultimate bk":9}
        restaurant={"udupi":ud,"meghana_food":mf,"dominos":dom,"burger_king":bk,"kfc":kfc}
        print("\n".join(restaurant.keys()))
    @classmethod
    def veg(cls):
        ud = {
            "plain dosa": 10,
            "masala dosa": 5,
            "paneer tikka masala": 3
        }
        mf = {
            "veg biriyani": 6,
            "mushroom biriyani": 4,
            "paneer tikka biriyani": 4
        }
        dom = {
            "corn pizza": 12,
            "margherita pizza": 8,
            "vedeshi paneer pizza": 6
        }
        bk = {
            "veg makhani burger": 5,
            "aloo tikki burger": 7
        }
        kfc = {
            "veg strips": 6,
            "veg zinger burger": 5
        }

        restaurant = {
            "udupi": ud,
            "meghana_food": mf,
            "dominos": dom,
            "burger_king": bk,
            "kfc": kfc
        }
        print("Veg Menu Available At:")
        print("\n".join(restaurant.keys()))
        cls.choice()

    @classmethod
    def non_veg(cls):
        ud = {
            "egg dosa": 4,
            "chicken curry dosa": 3
        }
        mf = {
            "chicken biriyani": 4,
            "mutton biriyani": 6,
            "chicken tikka biriyani": 8
        }
        dom = {
            "chicken sausage pizza": 2,
            "pepperoni pizza": 5
        }
        bk = {
            "crispy chicken burger": 3,
            "chicken whopper": 6
        }
        kfc = {
            "chicken strips": 7,
            "chicken ultimate burger": 9
        }

        restaurant = {
            "udupi": ud,
            "meghana_food": mf,
            "dominos": dom,
            "burger_king": bk,
            "kfc": kfc
        }
        print("Non-Veg Menu Available At:")
        print("\n".join(restaurant.keys()))
        
    section={"restaurant":restaurant,"veg":veg,"non_veg":non_veg}
    @classmethod
    def choice(cls):
        ch=input("enter the choice: ")
        if ch in ("udupi","1"):
            print(cls.restaurant())
        elif ch in ("meghana_food","2"):
            print(cls.veg())
        elif ch in ("nonveg","non_veg","non veg","3"):
            print(cls.non_veg())
        else:
            print("choose correct option: ",end="\n\n")
        
        
        
        
    @classmethod
    def display_home(cls):
        print("welcome to swiggy!!",end="\n\n")
        print("\n".join(cls.section.keys()),end="\n\n")
        print("pls select the one of filters from above: ",end="\n\n")
        ch=input("enter your choice : ")
        print()
        if ch in ("restaurant","1"):
            print(cls.restaurant())
        elif ch in ("veg","2"):
            print(cls.veg())
        elif ch in ("nonveg","non_veg","non veg","3"):
            print(cls.non_veg())
        else:
            print("choose correct option: ",end="\n\n")
            
            

    
    def __init__(self):
        pass
Swiggy.display_home()