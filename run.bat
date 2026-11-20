@echo off
cd /d "%~dp0"
set "PY=python"

echo Running LeetCode Daily Agent...
"%PY%" leetcode_agent.py
pause

