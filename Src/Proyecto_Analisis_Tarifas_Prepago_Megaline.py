#!/usr/bin/env python
# coding: utf-8

# # Hola Axel! <a class="tocSkip"></a>
# 
# Mi nombre es Oscar Flores y tengo el gusto de revisar tu proyecto. Si tienes algún comentario que quieras agregar en tus respuestas te puedes referir a mi como Oscar, no hay problema que me trates de tú.
# 
# Si veo un error en la primera revisión solamente lo señalaré y dejaré que tú encuentres de qué se trata y cómo arreglarlo. Debo prepararte para que te desempeñes como especialista en Data, en un trabajo real, el responsable a cargo tuyo hará lo mismo. Si aún tienes dificultades para resolver esta tarea, te daré indicaciones más precisas en una siguiente iteración.
# 
# Te dejaré mis comentarios más abajo - **por favor, no los muevas, modifiques o borres**
# 
# Comenzaré mis comentarios con un resumen de los puntos que están bien, aquellos que debes corregir y aquellos que puedes mejorar. Luego deberás revisar todo el notebook para leer mis comentarios, los cuales estarán en rectángulos de color verde, amarillo o rojo como siguen:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
#     
# Muy bien! Toda la respuesta fue lograda satisfactoriamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Existen detalles a mejorar. Existen recomendaciones.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Se necesitan correcciones en el bloque. El trabajo no puede ser aceptado con comentarios en rojo sin solucionar.
# </div>
# 
# Cualquier comentario que quieras agregar entre iteraciones de revisión lo puedes hacer de la siguiente manera:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# </div>
# 
# Mucho éxito en el proyecto!

# ## Resumen de la revisión 1 <a class="tocSkip"></a>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Buen trabajo Axel. Tu notebook tiene todo el desarrollo necesario, pero hay un solo punto que debes revisar, la conclusión del primer test realizado es incorrecta, revisa con atención los valores. Con eso tu notebook estará completo.
#     
# Saludos!    
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Es correcto, interprete mal los datos del valor_p, no me di cuenta que estaba expresado en un exponente negativo, por lo que es muchisimo menor al alpha, dando como resultado el Rechazo de la hipotesis nula. Gracias por tu Feedback.</b> <a class="tocSkip"></a>
# </div>

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# [Te proporcionamos algunos comentarios para orientarte mientras completas este proyecto. Pero debes asegurarte de eliminar todos los comentarios entre corchetes antes de entregar tu proyecto.]
# 
# [Antes de sumergirte en el análisis de datos, explica por tu propia cuenta el propósito del proyecto y las acciones que planeas realizar.]
# 
# [Ten en cuenta que estudiar, modificar y analizar datos es un proceso iterativo. Es normal volver a los pasos anteriores y corregirlos/ampliarlos para permitir nuevos pasos.]

# ## Inicialización

# In[333]:


# Cargar todas las librerías
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import math as mt
from scipy import stats as st
from math import factorial
import datetime as dt


# ## Cargar datos

# In[334]:


# Carga los archivos de datos en diferentes DataFrames
df_calls = pd.read_csv('/datasets/megaline_calls.csv')
df_internet = pd.read_csv('/datasets/megaline_internet.csv')
df_messages = pd.read_csv('/datasets/megaline_messages.csv')
df_plans = pd.read_csv('/datasets/megaline_plans.csv')
df_users = pd.read_csv ('/datasets/megaline_users.csv')


# ## Preparar los datos

# [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]

# ## Tarifas

# In[335]:


# Imprime la información general/resumida sobre el DataFrame de las tarifas

print(df_plans.info(show_counts = True))


# In[336]:


# Imprime una muestra de los datos para las tarifas
print(df_plans.head())



# **Considero que los datos de este dataframe estan correctos, unicamente voy a cambiar el tipo de datos en las columnas "usd_per_gb" y "usd_monthly_pay" estan como numeros enteros y los voy a cambiar a numeros flotantes ya que contienen valores de dinero y usualmente se trabaja como float64 y los demas datos corresponden a los datos de los planes tarifarios**

# ## Corregir datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[337]:


df_plans['usd_per_gb'] = df_plans['usd_per_gb'].astype('float64')
df_plans['usd_monthly_pay'] = df_plans['usd_monthly_pay'].astype('float64')


# ## Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[338]:


print(df_plans.head())


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Ok, correcto. En esta parte podrías haber convertido de mb a gb el consumo de internet incluido en el plan.
# 
# </div>

# ## Usuarios/as

# In[339]:


# Imprime la información general/resumida sobre el DataFrame de usuarios

print(df_users.info())


# In[340]:


# Imprime una muestra de datos para usuarios

print(df_users.head())


# **Podemos observar que no hay datos ausentes, ni valores repetidos. Tenemos unicamente valores ausentes en la columna 'churnd_date', pero esto significa que el usuario seguia usando la tarifa cuando esta base de datos fue extraida. Este DF contiene la informacion de los usuarios.
# Unicamente voy a cambiar el formato de la columna 'reg_date' y 'churn_date' a formatos tipo fecha por si tenemos que trabajar con estos valores posteriormente.**

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[341]:


df_users['reg_date'] = pd.to_datetime(df_users['reg_date'], format = '%Y/%m/%d')

df_users['churn_date'] = pd.to_datetime(df_users['churn_date'], format = '%Y/%m/%d')


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[342]:


print(df_users.info())


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien, correcto
# 
# </div>

# ## Llamadas

# In[343]:


# Imprime la información general/resumida sobre el DataFrame de las llamadas
print(df_calls.info())


# In[344]:


# Imprime una muestra de datos para las llamadas
print(df_calls
      .head(30))


# **Podemos observar que en este dataframe tenemos 4 columnas, a mi consideración, tengo que modificar la columna 'call_date' a formato de fecha porque como podemos ver, actualmente tiene formato tipo object. Asimismo considero que deberia de convertir la columna 'duration' a tipo int, ya que en la descripción del proyecto indica que los segundos de las llamadas se redondean al numero inmediato siguiente.
# No se tienen datos duplicados ni ausentes.**

# ### Corregir los datos

# **Convertire la columna 'call_date' a formato de fecha y voy a crear una columna nueva con los valores redondeados de la columna 'duration' ya que como nos menciona la descricpion del proyecto, debemos considerar 1 minuto completo aun si la llamada solo duro 1 seg.**

# In[345]:


df_calls['call_date'] = pd.to_datetime(df_calls['call_date'], format = '%Y/%m/%d')
df_calls['duration_rounded'] = np.ceil(df_calls['duration'])


# ### Enriquecer los datos

# **Voy a agregar una columna llamada 'month' y extraer el mes en el que se realizo la actividad, ya que la necesito para hacer el calculo del paso 1.12**

# In[346]:


df_calls['month'] = df_calls['call_date'].dt.month
print(df_calls.head(20))


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Muy bien, bien con calcular la duración a facturar
# 
# </div>

# ## Mensajes

# In[347]:


# Imprime la información general/resumida sobre el DataFrame de los mensajes
print(df_messages.info())


# In[348]:


# Imprime una muestra de datos para los mensajes
print(df_messages.head(20))


# **En este dataframe encontramos los datos correspondientes a los mensajes de los usuarios, cambiaremos la columna 'message_date' por un valor tipo time.** 

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[349]:


df_messages['message_date'] = pd.to_datetime(df_messages['message_date'], format = '%Y/%m/%d')


# ### Enriquecer los datos

# **Voy a agregar una columna llamada 'month' y extraer el mes en el que se realizo la actividad, ya que la necesito para hacer el calculo del paso 1.12**

# In[350]:


df_messages['month'] = df_messages['message_date'].dt.month

print(df_messages.head(20))


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien, correcto
# 
# </div>

# ## Internet

# In[351]:


# Imprime la información general/resumida sobre el DataFrame de internet
print(df_internet.info())


# In[352]:


# Imprime una muestra de datos para el tráfico de internet
print(df_internet.head(10))


# **En este dataframe podemos observar todos los datos de los usuarios acerca de su consumo de internet. Cambiare el tipo de datos de la columna 'session_date' por datos tipo time.**

# ### Corregir los datos

# 

# In[353]:


df_internet['session_date'] = pd.to_datetime(df_internet['session_date'], format = '%Y/%m/%d')


# ### Enriquecer los datos

# **Voy a agregar una columna llamada 'month' y extraer el mes en el que se realizo la actividad, ya que la necesito para hacer el calculo del paso 1.12**

# In[354]:


df_internet['month'] = df_internet['session_date'].dt.month
print(df_internet.head(20))


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien, correcto
# 
# </div>

# ## Estudiar las condiciones de las tarifas

# [Es sumamente importante entender cómo funcionan las tarifas, cómo se les cobra a los usuarios en función de su plan de suscripción. Así que te sugerimos imprimir la información de la tarifa para ver una vez más sus condiciones.]

# In[355]:


# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras
print(df_plans.info())
print(df_plans.head())


# ## Agregar datos por usuario
# 
# [Ahora que los datos están limpios, agrega los datos por usuario y por periodo para que solo haya un registro por usuario y por periodo. Esto facilitará mucho el análisis posterior.]

# In[356]:


# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.
users_calls = df_calls.groupby( by = ['user_id', 'month'])['id'].count().reset_index(name = 'calls')
print(users_calls.head(20))


# In[357]:


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.
users_minutes = df_calls.groupby( by = ['user_id', 'month'])['duration_rounded'].sum().reset_index(name = 'minutes_rounded')
print(users_minutes.head(20))


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Muy bien con los cálculos para llamadas
# 
# </div>

# In[358]:


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.
users_messages = df_messages.groupby( by = ['user_id', 'month'])['id'].count().reset_index(name = 'messages')
print(users_messages.head(20))


# In[359]:


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.
users_mb_used = (df_internet.groupby( by = ['user_id', 'month'])['mb_used'].sum())/1024 #dividimos entre 1024 para pasar los MB a GB
users_mb_used = np.ceil(users_mb_used).reset_index(name = 'gb_used_rounded') #Redondeamos los gb ya que asi nos dice la descripcion del ejercicio.
print(users_mb_used)


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho con los cálculos para mensajes y gb. 
# 
# </div>

# [Junta los datos agregados en un DataFrame para que haya un registro que represente lo que consumió un usuario único en un mes determinado.]

# In[360]:


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month
df_merged = users_calls.merge(users_minutes, on=['user_id', 'month'], how='outer') \
    .merge(users_messages, on=['user_id', 'month'], how='outer') \
    .merge(users_mb_used, on=['user_id', 'month'], how='outer')
print(df_merged.info())


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Correcto el uso del merge tipo outer, esto evita que se pierdan datos de usuarios.
# 
# </div>

# In[361]:


# Añade la información de la tarifa
df_activity_client = df_merged.merge(df_users[['user_id','plan']], how = 'left', on = 'user_id') #Fusionamos con df_clients para saber que plan tiene cada cliente

df_full = df_activity_client.merge(df_plans, how = 'left', left_on = 'plan', right_on = 'plan_name') #Fusionamos con df_plans para tener las caracteristicas de las tarifas y poder hacer operaciones.

print(df_full.head(20))


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien, en esta parte basta con el uso de left ya que la data de consumo de usuarios ya está completa.
# 
# </div>

# [Calcula los ingresos mensuales por usuario (resta el límite del paquete gratuito del número total de llamadas, mensajes de texto y datos; multiplica el resultado por el valor del plan de llamadas; añade la tarifa mensual en función del plan de llamadas). Nota: Dadas las condiciones del plan, ¡esto podría no ser tan trivial como un par de líneas! Así que no pasa nada si dedicas algo de tiempo a ello.]

# In[362]:


# Calcula el ingreso mensual para cada usuario

#En esta seccion calculamos la diferencia de minutos, mensajes o datos usados por el cliente, de esta forma sabremos si hubo sobre consumo por parte del usuario.
df_full['extra_minutes'] = (df_full['minutes_rounded'] - df_full['minutes_included']).clip(lower = 0)
df_full['extra_messages'] = (df_full['messages'] - df_full['messages_included']).clip(lower = 0)
df_full['extra_gb'] = (df_full['gb_used_rounded'] - (df_full['mb_per_month_included']/1024)).clip(lower = 0)

#En esta parte calculamos el cobro extra que se le tiene que hacer a cada cliente por haber excedido minutos, mensajes o datos en caso de aplicar.
df_full['cost_minutes'] = df_full['extra_minutes'] * df_full['usd_per_minute']
df_full['cost_sms'] = df_full['extra_messages'] * df_full['usd_per_message']
df_full['cost_gb'] = df_full['extra_gb'] * df_full['usd_per_gb']

#Calculamos cuanto tiene que pagar en total el cliente cada mes. 
df_full['total_revenue'] = df_full['usd_monthly_pay'] + df_full['cost_minutes'] + df_full['cost_sms'] + df_full['cost_gb']

print(df_full.head(20))


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Buen trabajo, el cálculo del ingreso está correcto.
# 
# </div>

# ## Estudia el comportamiento de usuario

# [Calcula algunas estadísticas descriptivas para los datos agregados y fusionados que nos sean útiles y que muestren un panorama general captado por los datos. Dibuja gráficos útiles para facilitar la comprensión. Dado que la tarea principal es comparar las tarifas y decidir cuál es más rentable, las estadísticas y gráficas deben calcularse por tarifa.]
# 
# [En los comentarios hallarás pistas relevantes para las llamadas, pero no las hay para los mensajes e Internet. Sin embargo, el principio del estudio estadístico que se aplica para ellos es el mismo que para las llamadas.]

# ### Llamadas

# In[363]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

avg_calls_duration = df_full.groupby(by = ['plan', 'month'])['minutes_rounded'].mean()
avg_calls_duration = avg_calls_duration.reset_index()

plt.figure(figsize=(12,5))
sns.barplot(data = avg_calls_duration, x = 'month', y = 'minutes_rounded', hue = 'plan')
plt.title('Duracion promedio de llamadas por mes y plan')
plt.xlabel('Mes')
plt.ylabel('Duracion promedio [min]')
plt.legend(title = 'Plan')
plt.tight_layout()
plt.show()


# In[364]:


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.
sns.histplot(data = df_full, x = 'minutes_rounded',bins = 20, hue = 'plan', multiple = 'dodge')
plt.title('Distribucion del uso mensual de minutos por plan')
plt.xlabel('Minutos al mes')
plt.ylabel('Numero de usuarios')
plt.tight_layout()
plt.show()


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Correcto, muy bien con los gráficos de análisis.
# 
# </div>

# [Calcula la media y la variable de la duración de las llamadas para averiguar si los usuarios de los distintos planes se comportan de forma diferente al realizar sus llamadas.]

# In[365]:


# Calcula la media y la varianza de la duración mensual de llamadas.
med_var = df_full.groupby(by = ['plan','month'])['minutes_rounded'].agg(['mean','var'])
med_var.plot(kind='bar', subplots = True, layout=(2,1),figsize=(10,6), sharex=True)
plt.suptitle("Media y Varianza de minutos mensuales por plan y mes")
plt.tight_layout()
plt.show()


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Ok, correcta la separación entre planes, aunque no era necesaria la separación por mes.
# 
# </div>

# In[366]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas
monthly_minutes = df_full.groupby(by = ['user_id','month','plan'])['minutes_rounded'].sum().reset_index()
sns.boxplot(data=monthly_minutes, x='plan', y='minutes_rounded')
plt.title('Distribución mensual de minutos por plan')
plt.xlabel('Plan')
plt.ylabel('Minutos al mes')
plt.tight_layout()
plt.show()


# **Podemos hacer la conclusion de que los usuarios tienen la misma distribucion, sin importar el plan que tengan. Ya que los rangos intercualtilicos son casi los mismos, asi como la media. Hay valores atipos que podrian estar relacionados a clientes que hacen un uso mas intenso en cuanto a llamadas.** 

# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho. En realidad ambos planes son similares en consumo de llamadas.
# 
# </div>

# ### Mensajes

# In[367]:


# Comprara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan
monthly_messages = df_full.groupby(['user_id','month','plan'])['messages'].sum().reset_index()
sns.histplot(data=monthly_messages, x='messages', bins=10, hue = 'plan', multiple = 'dodge')
plt.title('Distribucion del numero de mensajes enviados por plan')
plt.xlabel('Mensajes al mes')
plt.ylabel('Numero de usuarios')
plt.tight_layout()
plt.show()


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Muy bien, correcto
# 
# </div>

# In[368]:


# Compara la cantidad de tráfico de Internet consumido por usuarios por plan

#Unimos con df_users para saber que plan tiene cada usuario
users_mb_used = users_mb_used.merge(df_users[['user_id', 'plan']], on='user_id', how='left')
print(users_mb_used)


# In[369]:


sns.histplot(data=users_mb_used, x='gb_used_rounded', bins=10, hue='plan', multiple='dodge')
plt.title('Distribucion del consumo mensual de datos por plan')
plt.xlabel('Gygabytes usados al mes')
plt.ylabel('Numero de usuarios')
plt.tight_layout()
plt.show()


# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho, aunque si bien el template indica hacer este gráfico de internet aquí, este debería ir un poco más abajo.
# 
# </div>

# **En mi punto de vista, considero que los usuarios del plan surf son los que mas mensajes mandan.
# El valor moda es el 0, esto nos quiere decir que la mayoria de los usuarios no manda mensajes.
# Considero que en esta comparacion si hay una inclinacion un poco mas notable, los usuarios que mas mandan mensajes son los del plan surf.
# Por otro lado, notablemente el plan surf es el que tiene mayor uso de datos por mes. 
# Asimismo, los usuarios que tienen el plan surf, su limite de datos es de 15gb y la mayoria de usuarios se pasa. Mientras que para los usuarios del plan ultimate, el limite es de 30gb y solo unos pocos usuarios superan su limite de consumo.** 

# ### Internet

# In[370]:


# Compara el uso promedio de datos por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

avg_internet = df_full.groupby(by = ['plan', 'month'])['gb_used_rounded'].mean()
avg_internet = avg_internet.reset_index()

plt.figure(figsize=(12,5))
sns.barplot(data = avg_internet, x = 'month', y = 'gb_used_rounded', hue = 'plan')
plt.title('Uso promedio de datos por mes y plan')
plt.xlabel('Mes')
plt.ylabel('Uso promedio [Gb]')
plt.legend(title = 'Plan')
plt.tight_layout()
plt.show()


# In[371]:


# Compara el número de Gb mensuales que necesitan los usuarios de cada plan. Traza un histograma.
sns.histplot(data = df_full, x = 'gb_used_rounded',bins = 20, hue = 'plan', multiple = 'dodge')
plt.title('Distribucion del uso mensual de Gb por plan')
plt.xlabel('Gb al mes')
plt.ylabel('Numero de usuarios')
plt.tight_layout()
plt.show()


# In[372]:


# Calcula la media y la varianza del uso mensual de datos.
med_var_datos = df_full.groupby(by = ['plan','month'])['gb_used_rounded'].agg(['mean','var'])
med_var_datos.plot(kind='bar', subplots = True, layout=(2,1),figsize=(10,6), sharex=True)
plt.suptitle("Media y Varianza de Gb mensuales por plan y mes")
plt.ylabel('Gigabytes')
plt.tight_layout()
plt.show()


# In[373]:


# Traza un diagrama de caja para visualizar la distribución del uso mensual de datos
monthly_gbs = df_full.groupby(by = ['user_id','month','plan'])['gb_used_rounded'].sum().reset_index()
sns.boxplot(data=monthly_gbs, x='plan', y='gb_used_rounded')
plt.title('Distribución mensual de Gb por plan')
plt.xlabel('Plan')
plt.ylabel('Gb al mes')
plt.tight_layout()
plt.show()


# **A diferencia del analisis que hicimos a la duracion de las llamadas y que casi no variaban, aqui si hay difencia de uso, ya que los usuarios que tienen el plan Surf, al menos el 50% excede su limite que es de 15gb por mes, a diferencia de los usuarios del plan ultimate donde casi nadie supera su limite mensual de gb.**

# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Excelente, muy bien con el análisis de internet, también hay un consumo similar entre planes.
# 
# </div>

# ## Ingreso

# [Del mismo modo que has estudiado el comportamiento de los usuarios, describe estadísticamente los ingresos de los planes.]

# In[374]:


#Calcula el monto mensual que debera pagar el cliente incluyendo las tarifas por pasar el limite de su plan. (si aplica) 
df_incomes = df_full.groupby(['user_id','month','plan'])['total_revenue'].sum().reset_index()
print(df_incomes.head(10))


# In[375]:


# Calcula la media y la varianza del ingreso mensual por plan.
med_var_incomes = df_full.groupby(by = ['plan','month'])['total_revenue'].agg(['mean','var'])
med_var_incomes.plot(kind='bar', subplots = True, layout=(2,1),figsize=(10,6), sharex=True)
plt.suptitle("Media y Varianza de ingresos mensuales por plan")
plt.tight_layout()
plt.show()


# In[376]:


sns.boxplot(data=df_full, x='plan', y='total_revenue')
plt.title('Distribución de ingresos mensuales por plan')
plt.xlabel('Plan')
plt.ylabel('Ingresos [$]')
plt.tight_layout()
plt.show()


# **El plan ultimate tiene los ingresos mas estables, ya que su varianza es muy baja, sus datos son muy homogeneos. Aunque los usuarios del plan surf tienden a exceder sus tarifas de datos mensuales, no terminan pagando mas en comparacion a los usuarios que pagan por el plan ultimate. 
# Podriamos decir que en todo el año el promedio de ingresos generados por el plan ultimate es mayor al del plan surf, y mucho mas estable.**

# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho. Vemos que los planes se diferencian en el ingreso, a pesar de que el consumo de sus usuarios es muy similar. Esto ocurre porque la estructura de costos de cada plan define intervalos de consumo diferentes, para surf los usuarios tienden a salirse de esos rangos pero los de ultimate no
# 
# </div>

# ## Prueba las hipótesis estadísticas

# [Prueba la hipótesis de que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.]

# In[377]:


surf_incomes = df_full[df_full['plan']=='surf']['total_revenue']
ultimate_incomes =df_full[df_full['plan']=='ultimate']['total_revenue']

print(surf_incomes.head(10))
print(ultimate_incomes.head(10))


# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]
# 
# **Hipótesis nula (H0): No hay diferencia significativa entre los ingresos promedio del plan Surf y el plan Ultimate.**
# 
# **Hipótesis alternativa (H1): Hay una diferencia significativa entre los ingresos promedio de ambos planes.**
# 
# **Prueba estadistica t de student ya que hay 2 grupos independientes, estamos comparando medias y la variable ingresos es numerica continua, asumimos alfa = 0.05 ya que se le da este valor comunmente**

# In[378]:


# Prueba las hipótesis
surf_income = df_full[df_full['plan'] == 'surf']['total_revenue']
surf_income_clean = surf_income.dropna()
ultimate_income = df_full[df_full['plan'] == 'ultimate']['total_revenue']
ultimate_income_clean = ultimate_income.dropna()


# In[379]:


from scipy.stats import ttest_ind

# Ejecutamos la prueba t de Student
t_stat, p_value = ttest_ind(surf_income_clean, ultimate_income_clean, equal_var=False)

print(f'Estadístico t: {t_stat}')
print(f'Valor p: {p_value}')


# **como valor p < alpha, Se rechaza la hipótesis nula. Hay evidencia estadistica que puede afirmar que los ingresos difieren significativamente entre los dos planes.**

# <div class="alert alert-block alert-danger">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# La conclusión es incorrecta, revisa con atención el valor-p vs el alfa.
# 
# </div>

# [Prueba la hipótesis de que el ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.]

# In[380]:


df_full = df_full.merge(df_users[['user_id', 'city']], on='user_id', how='left')
df_full['region'] = np.where(df_full['city'] == 'New York-Newark-Jersey City, NY-NJ-PA MSA', 'NY-NJ', 'Other')


ny_nj_revenue = df_full[df_full['region'] == 'NY-NJ']['total_revenue'].dropna()
other_revenue = df_full[df_full['region'] == 'Other']['total_revenue'].dropna()



# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]
# 
# **Hipótesis nula (H0): El ingreso promedio de los usuarios de NY-NJ es igual al ingreso promedio de los usuarios de otras regiones.**
# 
# **Hipótesis alternativa (H1): El ingreso promedio de los usuarios de NY-NJ es diferente al de los usuarios de otras regiones.**
# 
# **Prueba estadistica t de student ya que hay 2 grupos independientes, estamos comparando medias y la variable ingresos es numerica continua, asumimos alfa = 0.05 ya que se le da este valor comunmente**

# In[381]:


# Prueba las hipótesis
# Ejecutamos la prueba t de Student
t_stat, p_value = ttest_ind(ny_nj_revenue, other_revenue, equal_var=False)

print(f'Estadístico t: {t_stat}')
print(f'Valor p: {p_value}')



# **como valor p < alpha, rechazamos la hipotesis nula. Los ingresos promedio de NY-NJ son estadísticamente diferentes a los de otras regiones.**

# <div class="alert alert-block alert-success">
# <b>Comentario de Revisor</b> <a class="tocSkip"></a>
# 
# Muy bien, correcto el uso del test.
# 
# </div>

# ## Conclusión general
# 
# [En esta sección final, enumera tus conclusiones importantes. Asegúrate de que estas abarquen todas las decisiones (suposiciones) importantes que adoptaste y que determinaron la forma elegida para procesar y analizar los datos.]

# **Durante este proyecto se analizaron los datos de uso de servicios por parte de los usuarios de la empresa de telecomunicaciones Megaline, con el objetivo de comparar el desempeño financiero de los planes Ultimate y Surf**
# 
# **Para el procesamiento de datos se agregaron y redondeador los datos de llamadas, mensajes y trafico de internet mensualmente por usuario. Fusione los distintos series para crear un solo dataframe (df_full) y poder hacer todos los analisis que  requerian para posteriormente poder hacer el calculo matematico y obtener el pago mensual del usuario incluyendo recargos por superar su limite mensual.**
# 
# **Posteriormente hicimos analisis estadisticos donde nos dimos cuenta que la duración de llamadas por mes en el plan Ultimate mostró una duración promedio más alta y una distribución más estable. En los mensajes llamo la atencion que la moda fuera 0, indicando que la mayoría de los usuarios no los usa, aunque los del plan Surf tienden a enviar más mensajes en promedio. En cuanto al uso de datos, el plan Surf mostró un consumo más alto y frecuente de datos que exceden el límite de 15 GB, mientras que en el plan Ultimate, con un límite de 30 GB, la mayoría de los usuarios se mantuvo dentro del rango.**
# 
# **Consecuentemente, en el analis de ingresos nos pidieron una comparacion entre los ingresos promedio y la varianza mensual por plan. El plan Ultimate generó ingresos más altos y estables, con muy poca variabilidad entre meses. Por otro lado, el plan Surf generó ingresos más bajos y con mayor variabilidad, principalmente debido a cargos por excedentes de uso.**
# 
# **Como ultimo las pruebas de hipotesis, en la Comparacion entre planes Surf y Ultimate realizamos una prueba t de student sobre los ingresos mensuales y obtuvimos como resultado el Rechazo de la hipotesis nula, concluyendo que existe una diferencia significativa en los ingresos promedio entre ambos planes, y para cerrar, en la Comparacion entre regiones (NY-NJ vs. otras) se categorizaron las ciudades para formar dos regiones, dando como resultado el Rechazo de la hipotesis nula, ya que los ingresos promedio de NY-NJ son estadísticamente diferentes a los de otras regiones.**

# In[ ]:




