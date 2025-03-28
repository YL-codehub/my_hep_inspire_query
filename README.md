# Search Hep Inspire with your saved queries of interest
HEP INSPIRE doesn't have a feature to save your queries of interest. This is a simple script for me to save my queries in a text file and search them with a single click.
## Fill search_query.txt
Create a 'search_query.txt' file to add your query of interest. You can jump lines for clarity.
See [HEP INSPIRE's help page](https://help.inspirehep.net/knowledge-base/inspire-paper-search/) for the search syntax or our example file.

## Run the script
### Using the python script
No need to install any package, just run the following command:
```
python main.py
```

### Using a .exe file generated from the python script
Install pyinstaller,
```
pip install pyinstaller
```
and run the following command to create the executable file:
```
pyinstaller --onefile --distpath ./ --name search_inspire --icon=logo_inspire.ico main.py
```
to get a single (clickable) executable file named search_inspire.exe in the current directory. The HEP inspire logo will appear when creating a shortcut, e.g. on your taskbar. After building the .exe, you can still edit the search_query.txt file and run the executable file to get the results.