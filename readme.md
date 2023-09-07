# Setup
After cloning the repo, before running the app you need to install requirements using following command
```
pip install -r requirements.txt
```
# Running the app
There are two modes for this app

## command line mode
In order to run the app in command line mode you should first set up config file either manually or using command line tools:

- set up broker with following:
```
python main.py -sb <host: string> <port: int>
```
or equivalent
```
python main.py --set-broker <host: string> <port: int>
```
for example
```
python main.py -sb mybroker.com 4444
```
---
- set up topics with following:
```
python main.py -at <topic name: string> <data format: string> <interval in seconds: float>
```
or equivalent
```
python main.py --add-topic <topic name: string> <data format: string> <interval in seconds: float>
```
for example
```
python main.py -at "my/topic" '{"data": {"x": <%randi%> }}' 1.5
```

To modify topic, simply override it with new values.

---
<b>Data format</b> is a string containg formula for a message. Assume we want to revieve messages in following format
```json
{
    "data": {
        "x": <some int>,
        "y": <some float>,
    }
}
```
To achieve this, we can use placeholders for int32, uint32 and float in out data_format. The placeholders are
- ```<%randi%>``` for random int32
- ```<%randu%>``` for random uint32
- ```<%randf%>``` for random float in [0; 1) range
  
Our <b>Data format</b> would then be
```json
{ "data": { "x": "<%randi%>", "y": "<%randf%>" } }
```
---
After setting up the broker and topics you'd like to use, you would simply run
```
python main.py -nogui
```
or equivalent
```
python main.py --no-gui
```

If you want to print logs to the console (in addition to the ```logs.txt``` file), you can add ```--verbose``` or ```-v``` to the end of the command.


### Manual setup of config file
You can always create ```config.json``` file yourself if you think writing it with the command line tool is too tedious - simply follow the format below
```json
{
    "broker": { 
        "host": "localhost",
        "port": 1883
    },
    "topics": {
        "topic1": {
            "data_format": "<%randi%>",
            "interval": 1
        },
        "test/topic2": {
            "data_format": "{ 'x': '<%randu%>' }",
            "interval": 1.5
        }
    }
}
```
> result - app publishes random value on 'topic 1' every second

## GUI mode
To run the app in GUI mode, you can simply run
```
python main.py
```
without any additional arguments. This should launch a QT application that is very simple to navigate.
Down below are some screenshots of the app.

<b>[INSERT IMGS HERE]</b>

# TLDR
- You are running the main.py file
- Available args
    - `--no-gui` / `-nogui` - doesn't launch GUI
    - `--verbose` / `-v` - prints logs to console (in addition to `logs.txt` file)
    - `--add-topic` / `-at` `<topic name> <data format> <interval>` - adds topic to config
    - `--set-broker` / `-sb` `<hostname> <port>` - sets broker (default is localhost:1883)
- GUI mode is pretty self explanatory - you simply launch the app without any additional args
