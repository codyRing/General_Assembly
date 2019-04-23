##List is a collection which is ordered and changeable. Allows duplicate members.
##Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
##Set is a collection which is unordered and unindexed. No duplicate members.
##Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

my_list = []
my_list.append(3)
my_list_2 = my_list
my_list_2.append(4)
my_list_3 = my_list_2
my_list.append(5)
print(my_list)
print(my_list_2)
print(my_list_3)


my_list = []
my_list_2 = []
my_list_3 = []
my_list = [1,6,2,70,4,1,3,4]
my_list_2 = sorted(my_list)
my_list.remove(my_list[4])
my_list_2.remove(my_list_2[4])
print(my_list)
print(my_list_2)




my_list = []
my_list_reversed = []
my_list = [1,6,2,70,4,1,3,4]
my_list.pop(7)
my_list_reversed = list(reversed(my_list))
my_list.reverse()
print(my_list)
print(my_list_reversed)



def myfunction(var1):
    var2 = var1 + 2
    return var2

five_var = myfunction(3)


	
def is_leap(n):
	leap = False
	if n % 4 == 0:
		if n % 100 == 0:
			if n % 400 == 0:
				return True
			return False
		return True
	else:
		return False

	return leap
	
	
def calc_default_add(x, y, op="add"):
	if op == ('add'):
		return x + y
	elif op == ('sub'):
		return x - y		
	else:
		print ("Valid operations: add, sub")
		
		
		

	
	
	
class Band(object):
    def __init__(self, band, members, albums, sold, genre):
        self.members = members
        self.band = band
        self.albums = albums
        self.sold = sold
        self.genre = genre

    def print_stats(self):
        return 'band: {} members: {} albums: {} sold: {} genre: {}'.format(self.band, self.members, self.albums, self.sold, self.genre)

Queen = Band('Queen',4,15,105000000,'Rock')
print(Queen.print_stats())



import numpy as np

import pandas as pd

df = pd.DataFrame(np.array([[.25,"w",60], [-.9,"x",20], [.2,"y",700], [.6,"z",350]]), columns=["A","B","C"])

print (df)

df["C"] = df.C.astype('float64')
df.C.mean()   # Return the mean of column C.
df.mean()   # Return the mean of all numeric columns.

import pandas

#load file1.csv as a DataFrame and print the result to screen
data = pandas.read_csv("file1.csv")
print("data:")
print(data)

#get overall sense of data by getting numeric summary info of numeric columns using .describe()
print(data.describe())
print()

#get distribution of non-numeric columns using .value_counts() on col2 and col3
print(data.col2.value_counts())
print()

print(data.col3.value_counts())
print()

#get the mean of col1 grouped by col2
print("col1 mean grouped by col2:")
print(data.groupby("col2")["col1"].mean())
print()
#get the mean of col1 grouped by col3
print("col1 mean grouped by col3:")
print(data.groupby("col3")["col1"].mean())
print()

#pivot data into a new table where col2 is the index, col3's values are the individual columns, and the average value in col1 is the value in each cell
pivoted_data = pandas.pivot_table(data,values="col1",index=["col2"],columns=["col3"],aggfunc="mean",fill_value=0)
print(pivoted_data)

import pandas as pd
data =[12, 17, 19, 22, 30, 65]
df = pd.DataFrame(data)
print(df.describe())

count  4.000000
mean   5.000000
std    2.581989
min    2.000000
25%    3.500000
50%    5.000000
75%    6.500000
max    8.000000




