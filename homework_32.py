################ 1

# def naughty_or_nice(data):
#     import json
#     with open(f"{data}", "r") as file:
#         result = json.load(file)
    
#     nice_count = 0
#     naughty_count = 0
#     for x, y in result.items():
#         for i, j in y.items():
#             if j == "Naughty":
#                 naughty_count += 1
#             else:
#                 nice_count += 1
#     print("Nice: ", nice_count)
#     print("Naughty: ", naughty_count)
#     if nice_count >= naughty_count:
#         print("Nice")
#         return "Nice!"
#     else:
#         print("Naughty")
#         return "Naughty!"

# naughty_or_nice("naughty_or_nice.json")


##################### 2

# def find_seventh_sons_of_seventh_sons(jstring):
#     import json  #remove this in the end
#     sevent_sons_set = set()
#     count = 0
#     gs_count = 0
#     result = json.loads(jstring)
#     with open(f"{jstring}", "r") as file:    #remove this in the end
#         result = json.load(file)             #remove this in the end
    
#     if result["gender"] != "male":
#         print("Is not man")#remove this in the end
#         return sevent_sons_set
#     elif result["children"] == []:
#         print("No any children")#remove this in the end
#         return sevent_sons_set
#     else:
#         if len(result["children"]) >= 7:
#             for i in result["children"]:
#                 if i["gender"] == "male":
#                     count += 1
#                 else:
#                     print("sequance of sons breaks")#remove this in the end
#                     count = 0
#                     return sevent_sons_set
#                 if count >= 7:
#                     if i["children"] == []:
#                         print("seventh son has no any child")#remove this in the end
#                         return sevent_sons_set
#                     elif len(i["children"]) >= 7:
#                         for j in i["children"]:
#                             if j["gender"] == "male":
#                                 gs_count += 1
#                             else:
#                                 print("sequance of grandsons breaks")#remove this in the end
#                                 gs_count = 0
#                                 return sevent_sons_set
#                         if gs_count >= 7:
#                             sevent_sons_set.add(j["name"])
#                             print("The sevent son of seventh son is: ", sevent_sons_set)#remove this in the end
#                         return sevent_sons_set
#                     else:
#                         print("seventh son's children less than 7")#remove this in the end
#                         return sevent_sons_set
#         else:
#             print("less than 7 children")#remove this in the end
#             return sevent_sons_set
    
# find_seventh_sons_of_seventh_sons("contains_seventh_son_of_seventh_son.json")
# find_seventh_sons_of_seventh_sons("does_not_contain_seventh_son_of_seventh_son.json")
# find_seventh_sons_of_seventh_sons("does_not_contain_seventh_son_of_seventh_son_chain_broken.json")
# find_seventh_sons_of_seventh_sons("does_not_contain_seventh_son_of_seventh_son_no_children.json")


