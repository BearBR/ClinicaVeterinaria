while ($true) {
    try {
        # Navegar até a pasta do projeto
        cd "C:\Users\masco\OneDrive\Unimar\Projeto Integrador Ext 3\RA13119972-23"

        # Ativar ambiente virtual
        .\.venv\Scripts\Activate.ps1

        # Rodar o servidor Flask
        python -m flask --app backend.app run --no-reload
    }
    catch {
        Write-Host "Erro durante a execução do servidor: $_"
    }
    Write-Host "Servidor finalizado. Reiniciando em 5 segundos..."
    Start-Sleep -Seconds 5
}
