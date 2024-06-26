<h1> Password Generator </h1>

<h5> This project is a Password Generator web application that allows users to generate secure passwords. Users can customize their passwords by selecting various character types (alphabets, integers, symbols, spaces) and setting the desired password length. The application also provides a feature to check the strength of the generated password.</h5>

## Features
- Generate passwords with customizable options:
  - Include Alpha Upper (A-Z)
  - Include Alpha Lower (a-z)
  - Include Numbers (0-9)
  - Include Symbols (e.g., !, @, #, $)
  - Include Spaces
- Set the length of the password
- Check the strength of the generated password

## Technologies Used
- *Backend*: Python, Flask 
- *Frontend*: HTML, CSS, JavaScript

## Setup and Installation
1. Clone the repository to your local machine.
```bash
git clone https://github.com/jaikrix/passwd-gen-.git
```

2. Install packages required for the tool.
```bash
pip install -r requirements.txt
```

3. Create necessary directories for templates and static files.
   
4. Move index.html to the templates folder and styles.css to the static folder.
```bash
mv path/to/your/index.html templates/index.html
mv path/to/your/styles.css static/styles.css
```
 
5. Run the backend server.
```bash
python app.py
```

6. Open your browser and navigate.
```bash
http://localhost:5000
```

<h2>Contribution</h2>
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

