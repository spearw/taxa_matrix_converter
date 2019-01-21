from main import run
import glob
import os


path="input/"

for filename in os.listdir(path):

    if filename == ".DS_Store":
        pass

    else:

        print filename
        full_path = path + filename
        print filename 


        result = run(full_path)

        f= open("output/taxa.csv","a")

        f.write(result)
        f.close