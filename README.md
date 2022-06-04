## First time

Donwload the chrome driver based on your OS in the root of the script.

Create and activate virtual environment:

```bash
python3 -m venv venv
. venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create text files (required):

Files wl.txt and done.txt are required. wl.txt contains all the wallets and done.txt are the wallets that has been processed.

```bash
touch wl.txt
touch done.txt
```

## Run every time

```bash
. venv/bin/activate
python run.py
```
