lockdown = False 
grana = 30

status = 'Fique em casa' if lockdown or grana <= 100 else 'Pode sair'

print(f'Recomendação: {status}')