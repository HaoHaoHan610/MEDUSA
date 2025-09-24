import pandas as pd

a = [1,3,7]

myvar = pd.Series(a,index=["x","y","z"])

print(myvar)
# use key value like DIC array

calories = {"Day 1":420,"Day 2":120,"Day 3":320}

myvar = pd.Series(calories)

print(myvar)
