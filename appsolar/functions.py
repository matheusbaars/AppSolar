def costOfDisponibility(cost):
    if cost == 'Monophasic':
        return 30
    elif cost == 'Biphasic':
        return 50
    elif cost == 'Triphasic':
        return 100
    elif cost == 'None':
        return 0

def monthlyEnergyConsumedLessCostDisponibility(energy, costOfDisponibility):
    return int(energy) - int(costOfDisponibility)