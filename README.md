# anomalydetector-evt

Este paquete se basa en la metodología para detección de anomalías en tiempo real propuesta por Siffer, Alban, et. al en el artículo *"Anomaly detection in streams with extreme value theory"*. La idea inicial es ajustar una distribución a los valores extremos de la distribución y finalmente se opta por ajustar una Distribución Pareto Generalizada a los excesos (datos - umbral). Se busca encontrar para cada nuevo valor $X_i$ un cuantil $z_q$ tal que $P(X_i>t)=q$, con $q$ una probabilidad muy pequeña.

El paquete contiene dos clases, `SPOT` y `DSPOT`. La primera es para detectar anomalías en datos estacionarios, la segunda para datos con drift. Entonces el objetivo en la detección de anomalías es definir dos valores. 

* $t$: Valor desde el cual se considerán valores extremos (determina la cola de la distribución que se ajustará mediante una DPG).
* $z_q$: Cuantil a partir del cual se considerarán anomalías. Este valor se recalcula en cada iteración.


#### Instalación

Lo primero es instalar los paquetes necesarios `numpy`, `scipy` y `pandas`, mediante `pip`. 

```python
!pip install numpy scipy pandas
```

Luego instalar el paquete de detección de anomalías como se muestra a continuación.

```python
!pip install git+https://github.com/angmnz/anomalydetector-evt
```

### Uso

A continuación se explicarán los parámetros y cómo utilizar las clases contenidas en el paquete.

#### SPOT

Lo primero es importar la librería `pandas` (asumiendo que se cargarán los datos posteriormente desde un csv) y la clase `SPOT`.

```python
import pandas as pd
from anomalydetector_evt import SPOT
```

Luego se deben cargar los para el entrenamiento, se asume que durante este periodo no existen anomalías.

```python
data = pd.read_csv('datos_entrenamiento.csv')
```

A continuación se realiza la inicialización de la clase y detección mediante el método `init`. La clase recibe tres parámetros:

* `data`: Datos para el entrenamiento con los cuales se definirá el $z_q$ y $t$ iniciales.
* `p`: Valor para definir el percentil desde el cual se considerarán los valores como extremos, se sugiere 0.98. Es importante que $p>q$.
* `q`: Probabilidad de la anomalía. Entre más pequeño sea el valor menos sensible será la detección.

```python
anomalydetector = SPOT(data, p=0.98, q=10e-4)
SPOT.init()
```

Luego se actualiza la clase con nuevos valores. El método `update` retorna `True` en caso de detectar una anomalía y `False` en caso contrario. 

```python
anomalia = anomalydetector.update(new_value)
```

En cada `update` se puede recuperar el valor de $z_q$.

```python
anomalydetector.zq
```

**Ejemplos aplicación SPOT**

* [Detección de anomalías con SPOT en datos simulados](https://github.com/angmnz/anomalydetector-evt/blob/main/tests/SPOT.ipynb)
* [Detección de anomalías con SPOT en datos reales](https://github.com/angmnz/anomalydetector-evt/blob/main/tests/detección_datos_reales.ipynb)

  
#### DSPOT

Lo primero es importar la librería `pandas` (asumiendo que se cargarán los datos posteriormente desde un csv) y la clase `DSPOT`.

```python
import pandas as pd
from anomalydetector_evt import DSPOT
```
Luego se deben cargar los para el entrenamiento, se asume que durante este periodo no existen anomalías.

```python
data = pd.read_csv('datos_entrenamiento.csv')
```
A continuación se realiza la inicialización de la clase y detección mediante el método `init`. La clase recibe tres parámetros:

* `data`: Datos para el entrenamiento con los cuales se definirá el $z_q$ y $t$ iniciales.
* `p`: Valor para definir el percentil desde el cual se considerarán los valores como extremos, se sugiere 0.98. Es importante que $p>q$.
* `q`: Probabilidad de la anomalía. Entre más pequeño sea el valor menos sensible será la detección.
* `d`: Número de observaciones para la media móvil que se utilizará para eliminar el drift.

```python
anomalydetector = DSPOT(data, p=0.98, q=10e-4, d=12)
DSPOT.init()
```

Luego se actualiza la clase con nuevos valores. El método `update` retorna `True` en caso de detectar una anomalía y `False` en caso contrario. 

```python
anomalia = anomalydetector.update(new_value)
```

**Ejemplos con DSPOT**

* [Detección de anomalías con DSPOT en datos simulados](https://github.com/angmnz/anomalydetector-evt/blob/main/tests/DSPOT.ipynb)
* [Detección de anomalías con DSPOT en datos reales](https://github.com/angmnz/anomalydetector-evt/blob/main/tests/detección_datos_reales.ipynb)

### Referencias      

Siffer, A., Fouque, P. A., Termier, A., & Largouet, C. (2017, August). Anomaly detection in streams with extreme value theory. In Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining (pp. 1067-1075).
