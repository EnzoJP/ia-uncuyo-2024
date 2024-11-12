
suppressMessages(library(readr))
suppressMessages(library(ROSE))
suppressMessages(library(ranger))
suppressMessages(library(caret))
suppressMessages(library(rpart))
suppressMessages(library(dplyr)) 

set.seed(2024)

#---------------------------------------------------------------------------------------

data_train <- readr::read_csv("tp7-ml/code/desafio/arbolado-mza-dataset.csv",
                              col_types = cols(
                                especie = col_character(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long= col_double(),
                                lat = col_double(),
                                nombre_seccion = col_character(),
                                seccion = col_integer(),
                                area_seccion = col_double(),
                                inclinacion_peligrosa = col_integer()
                              ))

data_test <- readr::read_csv("tp7-ml/code/desafio/arbolado-mza-dataset-test.csv",
                              col_types = cols(
                                especie = col_character(),
                                id = col_integer(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long= col_double(),
                                lat = col_double(),
                                nombre_seccion = col_character(),
                                seccion = col_integer(),
                                area_seccion = col_double(),
                              ))

# modificar categorías
data_train$altura <- as.numeric(gsub("[^0-9.]", "", data_train$altura))
data_test$altura <- as.numeric(gsub("[^0-9.]", "", data_test$altura))


#remove NA values
data_train <- na.omit(data_train)

#---------------------------------------------------------------------------------------

# tecnica de pesos Cost-Sensitive Learning

#weight_pos <- (nrow(data_train) / sum(data_train$inclinacion_peligrosa == 1))
weight_pos <- 1
weight_neg <- (nrow(data_train) / sum(data_train$inclinacion_peligrosa == 0))


weights <- ifelse(
  data_train$inclinacion_peligrosa == 1,
  case_when(
    data_train$especie == "Morera" ~ weight_pos * 3,
    data_train$especie == "Pltano" ~ weight_pos * 1.5,
    data_train$especie == "Paraiso" ~ weight_pos * 1.3,
    data_train$especie == "Fresno europeo" ~ weight_pos * 1.1,
    data_train$especie == "Acacia SP" ~ weight_pos * 2,
    data_train$especie == "Fresno americano" ~ weight_pos * 1,
    data_train$especie == "Aguaribay" ~ weight_pos * 1.5,
    data_train$especie == "Jacarand" ~ weight_pos * 1.8,
    data_train$especie == "Caducifolio" ~ weight_pos * 1,
    data_train$especie == "Eucalyptus" ~ weight_pos * 0.8,
    data_train$especie == "lamo criollo" ~ weight_pos * 0.000000001,
    data_train$especie == "Conifera" ~ weight_pos * 0.1,
    data_train$especie == "Algarrabo" ~ weight_pos * 5,
    data_train$especie == "Olmo bola" ~ weight_pos * 0.5,
    data_train$especie == "Acasia visco" ~ weight_pos * 1.8,
    data_train$especie == "Ligustro" ~ weight_pos * 0.1,
    data_train$especie == "Tipa" ~ weight_pos * 2,
    data_train$especie == "Catalpa" ~ weight_pos * 2.2,
    data_train$especie == "Arabia" ~ weight_pos * 0.000001,
    data_train$especie == "Maiten" ~ weight_pos * 0.000000001,
    
    TRUE ~ weight_pos  # valor por defecto si no coincide con nada
  ),
  weight_neg  # valor si inclinacion_peligrosa es 0
)


print(weight_pos)
print(weight_neg)


#---------------------------------------------------------------------------------------

#  Random Forest con ranger
data_train.rf <- ranger(
  inclinacion_peligrosa ~ ., 
  data = data_train, 
  num.trees = 300, 
  importance = "permutation",
  case.weights = weights,
  num.threads = 4,
  mtry = 2
)

predictions <- predict(data_train.rf, data_test)$predictions


resultados_validation <- data.frame(inclinacion_peligrosa = predictions) # en dataframe

#convertir en 1 y 0
#resultados_validation <- as.data.frame(lapply(resultados_validation, function(x) ifelse(x >= 0.30, 1, 0)))

#print(sum(resultados_validation$inclinacion_peligrosa))

#---------------------------------------------------------------------------------------

# envio de kaggle 
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = resultados_validation$inclinacion_peligrosa)

readr::write_csv(submission, "./arbolado-mza-dataset-envio-ejemplo-ranger.csv")

#---------------------------------------------------------------------------------------

