import matplotlib.pyplot as plt

# Datos de ejemplo
# Reflexivo: 10 muestras de Batería Usada y Performance para dirt_rate=0.4 y size=8
battery_used_reflexivo = [491, 830, 1000, 477, 306, 356, 1000, 688, 434, 377]
performance_reflexivo = [26, 24, 23, 21, 26, 24, 26, 18, 28, 22]

# Aleatorio: 10 muestras de Batería Usada y Performance para dirt_rate=0.4 y size=8
battery_used_aleatorio = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
performance_aleatorio = [20, 19, 22, 18, 21, 22, 21, 16, 24, 18]

# Crear los gráficos de caja y bigotes para la batería usada y performance
plt.figure(figsize=(12, 6))

# Gráfico de Batería Usada
plt.subplot(1, 2, 1)
plt.boxplot([battery_used_reflexivo, battery_used_aleatorio], labels=['Reflexivo', 'Aleatorio'])
plt.title('Comparación de Batería Usada\n(Size=8, Dirt Rate=0.4)')
plt.ylabel('Batería Usada')

# Gráfico de Performance
plt.subplot(1, 2, 2)
plt.boxplot([performance_reflexivo, performance_aleatorio], labels=['Reflexivo', 'Aleatorio'])
plt.title('Comparación de Performance\n(Size=8, Dirt Rate=0.4)')
plt.ylabel('Performance')

# Mostrar los gráficos
plt.tight_layout()
plt.show()
