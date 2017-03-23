# Matrix

## What it is?
This python project allows simulate a Matrix style screen. You could configure characters used or even the speed of
the effects.

## How it works?
You must download the project first

```
git clone https://github.com/luigonsec/matrix.git
```

Once the project is downloaded. You cd into the project folder and execute this to install dependencies

```
pip install -r requirements.txt
```

And you execute it:

```
python matrix.py
```

## configure
A couple of parameters can be configured.

| Command | Description | Examples |
| --- | --- | --- |
| -ch | It allows configure the set of characters to show. | python matrix.py -ch aeiou |
| -s | It allows to configure the speed: 1.2 or 3 | python matrix.py -s 3 |
| -b | Only 1 or 0 will be shown | python matrix.py -b |
