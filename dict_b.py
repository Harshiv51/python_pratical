Car_brands={'BMW': 'BMW M8',
            'MERCEDES-BENZ': 'S-class',
            'Audi':'RS-7',
            'Porsche':'911'
            }
# first dictionary of car brands
car_types={
    'gran_coupe':'BMW M8',
    'Sedan':'S-class',

}
# second dictionary of car types
Car_brands.update(car_types)#adding the car_types dictionary in Car brands dictionary
print(Car_brands)# finally printing it