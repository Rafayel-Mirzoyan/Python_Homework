############ 1

def naughty_or_nice(data):
    import json
    with open(f"{data}", "r") as file:
        result = json.load(file)
    
    nice_count = 0
    naughty_count = 0
    for x, y in result.items():
        for i, j in y.items():
            if j == "Naughty":
                naughty_count += 1
            else:
                nice_count += 1
    print("Nice: ", nice_count)
    print("Naughty: ", naughty_count)
    if nice_count >= naughty_count:
        print("Nice")
        return "Nice"
    else:
        print("Naughty")
        return "Naughty"

naughty_or_nice("naughty_or_nice.json")



############ 2


# def find_seventh_sons_of_seventh_sons(jstring):
#     import json
#     sevent_sons_set = set()
#     count = 0
#     gs_count = 0
    
#     with open(f"{jstring}", "r") as file:
#         result = json.load(file)
    
#     if result["gender"] != "male":
#         print("Iis not man")
#         return False
#     elif result["children"] == []:
#         print("No any children")
#         return False
#     else:
#         if len(result["children"]) >= 7:
#             for i in result["children"]:
#                 if i["gender"] == "male":
#                     count += 1
#                 else:
#                     print("sequance of sons breaks")
#                     count = 0
#                     return False
#                 if count == 7:
#                     if i["children"] == []:
#                         print("seventh son has no any child")
#                         return False
#                     elif len(i["children"]) >= 7:
#                         for j in i["children"]:
#                             if j["gender"] == "male":
#                                 gs_count += 1
#                             else:
#                                 print("sequance of grandsons breaks")
#                                 gs_count = 0
#                                 return False
#                         if gs_count == 7:
#                             sevent_sons_set.add(j["name"])
#                             print("The sevent son of seventh son is: ", sevent_sons_set)
#                             return sevent_sons_set
#                     else:
#                         print("seventh son's children less than 7")
#                         return False
#         else:
#             print("less than 7 children")
#             return False
    
# find_seventh_sons_of_seventh_sons("contains_seventh_son_of_seventh_son.json")
# find_seventh_sons_of_seventh_sons("does_not_contain_seventh_son_of_seventh_son.json")
# find_seventh_sons_of_seventh_sons("does_not_contain_seventh_son_of_seventh_son_chain_broken.json")
# find_seventh_sons_of_seventh_sons("does_not_contain_seventh_son_of_seventh_son_no_children.json")