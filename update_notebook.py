import json

# Load the notebook
with open('Notebook_01_Python_Basics.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Tasks to update with their new content
updates = {
    'Task 8.2': '''**Task 8.2: Pizza Party Cost**

You're ordering pizzas for a party. Create `price_per_pizza = 15` and `number_of_pizzas = 3`. Calculate:
- `total_cost = price_per_pizza * number_of_pizzas`
- `cost_per_person = total_cost / 3`

Print:
```
print("Total cost:", total_cost)
print("Cost per person:", cost_per_person)
```''',
    'Task 8.3': '''**Task 8.3: Battery Power Calculation**

Your phone battery is fully charged with 3 hours of usage remaining. Calculate:
- `battery_level = 3`
- How much 2 to the power of battery level: `power_result = 2 ** battery_level`
- Remaining battery percentage: `remainder = 100 % 15`

Print:
```
print("2 to the power of", battery_level, "=", power_result)
print("100 % 15 =", remainder)
```''',
    'Task 9.1': '''**Task 9.1: Compare Test Scores**

Compare two test scores:
- `midterm_score = 87`
- `final_score = 92`

Check:
- Is final score greater than midterm? `final_score > midterm_score`
- Is midterm lower than final? `midterm_score < final_score`
- Are they equal? `midterm_score == final_score`

Print:
```
print("Final > Midterm:", final_score > midterm_score)
print("Midterm < Final:", midterm_score < final_score)
print("Scores equal:", midterm_score == final_score)
```''',
    'Task 10.1': '''**Task 10.1: Check Driver License Eligibility**

To get a driver's license, you must be 16 AND have a permit. Check:
- `driver_age = 16`
- `has_permit = True`
- `can_get_license = (driver_age >= 16) and (has_permit == True)`

Print:
```
print("Can get license:", can_get_license)
print("Age requirement met:", driver_age >= 16)
print("Has permit:", has_permit)
```''',
    'Task 10.2': '''**Task 10.2: Check Free Shipping Eligibility**

You get free shipping if order is over $50 OR you have a coupon. Check:
- `order_total = 75`
- `has_coupon = True`
- `qualifies_for_free_shipping = (order_total >= 50) or (has_coupon == True)`

Print:
```
print("Qualifies for free shipping:", qualifies_for_free_shipping)
print("Order over $50:", order_total >= 50)
print("Has coupon:", has_coupon)
```''',
    'Task 10.3': '''**Task 10.3: Check Room Availability**

A meeting room is either reserved or available. Check availability using NOT:
- `room_reserved = True`
- `room_available = not room_reserved`

Print:
```
print("Room is reserved:", room_reserved)
print("Room is available:", room_available)
print("NOT True =", not True)
print("NOT False =", not False)
```''',
    'Task 11.1': '''**Task 11.1: Identify Library Book Data Types**

Create variables for a library book entry:
- `book_title = "Python Guide"`
- `total_pages = 350`
- `avg_rating = 4.5`
- `is_available = True`

Check each type:
```
print("Title type:", type(book_title))
print("Pages type:", type(total_pages))
print("Rating type:", type(avg_rating))
print("Available type:", type(is_available))
```''',
    'Task 12.1': '''**Task 12.1: Convert Zip Code to Number**

You have a zip code as a string. Convert it to an integer (Boston zip code: 02134):
- `zip_code_text = "02134"`
- `zip_code_number = int(zip_code_text)`

Print:
```
print("Before conversion:")
print("  Value:", zip_code_text)
print("  Type:", type(zip_code_text))
print("After conversion:")
print("  Value:", zip_code_number)
print("  Type:", type(zip_code_number))
```''',
    'Task 12.2': '''**Task 12.2: Convert Student Count to Text**

Your class has 28 students (an integer). Convert it to a string and use it in a sentence:
- `student_count = 28`
- `student_count_text = str(student_count)`
- `message = "There are " + student_count_text + " students in class."`

Print:
```
print("Count type:", type(student_count))
print("Text type:", type(student_count_text))
print(message)
```'''
}

# Find and update cells
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_text = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        for task_key, new_content in updates.items():
            if task_key in source_text:
                cell['source'] = new_content.split('\n')
                # Add newline markers for proper formatting
                cell['source'] = [line + '\n' if i < len(cell['source']) - 1 else line for i, line in enumerate(cell['source'])]
                break

# Save the notebook
with open('Notebook_01_Python_Basics.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Notebook updated successfully!')
