# Proveer las respuestas a los puntos 1,2,5,6,7 de la sección 2.4 (página 52 del ISLRv2)

## 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.
### (a) The sample size n is extremely large, and the number of predictors p is small.
    Sería mejor usar algo mas inflexible o restrictivo ya que el numero de variables es pequeño.
### (b) The number of predictors p is extremely large, and the number of observations n is small.
    Sería mejor usar algo mas flexible ya que el numero de observaciones es pequeño y tenemos muchos predictores a considerar.
### (c) The relationship between the predictors and response is highly non-linear.
    En este caso sería mejor usar algo mas flexible ya que la relación no es lineal y un modelo flexible puede capturar mejor la relación.
### (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.
    En este caso sería mejor usar algo mas inflexible ya que un modelo flexible podría sobreajustar los datos y capturar el ruido en lugar de la relación real aumentando la varianza del modelo.

## 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

### (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.
    Es un problema de regresión ya que la variable de interés es continua. Estamos interesados en inferencia ya que queremos entender que factores afectan el salario del CEO. n=500, p=3
### (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.
    Es un problema de clasificación ya que la variable de interés es categórica. Estamos interesados en predicción ya que queremos saber si nuestro producto será un éxito o un fracaso. n=20, p=13

### (c) We are interested in predicting the % change in the US dollar in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the dollar, the % change in the US market, the % change in the British market, and the % change in the German market.
    Es un problema de regresión. Estamos interesados en predicción ya que queremos predecir el cambio porcentual del dólar. n=52, p=3

### (d) We are interested in predicting the price of a stock. We collect data for the last month on the price of the stock at closing, the % change in the stock price each day, the volume of stocks traded each day, the price of the stock at opening, and the highest price the stock reached during the day.
    Es un problema de regresión ya que es un precio. Estamos interesados en predicción ya que queremos predecir el precio de la acción. n=30, p=4

## 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

    Las ventajas de un modelo flexible son que pueden capturar relaciones más complejas y ajustarse mejor a los datos. Sin embargo, los modelos flexibles tienden a sobreajustar los datos y pueden capturar ruido en lugar de la relación real. Un modelo flexible puede ser preferido cuando la relación entre las variables es compleja y no lineal. Un modelo menos flexible puede ser preferido cuando la relación es simple y lineal, ya que es menos probable que sobreajuste los datos.

## 6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

    Un modelo paramétrico hace suposiciones sobre la relación entre las variables y los parámetros del modelo (parametros de f). Un modelo no paramétrico no hace suposiciones,puede ajustarse a los datos de manera más flexible (forma de f) .
    Las ventajas de un modelo paramétrico es menos complejo estimar parámetros y requieren menos datos para ajustarse. Sin embargo, los modelos paramétricos pueden no capturar la verdadera relación entre las variables si las suposiciones del modelo son incorrectas.
    Los modelos no paramétricos pueden capturar relaciones más complejas, pero pueden requerir más datos para ajustarse y pueden ser menos interpretables.

## 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

#### a) Compute the Euclidean distance between each observation and the test point, x1 = x2 = x3 = 0.
    La distancia euclidiana entre los puntos se calcula como en forma general como sqrt((p1-q1)^2 + (p2-q2)^2 + ... + (pn-qn)^2), entonces siendo q(0,0,0) tenemos:

    Euclidean(obs_1)= 3

    Euclidean(obs_2)= 2

    Euclidean(obs_3)= sqrt(10)

    Euclidean(obs_4)= sqrt(5)

    Euclidean(obs_5)= sqrt(2)

    Euclidean(obs_6)= sqrt(3)

#### b) What is our prediction with K = 1? Why?

    Para k=1 la distancia mas corta es la de obs_5, por lo que la predicción sería verde.

#### c) What is our prediction with K = 3? Why?

    Para k=3 las distancias mas cortas son las de obs_5, obs_6 y obs_2, por lo que la predicción sería rojo.

    Esto es asi porque la clase mas comun entre los k vecinos mas cercanos es la que se predice.

#### d) If the Bayes decision boundary in this problem is highly non-linear, would we expect the best value for K to be large or small? Why?

    "As K grows, the method becomes less flexible and produces a decision boundary that is close to linear"

    Si la frontera de decisión de Bayes es altamente no lineal, esperaríamos que el mejor valor para K sea pequeño, ya que un valor grande de K produciría una frontera de decisión más lineal.