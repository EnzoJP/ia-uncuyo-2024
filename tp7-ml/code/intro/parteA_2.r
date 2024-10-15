
#------------------------------------#
# distribucion de la clase inclinacion peligrosa

library(ggplot2)
library(dplyr)

data <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-train.csv")

# Convertir a factor para visualizar mejor (para que se vea solo 0 e 1)
data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)

# Gráfico de barras 
ggplot(data, aes(x = inclinacion_peligrosa)) +
  geom_bar(fill = "steelblue") +
  labs(title = "Distribución de Inclinación Peligrosa", x = "Inclinación Peligrosa", y = "Cantidad") +
  theme_light()

ggsave("tp7-ml/images/class_dist_peligrosa.png",width = 10, height = 10, units = "cm")

#------------------------------------#
# cantidad de arboles peligrosos por seccion

seccion_peligrosa <- data %>%
  group_by(nombre_seccion, inclinacion_peligrosa) %>%
  summarise(count = n()) %>%
  filter(inclinacion_peligrosa == 1)

# barras árboles peligrosos por sección
ggplot(seccion_peligrosa, aes(x = reorder(nombre_seccion, -count), y = count)) +
  geom_bar(stat = "identity", fill = "red") +
  labs(title = "Árboles con Inclinación Peligrosa por Sección", x = "Sección", y = "Cantidad de Árboles Peligrosos") +
  coord_flip() +  # Para voltear el gráfico horizontalmente
  theme_light()

ggsave("tp7-ml/images/peligrosa_per_section.png",width = 23, height = 10, units = "cm")


#------------------------------------#
# arboles peligrosos por especie

especie_peligrosa <- data %>%
  group_by(especie, inclinacion_peligrosa) %>%
  summarise(count = n()) %>%
  filter(inclinacion_peligrosa == 1)

ggplot(especie_peligrosa, aes(x = reorder(especie, -count), y = count)) +
  geom_bar(stat = "identity", fill = "darkgreen") +
  labs(title = "Árboles con Inclinación Peligrosa por Especie", x = "Especie", y = "Cantidad de Árboles Peligrosos") +
  coord_flip() +  # Voltear el gráfico
  theme_light()

ggsave("tp7-ml/images/peligrosa_per_species.png",width = 23, height = 10, units = "cm")

#------------------------------------#
