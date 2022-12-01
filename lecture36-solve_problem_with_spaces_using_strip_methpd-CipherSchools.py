name=" Tarun"
dots="........"
print(name +dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ",""))

# solving problem 

name,char=input("emter comma seperated name and charcter:").split(',')
print(f"lenth of nsme is{len(name)}")
print(f"character count: {name.strip().lower().count(char.strip().lower())}")


name.strip().lower().count(char.strip().lower())
char.strip().lower()
