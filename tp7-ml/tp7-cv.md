
### create_folds

```
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

```

### cross_validation

```

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
    
```

|accuracy_mean|accuracy_sd|precision_mean|precision_sd|sensitivity_mean|sensitivity_sd|specificity_me|specificity_sd|
|-------------|-----------|--------------|------------|----------------|--------------|--------------|--------------|
|0.8910977    |0.01451993 |1             |0           |0.8910977       |0.01451993    |NaN           |NA            |


