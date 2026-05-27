
#Variables necesarias para guardar los datos
total = 0
cont = 0
min_ventas = 0
max_ventas = 0
fecha_min = ""
fecha_max = ""
ventas_por_mes = {}

with open ("datos/sales_sample_2024.csv", "r") as f:
    encabezado = f.readline()


    min_ventas = None
    max_ventas = None

    #Este for cumple la funcion de recorrer linea por linea e ir extrayendo los valores de dicha linea
    for lineas in f:
        partes = lineas.strip().split(",")
        fecha = partes[1]
        mes = fecha[5:7] #Tomo solamente el mes
        ventas = int(partes[2])

        #Sumamos el valor de las ventas a la variable llamada "total" y sumamos 1 al contador
        total += ventas
        cont += 1

        #maximo y minimo
        if max_ventas is None or ventas > max_ventas:
            max_ventas = ventas
            fecha_max = fecha

        if min_ventas is None or ventas < min_ventas:
            min_ventas = ventas
            fecha_min = fecha
        
        # convertir número de mes a nombre
        nombres_meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        mes = nombres_meses[int(fecha[5:7])]
        
        if mes not in ventas_por_mes:
            #Si el mes no esta en el diccionario lo agrego
            ventas_por_mes[mes] = 0
        ventas_por_mes[mes] += ventas


#Guardamos los resultados en un archivo de texto llamado "resultados.txt" en la carpeta resultados del repositorio
with open ("resultados/resultados.txt", "w") as f:
    f.write(f"Total de ventas: {total}\n")
    f.write(f"Promedio de ventas: {total / cont}\n")
    f.write(f"Minimo de ventas: {min_ventas} en la fecha {fecha_min}\n")
    f.write(f"Maximo de ventas: {max_ventas} en la fecha {fecha_max}\n")
    f.write("\n") #salto de linea para que no este toda la informacion junta
    f.write("Ventas por mes:\n")
    for mes, total_por_mes in ventas_por_mes.items():
        f.write(f"{mes}: {total_por_mes}\n")
#Parte de la generacion del grafico

#creamos el archivo en el cual se va a guardar
with open ("resultados/grafico_ventas.txt", "w") as fg:
  fg.write("==========================================================\n")
  fg.write("    DIAGRAMA DE BARRAS - EVOLUCION DE VENTAS MENSUALES    \n")
  fg.write("==========================================================\n")
  fg.write("\n")

  #Encontrar el mes con mayor facturacion con un for y comparando con condicionales
  max_facturacion_mes = 0
  mes_max_facturacion = ""
  long_max_barras = 40
  for i in ventas_por_mes:
    if ventas_por_mes[i] > max_facturacion_mes:
      max_facturacion_mes = ventas_por_mes[i]
      mes_max_facturacion = i
    
  #Generamos el diagrama de barras
  for mes, total_mes in sorted(ventas_por_mes.items()):
     if mes == "Enero":
        num_mes = 1
     elif mes == "Febrero":
        num_mes = 2
     elif mes == "Marzo":
        num_mes = 3
     elif mes == "Abril":
        num_mes = 4
     elif mes == "Mayo":
        num_mes = 5
     elif mes == "Junio":
        num_mes = 6
     elif mes == "Julio":
        num_mes = 7
     elif mes == "Agosto":
        num_mes = 8
     elif mes == "Septiembre":
        num_mes = 9
     elif mes == "Octubre":
        num_mes = 10
     elif mes == "Noviembre":
        num_mes = 11
     elif mes == "Diciembre":
        num_mes = 12
     nombre_mes = nombres_meses[num_mes]

     #Regla de 3 simple para calcular el tamaño de la barra
     proporcion = total_mes / max_facturacion_mes
     tamaño_barra = int(proporcion * long_max_barras)
     barra_visual = "#" * tamaño_barra

     #Mostramos y escribimos las barras en el archivo
     fg.write(f"{nombre_mes}: {barra_visual}\n")
     fg.write(f"Ventas: {total_mes}\n")
     fg.write("\n")
    
  fg.write("====================================================================\n")
  fg.write("  NOTA: Se calcula el grafico en base al mes con mayor facturacion  \n")
  fg.write("====================================================================\n")

