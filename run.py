import os
import webbrowser
from backend.app import app

if __name__ == "__main__":
    print("Iniciando o Sistema de Gerenciamento da Clínica Veterinária PetCare...")
    print("Abrindo o navegador automaticamente...")
    
    # Abre o navegador automaticamente na página inicial
    webbrowser.open('http://127.0.0.1:5000')
    
    # Inicia o servidor Flask
    app.run(debug=False)