#Reading files in python
country_file= open('countries.txt', 'r')
for lines in country_file.readlines():
  print(lines)
country_file.close()