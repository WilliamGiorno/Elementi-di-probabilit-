# Un allevatore ha una bufala che in 14 giorni consecutivi ha prodotto le
# quantità di latte seguenti (misurate in litri): 14.0 15.1 13.9 12.2 14.9 12.0 14.9 12.9 16.1 13.0 13.7 15.8 13.5 13.9 

import distribuzioni.distribuzione_normale as dn

# Si verifichi al 5% di significatività, se la bufala in questione abbia una produzione media giornaliera analoga a quella tipica, che è di 14.5 litri
campione = [14.0, 15.1, 13.9, 12.2, 14.9, 12.0, 14.9, 12.9, 16.1, 13.0, 13.7, 15.8, 13.5, 13.9]

mu_campionaria = dn.calcola_media(campione)
sigma_campionaria = dn.calcola_deviazione_standard(campione)
n = len(campione)
media_popolazione = 14.5
alpha = 0.10

print(f"mu_campionaria: {mu_campionaria}, sigma_campionaria: {sigma_campionaria}")

t_stat = dn.test_t(mu_campionaria, media_popolazione, sigma_campionaria, n)
p_value_T = dn.p_value_t(t_stat, n-1)

print(f"t_stat: {t_stat}, p_value: {p_value_T}")

print(dn.discuti_risultati_test(mu_campionaria, media_popolazione, None, p_value_T, alpha))

# Negli stessi 14 giorni una seconda bufala ha prodotto latte con media campionaria di 15.33 litri e deviazione standard campionaria di 1.45 litri. 
# Si verifichi tramite il p-value se sia plausibile che le due bufale abbiano la stessa produzione media.

mu_campionaria_2 = 15.33
sigma_campionaria_2 = 1.45

t_stat = dn.test_t(mu_campionaria, mu_campionaria_2, sigma_campionaria_2, n)
p_value_T = dn.p_value_t(t_stat, n-1)

print(f"t_stat: {t_stat}, p_value: {p_value_T}")
print(dn.discuti_risultati_test(mu_campionaria, mu_campionaria_2, None, p_value_T, alpha))

# Considerando ancora il test del punto precedente, si stimi grossolanamente per quanti giorni di produzione andrebbero raccolti i dati delle due bufale, 
# affinchè il test abbia una potenza del 50% a fronte di una differenza di produzione media tra i due animali del 10%

potenza_test = dn.calcola_potenza_test(6, sigma_campionaria_2**2, alpha, sigma_campionaria_2, test='t')
print(f"Potenza del test: {potenza_test:.4f}")