import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
sep = "|"
index_col = "user_id"
users = pd.read_csv(url,sep, index_col ='user_id')

users.head(25)
users.tail(10)

chipo.shape[0] #number of records
chipo.shape[1] #number of columns
chipo.shape #number of rows and columns
chipo.columns #chipo.col
chipo.columns[104] # select * from chipo where col_index = 104
chipo.dtypes #data types
chipo['occupation'] #select occupation from user
chipo['occupation'].nunique() #select distinct occupation from user
chipo.occupation.value_counts().head() #select occupation,count(*) from chipo group by occupation
chipo.sort_values(by = "item_name") #select * from chipo sort by item_name

chipo.describe() #basic statistics for only numeric columns
chipo.describe(include = "all") #all Columns
chipo.occupation.describe() #Describe a selected columns
chipo.age.mean() #mean of a column


chipo.age.value_counts().tail()




url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
sep = "\t"
chipo = pd.read_csv(url,sep)

#Drop $ from item_price, not exactly sure how??
prices = [float(value[1 : -1]) for value in chipo.item_price] 

#Reassign cleaned values
chipo.item_price = prices

# delete the duplicates in item_name and quantity create new DF of 
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

chipo_one_prod[chipo_one_prod['item_price']>10].item_name.nunique()

#select count(*)
chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)