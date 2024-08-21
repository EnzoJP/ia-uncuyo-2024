
---en proceso---

Introducción:

En la presente investigación se aborda el problema de la limpieza autónoma de un entorno dado con dos
agentes aspiradora que deberán recorrer el entorno, detectar la suciedad, limpiarla, y continuar hasta que su vida útil se agote. El objetivo principal es evaluar el rendimiento de los agentes en diferentes configuraciones de tamaño del entorno y niveles de suciedadluego compararemos los resultados de estos dos y veremos si alcanzan un resultado óptimo.

Marco teorico:

En la simulación, el entorno está representado por una matriz, donde cada celda puede estar sucia o limpia (esto lo determinará el nivel de suciedad dado). Los agentes, que se mueven por este entorno, están equipados con sensores que les permiten detectar si la celda en la que se encuentran está sucia, y con actuadores que les permiten moverse y limpiar la suciedad.

El agente toma decisiones en cada paso del tiempo, eligiendo entre limpiar la celda actual o moverse a otra celda. El rendimiento (performance) del agente se mide en función de la cantidad de suciedad eliminada antes de que su vida útil se agote.

La batería del agente se reduce en cada acción que realiza, ya sea mover o limpiar. De esta manera,podemos observar en un periodo de 1000 unidades que agente realiza mejor el trabajo de maximizar la performance.

Dise˜no experimental:

Para evaluar el rendimiento de los agentes, se decidió varíar tanto el tamaño del entorno como el porcentaje de suciedad inicial. Los tamaños del entorno incluyen matrices de 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, y 128x128 celdas. Los porcentajes de suciedad se establecieron en 10%, 20%, 40%, y 80%, para simular diferentes niveles de dificultad.

Cada combinación de tamaño y porcentaje de suciedad fue repetida 10 veces y el rendimiento se midió en términos del número de celdas limpias al agotarse la batería del agente.

Análisis y discusión de resultados:

--hacer--



conclusiones:

En conclusión se puede observar como el tanto el agente reflexivo simple como el agente reflexivo aleatorio pueden llegar a ser útiles en un entorno chico de limpieza, solo ahi poidríamos hablar de racional, pero como observamos a medida que este entorno se hace cada vez mas grande si bien el primero (ARS) lo maneja un poco mejor vemos que gastan toda su vida útil y no logran limpiar el entorno completo, por lo que al no llegar a un resultado lo suficientemete óptimo o aceptable no podemos asegurar que estos sean racionales en su entorno.
Por otro lado sería interesante pensar lo que poidría lograr un agente con alguna información extra de entrada o que se guarde a medida que limpie el entorno como lo puede ser por ejemplo saber que camino tomar de menor resistencia al saber la ubicación de la basura o saber la geografía del etorno u otras ideas que poidrían acercarce a que se alcance un resultado mas óptimo, maximizando la performance.
