# strings
name="tarun"
# string indexing
print(name[1])
print(name[-1])
#  string slicing
print(name[0:])
print(name[:-2])
print(name[-1:0:-1])

#  take user input
age=int(input("enter your age:")) #strings
print(age)
# take two user input
user_name=input("enter your name and age:").split(",")
print(user_name)
# len function
print(len(name))
# lower , upper,title method
print(name.title())
# find.replace,center method
r_pos=name.find("r")
r_pos_2=name.find("r",r_pos+1)
print(r_pos_2)
# **tarun**
print(name.center(11,"*"))
print(name.replace("t","T"))