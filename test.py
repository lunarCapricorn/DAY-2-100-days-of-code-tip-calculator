cost = input('Cost? ')
peeps = input('Amount of people? ')
percent = input('Percentage? [5/15/20]')

print(f'{cost} * (1 + {percent}/100) / {peeps} = ', round(int(cost)*(1 + (int(percent)/100))/int(peeps), 2))