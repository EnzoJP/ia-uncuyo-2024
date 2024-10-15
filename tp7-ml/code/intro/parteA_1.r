
library(dplyr)
library(ggplot2)


data <- read.csv("tp7-ml/data/arbolado-mza-dataset.csv")

data_train <- data %>% sample_frac(0.8)

data_test <- data %>% anti_join(data_train, by = "id")

write.csv(data_train, "tp7-ml/data/arbolado-mendoza-dataset-train.csv", row.names = FALSE)
write.csv(data_test, "tp7-ml/data/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
