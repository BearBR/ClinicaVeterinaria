#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import webbrowser
import time
import threading
from backend.app import app

if __name__ == "__main__":
    print("=" * 50)
    print("  Clinica Veterinaria Unimar")
    print("=" * 50)
    print()
    print("Servidor iniciando...")
    print("Vai abrir em: http://127.0.0.1:5000")
    print("Aperta CTRL+C pra parar")
    print()
    
    # abre navegador em 2 segundos
    def abrir():
        time.sleep(2)
        webbrowser.open('http://127.0.0.1:5000')
    
    threading.Thread(target=abrir, daemon=True).start()
    
    # roda o servidor
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False,
        threaded=True,
        use_reloader=False
    )