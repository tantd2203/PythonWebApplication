# Project Name
Ecommerce With Pyhon

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    git clone https://github.com/tantd2203/PythonWebApplication.git

2. Navigate to the project directory:

      ```bash
    cd ecommerce
    ```


3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### Database Configuration

1. Open `settings.py` in the `your_project` directory.

2. Locate the `DATABASES` section.

3. Configure the database settings, including `ENGINE`, `NAME`, `USER`, `PASSWORD`, etc.

   Example for SQLite:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / "db.sqlite3",
       }
   }
  ```
Example for PostgreSQL:
   ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }  
    ```

### Static Files and Media Configuration
1 Open settings.py in the your_project directory.
2 Configure the STATIC_URL and MEDIA_URL settings:

    ```python
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    ```
###Usage
    ``` bash
  python manage.py runserver
    ```