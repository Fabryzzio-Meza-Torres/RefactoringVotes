import csv

#Eliminacion de codigo duplicado
#Division de métodos y renombramiento de variables
def count_votes(file_path):
    results = process_votes(file_path)
    if results:  # Solo imprimir resultados si hay datos
        print_results(results)
        winner = define_winner(results)
        print(f"The winner is {winner[0]} with {winner[1]} votes")
    else:
        print("No votes were cast")

def process_votes(file_path):
    results = {}
    with open(file_path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)  # Skip header
        for row in reader:
            if len(row) >= 3:  # Verificar que la fila tenga todos los campos necesarios
                candidate = row[1]
                try:
                    votes = int(row[2])
                except ValueError:
                    votes = 0
                set_canditate(results, candidate, votes)
    return results

#Simplificacion de condicionales.
def set_canditate(results, candidate,votes):
    if candidate in results:
        results[candidate]+=votes
    else:
        results[candidate]=votes

#Extracción de métodos y renombramiento de funciones y variables
def print_results(results):
    for canditate, total_votes in results.items():
        print(f"{canditate}:{total_votes} votes")

#Extracción de métodos y renombramiento de funciones y variables
def define_winner(results):
    if not results:  # Si el diccionario está vacío
        return ("No candidates", 0)
    return max(results.items(), key=lambda item: item[1])



# Example usage
count_votes('votes.csv')
