#dictionary

dict = {
    "key" : "value",
    "name" : "Rakib ",
    "age" : 22,
    "city" : "Dhaka",
    "country" : "Bangladesh"
}

null_info = {}  
null_info["name"] = None
print(null_info)

dict["name"] = "Rakibul Islam"
dict["age"] = 23
print(dict)

#dictionary methods
#nested dictionary 

student = {
    "name" : "Rakibul Islam",
    "age" : 22,
    "city" : "Dhaka",
    "country" : "Bangladesh",
    "subject" : "CSE",
    "education" : {
        "school" : "Rajgonj High School",
        "college" : "BAF Shaheen College",
        "university" : "Northern University Bangladesh"
    }
}
student.update({"subject": "Computer Science and Engineering"})

print(student)
print(list(student.keys()))
print(len(student.keys()))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))


#set

collection = {1, 2, 3}
collection.add(4)
collection.remove(2)
collection.clear()

print(collection)
print(type(collection))
print(collection.pop())

empty_set = set()   
print(empty_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))
print(set1.intersection(set2))