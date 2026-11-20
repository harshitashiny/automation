@echo off
cd /d "%~dp0"
set "PY=python"

echo Starting Fast Batch Solver to 400 problems...
"%PY%" batch_solver.py 400
pause

