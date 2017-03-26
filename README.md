# Deckard
Discord Bot for Tristram La Magnifique

# Installation
Create a file named config.yml contaiing

```
bot:
  api_token: <discord api token>
server:
  address: <minecraft server address>

```
Execute:
```
source env/bin/activate
python main.py
```

# Build
We use docker to build and run the application
```
docker build -t app:tag .
```
