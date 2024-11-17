agencies = {
    'CCC' : 'Civilian Conservation Corps',
    'FCC' : 'Fderal Communications Commision',
    'FDIC' : 'Federal Deposit Insurance Corporation',
    'SSB' : 'Social Security Board',
    'WPA' : 'Works Progress Administration'
}

# part a
agencies.update({'SEC' : 'Securities and Exchange Comission'})

# part b
agencies.update({'SSB' : 'Social Security Administration'})

# part c
agencies.pop('CCC')
agencies.pop('WPA')