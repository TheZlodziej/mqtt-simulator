# config format
```json
{
    "broker": { 
        "host": "localhost",
        "port": 1883
    },
    "topics": {
        "topic 1": {
            "data_format": "<%rand%>",
            "interval": 1
        }
    }
}
```
## this should publish random value on 'topic 1' every second