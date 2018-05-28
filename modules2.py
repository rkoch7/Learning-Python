print('--------------- Running {} ---------------'.format(__name__))

def pprint_dict(header, d):
    print('\n\n-----------------------------------------')
    print('*********** {} ***********'.format(header))
    for key, value in d.items():
        print(key, value)
    print('-----------------------------------------\n\n')

pprint_dict('module2.globals', globals())

print('--------------- End of {} ---------------'.format(__name__))

