import scipy.stats as stats
import math

def media(n, p):
    return n*p


def deviazione_standard(n, p):
    return (n * p * (1 - p)) 


# Utilizzata soprattutto quando ci si interessa alla variabilità della proporzione di successi piuttosto che al conteggio totale dei successi. 
# Questo tipo di calcolo è tipico quando si lavora con proporzioni o percentuali in grandi campioni.
def deviazione_standard_dei_successi(n, p):
    return math.sqrt(p * (1 - p) / n)


def probabilita_piu_di_k_successi(k,n=0, p=0, mu=0, sigma=0):
    if mu == 0:
        mu = media(n, p)
    if sigma == 0:
        sigma = deviazione_standard(n, p)

    # Calcolo della z-score per k
    z = (k - mu) / sigma

    probabilita_comulativa = stats.norm.cdf(z)

    return 1 - probabilita_comulativa


def trova_k(mu, sigma, probabilita):
    z = stats.norm.ppf(1 - probabilita)
    return math.ceil(mu + z * sigma - 0.5) # 0.5 è la correzione di continuità


def calcola_z_massimo(alpha, n=0, p=0, mu=0, sigma=0):
    # Calcolo della media (mu) e della deviazione standard (sigma)
    if mu == 0:
        mu = media(n, p)
    if sigma == 0:
        sigma = deviazione_standard(n, p)

    # Trovare il valore z corrispondente al 90° percentile (1 - alpha)
    z = stats.norm.ppf(1 - alpha)
    
    # Calcolare il numero massimo di pezzi difettosi (x_max) usando l'approssimazione normale
    # e applicando la correzione di continuità
    x_max = z * sigma + mu - 0.5
    
    # Calcolare z come frazione del numero totale di pezzi
    z_massimo = x_max / n
    
    return z_massimo

def calcola_x_massimo(sigma, n, p, alpha=0.10):
    # Calcolo della media (mu)
    mu = n * p
    
    # Trovare il valore z corrispondente al 90° percentile (1 - alpha)
    z_0_90 = stats.norm.ppf(1 - alpha)
    
    # Calcolare il numero massimo di pezzi difettosi (x_max) usando sigma dato
    x_max = z_0_90 * sigma + mu - 0.5
    
    # Convertire x_max in percentuale rispetto al totale
    z_massimo_percentuale = (x_max / n) * 100
    
    return x_max, z_massimo_percentuale

def limite_superiore_confidenza(p, n, alpha):
    # Calcolo della deviazione standard della proporzione di successi
    sigma = deviazione_standard_dei_successi(n, p)
    z = stats.norm.ppf(1 - alpha)

    # Calcolo del limite superiore dell'intervallo di confidenza
    limite_superiore = z * sigma + p

    return limite_superiore