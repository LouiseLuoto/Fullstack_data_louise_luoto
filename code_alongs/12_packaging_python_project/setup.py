from setuptools import setup
from setuptools import find_packages

print(find_packages(exclude=["test*", "explorations"]))

setup(
    name = "travel_planner",
    version = "0.0.2",
    description = """
    This package is used for travel planning in public transport.
    It has backend, frontend and utils.
    """,
    author = "Louise Luoto",
    author_email = "email@gmail.com",
    install_packages = ["streamlit", "pandas", "requests", "folium", "pprint", "python-dotenv"
    ],
    packages = find_packages(exclude=["test*", "explorations"]),
    entry_points = {"console_scripts": ["dashboard = utils.run_dashboard:run_dashboard"]},
)