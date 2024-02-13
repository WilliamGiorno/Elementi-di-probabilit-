import  scipy.stats as stats

def calcola_media(campione):
    return sum(campione) / len(campione)


def normalizzazione_media(media, n):
    return media * n


def normalizzazione_deviazione_standard(dev_std, n):
    return dev_std * (n ** 0.5)


def somma_media(media_1, media_2):
    return media_1 + media_2


def calcola_deviazione_standard(campione):
    media = calcola_media(campione)
    return (sum([(x - media)**2 for x in campione]) / (len(campione) - 1))**0.5


def somma_deviazione_standard(dev_std_1, dev_std_2):
    return (dev_std_1**2 + dev_std_2**2)**0.5


def prob_inferiore_a_soglia(media_totale, dev_std_totale, soglia):
    """Calcola la probabilità che il peso totale sia inferiore a una certa soglia."""
    Z = (soglia - media_totale) / dev_std_totale
    probabilita = stats.norm.cdf(Z)
    return probabilita

def intervallo_di_confidenza(media, deviazione_standard, alpha):
    z = stats.norm.ppf(1 - alpha/2)
    errore_standard = z * deviazione_standard
    return media - errore_standard, media + errore_standard

# Varianza nota
def test_z(media_campionaria, media_popolazione, sigma_popolazione, n):
    numeratore = media_campionaria - media_popolazione
    denominatore = sigma_popolazione / (n ** 0.5)
    return numeratore / denominatore


# Varianza stimata del campione
def test_t(media_campionaria, media_popolazione, dev_std_campionaria, n):
    numeratore = media_campionaria - media_popolazione
    denominatore = dev_std_campionaria / (n ** 0.5)
    return numeratore / denominatore


def p_value_z(z_stat):
    return 1 - stats.norm.cdf(abs(z_stat))


def p_value_t(t_stat, df):
    return 1 - stats.t.cdf(abs(t_stat), df)


def discuti_risultati_test(p_value_Z, p_value_T, alpha=0.10):
    discussione = ""
    
    # Discussione per il Test Z
    if p_value_Z < alpha:
        discussione += f"Basandoci sul test Z (p-value = {p_value_Z:.4f}), rifiutiamo l'ipotesi nulla. Vi è evidenza statistica significativa al livello {alpha} che le vendite sono aumentate dopo la campagna pubblicitaria.\n"
    else:
        discussione += f"Basandoci sul test Z (p-value = {p_value_Z:.4f}), non rifiutiamo l'ipotesi nulla. Non vi è evidenza statistica sufficiente al livello {alpha} per affermare che le vendite sono aumentate dopo la campagna pubblicitaria.\n"
    
    # Discussione per il Test T
    if p_value_T < alpha:
        discussione += f"Basandoci sul test T (p-value = {p_value_T:.4f}), rifiutiamo l'ipotesi nulla. Vi è evidenza statistica significativa al livello {alpha} che le vendite sono aumentate dopo la campagna pubblicitaria, anche quando si considera la varianza stimata dal campione.\n"
    else:
        discussione += f"Basandoci sul test T (p-value = {p_value_T:.4f}), non rifiutiamo l'ipotesi nulla. Non vi è evidenza statistica sufficiente al livello {alpha} per affermare che le vendite sono aumentate dopo la campagna pubblicitaria quando si considera la varianza stimata dal campione.\n"
    
    return discussione