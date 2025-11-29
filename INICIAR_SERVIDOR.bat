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

REM Detecta o lançador Python a usar (prefere 'py -3' no Windows)
echo Detectando Python...
py -3 --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set "PYCMD=py -3"
) else (
    python --version >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set "PYCMD=python"
    ) else (
        echo [ERRO] Python não encontrado!
        echo Por favor, instale o Python 3.x
        echo Download: https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

echo Usando: %PYCMD%

REM Garante que pip esteja disponível e instala dependências
echo Verificando e instalando dependências (pode demorar)...
%PYCMD% -m ensurepip --upgrade >nul 2>&1
%PYCMD% -m pip install --upgrade pip >nul 2>&1

REM tenta detectar se Flask ja esta instalado
%PYCMD% -m pip show Flask >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias do projeto...
    %PYCMD% -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias com "%PYCMD% -m pip install -r requirements.txt"
        echo Tente executar manualmente neste computador:
        echo %PYCMD% -m pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo Dependencias OK!
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

REM Inicia o servidor (ele ja abre o navegador automaticamente)
%PYCMD% INICIAR.py

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
