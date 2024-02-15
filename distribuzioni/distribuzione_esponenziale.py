from scipy import stats

def calcolo_media(lambda_):
    return 1 / lambda_


def calcolo_media_campionaria(campione):
    return sum(campione) / len(campione)


def caclolo_media_normalizzata(lambda_, n):
    return calcolo_media(lambda_) * n


def calcolo_deviazione_standard(lambda_):
    return 1 / (lambda_ ** 0.5)


def calcolo_deviazione_standard_campionaria(campione):
    media = calcolo_media_campionaria(campione)
    return (sum([(x - media)**2 for x in campione]) / (len(campione) - 1))**0.5


def calcolo_deviazione_standard_normalizzata(lambda_, n):
    return calcolo_deviazione_standard(lambda_) * (n ** 0.5)


def intervallo_di_confidenza(mu, sigma, alpha):
    z = stats.norm.ppf(1 - alpha/2)
    errore_standard = z * sigma
    return mu - errore_standard, mu + errore_standard

