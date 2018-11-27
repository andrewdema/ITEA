DEN_KURSA = 19   # день месяца начала курса
MES_KURSA = 11   # месяц начала курса
GOD_KURSA = 2018 # год начала курса
MES_V_GODU = 12  # кол-во месяцев в году
DNEI_V_MES = 30  # кол-во дней в месяце

name_fam = input('Введите имя и фамилию: ')
print('Добрый день, ', name_fam)
data_r_d = int(input('Введите День даты рождения: '))
data_r_m = int(input('Введите Месяц рождения числом, например, январь - это 1: '))
data_r_g = int(input('Введите Год рождения: '))

# Например, вычислим разницу Дата Курса (19/11/2018) - Дата Рождения (17/01/1985) = 2 / 10 / 33:
raznica_god = GOD_KURSA - data_r_g # 33 года: 33 * 12 = 396 мес * 30 = 11880 дней
raznica_mes = MES_KURSA - data_r_m # +10 мес: 396 + 10 = 406 мес = 406 * 30 = 12180 дней
raznica_den = DEN_KURSA - data_r_d # +2 дня: 12180 + 2 = 12182 дня

# Вычислим количество лет, месяцев и дней до дня начала курса:
vsego_let = raznica_god
vsego_mes = raznica_god * MES_V_GODU + raznica_mes
vsego_dnei = vsego_mes * DNEI_V_MES + raznica_den

print('Кол-во прожитых лет до дня начала курса: ', vsego_let)
print('Кол-во прожитых месяцев до дня начала курса: ', vsego_mes)
print('Кол-во прожитых дней до дня начала курса: ',vsego_dnei)