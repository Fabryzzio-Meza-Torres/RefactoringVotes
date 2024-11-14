import csv

#Eliminacion de codigo duplicado
#Division de métodos y renombramiento de variables
def count_votes(file_path):
    results=process_votes(file_path)
    print_results(results)
    winner= define_winner(results)
    print(f"The winner is {winner[0]} with {winner[1]} votes")

#Extracción de métodos y renombramiento de funciones y variables
def process_votes(file_path):
    results={}

    with open(file_path, newline='') as csv_file:
        reader=csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            city=row[0]
            candidate=row[1]
            try:
                votes=int(row[2])
            except:
                votes=0
           
            set_canditate(results, candidate,votes)

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
    return max(results.items(), key=lambda item:item[1])




# Example usage
count_votes('votes.csv')
