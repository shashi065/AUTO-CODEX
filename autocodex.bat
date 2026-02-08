@echo off
REM AUTO-CODEX CLI ENTRYPOINT

if "%1"=="" (
    echo Usage: autocodex generate
    exit /b 1
)

if "%1"=="generate" (
    py -3.11 -m codex_engine.generate
    exit /b 0
)

echo Unknown command: %1
