To generate icons file use ```pyside6-rcc``` tool. This needs to be run every time you change/add an icon - they are copied into the optput file as string.

```
pyside6-rcc <qrc file> -o <output file>
```

for example (running from main directory)

```
pyside6-rcc icons/icons.qrc -o icons/generated/icons.py
```