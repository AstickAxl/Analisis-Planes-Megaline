# 📱 Análisis de Tarifas de Prepago - Megaline

Este proyecto analiza el comportamiento de 500 clientes de la empresa de telecomunicaciones Megaline, con el objetivo de determinar cuál de sus dos planes de prepago (Surf o Ultimate) genera mayores ingresos. El análisis incluye limpieza, enriquecimiento de datos, visualizaciones, estadística descriptiva e inferencial.

## 📌 Objetivo

Evaluar el rendimiento financiero de los planes **Surf** y **Ultimate**, y proponer recomendaciones basadas en el análisis de datos reales de consumo (llamadas, mensajes, internet) por usuario.

## 🧰 Herramientas utilizadas

- Python (Pandas, NumPy, SciPy, Seaborn, Matplotlib)
- Jupyter Notebook
- Pruebas de hipótesis (t-test)
- Estadística descriptiva e inferencial

## 📊 Contenido del análisis

- Limpieza y transformación de cinco datasets (usuarios, llamadas, mensajes, internet, planes)
- Cálculo de ingresos mensuales por usuario
- Visualización del comportamiento de consumo por plan
- Comparación de ingresos entre planes
- Análisis geográfico de ingresos (NY-NJ vs otras regiones)
- Pruebas estadísticas para validar diferencias de ingresos

## 📎 Archivos

- `Data/` : Datasets utilizados en este proyecto
- `Proyecto_Analisis_Tarifas_Prepago_Megaline.py`: Código completo del proyecto
- `requirements.txt`: Librerías necesarias para ejecutar el proyecto

## 📈 Resultados clave

- El plan **Ultimate** genera mayores ingresos promedio y es más estable en comparación con **Surf**, a pesar de un consumo de recursos relativamente similar.
- Usuarios del plan **Surf** tienden a exceder su límite de datos, generando ingresos variables por sobrecargos.
- Existen diferencias estadísticamente significativas entre los ingresos por plan y entre regiones.

## 🧠 Conclusión

Recomendar una revisión estratégica del plan **Surf**, ya que muchos usuarios superan sus límites sin que eso se traduzca en mayores ingresos sostenibles. El plan **Ultimate**, aunque más costoso, ofrece ingresos más estables y predecibles para la empresa.

---

👨‍💻 Desarrollado por Axel López  
📅 Proyecto de portafolio - Bootcamp de Ciencia de Datos  
🔗 [LinkedIn](https://www.linkedin.com/in/axel-lópez-linares/)
