# Prerequisites #
- **python3**, preferably **python3.11** or higher
- **Linux/MacOS** or **Windows** as an Operating System

# HOW TO RUN THE GAME #
## 1. By running Scripts  ##
### For Linux Operating System ###
- Give executing permission to the script **run.sh** for the current user.
```bash
chmod u+x run.sh
```
- Run the script **run.sh**
### For Windows Operating System
- Run the script **run.bat**
## 2. Manual Project Setup
1. Clone the repo to your local drive
2. Create a python virtual environment using  the command 
```bash
    python3 -m venv g_env.
```
3. Activate the virtual environment by using the command
```bash
    source g_env/bin/activate 
```

  -  or if you are in **windows** just type the command 

```bash 
./g_env/Scripts/activate
```
4. Then install the dependencies using the command 
```bash
    pip install -r requirements.txt"
```
5. Start the game using the command
```bash
python main.py
```