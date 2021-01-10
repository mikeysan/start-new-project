# Create a new project folder and setup git using a python script

This litte project was inspired by a [youtube video](https://youtu.be/7Y8Ppin12r4) I watched the other day about automating everyday things with python

## Assumptions or requirements

- You are running Windows 10 (at least)
- You have python 3 installed on your system
- You have [git](https://git-scm.com/download/win) installed
- You have the new [GitHub CLI](https://github.com/cli/cli) tool (gh) installed as well.
- You have gone through the gh login process and are able to create repositories using gh
- You have VS code installed. We use it at the end, but it is not needed


## How to use the script

- Using your favourite editor (vscode), edit the line 7 in the create_project.py script to match your file structure.

```py
# For Windows
chgDir = os.chdir('C:\\Users\\phil4\\Documents\\development')
# For Linux
chgDir = os.chdir('/home/sspade/Documents/development')
```

- Open a Powershell terminal and run: (change folder name to match whatever name you want)
```py
python .\create_project.py <folder name>
```
- This should create the new folder and setup git init
- It will also create the repository on GitHub for you
- If, like me, you are using ssh auth, you will be asked to enter your pass phrase.
- That's it.

###### This script was used to create this repo and its working folder
