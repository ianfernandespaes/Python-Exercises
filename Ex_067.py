teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('=' * 30)
print(f'List of Brasileirão teams: {teams}')
print('=' * 30)
print(f'The first 5 are: {teams[0:5]}')
print('=' * 30)
print(f'The last 4 are: {teams[-4:]}')
print('=' * 30)
print(f'Teams in alphabetical order: {sorted(teams)}')
print('=' * 30)
print(f'Chapecoense is in the {teams.index("Chapecoense") + 1} position')
