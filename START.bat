@echo off
title Brewsko Bistro POS System
color 0A

:: Auto-navigate to the folder where this bat file is located
cd /d "%~dp0"

echo.
echo  ========================================
echo      BREWSKO BISTRO POS SYSTEM
echo  ========================================
echo.

:: Check if Django is installed
python -c "import django" 2>nul
if errorlevel 1 (
    echo  Installing Django... please wait...
    pip install django
    echo  Django installed!
    echo.
)

:: Run migrations silently
echo  Setting up database...
python manage.py makemigrations accounts panel cashier kitchen >nul 2>&1
python manage.py migrate >nul 2>&1

:: Create default users and menu items if not yet existing
echo  Checking accounts...
python manage.py shell -c "
from accounts.models import User
from panel.models import MenuItem, InventoryItem

users = [
    ('admin','admin123','admin'),
    ('cashier','cashier123','cashier'),
    ('kitchen','kitchen123','kitchen'),
]
for username, password, role in users:
    if not User.objects.filter(username=username).exists():
        u = User.objects.create_user(username=username, password=password)
        u.role = role
        u.is_staff = (role == 'admin')
        u.is_superuser = (role == 'admin')
        u.save()
        print(f'  Created: {username}')
" 2>nul

:: Open browser after 2 seconds
start /b cmd /c "timeout /t 2 >nul && start http://127.0.0.1:8000"

echo.
echo  ========================================
echo   System is RUNNING!
echo   Browser will open automatically...
echo.
echo   URL:     http://127.0.0.1:8000
echo   Admin:   admin / admin123
echo   Cashier: cashier / cashier123
echo   Kitchen: kitchen / kitchen123
echo.
echo   Press CTRL+C to STOP the system
echo  ========================================
echo.

python manage.py runserver

pause
