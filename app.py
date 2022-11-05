"""
Aaron Whitaker
11/1/2022
CRN: 10235
CIS 226: Advanced Python Programming
Aprox Time: 5 hours
"""
import textual

from flask import Flask, render_template
# from textual.app import App, ComposeResult
# from textual.containers import Container, Horizontal, Vertical
# from textual.widgets import Static, Button, Input, DataTable


# import sqlite3

# conn = sqlite3.connect(':memory:')
# c = conn.cursor()
app = Flask(__name__)

# name = ""
# quantity = 0

# INSERT: object = Button("Insert", id="insert")
# SELECT: object = Button("Select", id="select")
# CREATE: object = Button("Create", id="create")
# ERROR: object = Static("error", id="error")
# WARNING: object = Static("warning", id="warning")
# CONFIRM: object = Static("confirm", id="confirm")
# OUTPUT: object = Static("No Vegetables Here!")
# VEGETABLE: object = Input(placeholder="Enter vegetable", id="vegetable")
# QUANTITY: object = Input(placeholder="Enter quantity", id="quantity")


@app.route('/')
def home():
    # points flask to the home page
    return render_template(
        'home.html',
        title='home',
        )


# def setup() -> bool:
#     # builds database
#     try: 
#         c.execute("CREATE TABLE IF NOT EXISTS vegetable (name text, quantity integer)")
#         conn.commit()
#         if CONFIRM.display == True:
#             CONFIRM.display = False
#         CONFIRM.update(renderable="Database created!")
#         return True
#     except:
#         return False

# def insert_vegetable( name, quantity):
#     # inserts a vegetable and quantity into the database
#     try:
#         c.execute("INSERT INTO vegetable VALUES (?, ?)", [name, quantity])
#         OUTPUT.update(renderable=f"\nAdded {name} as a new vegetable.")
#         return True
#     except:
#         ERROR.update(renderable=f"\nError inserting {name} into database.")
#         return False

# def select_vegetable(name, quantity) -> bool:
#     # finds vegetable in database or notify user if not found
#     c.execute("SELECT quantity, name FROM vegetable WHERE name=?", [name, ])
#     row = c.fetchone() 
#     if name == "":
#         name = "Vegetable"
#     if row is None:
#         ERROR.update(renderable=f"{name} not found!")
#         return False
#     else:
#         OUTPUT.update(renderable=f"{row[1]} found! {row[0]} in stock.")
#         return True

# def db_check() -> bool:
#     # checks if database has been created
#     try:
#         c.execute("SELECT * FROM vegetable")
#         return True
#     except:
#         return False

# def display_error():
#     # changes visibility of messages
#     if ERROR.display == False:
#         if CONFIRM.display == True:
#             CONFIRM.display = False
#         if WARNING.display == True:
#             WARNING.display = False
#         ERROR.display = True

# def display_warning():
#     # changes visibility of messages
#     if WARNING.display == False:
#         if CONFIRM.display == True:
#             CONFIRM.display = False
#         if ERROR.display == True:
#             ERROR.display = False
#         WARNING.display = True

# def display_confirm():
#     # changes visibility of messages
#     if CONFIRM.display == False:
#         if ERROR.display == True:
#             ERROR.display = False
#         if WARNING.display == True:
#             WARNING.display = False
#         CONFIRM.display = True

# class TuiGrid(App):
#     CSS_PATH = "main.css"

#     def compose(self) -> ComposeResult:
#         # builds and lays out the contents of the app
#         yield Container(
#                 Horizontal(
#                     Static("Vegetable Stand"),
#                     id="header",
#                 ),
#                 Container(
#                     Container(
#                         INSERT,
#                         SELECT,
#                         CREATE,
#                         id="top-left",
#                     ),
#                     Container(
#                         VEGETABLE,
#                         QUANTITY,
#                         Container(
#                             ERROR,
#                             WARNING,
#                             CONFIRM,
#                             id="middle-pane",
#                         ),
#                         id="top-right",
#                     ),
#                     Vertical(OUTPUT, DataTable(), id="output"),
#                     id="app-grid",
#                 ),
#                 Horizontal(
#                     Static("@ 2022 Aaron Whitaker"),
#                     id="footer",
#                 ),
#                 )
                
#     def on_mount(self):
#         # actions made when app is run
#         ERROR.display = False
#         WARNING.display = False
#         CONFIRM.display = False
#         table = self.query_one(DataTable)
#         table.add_columns('Vegetables', 'Quantity')
#         DataTable.display=False

#     def on_button_pressed(self, event: Button.Pressed) -> None:
#         # actions made when a button is pressed
#         """buttons and their function calls etc"""

#         OUTPUT.update(renderable="No Vegetables Here!")

#         button_id = event.button.id

#         if button_id == "create":
#             if setup() == True:
#                 display_confirm()
#             elif setup() == False:
#                 if ERROR.display == True:
#                     ERROR.display = False
#                 ERROR.update(renderable="ERROR\n\nNo Database Created!")
#                 display_error()
 
#         elif button_id == "insert":
#             if db_check() == True:
#                 # name = ""
#                 # quantity = 0
#                 try: 
#                     name = str(VEGETABLE.value)
#                     name != "" == True
#                     assert name
#                     CONFIRM.update(renderable=f"-{name}-")
#                     display_confirm()
#                 except:
#                     ERROR.update(renderable="----->  ERROR  <-----\n\nNo Vegetable Entered!")
#                     display_error()
#                     return
#                 try:
#                     quantity = int(QUANTITY.value)
#                 except:
#                     ERROR.update(renderable="------->  ERROR  <-------\n\nInvalid Quantity Entered!")
#                     display_error()
#                     return
#                 name = VEGETABLE.value
#                 quantity = QUANTITY.value
#                 if insert_vegetable(name, quantity) == True:
#                     CONFIRM.update(renderable=f"{quantity} {name} added to Vegetable Stand.")
#                     display_confirm()
#                 else:
#                     ERROR.update(renderable=f"----->  ERROR  <-----\n\n{name} not added to Vegetable Stand.")
#                     display_error()
#                     return
#             elif db_check() == False:
#                 ERROR.update(renderable="No Database Available!\nPlease create a database.")
#                 display_error()
#             VEGETABLE.value=""
#             QUANTITY.value=""

#         elif button_id == "select":
#             if db_check() == True:
#                 if VEGETABLE.value != "":
#                     name = VEGETABLE.value
#                 else:
#                     name = ""
#                 quantity = 0
#                 try:
#                     assert name   
#                 except:       
#                     WARNING.update(renderable="WARNING\n\nEnter a quantity.")
#                     display_warning()
#                 pad = len(name)
#                 CONFIRM.update(renderable=f"Looking for a {name}...")
#                 if select_vegetable(name, quantity) == True:
#                     display_confirm()
#                 else:
#                     display_error()
#             elif db_check() == False:
#                 if ERROR.display == True:
#                     ERROR.display = False
#                 ERROR.update(renderable="No Database Available!\nPlease create a database.")
#                 display_error()
#             VEGETABLE.value=""
#             QUANTITY.value=""

"""
Design: 
Develop: 
Test: 
Docs: 
"""