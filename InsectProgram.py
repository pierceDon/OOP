import InsectClass as i

name = input('Enter insect name:' )

insect = i.Insect(2,4,name)

insect.calc_flight()


print(f'the {insect.get_name()} can fly up to {insect.get_flight()} miles')
