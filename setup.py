from setuptools import setup, find_packages


setup(
    name="edu_pad",
    version="0.0.1",
    author="Carlos Isaza",
    author_email="carlosisaza21@hotmail.com",
    description="Proyecto realizado en clase Mayo 2025",
    py_modules=["actividad1","actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
    ]
)