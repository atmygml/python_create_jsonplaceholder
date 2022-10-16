from faker import Faker
import string
import datetime
import random
import json
from decimal import *

fake = Faker()
fake002 = Faker(locale='la')

'''
Create JSON data with the following format :-
[
    {
        'Date' : xxx,
        'UserID' : xxx,
        'First Name' : xxx,
        'Last Name' : xxx,
        'Email' : xxx,
        'Company' : xxx,
        'Location' : {
            'Town' : xxx,
            'State' : xxx
        },
        'Item' : xxx,
        'Price' : xxx,
        'Comments' : xxx
    }
]
'''

keys = ['Date', 'UserID', 'First Name', 'Last Name', 'Email', 'Company', 'Location', 'Town', 'State', 'Item', 'Price', 'Comments']

popular_first_names_list = ['James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda', 'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Lisa', 'Daniel', 'Nancy', 'Matthew', 'Betty', 'Anthony', 'Margaret', 'Mark', 'Sandra', 'Donald', 'Ashley', 'Steven', 'Kimberly', 'Paul', 'Emily', 'Andrew', 'Donna', 'Joshua', 'Michelle', 'Kenneth', 'Carol', 'Kevin', 'Amanda', 'Brian', 'Dorothy', 'George', 'Melissa', 'Timothy', 'Deborah', 'Ronald', 'Stephanie', 'Edward', 'Rebecca', 'Jason', 'Sharon', 'Jeffrey', 'Laura', 'Ryan', 'Cynthia', 'Jacob', 'Kathleen', 'Gary', 'Amy', 'Nicholas', 'Angela', 'Eric', 'Shirley', 'Jonathan', 'Anna', 'Stephen', 'Brenda', 'Larry', 'Pamela', 'Justin', 'Emma', 'Scott', 'Nicole', 'Brandon', 'Helen', 'Benjamin', 'Samantha', 'Samuel', 'Katherine', 'Gregory', 'Christine', 'Alexander', 'Debra', 'Frank', 'Rachel', 'Patrick', 'Carolyn', 'Raymond', 'Janet', 'Jack', 'Catherine', 'Dennis', 'Maria', 'Jerry', 'Heather', 'Tyler', 'Diane', 'Aaron', 'Ruth', 'Jose', 'Julie', 'Adam', 'Olivia', 'Nathan', 'Joyce', 'Henry', 'Virginia', 'Douglas', 'Victoria', 'Zachary', 'Kelly', 'Peter', 'Lauren', 'Kyle', 'Christina', 'Ethan', 'Joan', 'Walter', 'Evelyn', 'Noah', 'Judith', 'Jeremy', 'Megan', 'Christian', 'Andrea', 'Keith', 'Cheryl', 'Roger', 'Hannah', 'Terry', 'Jacqueline', 'Gerald', 'Martha', 'Harold', 'Gloria', 'Sean', 'Teresa', 'Austin', 'Ann', 'Carl', 'Sara', 'Arthur', 'Madison', 'Lawrence', 'Frances', 'Dylan', 'Kathryn', 'Jesse', 'Janice', 'Jordan', 'Jean', 'Bryan', 'Abigail', 'Billy', 'Alice', 'Joe', 'Julia', 'Bruce', 'Judy', 'Gabriel', 'Sophia', 'Logan', 'Grace', 'Albert', 'Denise', 'Willie', 'Amber', 'Alan', 'Doris', 'Juan', 'Marilyn', 'Wayne', 'Danielle', 'Elijah', 'Beverly', 'Randy', 'Isabella', 'Roy', 'Theresa', 'Vincent', 'Diana', 'Ralph', 'Natalie', 'Eugene', 'Brittany', 'Russell', 'Charlotte', 'Bobby', 'Marie', 'Mason', 'Kayla', 'Philip', 'Alexis', 'Louis', 'Lori']
popular_last_names_list = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper', 'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson', 'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennet', 'Gray', 'Mendoza', 'Ruiz', 'Hughes', 'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez']

vowels = 'aeiou'

# no. of entries = 50
number_of_entries = 50

random_dates = []
FORMAT = '%d/%m/%Y'
random_ids = []
email_list = []
company_list = []
company_type = ['Pte Ltd', 'Co', 'Corp', 'Holdings', 'Ltd']
town_list = []
state_list = []
item_list = []
price_list = []
comment_list = []

# generate 50 random dates from 01/2020 to present and put in a list and arrange in chronological order
for _ in range(number_of_entries):
    start_date = datetime.date(year=2020, month=1, day=1)
    random_date = fake.date_between(start_date=start_date, end_date='now').strftime(FORMAT)
    random_dates.append(random_date)

# sort the random dates

# create a list of sorted datetime objects
# sorted_dates = sorted([datetime.datetime.strptime(d, FORMAT) for d in random_dates])

# create a list of sorted dates as strings
sorted_dates = sorted(random_dates, key=lambda d: datetime.datetime.strptime(d, FORMAT))

# print(sorted_dates)

# create 50 random IDs from 101 to 700
for _ in range(number_of_entries):
    random_id = random.randint(101, 700)
    random_ids.append(str(random_id))

random.shuffle(random_ids)

# create a random list of 50 popular first names
random_first_names = random.sample(popular_first_names_list, number_of_entries)
random.shuffle(random_first_names)

# print(random_first_names)

# create a random list of 50 popular last names
random_last_names = random.sample(popular_last_names_list, number_of_entries)
random.shuffle(random_last_names)

# print(random_last_names)

# create the 50 emails in the email list
for i in range(number_of_entries):
    email = f'{str(random_first_names[i]).lower()}{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_lowercase)}{random.randint(11, 98)}@example.com'
    email_list.append(email)

# print(email_list)

# create random strings for 50 company names using faker lorem ipsum

fake002.seed_instance(10)
for _ in range(number_of_entries):
    company_name_001 = str(fake002.sentence(nb_words=3, variable_nb_words=True))[:-1].title()
    company_name_002 = f'{company_name_001} {random.choice(company_type)}'
    company_list.append(company_name_002)

random.shuffle(company_list)

# print(company_list)

# create random strings for 50 town names using faker lorem ipsum
fake002.seed_instance(11)
for _ in range(number_of_entries):
    town_name = f'{random.choice(string.ascii_uppercase)}{random.choice(vowels)}{str(fake002.word()).lower()}{str(fake002.city_suffix()).lower()}'
    if town_name in town_list:
        town_name = f'{random.choice(string.ascii_uppercase)}{random.choice(vowels)}{random.choice(string.ascii_lowercase)}{str(fake002.word()).lower()}{str(fake002.city_suffix()).lower()}'
    town_list.append(town_name)

random.shuffle(town_list)

# print(town_list)
# check for duplicate towns
# print(len(town_list) != len(set(town_list)))
# returns False means NO DUPLICATES

# create random 50 state names using faker
fake.seed_instance(1)
for _ in range(number_of_entries):
    state_name = str(fake.state()).title()
    state_list.append(state_name)

random.shuffle(state_list)

# print(state_list)

# create random list of 50 items using faker lorem ipsum
fake002.seed_instance(12)
for _ in range(number_of_entries):
    item_name = f'{random.choice(string.ascii_uppercase)}{random.choice(vowels)}{random.choice(string.ascii_lowercase)}{str(fake002.sentence(nb_words=2, variable_nb_words=True))[:-1].lower()}'
    item_list.append(item_name)

random.shuffle(item_list)

# (item_list)


# create random list of 50 item price list
for _ in range(number_of_entries):
    item_price_001 = random.randint(10, 200)
    item_price_002 = Decimal(item_price_001).quantize(Decimal('.01'), rounding=ROUND_DOWN)
    item_price_003 = str(item_price_002)
    price_list.append(item_price_003)

random.shuffle(price_list)

# print(price_list)


# create random list of 50 comments from faker lorem ipsum
fake002.seed_instance(13)
for _ in range(number_of_entries):
    comment_head = f'{random.choice(string.ascii_uppercase)}{random.choice(vowels)}{random.choice(string.ascii_lowercase)}{str(fake002.sentence(nb_words=1, variable_nb_words=False))[:-1].lower()}'
    comment = f'{comment_head}{str(fake002.paragraph(nb_sentences=2, variable_nb_sentences=False))[1:]}'
    comment_list.append(comment)

random.shuffle(comment_list)

# print(comment_list)

'''
Create JSON data with the following format :-
[
    {
        'Date' : xxx,
        'UserID' : xxx,
        'First Name' : xxx,
        'Last Name' : xxx,
        'Email' : xxx,
        'Company' : xxx,
        'Location' : {
            'Town' : xxx,
            'State' : xxx
        },
        'Item' : xxx,
        'Price' : xxx,
        'Comments' : xxx
    }
]
'''

# create JSON Data
json_list = []
json_element_dict = {}

for i in range(number_of_entries):
    json_element_dict = {}

    # update nested json - for the Location : Town, State
    inner_element_dict = {}
    inner_element_list = [{'Town': town_list[i]}, {'State': state_list[i]}]
    for inner_dicts in inner_element_list:
        inner_element_dict.update(inner_dicts)

    json_update_list = [{'Date': sorted_dates[i]},
                        {'UserID': random_ids[i]},
                        {'First Name': random_first_names[i]},
                        {'Last Name': random_last_names[i]},
                        {'Email': email_list[i]},
                        {'Company': company_list[i]},
                        {'Location': inner_element_dict},
                        {'Item': item_list[i]},
                        {'Price': price_list[i]},
                        {'Comments': comment_list[i]}
                        ]
    for dicts in json_update_list:
        json_element_dict.update(dicts)
    json_list.append(json_element_dict)

# print(json_list)
json_list_write = json.dumps(json_list, indent=4)

with open('json_placeholder.json', "w") as outputfile:
    outputfile.write(json_list_write)

