pos is a flask app that prints receipts.

To run it, run:

```
FLASK_APP=pos.py python3 -m flask run
```

It'll listen on port 5000 and print everything that's posted
to it to an Epson POS printer, assuming it exists and is connected via USB.
