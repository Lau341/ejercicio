import pandas as pd     
df = pd.read_csv('StudentsPerformance.csv')  
print (df['gender'])  

#ATRIBUTOS  
# .dtypes (tipo de datos de las columnas)  
# .shape (cantidad de filas y columnas)  
#FUNCIONES   
# .head() - muestra las primeras 5 filas    
# .tail() - muestra las ultimas 5 filas   
# .describe() - muestra estadisticas de las columnas numericas   
# .info() - muestra las filas vacias (Tipo de data de nada es: non-null)  
#ARREGLOs  
#['x'] - x=nombre de la columna   