@echo off
title Sistema de Clínica Veterinária - Unimar
color 0A
cls

echo =========================================================
echo    SISTEMA DE GERENCIAMENTO - CLÍNICA VETERINÁRIA
echo                      UNIMAR
echo =========================================================
echo.
echo Inicializando o sistema...
echo.

cd /d "%~dp0"

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não encontrado!
    echo Por favor, instale o Python 3.x
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Verifica se as dependências estão instaladas
echo Verificando dependências...
pip show Flask >nul 2>&1
if errorlevel 1 (
    echo Instalando dependências necessárias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependências
        pause
        exit /b 1
    )
)

echo Dependências OK!
echo.

REM Loop infinito para reiniciar o servidor automaticamente se cair
:LOOP
echo =========================================================
echo Iniciando servidor...
echo Acesse: http://127.0.0.1:5000
echo.
echo Para PARAR o sistema, feche esta janela ou pressione Ctrl+C
echo =========================================================
echo.

REM Abre o navegador automaticamente após 3 segundos
start "" cmd /c "timeout /t 3 /nobreak >nul && start http://127.0.0.1:5000"

REM Inicia o servidor
python INICIAR.py

REM Se o servidor parar, pergunta se quer reiniciar
echo.
echo [AVISO] O servidor foi encerrado!
echo.
choice /C SN /M "Deseja reiniciar o servidor? (S=Sim, N=Não)"
if errorlevel 2 goto FIM
if errorlevel 1 goto LOOP

:FIM
echo.
echo Sistema encerrado.
timeout /t 2
exit /b 0
