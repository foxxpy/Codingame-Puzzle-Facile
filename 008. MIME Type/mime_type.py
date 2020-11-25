import sys
import math

def find_last_occurence(fname, character_to_find):
    index=-1
    j=0
    
    #On parcourt le nom du fichier à l'envers pour récupérer la dernière occurence du point "."
    for character in fname[::-1]:
        if character == character_to_find:
            index = len(fname) - j - 1
            return index
        j = j + 1
    return -1
        
        

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
extensions_list = list()
MIME_list = list()

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    extensions_list.append(ext.lower())
    MIME_list.append(mt)


for i in range(q):
    fname = input()  # One file name per line.

    #On cherche où se trouve le point dans le nom du fichier
    index_point = find_last_occurence(fname, ".")
    
    #Si on a trouvé un point, on regarde si l'extension existe dans notre liste d'extension
    if index_point != -1:
        file_extension = fname[index_point+1:].lower()

        if file_extension in extensions_list:
            index_MIME = extensions_list.index(file_extension)
            print(MIME_list[index_MIME])
            
        else:
            print("UNKNOWN")
        
    else:
        print("UNKNOWN")

