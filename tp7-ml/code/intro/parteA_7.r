library(rpart)
library(dplyr)

calculate_metrics <- function(conf_matrix) {
  TP <- conf_matrix[1, 1]
  FP <- conf_matrix[1, 2]
  FN <- conf_matrix[2, 1]
  TN <- conf_matrix[2, 2]
  
  accuracy <- (TP + TN) / (TP + TN + FP + FN)
  precision <- TP / (TP + FP)
  sensitivity <- TP / (TP + FN)  
  specificity <- TN / (TN + FP)
  
  return(c(accuracy, precision, sensitivity, specificity))
}

create_folds <- function(dataframe, k) {
    n <- nrow(dataframe)
    indices <- sample(1:n) #división en folds aleatoria 
    # Crear los k folds, dividiendo los índices en k subconjuntos
    list_indices <- split(indices, rep(1:k, length.out = n))
    
    # Crear la estructura de la lista con los nombres de los folds
    folds <- list()
    for (i in 1:k) {
        fold_name <- paste0("Fold", i)
        folds[[fold_name]] <- list_indices[[i]]  # Guardar los índices
    }
    
    return(folds)
}

cross_validation <- function(dataframe, k,folds) {
  n <- nrow(dataframe)

  accuracies <- c()
  precisions <- c()
  sensitivities <- c()
  specificities <- c()

  dataframe$inclinacion_peligrosa <- as.factor(dataframe$inclinacion_peligrosa)


  # Fórmula de entrenamiento
  train_formula <- formula(inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion + especie)

  # Cross-validation
  for (i in 1:k) {
    # Dividimos el conjunto de datos en entrenamiento y validación
    test_indices <- folds[[i]]
    train_indices <- setdiff(1:n, test_indices)
    
    data_train <- dataframe[train_indices, ]
    data_test <- dataframe[test_indices, ]
    
    # Entrenamos el modelo de árbol de decisión
    tree_model <- rpart(train_formula, data = data_train)
    
    # Predicciones para el conjunto de test
    predictions <- predict(tree_model, data_test, type = "class")

    #print(predictions)
    
    conf_matrix <- table(data_test$inclinacion_peligrosa, predictions)

    #print(conf_matrix)
    
    metrics <- calculate_metrics(conf_matrix)
    
    accuracies <- c(accuracies, metrics[1])
    precisions <- c(precisions, metrics[2])
    sensitivities <- c(sensitivities, metrics[3])
    specificities <- c(specificities, metrics[4])
  }

  metrics_summary <- list(
    accuracy_mean = mean(accuracies), accuracy_sd = sd(accuracies),
    precision_mean = mean(precisions), precision_sd = sd(precisions),
    sensitivity_mean = mean(sensitivities), sensitivity_sd = sd(sensitivities),
    specificity_mean = mean(specificities), specificity_sd = sd(specificities)
  )
  
  return(metrics_summary)
}
    
#------------------------------------------

seed <- 123
set.seed(seed)
data <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-validation.csv")
folds <- create_folds(data, 10)

#------------------------------------------


result <- cross_validation(data, 10,folds)
print(result)