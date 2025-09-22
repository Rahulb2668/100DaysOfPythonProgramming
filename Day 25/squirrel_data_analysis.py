import pandas

data = pandas.read_csv("squirrel_data.csv")

squirrel_colors = data["Primary Fur Color"].unique()
# print(squirrel_colors)
squirrel_count =[]
for color in squirrel_colors:
    squirrel_count.append(data[data["Primary Fur Color"] == color].shape[0])

data_to_dict = {
    "Fur Color" : squirrel_colors,
    "Squirrel Count" : squirrel_count
}


df = pandas.DataFrame(data_to_dict)

print(df.to_csv("squirrel_count.csv"))




