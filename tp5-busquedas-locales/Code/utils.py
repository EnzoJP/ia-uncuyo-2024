import csv

def guardar_resultados_csv(file,a, b, c, d, e,f,g):
    writer = csv.writer(file)
    writer.writerow([a,b,c,d,e,f,g])