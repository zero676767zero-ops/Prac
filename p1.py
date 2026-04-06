plays={
"Anthony and Cleopatra":"Anthony is there, Brutus is Caeser is with Cleopatra mercy worser.",
"Julius Ceaser":"Anthony is there, Brutus is Caeser is but Calpurnia is.",
"The Tempest":"mercy worser",
"Ham let":"Caeser and Brutus are present with mercy and worser",
"Othello":"Caeser is present with mercy and worser",
"Macbeth":"Anthony is there, Caeser, mercy."
}
words=["Anthony","Brutus","Caeser","Calpurnia","Cleopatra","mercy","worser"]

list1 = [[0 for _ in range(len(words))]for _ in range(len(plays))]
print(list1)

def prepare_matrix(list1, plays, words):
    for i in range(len(words)):
        for key in plays.keys():
            if words[i] in plays[key]:
                key_list = list(plays.keys())
                list1[key_list.index(key)][i] = 1
prepare_matrix(list1, plays, words)
for row in list1:
    print(row)

def findAnd(list1, variable1, variable2):
    idx_variable1 = words.index(variable1)
    idx_variable2 = words.index(variable2)
    for i in range(len(plays)):
        if list1[i][idx_variable1] and list1[i][idx_variable2]:
            return list1[i]

def findOr(list1, variable1, variable2):
    idx_variable1 = words.index(variable1)
    idx_variable2 = words.index(variable2)
    for i in range(len(plays)):
        if list1[i][idx_variable1] or list1[i][idx_variable2]:
            return list1[i]

key_list = list(plays.keys())
print("Anthony and Calpurnia is together in play: ", key_list[list1.index(findAnd(list1, "Anthony", "Calpurnia"))], findAnd(list1, "Anthony", "Calpurnia"))
print("Anthony and Calpurnia is in or condition: ", key_list[list1.index(findOr(list1, "Anthony", "Calpurnia"))], findOr(list1, "Anthony", "Calpurnia"))

# Second Code : 
plays={
    "Antony and Cleopatra, Act III, Scene ii":"When Antony found Julius Caesar dead,He cried almost to roaring; and he wept When at Philippi he found Brutus slain.", 
    "Julius Ceaser":"I did enact Julius Caesar: I was killed i' the Capitol; Brutus killed me."
    } 
words=["Antony","Brutus","Caesar","Calpurnia","Cleopatra","mercy","worser","Philippi"] 

list2 = [[0 for _ in range(len(words))]for _ in range(len(plays))]
print(list2)

def prepare_matrix2(list1, plays, words):
    for i in range(len(words)):
        for key in plays.keys():
            if words[i] in plays[key]:
                key_list = list(plays.keys())
                list2[key_list.index(key)][i] = 1

prepare_matrix2(list2, plays, words)
for i in list2:
    print(i)

def findAnd2(list2, a, b, c):
    idx_1=words.index(a)
    idx_2=words.index(b) 
    idx_3=words.index(c) 
    for i in range(len(plays)): 
        if list2[i][idx_1] and list2[i][idx_2] and not list2[i][idx_3]: 
            return list2[i] 

key_list = list(plays.keys()) 

# def findor(l, a, b, c): 
#     idx_1=words.index(a) 
#     idx_2=words.index(b) 
#     for i in range(len(plays)): 
#         if l[i][idx_1] or l[i][idx_2]: 
#             return l[i] 


print("Brutus AND Caesar AND NOT Calpurnia:",key_list[list2.index(findAnd2(list2,"Brutus","Caesar","Calpurnia"))],findAnd2(list2,"Brutus","Caesar","Calpurnia")) 
# print("Brutus OR Caesar OR NOT Calpurnia:",key_list[list2.index(findand(listt,"Brutus","Caesar","Calpurnia"))],findand(l istt,"Brutus","Caesar","Calpurnia")) 

