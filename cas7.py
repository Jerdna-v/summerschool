import pandas as pd
#
# df = pd.read_csv('csv_primer.csv')
# # print(df)
#
#
# a = [1, 7, 2]
# myvar = pd.Series(a, index=["a", "b", "c"])
# print(myvar)
#
# calories = {"day1": 420,
# "day2": 380,
# "day3": 390}
# myvar = pd.Series(calories, index = ["day1","day2"])
# print(myvar)
#
# data = {
# "calories": [420, 380, 390],
# "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data)
# print(df.loc[1])
# from matplotlib import pyplot as plt
#
# data = {
# "calories": [420, 420, 390, 230, 430, 230, 213, 245, None, None, 234, 450, 245],
# "duration": [50, 50, 45, 40, 40, 40, 45, 45, 45, 50, 60, 40, 42]
# }
# df = pd.DataFrame(data)
# print(df)


# print(df.head())
# print(df.tail(3))

# print(df.info())

# df = df.sort_values(by=["calories"], ascending=False)
# print(df)

# new_df = df.dropna() # vrakja nov dataframe, bez None vrednosti, nema promeni vo momentalniot
#df.dropna(inplace=True) # ne ni vrakja nishto (vrakja None), go menuva momentalniot dataframe

# print(df)
# print(new_df)

# df["calories"].fillna(400, inplace=True)
# df.fillna(100, inplace=True)
#
# print(df)
#
# x = df["calories"].mean()
# print(x)
# df["calories"].fillna(x, inplace = True)
# print(df)

# for x in df.index:
#     if df.loc[x, "calories"] < 400:
#         df.drop(x, inplace=True)

# print(df)
#
# print(df.duplicated())
# df.drop_duplicates(inplace=True)
# print(df)
#
# print(df.groupby("calories")["duration"].sum())
# df_245_cal = df[df["calories"] == 245]
# print(df_245_cal)
#
# df.to_csv("df_to_csv.csv", index=True)
# df.to_csv("df_to_csv_2.csv", index=False)
#
# df.plot()
# plt.show()

dictionary = {
    "Name": ["John", "Emma", "Peter", "Lisa", "James", "Jessica"],
    "Age": [28, 24, 32, 35, 38, 23],
    "City": ["New York", "Seattle", "Chicago", "San Francisco", "New York", "Seattle"]
}

df = pd.DataFrame(dictionary)
df["Salary"] = [5000, 6000, 7000, 5500, 6500, 4900]
df.loc[df["Name"]=="Emma","Age"]=25
print(df)

# Da se ispechatat kolonite Name i City
print(df[["Name","City"]])
# Da se sortira spored Age
df.sort_values(by=["Age"], ascending=True, inplace=True)
print(df)


for name in df["Name"]:
    df.loc[df["Name"]==name,"Salary"]+=1000
print(df)

# da se prikazhat podatocite za lichnostite so nad 30 god
df_new = df[df["Age"] >=30]
print(df_new)
## da se najde prosechnata, maksimalnata i minimalnata plata
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())

# da se dodade nova kolona 'Position' so None vrednost vo sekoj red
df["Position"] = None

# poziciite koishto mozhe da gi ima eden vraboten se: CEO, Manager, Worker
# da se ovozmozhi korisnikot da vnese ime za CEO i Manager i soodvetno da se izvrshat ovie 2 promeni vo dataframe-ot
df.loc[df["Name"]==input("CEO Name: "),"Position"]="CEO"
df.loc[df["Name"]==input("Manager Name: "),"Position"]="Manager"

# na redovite so vrednost None za kolonata Position da se stavi vrednost 'Worker'
df["Position"].fillna("Worker", inplace = True)

print(df)

print(df.groupby("City")["Salary"].sum())