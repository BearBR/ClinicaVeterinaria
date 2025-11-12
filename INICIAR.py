#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script para iniciar o servidor
import os
import webbrowser
import time
import threading
from backend.app import app

if __name__ == "__main__":
    print("=" * 60)
    print("  Sistema de Gerenciamento da Clínica Veterinária Unimar")
    print("=" * 60)
    print()
    print("[INFO] Iniciando servidor...")
    print("[INFO] Acesse: http://127.0.0.1:5000")
    print("[INFO] Pressione CTRL+C para parar")
    print()
    print("DICA: Para versão mais estável, use: INICIAR_SERVIDOR.bat")
    print()
    
    # Abre o navegador após 2 segundos em thread separada
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://127.0.0.1:5000')
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Inicia o servidor Flask com configurações melhoradas
    try:
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=False,
            threaded=True,
            use_reloader=False
        )
    except KeyboardInterrupt:
        print("\n[INFO] Servidor encerrado pelo usuário")
    except Exception as e:
        print(f"\n[ERRO] Falha ao iniciar servidor: {e}")
        print("\nTENTE USAR: INICIAR_SERVIDOR.bat (mais estável)")