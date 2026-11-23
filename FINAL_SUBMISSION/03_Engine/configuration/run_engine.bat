@echo off
echo ========================================================
echo IncuBrix AEO, SEO & GEO Visibility Engine
echo Starting Streamlit Web Dashboard...
echo ========================================================
py -m streamlit run Engine\src\app.py || python -m streamlit run Engine\src\app.py || C:\Users\pc\AppData\Local\Programs\Python\Python314\python.exe -m streamlit run Engine\src\app.py
pause
