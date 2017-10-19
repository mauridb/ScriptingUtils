import csv
import uuid
from datetime import datetime

learnt_thing = raw_input('1)Type what did you learnt..\n')
category_of_thing = raw_input('2)Type the category..\n')
subcategory_of_thing = raw_input('3)Type the specific subcategory..\n')
description_of_thing = raw_input('4)Type a short description..\n')
created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_thing_to_file_csv(learnt_thing, category_of_thing, subcategory_of_thing, description_of_thing, created_at):
	with open('knowledge_db.csv','ab') as csvfile:
		thing_id = str(uuid.uuid1())
		fieldnames = ['ID','COMMAND','CATEGORY','SUBCATEGORY','DESCRIPTION','LEARN_DATE']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'ID':thing_id, 'COMMAND': learnt_thing, 'CATEGORY':category_of_thing, 'SUBCATEGORY':subcategory_of_thing, 'DESCRIPTION':description_of_thing, 'LEARN_DATE':created_at})




add_thing_to_file_csv(learnt_thing,category_of_thing,subcategory_of_thing,description_of_thing,created_at)
