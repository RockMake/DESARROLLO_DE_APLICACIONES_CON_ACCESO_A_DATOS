from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["peliculas_db"]
peliculas_collection = db["peliculas"]

# 1. contar cuantas películas hay por director
pipeline = [
    {
        "$group": {
            "_id": "$director",
            "total_peliculas": {"$sum": 1}
        }
    }
]
for result in peliculas_collection.aggregate(pipeline):
    print(f"Director: {result['_id']}, Total de películas: {result['total_peliculas']}")
    print("--------------------------------------------------")

# 2. buscar películas que contengan la palabra "The"
pipeline = [
    {
        "$match": {
            "titulo": {"$regex": "The", "$options": "i"}
        }
    }
]
for result in peliculas_collection.aggregate(pipeline):
    print(f"Película: {result['titulo']}, Director: {result['director']}, Año: {result['anio']}")
    print("--------------------------------------------------")
# 3. consultar las películas de Cristopher Nolan y ordenarlas por año descendente.
pipeline = [
    {
        "$match": {
            "director": "Christopher Nolan"
        }
    },
    {
        "$sort": {
            "año": -1
        }
    }
]
for result in peliculas_collection.aggregate(pipeline):
    print(f"Película: {result['titulo']}, Año: {result['anio']}, Director: {result['director']}")
    print("--------------------------------------------------")
