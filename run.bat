IF NOT EXIST venv (
py -3 -m venv venv
call venv/Scripts/activate.bat
pip3 install -r requirements.txt
) ELSE (
call venv/Scripts/activate.bat
)
