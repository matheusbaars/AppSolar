from json import dumps
from sqlalchemy.orm import class_mapper

def costOfDisponibility(cost):
    if cost == 'Monophasic':
        return 30
    elif cost == 'Biphasic':
        return 50
    elif cost == 'Triphasic':
        return 100
    elif cost == 'None':
        return 0
    else:
        return 0

def monthlyEnergyConsumedLessCostDisponibility(energy, costOfDisponibility):
    return int(energy) - int(costOfDisponibility)

def number_of_modules(net_energy_per_day, modulePower):
    pass

def typeOfMounting(type):
    if type == 'standard rail system':
        return 29
    elif type == 'ballasted system':
        return 28
    elif type == 'non-penetrating system':
        return 32
    elif type == 'Elevated structure':
        return 22
    


