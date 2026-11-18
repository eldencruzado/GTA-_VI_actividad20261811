from flask import Flask, render_template

app = Flask(__name__)

# Lista de al menos 4 elementos con 3 datos cada uno (nombre, categoria, descripcion)
elementos_gta6 = [
    {
        "nombre": "Lucia Caminos",
        "categoria": "Protagonista",
        "descripcion": "La primera protagonista femenina principal de la era HD de la saga, exreclusa que busca un nuevo comienzo en Leonida junto a su pareja."
    },
    {
        "nombre": "Jason Duval",
        "categoria": "Protagonista",
        "descripcion": "Compañero sentimental y criminal de Lucia; juntos protagonizan una historia de asaltos y supervivencia al estilo Bonnie y Clyde."
    },
    {
        "nombre": "Vice City",
        "categoria": "Ubicación Principal",
        "descripcion": "Metrópoli bañada en neón inspirada en Miami, llena de playas, vida nocturna, clubes exclusivos y crimen organizado moderno."
    },
    {
        "nombre": "Estado de Leonida",
        "categoria": "Mundo Abierto",
        "descripcion": "El mapa más grande y detallado de Rockstar Games, inspirado en Florida, que incluye cayos tropicales, pantanos con caimanes y zonas industriales."
    }
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/personajes")
def personajes():
    return render_template("personajes.html", lista_elementos=elementos_gta6)

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

if __name__ == "__main__":
    app.run(debug=True)