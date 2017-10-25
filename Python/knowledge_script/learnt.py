import csv
import uuid
from datetime import datetime

# STATIC VARIABLES
LIST_COMMANDS = []


def list_of_things():
    with open('knowledge_db.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            LIST_COMMANDS.append(row['COMMAND'])


def add_thing_to_file_csv(learnt_thing):
    if learnt_thing not in LIST_COMMANDS:
        category_of_thing = raw_input('2)Type the category..\n')
        subcategory_of_thing = raw_input('3)Type the specific subcategory..\n')
        description_of_thing = raw_input('4)Type a short description..\n')
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        print "COMMAND ALREADY EXIST.."
        return
    with open('knowledge_db.csv', 'ab') as csvfile:
        thing_id = str(uuid.uuid1())
        fieldnames = ['ID', 'COMMAND', 'CATEGORY', 'SUBCATEGORY', 'DESCRIPTION', 'LEARN_DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'ID': thing_id, 'COMMAND': learnt_thing, 'CATEGORY': category_of_thing.upper(),
                         'SUBCATEGORY': subcategory_of_thing, 'DESCRIPTION': description_of_thing,
                         'LEARN_DATE': created_at})

# Application
list_of_things() # create list of exist commands

learnt_thing = raw_input('1)Type what did you learnt..\n')

add_thing_to_file_csv(learnt_thing)
