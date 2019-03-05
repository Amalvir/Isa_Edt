from cx_Freeze import setup, Executable

#On appelle setup

setup(
    name="Edt_PCS3",
    version="1",
    description="Programme donnant les colles et les particularités par semaine de l'edt PCS3",
    executables=[Executable("main.py")]
)
