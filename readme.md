## GTK 3 PROJECT

This project is a simple GTK3 that aims to display the weather and currency 

## USAGE

> **NOTE**</br>
>
> - You need API KEYS that can be gotten from https://openweathermap.org and https://exchangeratesapi.io


- Clone this repo

  ```bash
  git clone https://github.com/rammyblog/gtk3-project
  ```

- Change directory to project directory

  ```bash
  cd gtk3-project
  ```

- Replace the API_KEYS

- Replace line 8 in main.py with the API key gotten from https://openweathermap.org

- Replace line 11 in main.py with API key gotten from https://exchangeratesapi.io

- Create a virtual environment

```bash
virtualenv venv
```

- Activate virtual environment

```bash
source venv/bin/activate
```

- Install the dependencies 

```bash
pip install -r requirements.txt
```

- Start the app
```bash
python main.py
```