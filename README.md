# Movement Vector

## Instructions:

1. **Pipenv:**
   - Ensure you have Pipenv installed on your system.
   - If not, install it using:
     ```bash
     pip install pipenv
     ```

2. **Navigate to Project Folder:**
   - Open a terminal or command prompt.
   - Change directory to the project's root folder where the `Pipfile` is located.


3. **Activate Pipenv Shell:**
   - Run the following command to activate the Pipenv shell:
     ```bash
     pipenv shell
     ```

   This will activate the virtual environment, and your terminal prompt should change to indicate the virtual environment.


4. **Update Commands:**
   - Before running the project, ensure the `commands.txt` file in the 'src' folder contains the desired drone movement commands.
     - Open the file and add or modify commands as needed.
     ```bash
     nano src/commands.txt
     ```
     
5. **Run the Project:**
   - Once in the virtual environment, navigate to the 'src' folder:
     ```bash
     cd src
     ```

   - Execute the following command to run the project:
     ```bash
     python drone_controller.py
     ```

6. **Run Tests with Pytest:**
   - Execute the following command to run the tests:
     ```bash
     pytest
     ```

   Pytest will automatically discover and run all tests in the project.


6. **Review Output:**
   - After running the tests, review the console output to ensure all tests pass without any errors.

Feel free to reach out if you encounter any issues or have further questions.

Happy coding!
