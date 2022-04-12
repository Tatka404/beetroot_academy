# 3
month = '-09-'
file = open('weather.log', 'r', encoding='utf-8')
lines = [line for line in file.readlines() if month in line]
file.close()
s = 0

for i in lines:
    temp_txt = i.split()[2]
    temp_int = int(temp_txt.replace('°C,', ''))
    s = s + temp_int
print(f'Number of lines: {len(lines)}. Average temperature: {round(s / len(lines), 2)}°C')



