
library(ggplot2)
data <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-train.csv")

#------------------------------------#
# Histograma con diferentes bins de circunferencia del tronco
ggplot(data, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 20, fill = "blue", alpha = 0.7) +
  labs(title = "Histograma de Circunferencia del Tronco (20 bins)", x = "Circunferencia del Tronco (cm)", y = "Frecuencia") +
  theme_light()

ggsave("tp7-ml/images/histograma_circunferencia_tronco_20bins.png",width = 15, height = 10, units = "cm")

ggplot(data, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 100, fill = "green", alpha = 0.7) +
  labs(title = "Histograma de Circunferencia del Tronco (100 bins)", x = "Circunferencia del Tronco (cm)", y = "Frecuencia") +
  theme_light()

ggsave("tp7-ml/images/histograma_circunferencia_tronco_100bins.png",width = 15, height = 10, units = "cm")

#------------------------------------#
#mismo histograma pero separado por inclinacion_peligrosa
data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)

ggplot(data, aes(x = circ_tronco_cm, fill = inclinacion_peligrosa)) +
  geom_histogram(bins = 20, alpha = 0.6, position = "identity") +
  labs(title = "Histograma(20bins) Circ del Tronco por Inclinación Peligrosa", x = "Circunferencia del Tronco (cm)", y = "Frecuencia") +
  facet_wrap(~ inclinacion_peligrosa) +  # Separa los histogramas por la clase de inclinacion_peligrosa
    theme_light()

ggsave("tp7-ml/images/histograma_circunferencia_tronco_inclinacion_peligrosa.png",width = 15, height = 10, units = "cm")

#------------------------------------#
#puntos de corte 
# Cortes: 0-50 (Bajo), 50-100 (Medio), 100-170 (Alto), >170 (Muy alto)

data$circ_tronco_cm_cat <- cut(data$circ_tronco_cm, 
                               breaks = c(-Inf, 50, 100, 170, Inf), 
                               labels = c("bajo", "medio", "alto", "muy alto"),
                               right = FALSE)  # right = FALSE para incluir el límite inferior en cada rango

# Verificar la distribución de la nueva variable categórica
table(data$circ_tronco_cm_cat)
write.csv(data, "arbolado-mendoza-dataset-circ_tronco_cm-train.csv", row.names = FALSE)
