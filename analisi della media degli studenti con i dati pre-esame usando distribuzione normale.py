# I voti degli scritti di questo insegnamento hanno di solito media 19.38 e deviazione standard 8.33. 
# I voti dello scorso scritto sono stati i seguenti: 2 3 10 11 18 18 19 19 25 26 27 20 20 20 20 22 24 28 28 30 30 33

import distribuzioni.distribuzione_normale as dn

# Si verifichi al 10% di significatività se vi sia evidenza statistica che la media dei voti sia cambiata.
# Si verifichi tramite calcolo del p-value se vi sia evidenza statistica che la deviazione standard dei voti sia cambiata.

# Dati pre-esami
media_pre_esami = 19.38
dev_std_pre_esami = 8.33

# Dati esami
voti = [2, 3, 10, 11, 18, 18, 19, 19, 25, 26, 27, 20, 20, 20, 20, 22, 24, 28, 28, 30, 30, 33]

media_esami = dn.calcola_media(voti)
dev_std_esami = dn.calcola_deviazione_standard(voti)

print(f"Media esami: {media_esami:.2f}")
print(f"Deviazione standard esami: {dev_std_esami:.2f}")

test_z = dn.test_z(media_esami, media_pre_esami, dev_std_pre_esami, len(voti))
test_t = dn.test_t(media_esami, media_pre_esami, dev_std_esami, len(voti))

p_value_z = dn.p_value_z(test_z)
p_value_t = dn.p_value_t(test_t, len(voti) - 1)

interpretazione = dn.discuti_risultati_test(test_z, test_t, p_value_z, p_value_t, alpha=0.10)
print(interpretazione)

# Quanto vale la potenza del test del primo punto, per una variazione della media dei voti di 17

potenza_test = dn.calcola_potenza_test(len(voti), 17, 0.10, dev_std_esami, test='z')
print(f"Potenza del test: {potenza_test:.4f}")
