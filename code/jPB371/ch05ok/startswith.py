wd = 'Programming design'
print('字串:', wd)
print('Prog?', wd.startswith('Prog'))   #回傳True
print('gram?', wd.startswith('gram', 0))#回傳False
print('de?', wd.startswith('de', 12))  #回傳True
print('ign?', wd.endswith('ign'))  #回傳True
print('ing?', wd.endswith('ing', 0, 11))  #回傳True
