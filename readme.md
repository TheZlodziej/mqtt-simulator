# Setup
After cloning the repo, before running the app you need to install requirements using following command
```
pip install -r requirements.txt
```
then, to start the app run
```
python main.py
```

## Arguments
You can run the app with several arguments described below:

| command       | shortened | arguments                                                             | example                                      | description                                         |
| ------------- | --------- | --------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| `--set-broker` | `-sb`      | host (string), port (int)                                                         | python main.py -sb localhost 1883            | sets current broker                                 |
| `--add-topic`  | `-at`      | topic name (string), data format (string), interval [seconds] (float) | python main.py -at "my/topic" "<%randi%>" 10 | adds topic to list                                  |
| `--no-gui`     | `-nogui`   | \-                                                                    | python main.py -nogui                        | launches app without gui                            |
| `--verbose`    | `-v`      | \-                                                                    | python main.py -v                            | prints logs to console in addition to logs.txt file |

## Data format
Data format is a string containg formula for a message. Additionally, data format functions can accept arguments. Here is table with each function and argument described

| function | accepted arguments                         | default                   | example data format                     | description                                                                                                                                          |
| -------- | ------------------------------------------ | ------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `randi`   | `min` (int), `max` (int)                       | min = -2^31, max = 2^31-1 | <%randi min=-10 max=10%>                | Sends random int from [min; max] range                                                                                                               |
| `randu`    | `min` (int), `max` (int)                       | min = 0, max = 2^32 - 1   | <%randu min=10 max=20%>                 | Sends random uint from [min; max] range                                                                                                              |
| `randf`    | `min` (float), `max` (float)                   | min = 0, max = 1          | <%randf min=-1 max=16.9%>               | Sends random float from [min; max) range                                                                                                             |
| `rands`    | `collection` (list of strings), `length` (int) | length = 10               | <%rands collection=["a","ab",'abc']%> | Sends random string from given collection or generates random string with given length. If both arguments are passed, it will prioritize collection. |
| `file`     | `src` (string), `separator` (string)           | separator = ","           | <%file src="test.txt" separator="\\n"%> | Sends data from file one by one                                                                                                                      |
| `time`    | -               | -       | <%time%>               | Sends current time (datetime.now().time()) 

Keep in mind that <b>you dont always have to pass in all the arguments</b>. If you skip any (for example max in ```randi```, it will use the default value).

Argument value cannot contain space characters unless it's a string or a list (starts with `'`, `"` or `[`). For example: 
- ```<%rands collection=["x", "y"]%>``` - OK (collection value uses `[` ... `]`)
- ```<%rands collection= ["x", "y"]%>``` - ERROR (space before opening square bracket)
- ```<%file src="hello world.txt"%>``` - OK (src value uses `"` ... `"`)
- ```<%randi max= 10%>``` - ERROR (space after parameter value)

### Example
Assume we want to revieve messages with following format

```json
{
    "data": {
        "x": <some int>,
        "y": <some float>,
    }
}
```

Our <b>Data format</b> would then be
```json
{ "data": { "x": "<%randi%>", "y": "<%randf%>" } }
```

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
            "interval": 1,
            "manual": false
        },
        "test/topic2": {
            "data_format": "{ 'x': '<%randu%>' }",
            "interval": 1.5,
            "manual": false
        }
    }
}
```
> result - app publishes random int value on 'topic1' every second and random uint value on 'test/topic2'

## Screenshots
<p align="center">
  <img src="./images/app.png">
  <br>
Main window
</p>

<p align="center">
  <img src="./images/add.png">
  <br>
Add topic window
</p>

<p align="center">
  <img src="./images/edit.png">
  <br>
Edit topic window
</p>

# Protobuf
To use protobuf messages please place compiled *.py in protofiles folder.
