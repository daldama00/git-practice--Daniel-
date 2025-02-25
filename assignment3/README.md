Purpose: This script generates a rotating globe using Plotly and geopandas,while also displaying the countries geometries.

Steps Followed
1. Created a new project in PyCharm and intialized a Git repository.
2. Created and activated a virtual environment using Pycharm.
3. Installed all of the necessary libraries('geopandas, pandas, ploty, etc).
4. Generated a "all_requirements.txt" using "pip freeze".
5. Used 'pipdeptree' and "pipreqs" to make a cleaner "requirements.txt".
6. Removed all installed packages to simulate a clean environment.
7. Then Reinstalled only the necessary dependencies
8. Made sure that the script worked
9. Made and saved the dependency tree using "pipdeptree".

Output : [dependency_tree.txt](dependency_tree.txt)

Observations : After cleaning the "requirements.txt" the script worked good and only the essential packages were installed.
Some dependencies, like "requests", were found to be unnecessary for the script's functionality. 