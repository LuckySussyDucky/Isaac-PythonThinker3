egg_code = ['1UK42211','2FR92921','1UK29292','0NL24555','0NL93933']
valid = 0

for i in range(len(egg_code)):
    check = 0
    if len(egg_code[i]) > 7:
        check += 1
    if egg_code[i][0] == "0" or egg_code[i][0] == "1" or egg_code[i][0] == "2" or egg_code[i][0] == "3":
        check += 1
    if egg_code[i][1:3].isalpha:
        check += 1
    if egg_code[i][3:8].isdigit:
        check += 1
    if check == 4:
        valid += 1
if valid == len(egg_code):
    print("Codes for the entire batch of eggs are valid.")
    # Collate the number of eggs sampled according to farm method
    farm_method_eggs = [0, 0, 0, 0]

    for j in range(len(egg_code)):
        farm_method_eggs[int(egg_code[j][0])] += 1

    farm_method = ['Organic','Free Range','Barn','Cage']

    for k in range(len(egg_code) - 1):
        print("Number of {0} eggs: {1}".format(farm_method[k - 1], farm_method_eggs[k - 1]))

    # Collate the number of eggs sampled according to country of origin
    countries = ['UK', 'FR', 'NL']
    countries_eggs = [0,0,0]
    for m in range(len(egg_code)):
        for n in range(len(countries)):
            if egg_code[m][1:3] == countries[n]:
                countries_eggs[n] += 1
    for p in range(len(countries_eggs)):
        print("Number of {0} eggs: {1}".format(countries[p], countries_eggs[p]))
else:
    print("Invalid egg codes found for this batch of eggs.")
    print("No data will be presented.")