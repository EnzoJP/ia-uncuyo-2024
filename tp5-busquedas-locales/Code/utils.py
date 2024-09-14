import csv

def guardar_resultados_csv(file,number_escenario, algoritmo, result, explored, finish_time):
    writer = csv.writer(file)
    writer.writerow([number_escenario, algoritmo, result, explored, finish_time])