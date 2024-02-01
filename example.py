from dekimashita import Dekimashita

text = 'Moon Beautiful Isn"t It'

clear = Dekimashita.vdir(text)

print('without Dekimashita filter: '+ text)
print('with Dekimashita filter: ' + clear)