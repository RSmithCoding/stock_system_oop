# Stock Management System

A command-line stock manager for a small shop, written in Python using
object-oriented programming. You can sell products, take in deliveries, add
new products, see reports of stock levels and value, and look back through a
history of every sale and delivery. Everything is saved automatically, so the
stock and history are remembered between runs.

This is my first OOP project built from scratch. I designed the classes and
structure myself from a written brief, then extended it with a history log
and file storage.

## Features

- **Sell** products. A sale is refused if there isn't enough stock, and you
  get a warning when a product drops to its reorder level.
- **Receive** deliveries to top up stock.
- **Add** new products with a name, price, starting quantity and reorder level.
- **Report** every product's price, quantity, reorder level and stock value,
  plus the total value of all stock.
- **Reorder list** showing only the products at or below their reorder level.
- **Sales history:** every sale and delivery is logged with the date and time.
  You can view all history, or only sales or only deliveries, with a total.
- **Automatic saving and loading:** stock and history are saved to JSON files
  after every change and loaded again on start-up. If a file is missing or
  corrupt, the program starts with the default stock instead of crashing.
- **Input checking.** Every prompt keeps asking until it gets a valid answer:
  no blank names, no words where numbers are needed, and no zero or negative
  amounts.

## Getting started

You need Python 3. No other packages are required.

```
python main.py
```

On Windows you may need to use `py main.py`.

The first time you run it, the program creates `stock_backup.json` with the
default stock. `history_backup.json` is created after the first sale or
delivery.

## Example

```
Please enter one of the following (sell / receive / add / report / reorder / history / quit): sell
Please enter the name of the product to sell: pens
Please enter the quantity: 10
Order Processed and added to history

Please enter one of the following (sell / receive / add / report / reorder / history / quit): receive
Please enter the product name that has been received: staplers
Please enter the quantity: 20
20 x staplers have been added to stock and saved in history

Please enter one of the following (sell / receive / add / report / reorder / history / quit): history
Please choose which history report or enter for 'all' (sale / delivery):

26/11/2026 17:03 sale       pens                 £ 0.80   10  £ 8.00
26/11/2026 17:03 delivery   staplers             £ 6.00   20  £ 120.00

                                                 Grand Total: £ 128.00
```

## Project structure

```
stock_system_oop/
├── main.py               # The menu loop and user input
├── stock.py              # The Product and Stock classes
├── history.py            # The HistoryItem and History classes
├── storage.py            # Saving to and loading from JSON files
├── stock_backup.json     # Saved stock (created automatically)
└── history_backup.json   # Saved history (created automatically)
```

### How it's designed

The program is split so that each part has one job.

**`Product`** (in `stock.py`) is one item the shop sells. It stores its own
name, price, quantity and reorder level, and answers questions about itself:

| Method | What it does |
|---|---|
| `add_stock(amount)` | Increases the quantity |
| `down_stock(amount)` | Decreases the quantity |
| `check_stock(amount)` | Returns `True` if there's enough for a sale |
| `level_is_low()` | Returns `True` if at or below the reorder level |
| `stock_value()` | Returns price × quantity |
| `to_dict()` | Returns the product's details as a dictionary for saving |

**`Stock`** (in `stock.py`) looks after all the products, stored in a
dictionary keyed by product name:

| Method | What it does |
|---|---|
| `check_product(name)` | Returns the product, or `None` if it isn't stocked |
| `add_new_product(name, price, quantity, reorder)` | Creates and stores a new product |
| `report()` | Prints every product and the total stock value |
| `reorder_level()` | Prints only the products that need reordering |
| `stock_to_dict()` | Returns every product as a list of dictionaries for saving |

**`HistoryItem`** (in `history.py`) is one sale or delivery. It stamps
itself with the current date and time, unless it's given a saved date when
loading from a file:

| Method | What it does |
|---|---|
| `line_total()` | Returns price × quantity for this entry |
| `__str__()` | Returns the entry as one formatted line of text |
| `to_dict()` | Returns the entry as a dictionary, with the date as text |

**`History`** (in `history.py`) keeps every entry in a list, in the order
they happened:

| Method | What it does |
|---|---|
| `add_history(status, name, price, quantity, date=None)` | Records a new entry |
| `print_history(status="all")` | Prints all entries, or only sales or deliveries |
| `grand_total(status="all")` | Returns the total value of the matching entries |
| `history_to_dict()` | Returns every entry as a list of dictionaries for saving |

**`storage.py`** handles the files. It has `save_stock` and `load_stock`, plus
`save_history` and `load_history`. The classes turn themselves into
dictionaries, so `storage.py` only has to read and write JSON.

**`main.py`** handles the user. It shows the menu, uses helper functions
(`get_name`, `get_price`, `get_value` and `get_status`) to collect valid
input, calls the right methods, and saves after every change. It contains no
stock logic of its own.

`report()`, `reorder_level()` and `grand_total()` don't do any calculating
themselves. They ask each product or history entry for its value. Because of
that, the rules for an item live in one place, its own class.

## What I learned

- Designing classes from a brief: picking out the "things" (classes), what
  they store (attributes) and what they do (methods)
- The difference between a class (the blueprint) and an object (an actual
  product), and when to use `self`
- Storing objects in a dictionary or a list and looping over them
- Methods that return `True`/`False` so other code can make decisions
- Validating input with `while` loops and `try`/`except`
- Writing reusable helper functions instead of repeating the same loop
- Using `__str__` to control how an object is shown when printed
- Default parameters (like `status="all"` and `date=None`), and why
  parameters with defaults have to come last
- Saving and loading data with JSON, and converting objects to dictionaries
  with `to_dict()` so they can be stored
- Converting dates to text and back with `isoformat()` and `fromisoformat()`
- Handling missing or corrupt files with `FileNotFoundError` and
  `json.JSONDecodeError`

## Possible future features

- [ ] Record the cost price paid to suppliers, so deliveries are valued at cost
- [ ] Remove a product from stock
- [ ] Search or filter the history by product or date
- [ ] Unit tests for the classes
