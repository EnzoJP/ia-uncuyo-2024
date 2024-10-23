
# TP7 - ID3 


```
    Atributo: outlook
  └── Valor: sunny
      Atributo: humidity
        └── Valor: high
              └── Clasificación: no
        └── Valor: normal
              └── Clasificación: yes
  └── Valor: rainy
      Atributo: windy
        └── Valor: true
              └── Clasificación: no
        └── Valor: false
              └── Clasificación: yes
  └── Valor: overcast
        └── Clasificación: yes
```

. Comentario: El arbol no llega a considerar temperatura :(

## estrategias de los árboles de decisión para datos de tipo real 

- Particionamiento en Rango (Intervalo)
Ya que no podemos particionar en un numero discreto de valores, se puede usar un rango (intervalo) de valores para cada atributo para crear nuevas ramas .

- Divisiones Basadas en Umbrales
Para cada atributo continuo, se puede calcular un umbral (o punto de corte) que divida los datos en dos grupos.

- Uso de Algoritmos de División Eficientes

CART (Classification and Regression Trees): Este algoritmo es ampliamente utilizado para árboles de decisión y maneja datos continuos muy bien. Utiliza divisiones binarias y busca el mejor punto de corte en cada paso.
ID3 y C4.5: Aunque ID3 es menos efectivo con datos continuos, C4.5 maneja mejor los datos reales al calcular puntos de corte óptimos.

- Binificación de Atributos Continuos

Definición: Consiste en dividir un atributo continuo en varias categorías (bins) antes de construir el árbol. Esto permite trabajar con datos continuos como si fueran discretos.
Ejemplo: Dividir el ingreso en categorías como "bajo", "medio" y "alto".
