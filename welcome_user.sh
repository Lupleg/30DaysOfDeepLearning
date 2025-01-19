#!/bin/bash

# Prompt the user for their name
echo "Please enter your name:"
read user_name

# Use Python to print a welcome message with ASCII art
python3 - <<END
name = "$user_name"

# ASCII Art for a banner
ascii_art = '''
  __        __   _
  \ \      / /__| | ___ ___  _ __ ___   ___   | |_ ___
   \ \ /\ / / _ \ |/ __/ _ \| '_ \` _ \ / _ \ | __/ _ \
    \ V  V /  __/ | (_| (_) | | | | | |  __/  | || (_) |
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___ /
'''

# Enhanced welcome message
welcome_message = f"""
{ascii_art}

Welcome, {name}!

We're thrilled to have you here. Enjoy your time exploring the world of Python and shell scripting!

"""

print(welcome_message)
END

# 1. Save the script to a file, for example, `welcome_user.sh`.
# 2. Make the script executable by running:
#    ```sh
#    chmod +x welcome_user.sh
#    ```
# 3. Run the script:
#    ```sh
#    ./welcome_user.sh
#    ```
