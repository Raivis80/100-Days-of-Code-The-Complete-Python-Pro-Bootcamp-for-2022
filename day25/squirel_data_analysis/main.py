import pandas

# Get primary fur colour and count
data = pandas.read_csv('Squirrel_Data.csv')['Primary Fur Color']
gray = len(data[data == 'Gray'])
red = len(data[data == 'Cinnamon'])
black = len(data[data == 'Black'])

data_dict = {
    'fur color': ['gray', 'red', 'black'],
    'count': [gray, red, black]
}

print(data_dict)
data_done = pandas.DataFrame(data_dict)
data_done.to_csv('new_data.csv')