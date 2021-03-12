year_str = input('あなたの生まれ年を西暦４桁で入力してね: ')
year = int(year_str)
number_of_eto = (year + 8) % 12
eto_tuple = ('子',"牛","虎","卯","辰","巳","午","未","申","酉","戌","亥")
eto_name = eto_tuple[number_of_eto]
print(f'あなたの干支は{eto_name}だよ。')
