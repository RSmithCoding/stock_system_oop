# Stock Management System

A command-line stock manager for a small shop, written in Python using
object-oriented programming. You can sell products, take in deliveries, add
new products, and see reports of stock levels and value. It warns you when
stock gets low.

This is my first OOP project built from scratch: I designed the classes and
structure myself from a written brief.

## Features

- **Sell** products. A sale is refused if there isn't enough stock, and you
  get a warning when a product drops to its reorder level.
- **Receive** deliveries to top up stock.
- **Add** new products with a name, price, starting quantity and reorder level.
- **Report** every product's price, quantity, reorder level and stock value,
  plus the total value of all stock.
- **Reorder list** showing only the products at or below their reorder level.
- **Input checking.** Every prompt keeps asking until it gets a valid answer:
  no blank names, no words where numbers are needed, and no zero or negative
  amounts.

## Getting started

You need Python 3. No other packages are required.

```
python main.py
```

On Windows you may need to use `py main.py`.

## Example

```
Please enter one of the following (sell / receive / add / report / reorder / quit): sell
Please enter the name of the product to sell: notebooks
Please enter the quantity: 6
Order Processed
Warning Stock is Low

Please enter one of the following (sell / receive / add / report / reorder / quit): sell
Please enter the name of the product to sell: staplers
Please enter the quantity: 10
Not enough stock only 4 left

Please enter one of the following (sell / receive / add / report / reorder / quit): receive
Please enter the product name that has been received: staplers
Please enter the quantity: 20
20 x staplers have been added to stock

Please enter one of the following (sell / receive / add / report / reorder / quit): report

Name            Price     Quantity      Reorder Level   Stock Value
pens            £0.80     50            20            £40.00
notebooks       £2.50     9             10            £22.50
staplers        £6.00     24            5             £144.00

                                Total Stock Value:    £206.50
```

## Project structure

```
stock_system_oop/
├── main.py     # The menu loop and user input
└── stock.py    # The Product and Stock classes
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

**`Stock`** (in `stock.py`) looks after all the products, stored in a
dictionary keyed by product name:

| Method | What it does |
|---|---|
| `check_product(name)` | Returns the product, or `None` if it isn't stocked |
| `add_new_product(name, price, quantity, reorder)` | Creates and stores a new product |
| `report()` | Prints every product and the total stock value |
| `reorder_level()` | Prints only the products that need reordering |

**`main.py`** handles the user. It shows the menu, uses three helper functions
(`get_name`, `get_price` and `get_value`) to collect valid input, and calls
the right methods. It contains no stock logic of its own.

`report()` and `reorder_level()` don't do any calculating themselves. They ask
each product for its value or whether it's low. Because of that, the rules
for a product live in one place, the `Product` class.

## What I learned

- Designing classes from a brief: picking out the "things" (classes), what
  they store (attributes) and what they do (methods)
- The difference between a class (the blueprint) and an object (an actual
  product), and when to use `self`
- Storing objects in a dictionary and looking them up by name
- Methods that return `True`/`False` so other code can make decisions
- Validating input with `while` loops and `try`/`except`
- Writing reusable helper functions instead of repeating the same loop

## Planned features

- [ ] **Sales history:** a log of every sale and delivery, with a `history` command to view it
- [ ] **Saving and loading:** write the stock to a file when quitting and read it back
      on start-up, in a separate `storage.py` module
