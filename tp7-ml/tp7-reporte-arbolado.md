
# Parte B

## Equipo formado por: Enzo Palau y Paula Martínez 

# Descripción del proceso de preprocesamiento

- Se eliminaron las columnas que no aportaban información relevante, en concreto última_modificación e id, pero esta ultima no tenía impacto en el modelo.

- La clase de inclinacion_peligrosa predominaba el 0 (sin inclinación peligrosa) por lo que se implementó un sistema de pesos (Cost-Sensitive Learning) observando la cantidad y proporción de los datos.

# Resultados obtenidos

- Algunas filas son:

id,inclinacion_peligrosa
1,0.18553537295162367
2,0.21489908402204913
4,0.11846518644706276
6,0.12428145316948067
9,0.42302011915120014
13,0.06190434127909057
14,0.15962411375513308
17,0.15078292552942463
23,0.04137173853462892
28,0.14182929009481096
30,0.13241132201958236


# Resultados en kaggle

- Se obtuvo un resultado en la parte pública de 0.78509.

# Descripción del modelo

- Se lee el archivo de entrenamiento y se elimina la columna de última_modificación.

- Se aplica Cost-Sensitive Learning para balancear las clases y se obtienen los pesos.

- Se utilizó un modelo de Random Forest con 300 árboles utilizando ranger para optimizar la ejecución del modelo en CPU y poder aplicar los pesos.

- Se entrena el modelo y se obtiene la predicción para el archivo de test.


