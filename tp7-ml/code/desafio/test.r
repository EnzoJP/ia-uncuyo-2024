#library(ROSE)

# oversampling
"""
data(data_train)
data_train$inclinacion_peligrosa <- as.factor(ifelse(data_train$inclinacion_peligrosa == 1, "si", "no"))
oversampled_data <- ovun.sample(inclinacion_peligrosa ~ ., data = data_train, method = "over", N = 2 * nrow(data_train), seed = 100)$data
"""
#undersampling

"""
data(data_train)
data_train$inclinacion_peligrosa <- as.factor(ifelse(data_train$inclinacion_peligrosa == 1, "si", "no"))
undersampled_data <- ovun.sample(inclinacion_peligrosa ~ ., data = data_train, method = "under", seed = 100)$data
"""
#Synthetic Minority Over-sampling Technique (SMOTE)
"""
library(DMwR)
data(data_train)
data_train$inclinacion_peligrosa <- as.factor(ifelse(data_train$inclinacion_peligrosa == 1, "si", "no"))
smothed_data <- SMOTE(inclinacion_peligrosa ~ ., data = data_train, perc.over = 100, perc.under = 200)$data
"""

# weights
"""
data_train$inclinacion_peligrosa <- as.factor(ifelse(data_train$inclinacion_peligrosa == 1, "si", "no"))

weights <- ifelse(data_train$inclinacion_peligrosa == "si", 0.5, 0.01)


fit <- rpart(inclinacion_peligrosa ~ ., data = data_train, weights = weights, method = "class")
"""