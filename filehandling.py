
#opening file in a read mode( using 'try' and 'finally' for exception handling)
# try:
#     file_obj = open('testfile.txt', 'r')

#     content = file_obj.read(6)



#     print(content)

#     content = file_obj.read()
#     print(content)

# finally:

#     file_obj.close()





# working with directories in python

import os 
print(f'current directory ={os.getcwd()}') #get current working directory

os.chdir('/home/anups/Helix_workspace') #change directory
print(f'current new directory ={os.getcwd()}') 

os.mkdir('Python_files') #create directory
os.rename('Python_files', 'Pytho') #Rename direcotry


print(f'New directory ={os.getcwd()}')

os.rmdir('pytho') #remove directory

print(os.listdir()) #list directory


#working with files in python
with open('testfile.txt', 'w') as f: #create file and write , if exists erase the contents and replace with new contents
    f.write('python is soooupop and crazyy ass bitch')

with open('testfile.txt', 'a') as f:
    f.write('\n python is soooupop and crazy ass bitch') # open file and append

with open('testfile.txt', 'r') as f: #read the existing file
    contet = f.read()
    print(contet)

