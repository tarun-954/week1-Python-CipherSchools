# answers
name=input("please enter your name ")
# tarun 
# name.count("t") ,name.count(name[0])=2
# name.count("a") ,name.count(name[0])=1
# name.count("r") ,name.count(name[0])=1
# name.count("u") ,name.count(name[0])=2
# name.count("n") ,name.count(name[0])=1
temp_var=""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1