#dont forget to add pyinstaller to path
rm -rf build/
rm -rf dist/
pyinstaller --onefile --windowed --icon "./app.ico"  "./CardioRiskCalc.py"