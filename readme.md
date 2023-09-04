# config format
```json
{
    broker: localhost,
    topics: {
        'topic 1': {
            data_format: '<%rand%>'
            interval: 1
        }
    }
}
```
## this should publish random value on 'topic 1' every second