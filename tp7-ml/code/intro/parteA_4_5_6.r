library(dplyr)

#--------Ejercicio 4-------------------
# a)
generate_random_prob <- function(data) {
  set.seed(123) 
  data$prediction_prob <- runif(nrow(data))  # Valores aleatorios entre 0 y 1
  return(data)
}

# b)
#  colunmna 'prediction_class' basada en 'prediction_prob'
random_classifier <- function(data) {
  # Asignar clases basadas en la condición
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

# c)
data_validation <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-validation.csv")
data_with_prob <- generate_random_prob(data_validation)  
data_with_class <- random_classifier(data_with_prob)     

#d)
# Calcular True Positives (TP)
TP <- data_with_class %>%
  filter(inclinacion_peligrosa == 1 & prediction_class == 1) %>%
  nrow()

# Calcular True Negatives (TN)
TN <- data_with_class %>%
  filter(inclinacion_peligrosa == 0 & prediction_class == 0) %>%
  nrow()

# Calcular False Positives (FP)
FP <- data_with_class %>%
  filter(inclinacion_peligrosa == 0 & prediction_class == 1) %>%
  nrow()

# Calcular False Negatives (FN)
FN <- data_with_class %>%
  filter(inclinacion_peligrosa == 1 & prediction_class == 0) %>%
  nrow()

# Crear matriz de confusión
confusion_matrix_4 <- matrix(c(TP, FP, FN, TN), nrow = 2, byrow = TRUE)
rownames(confusion_matrix_4) <- c("Real Positives", "Real Negatives")
colnames(confusion_matrix_4) <- c("Predicted Positives", "Predicted Negatives")

print(confusion_matrix_4)

#------------Ejericio 5-------------------
# a)
# columna 'prediction_class' con la clase mayoritaria
biggerclass_classifier <- function(data) {
  # Encontrar la clase mayoritaria en la columna 'inclinacion_peligrosa'
  majority_class <- as.integer(names(which.max(table(data$inclinacion_peligrosa))))

  data$prediction_class <- majority_class
  
  return(data)
}

# b)
data_validation <- read.csv("tp7-ml/data/arbolado-mendoza-dataset-validation.csv")
data_with_majority_class <- biggerclass_classifier(data_validation)

TP <- data_with_majority_class %>%
  filter(inclinacion_peligrosa == 1 & prediction_class == 1) %>%
  nrow()

TN <- data_with_majority_class %>%
  filter(inclinacion_peligrosa == 0 & prediction_class == 0) %>%
  nrow()

FP <- data_with_majority_class %>%
  filter(inclinacion_peligrosa == 0 & prediction_class == 1) %>%
  nrow()

FN <- data_with_majority_class %>%
  filter(inclinacion_peligrosa == 1 & prediction_class == 0) %>%
  nrow()

#crear matriz de confusion
confusion_matrix_5 <- matrix(c(TP, FP, FN, TN), nrow = 2, byrow = TRUE)
rownames(confusion_matrix_5) <- c("Real Positives", "Real Negatives")
colnames(confusion_matrix_5) <- c("Predicted Positives", "Predicted Negatives")

print(confusion_matrix_5)


#------------Ejercicio 6-------------------

calculate_accuracy <- function(TP, TN, FP, FN) {
  accuracy <- (TP + TN) / (TP + TN + FP + FN)
  return(accuracy)
}

calculate_precision <- function(TP, FP) {
  precision <- TP / (TP + FP)
  return(precision)
}

calculate_sensitivity <- function(TP, FN) {
  sensitivity <- TP / (TP + FN)
  return(sensitivity)
}

calculate_specificity <- function(TN, FP) {
  specificity <- TN / (TN + FP)
  return(specificity)
}

calculate_negative_predictive_value <- function(TN, FN) {
  npv <- TN / (TN + FN)
  return(npv)
}

calculate_for_confution_matrix <- function(confusion_matrix) {
  TP <- confusion_matrix[1, 1]
  FP <- confusion_matrix[1, 2]
  FN <- confusion_matrix[2, 1]
  TN <- confusion_matrix[2, 2]

  accuracy <- calculate_accuracy(TP, TN, FP, FN)
  precision <- calculate_precision(TP, FP)
  sensitivity <- calculate_sensitivity(TP, FN)
  specificity <- calculate_specificity(TN, FP)
  npv <- calculate_negative_predictive_value(TN, FN)

  return (list(accuracy = accuracy, precision = precision, sensitivity = sensitivity, specificity = specificity, npv = npv))
}


result_4 <- calculate_for_confution_matrix(confusion_matrix_4)
cat("Ejercicio 4\n")
cat("Accuracy: ", result_4$accuracy, "\n")
cat("Precision: ", result_4$precision, "\n")
cat("Sensitivity: ", result_4$sensitivity, "\n")
cat("Specificity: ", result_4$specificity, "\n")
cat("Negative Predictive Value: ", result_4$npv, "\n")


result_5 <- calculate_for_confution_matrix(confusion_matrix_5)
cat("Ejercicio 5\n")
cat("Accuracy: ", result_5$accuracy, "\n")
cat("Precision: ", result_5$precision, "\n")
cat("Sensitivity: ", result_5$sensitivity, "\n")
cat("Specificity: ", result_5$specificity, "\n")
cat("Negative Predictive Value: ", result_5$npv, "\n")









