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



