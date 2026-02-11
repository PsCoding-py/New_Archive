class Person(object): 
    def __init__(self):
        self.annoyingness = int() 
        self.intelligence = "" 
        self.emmaness = float() 
        self.comments = "" 
        self.age = int()
emma = Person()
emma.annoyingness = 10000 
emma.intelligence = "comme ci comme ca" 
emma.emmaness = 100  
emma.comments = "One of the most irritating human beings in the world."  
emma.age = 12
lucas = Person() 
lucas.age = 12
lucas.intelligence = "smart" 
lucas.annoyingness = 800
lucas.emmaness =  10
lucas.comments = "Cool."

dad = Person() 
dad.intelligence = "very smart" 
dad.annoyingness = 1000 
dad.emmaness = 20 
dad.comments = "Smart (sometimes) likes annoying me, smart aleck."  
dad.age = 43
nana = Person()  
nana.age = 71
nana.annoyingness = 500 
nana.intelligence = "Not so good for academics or tech, but great at other things" 
nana.emmaness = 20 
nana.comments = "Nice, fun, funny. Not great at sport or excercise but great at art. Although her art room right now is quite messy.\nHer shepards pie is so good!. Her cakes are really nice but not as good as Aunty Nicole's." 
grandad = Person() 
grandad.age = 74 
grandad.annoyingness = 1 
grandad.emmaness = 30
grandad.intelligence = "really smart" 
grandad.comments = "Fun cracks good jokes. Loves fishing and bikes. His cooking is the best!" 
patrick = Person() 
patrick.annoyingness = 850
patrick.intelligence = "smart" 
patrick.emmaness =  30
patrick.comments = "Good at Minecraft and coding unlike me lol, also good at baking. by Lucas" 
patrick.age = 14
pop = Person() 
pop.age = 76 
pop.annoyingness = 0 
pop.intelligence = "really smart" 
pop.emmaness = 5 
pop.comments = "Legendary jokes. Loves board games, jokes, liquorice and general mathematics. \nHis Corned beef is so good i wish i could eat it by the bucketful."
database = {  

    "emma" : emma, 
    
    "dad" : dad, 
    
    "nana" : nana, 
    
    "grandad" : grandad,  

    "pop" : pop, 

    "lucas" : lucas
    
    } 
b=1 
a=1
def program(): 
    while True:
        person = input("Name: ") 
        if person.lower() == "exit": 
            break 
        else:
            person = database.get(person) 
            print("Human Statistics") 
            print("Age: ", person.age)
            print("Annoyingness Level: ", person.annoyingness) 
            print("Intelligence Level: ", person.intelligence) 
            print("Emmaness Level: ", person.emmaness)  
            print("Comments: ", person.comments) 
            x = input("Press [Enter] to continue . . .")
            print("\x1b[2J\033[H")
    
    
