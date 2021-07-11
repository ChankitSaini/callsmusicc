# Install JS deps, build

```
cd server
npm i
npx tsc
```

# Install Python deps, run

```
pip install -Ur requirements.txt
python -m bot
```

# .env

## Required

`BOT_TOKEN` - Telegram bot token  
`STRING_SESSION` - [Telethon/GramJS string session](https://rojserbest.github.io/bssg)  
`API_ID` - Telegram app ID  
`API_HASH` - Telegram app hash

## Optional

`PORT` - Server port (default: 8080)  
`PREFIXES` - Command prefixes (default: / !)
