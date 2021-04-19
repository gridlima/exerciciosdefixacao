larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = larg * alt
print('Sua parede tema a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {} de tinta.'.format(tinta))
