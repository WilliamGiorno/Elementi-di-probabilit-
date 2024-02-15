# Un centro commercial fatica a vendere un nuovo tipo di caffettiera elettrica: 
# fino ad ora le vendite settimanali hanno mostrato una media di 7.33 pezzi e una deviazione standard di 2.08 pezzi. 
# Viene tentata una campagna pubblicitaria più aggressiva, che nelle 8 settimane seguenti porta alle vendite seguenti:
# 7 7 16 8 10 9 11 14

import distribuzioni.distribuzione_normale as dn

# Questi dati dimostrano che le vendite sono cresciute? Rispondere al 10% di significatività, 
# sia nel caso in cui la varianza del le vendite sia rimasta invariata da prima della promozione
# sia nel caso in cui sia cambiata.

# Dati pre-campagna
media_pre = 7.33
dev_std_pre = 2.08
n_pre = 8  # Assumiamo che il numero di settimane pre-campagna sia uguale a quello post per semplicità

# Dati post-campagna
vendite_post = [7, 7, 16, 8, 10, 9, 11, 14]

# Calcolo delle statistiche del campione
media_post = dn.calcola_media(vendite_post)
dev_std_post = dn.calcola_deviazione_standard(vendite_post)

# Applicazione dei test
z_stat = dn.test_z(media_post, media_pre, dev_std_pre, len(vendite_post))
t_stat = dn.test_t(media_post, media_pre, dev_std_post, len(vendite_post))

# Calcolo dei p-values
p_value_Z = dn.p_value_z(z_stat)
p_value_T = dn.p_value_t(t_stat, len(vendite_post) - 1)

print(f"Statistica Z: {z_stat:.4f}, P-value (Varianza nota): {p_value_Z:.4f}")
print(f"Statistica T: {t_stat:.4f}, P-value (Varianza stimata): {p_value_T:.4f}")

interpretazione = dn.discuti_risultati_test(z_stat, t_stat, p_value_Z, p_value_T, alpha=0.10)
print(interpretazione)