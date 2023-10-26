exmp2 = 'Example2.txt'
exmp1 = 'Example1.txt'
# with open(exmp2, 'w') as writefile:
#     writefile.write("This is line C")

# with open(exmp2, 'r') as testwritefile:
#     print(testwritefile.read())

# with open(exmp2, 'w') as writefile:
#     with open(exmp1, 'r') as readfile:
#         for line in readfile:
#             writefile.write(line)


'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
'''
def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as currentMembers:
        with open(exMem, 'a+') as exMembers:
            members = currentMembers.readlines()
            inactive=[]
            header=members[0]
            members.pop(0)
            for member in members:
                if 'no' in member:
                    inactive.append(member)
            currentMembers.seek(0)
            currentMembers.write(header)
            for member in members:
                if (member in inactive):
                    exMembers.write(member)
                else: 
                    currentMembers.write(member)
            currentMembers.truncate()
# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
    