# Playstation-Purchases
This python script totals your PSN purchases in two ways; it provides a number of total purchases made, and the total amount of money spent on those purchases.

#### What is the point of this? Can't I add up the spending myself?
Sure you could! But if your account is as old as mine (15 years old as of 2024) it likely has hundreds, if not thousands of transactions. For old accounts, then, it's not feasible to manually count up each and every transaction - hence why I wrote this code! I've now shared it for anyone else curious for their total spending on PSN.

Future work on this project: Migrating to a user-friendly web-page, removing the need for a downloaded script and terminal/command prompt usage.

## What it looks like when you run this program:
<img width="1022" alt="Screenshot 2024-01-16 at 21 15 45" src="https://github.com/Natino64/Playstation-Purchases/assets/30630493/b3545935-8aa0-421a-aaa9-6afe45ab0f0f">

### Video Demo:
https://youtu.be/1nFyGXUz6tk

## How to run:

Firstly, download the playstation_purchases.py file.

Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

#### For Mac:

**1. Open Terminal:**
   - Press `Cmd + Space` to open Spotlight Search.
   - Type "Terminal" and press `Enter` to open the Terminal.

**2. Navigate to the Script's Directory:**
   - Use the `cd` command to change the directory to where your Python script is located. For example:
     ```bash
     cd path/to/your/script
     ```

**3. Run the Script:**
   - Once you're in the script's directory, run the script using the `python` command:
     ```bash
     python playstation_purchases.py
     ```


#### For Windows:

**1. Open Command Prompt:**
   - Press `Win + R` to open the Run dialog.
   - Type "cmd" and press `Enter` to open the Command Prompt.

**2. Navigate to the Script's Directory:**
   - Use the `cd` command to change the directory to where your Python script is located. For example:
     ```cmd
     cd path\to\your\script
     ```

**3. Run the Script:**
   - Once you're in the script's directory, run the script using the `python` command:
     ```cmd
     playstation_purchases.py
     ```
### Troubleshooting:

Is python not recognised by your command line? Here's how to fix the issue:

#### For Mac:

1. **Find Python Executable Path:**
   - Open Terminal.
   - Type the following command to find the Python executable path:
     ```bash
     which python
     ```
   This will display the path to the Python executable.

2. **Add Python to PATH:**
   - Open or create your shell configuration file. For example, for the default Bash shell, you can use:
     ```bash
     nano ~/.bash_profile
     ```
   - Add the following line at the end of the file:
     ```bash
     export PATH="/path/to/python/bin:$PATH"
     ```
     Replace "/path/to/python/bin" with the actual path you obtained from the first step.

   - Save the file and exit. If you used `nano`, press `Ctrl + X`, then `Y` to confirm changes, and `Enter` to exit.

   - Restart Terminal or run the following command to apply the changes:
     ```bash
     source ~/.bash_profile
     ```

3. **Verify:**
   - Type `python` again in the terminal. It should now recognize the command.

#### For Windows:

1. **Find Python Executable Path:**
   - Open Command Prompt.
   - Type the following command to find the Python executable path:
     ```cmd
     where python
     ```
   This will display the path to the Python executable.

2. **Add Python to PATH:**
   - Right-click on "This PC" or "Computer" on your desktop or in File Explorer.
   - Select "Properties" > "Advanced system settings" > "Environment Variables."
   - In the "System variables" section, find and select the "Path" variable, then click "Edit."

   - Click "New" and add the path to the Python executable (without the actual executable filename) that you obtained from the first step.

   - Click "OK" to close each dialog.

   - Restart Command Prompt.

3. **Verify:**
   - Type `python` again in the Command Prompt. It should now recognize the command.

After following these steps, your system should recognize the `python` command in the terminal or Command Prompt.
