# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)
#%%
example1 = "example1.txt"
# file1 = open(example1, 'r')
# FileContent = file1.read()
# file1.close()

with open(example1, 'r') as file1:
    # FileContent = file1.read()
    
    # print(file1.read(4))
    # print(file1.read(2))
    # print(file1.read(3))
    
    # print("first line: " + file1.readline(30))
    # print("first line: " + file1.readline())
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i += 1
#%%