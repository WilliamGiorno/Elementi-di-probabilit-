
from scipy.stats import chi2
import math

def media_campionaria(campione):
    return sum(campione) / len(campione)


def deviazione_standard_campionaria(campione):
    media = media_campionaria(campione)
    return (sum([(x - media)**2 for x in campione]) / (len(campione) - 1))**0.5


def test_chi_quadrato(campione, sigma):
    n = len(campione)
    deviazione_standard = deviazione_standard_campionaria(campione)
    z = (n - 1) * (deviazione_standard / sigma)**2
    p_value = 1 - chi2.cdf(z, n - 1)
    return p_value


def limite_inferiore_S(alpha, n, sigma):
    df = n - 1
    chi2_critico = valore_critico_chi2(alpha, df)
    limite_inferiore = math.sqrt(chi2_critico / df) * sigma
    return limite_inferiore


def limite_superiore_S(alpha, n, sigma):
    df = n - 1
    chi2_critico = valore_critico_chi2(1 - alpha, df)
    limite_superiore = math.sqrt(chi2_critico / df) * sigma
    return limite_superiore


def limite_inferiore_e_superiore_bilaterale(alpha, n, sigma):
    df = n - 1
    chi2_critico_inferiore = valore_critico_chi2(alpha / 2, df)
    chi2_critico_superiore = valore_critico_chi2(1 - (alpha / 2), df)
    limite_inferiore = math.sqrt((df * sigma ** 2) / chi2_critico_superiore)
    limite_superiore = math.sqrt((df * sigma ** 2) / chi2_critico_inferiore)
    return limite_inferiore, limite_superiore


def valore_critico_chi2(alpha, df):
    chi2_critico = chi2.ppf(alpha, df)
    return chi2_critico


def calcola_chi_quadrato(campione, sigma):
    n = len(campione)
    deviazione_standard = deviazione_standard_campionaria(campione)
    z = (n - 1) * (deviazione_standard / sigma)**2
    return z


def potenza_test_chi_quadrato(campione, sigma):
    n = len(campione)
    deviazione_standard = deviazione_standard_campionaria(campione)
    z = (n - 1) * (deviazione_standard / sigma)**2
    potenza = 1 - chi2.cdf(z, n - 1)
    return potenza


def conferma_ipotesi(chi_quadrato, p_value, alpha, campione):
    # Confermare o rifiutare H0 basandosi sul p-value
    if p_value < alpha:
        result = f"Rifiutiamo H0: c'è evidenza statistica che la deviazione standard della popolazione è diversa da {alpha}."
        if chi_quadrato > chi2.ppf(1 - alpha/2, df=len(campione)-1):
            result += f" La deviazione standard della popolazione è probabilmente maggiore di {alpha}"
        else:
            result += f" La deviazione standard della popolazione è probabilmente minore di {alpha}"
    else:
        result = f"Non rifiutiamo H0: non c'è evidenza statistica sufficiente per affermare che la deviazione standard della popolazione sia diversa da {alpha}"
    
    return result
