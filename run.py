from main import run
import re
        
result = run("input/input.nex")

f= open("output/taxa.csv","w")

f.write(result)
f.close