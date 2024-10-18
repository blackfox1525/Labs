# TODO Найдите количество книг, которое можно разместить на дискете

V = 1.44 * 1024**2
kolich_str = 100
chislo_strok = 50
kolich_symb = 25

kolich_symb_v_knige = kolich_str * chislo_strok * kolich_symb

kolich_koda_v_knige = kolich_symb_v_knige * 4

itog = V // kolich_koda_v_knige

print("Количество книг, помещающихся на дискету:", int(itog))
