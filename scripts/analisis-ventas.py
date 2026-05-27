
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

        if fecha == "2024-01-01" or fecha == "2024-02-01":
            print(f"DEBUG: Detectada línea {fecha} con ventas {ventas}")

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
