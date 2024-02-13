def calcola_media_per_quantita(quantita, probabilita):
    return (1/probabilita) * quantita

def calcola_deviazione_standard_per_quantita(quantita, probabilita):
    return (1/probabilita) * (1 - probabilita)**0.5 * quantita