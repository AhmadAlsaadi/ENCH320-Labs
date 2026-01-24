#!/usr/bin/env python3
"""
Generate Lab 2 (Control Flow) and Lab 3 (Looping) notebooks with enhanced content,
comprehensive tasks, and Mermaid mindmaps.
"""

import json

def create_control_flow_notebook():
    """Create Lab 2: Control Flow Statements notebook."""
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "id": "lab2_title",
                "metadata": {},
                "source": [
                    "# Lab 2: Control Flow - Making Decisions\n",
                    "\n",
                    "Master decision-making with `if`, `if-else`, `if-elif-else`, and nested conditionals.\n",
                    "\n",
                    "## Learning Objectives\n",
                    "By the end of this lab, you will:\n",
                    "- Use `if` statements to execute code conditionally\n",
                    "- Create branching logic with `if-else` statements\n",
                    "- Handle multiple conditions with `if-elif-else` statements\n",
                    "- Build nested conditionals for complex decision trees\n",
                    "- Write clean, readable conditional code\n",
                    "- Solve real-world problems using control flow logic"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept1_intro",
                "metadata": {},
                "source": [
                    "## Concept 1: if Statements - Making Decisions\n",
                    "\n",
                    "An `if` statement allows your program to make decisions based on conditions.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "if condition:\n",
                    "    # Code executes if condition is True\n",
                    "```\n",
                    "\n",
                    "**How it works:**\n",
                    "1. The condition is evaluated (True or False)\n",
                    "2. If True, the indented code block executes\n",
                    "3. If False, the code block is skipped\n",
                    "\n",
                    "**Key Points:**\n",
                    "- Conditions evaluate to True or False\n",
                    "- Use comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`\n",
                    "- Indentation (4 spaces) is critical in Python\n",
                    "- The colon `:` ends the condition line"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept1_arabic",
                "metadata": {},
                "source": [
                    "<details>\n",
                    "<summary style=\"cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;\">🌍 Arabic Translation / الترجمة العربية</summary>\n",
                    "\n",
                    "<div dir=\"rtl\" style=\"text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;\">\n",
                    "\n",
                    "<link href=\"https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap\" rel=\"stylesheet\">\n",
                    "\n",
                    "### العربية: جملة if\n",
                    "\n",
                    "جملة `if` تسمح لبرنامجك باتخاذ قرارات بناءً على الشروط.\n",
                    "\n",
                    "**الصيغة:**\n",
                    "```python\n",
                    "if condition:\n",
                    "    # يتم تنفيذ الكود إذا كان الشرط صحيحاً\n",
                    "```\n",
                    "\n",
                    "**كيفية العمل:**\n",
                    "1. يتم تقييم الشرط (صحيح أو خاطئ)\n",
                    "2. إذا كان صحيحاً، يتم تنفيذ كتلة الكود المسافة بها\n",
                    "3. إذا كان خاطئاً، يتم تخطي كتلة الكود\n",
                    "\n",
                    "</div>\n",
                    "</details>"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept1_example",
                "metadata": {},
                "source": [
                    "### Example 1.1: Age Verification\n",
                    "\n",
                    "Check if someone is old enough to vote:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept1_code1",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Age verification\n",
                    "age = 18\n",
                    "\n",
                    "if age >= 18:\n",
                    "    print(\"You are eligible to vote!\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept1_example2",
                "metadata": {},
                "source": [
                    "### Example 1.2: Weather Check\n",
                    "\n",
                    "Determine if it's cold:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept1_code2",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Temperature check\n",
                    "temperature = 5\n",
                    "\n",
                    "if temperature < 10:\n",
                    "    print(\"It's cold! Wear a jacket.\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept1_task",
                "metadata": {},
                "source": [
                    "### Task 1: Check Eligibility\n",
                    "\n",
                    "Write an `if` statement to check if a student's score is 80 or higher. If so, print \"Pass!\".\n",
                    "\n",
                    "Test with: score = 85\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept1_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Write an if statement\n",
                    "score = 85\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept2_intro",
                "metadata": {},
                "source": [
                    "## Concept 2: if-else Statements - Two Paths\n",
                    "\n",
                    "An `if-else` statement provides two execution paths: one when the condition is True, another when it's False.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "if condition:\n",
                    "    # Code if condition is True\n",
                    "else:\n",
                    "    # Code if condition is False\n",
                    "```\n",
                    "\n",
                    "**Key Points:**\n",
                    "- Exactly one code block executes\n",
                    "- Use `else` to handle the False case\n",
                    "- Perfect for binary (yes/no) decisions\n",
                    "- The program always takes one path"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept2_arabic",
                "metadata": {},
                "source": [
                    "<details>\n",
                    "<summary style=\"cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;\">🌍 Arabic Translation / الترجمة العربية</summary>\n",
                    "\n",
                    "<div dir=\"rtl\" style=\"text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;\">\n",
                    "\n",
                    "<link href=\"https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap\" rel=\"stylesheet\">\n",
                    "\n",
                    "### العربية: جملة if-else\n",
                    "\n",
                    "توفر جملة `if-else` طريقين للتنفيذ: أحدهما عندما يكون الشرط صحيحاً، والآخر عندما يكون خاطئاً.\n",
                    "\n",
                    "</div>\n",
                    "</details>"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept2_example",
                "metadata": {},
                "source": [
                    "### Example 2.1: Weather Advice\n",
                    "\n",
                    "Give clothing advice based on temperature:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept2_code1",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Weather advice\n",
                    "temperature = 5\n",
                    "\n",
                    "if temperature > 15:\n",
                    "    print(\"It's warm! Wear light clothing.\")\n",
                    "else:\n",
                    "    print(\"It's cold! Wear warm clothing.\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept2_task",
                "metadata": {},
                "source": [
                    "### Task 2: Discount Calculator\n",
                    "\n",
                    "Write an `if-else` statement to check if the purchase amount is 100 or more.\n",
                    "- If yes: print \"Discount applied!\"\n",
                    "- If no: print \"No discount.\"\n",
                    "\n",
                    "Test with: purchase_amount = 150\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept2_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Write an if-else statement\n",
                    "purchase_amount = 150\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept3_intro",
                "metadata": {},
                "source": [
                    "## Concept 3: if-elif-else Statements - Multiple Paths\n",
                    "\n",
                    "When you need to check multiple conditions, use `if-elif-else`. The program checks each condition in order and executes the first True block.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "if condition1:\n",
                    "    # Code if condition1 is True\n",
                    "elif condition2:\n",
                    "    # Code if condition2 is True\n",
                    "elif condition3:\n",
                    "    # Code if condition3 is True\n",
                    "else:\n",
                    "    # Code if all conditions are False\n",
                    "```\n",
                    "\n",
                    "**Key Points:**\n",
                    "- `elif` stands for \"else if\"\n",
                    "- Can have multiple `elif` blocks\n",
                    "- Only the first True condition executes\n",
                    "- `else` catches all remaining cases (optional)"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept3_arabic",
                "metadata": {},
                "source": [
                    "<details>\n",
                    "<summary style=\"cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;\">🌍 Arabic Translation / الترجمة العربية</summary>\n",
                    "\n",
                    "<div dir=\"rtl\" style=\"text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;\">\n",
                    "\n",
                    "<link href=\"https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap\" rel=\"stylesheet\">\n",
                    "\n",
                    "### العربية: جملة if-elif-else\n",
                    "\n",
                    "عندما تحتاج للتحقق من عدة شروط، استخدم `if-elif-else`. البرنامج يفحص كل شرط بالترتيب.\n",
                    "\n",
                    "</div>\n",
                    "</details>"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept3_example",
                "metadata": {},
                "source": [
                    "### Example 3: Grading System\n",
                    "\n",
                    "Assign a letter grade based on score:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept3_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Grading system\n",
                    "score = 85\n",
                    "\n",
                    "if score >= 90:\n",
                    "    print(\"Grade: A\")\n",
                    "elif score >= 80:\n",
                    "    print(\"Grade: B\")\n",
                    "elif score >= 70:\n",
                    "    print(\"Grade: C\")\n",
                    "else:\n",
                    "    print(\"Grade: F\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept3_task",
                "metadata": {},
                "source": [
                    "### Task 3: Ticket Price\n",
                    "\n",
                    "Calculate ticket price based on age:\n",
                    "- Age < 5: \"Free\"\n",
                    "- Age 5-12: \"$5\"\n",
                    "- Age 13-64: \"$15\"\n",
                    "- Age 65+: \"$10 (Senior)\"\n",
                    "\n",
                    "Test with: age = 25\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept3_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Determine ticket price\n",
                    "age = 25\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept4_intro",
                "metadata": {},
                "source": [
                    "## Concept 4: Nested Conditionals - Complex Decisions\n",
                    "\n",
                    "Nested conditionals are `if` statements inside other `if` statements. Use them for complex, hierarchical decisions.\n",
                    "\n",
                    "**Example:**\n",
                    "```python\n",
                    "if age >= 18:\n",
                    "    if has_license:\n",
                    "        print(\"You can drive!\")\n",
                    "```\n",
                    "\n",
                    "**Key Points:**\n",
                    "- Inner conditions only check if outer condition is True\n",
                    "- Use proper indentation (8 spaces for nested)\n",
                    "- Avoid deeply nested code (use `elif` or `and` operator instead)\n",
                    "- Can use with `and`, `or`, `not` operators"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept4_example",
                "metadata": {},
                "source": [
                    "### Example 4: Driver Eligibility\n",
                    "\n",
                    "Check multiple conditions:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept4_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Driver eligibility\n",
                    "age = 18\n",
                    "has_license = True\n",
                    "\n",
                    "if age >= 18:\n",
                    "    if has_license:\n",
                    "        print(\"You can drive!\")\n",
                    "    else:\n",
                    "        print(\"You need a license first.\")\n",
                    "else:\n",
                    "    print(\"You must be 18 to drive.\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_concept4_task",
                "metadata": {},
                "source": [
                    "### Task 4: Loan Eligibility\n",
                    "\n",
                    "Determine loan eligibility:\n",
                    "- Age >= 21 AND Credit Score >= 700 → \"Approved\"\n",
                    "- Age >= 21 BUT Credit Score < 700 → \"Need better credit\"\n",
                    "- Age < 21 → \"Too young\"\n",
                    "\n",
                    "Test with: age = 25, credit_score = 750\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_concept4_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Check loan eligibility\n",
                    "age = 25\n",
                    "credit_score = 750\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_mindmap",
                "metadata": {},
                "source": [
                    "## Control Flow Summary - Visual Mindmap\n",
                    "\n",
                    "```mermaid\n",
                    "mindmap\n",
                    "  root((Control Flow))\n",
                    "    if Statement\n",
                    "      Single condition\n",
                    "      True path only\n",
                    "      Skip if False\n",
                    "    if-else Statement\n",
                    "      Two paths\n",
                    "      True or False\n",
                    "      Binary decision\n",
                    "    if-elif-else Statement\n",
                    "      Multiple paths\n",
                    "      Many conditions\n",
                    "      First match wins\n",
                    "    Nested Conditionals\n",
                    "      Complex logic\n",
                    "      Conditions within conditions\n",
                    "      Use with caution\n",
                    "    Operators\n",
                    "      Comparison: ==, !=, <, >, <=, >=\n",
                    "      Logical: and, or, not\n",
                    "      Combine conditions\n",
                    "```"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_capstone_intro",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "## Capstone Project: Student Grade Report System\n",
                    "\n",
                    "**Objective:** Build a comprehensive grade analysis system using all control flow concepts.\n",
                    "\n",
                    "**Requirements:**\n",
                    "1. Accept a student name and three test scores\n",
                    "2. Calculate the average score\n",
                    "3. Assign a letter grade (A: 90+, B: 80-89, C: 70-79, F: <70)\n",
                    "4. Check if the student passed (70+) or failed (<70)\n",
                    "5. Provide feedback based on performance:\n",
                    "   - 90+: \"Excellent work!\"\n",
                    "   - 80-89: \"Good job!\"\n",
                    "   - 70-79: \"Passing, but study more.\"\n",
                    "   - <70: \"You need to retake this course.\"\n",
                    "6. Show a bonus message if student scored above 95\n",
                    "\n",
                    "**Output Example:**\n",
                    "```\n",
                    "Student Name: John\n",
                    "Average Score: 87.5\n",
                    "Letter Grade: B\n",
                    "Status: PASSED\n",
                    "Feedback: Good job!\n",
                    "```"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab2_capstone_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Capstone: Student Grade Report System\n",
                    "# TODO: Implement the grade report system\n",
                    "\n",
                    "# Get input\n",
                    "student_name = input(\"Enter student name: \")\n",
                    "score1 = float(input(\"Enter test 1 score: \"))\n",
                    "score2 = float(input(\"Enter test 2 score: \"))\n",
                    "score3 = float(input(\"Enter test 3 score: \"))\n",
                    "\n",
                    "# TODO: Calculate average\n",
                    "# TODO: Determine grade (A, B, C, F)\n",
                    "# TODO: Check pass/fail\n",
                    "# TODO: Provide feedback\n",
                    "# TODO: Display bonus message if applicable\n",
                    "\n",
                    "# Starter structure:\n",
                    "# average = (score1 + score2 + score3) / 3\n",
                    "# Print the results\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_resources",
                "metadata": {},
                "source": [
                    "## Key Takeaways\n",
                    "\n",
                    "✅ **if** - Execute code conditionally  \n",
                    "✅ **if-else** - Two decision paths  \n",
                    "✅ **if-elif-else** - Multiple conditions  \n",
                    "✅ **Nested conditionals** - Complex hierarchical logic  \n",
                    "✅ **Operators** - Compare and combine conditions  \n",
                    "✅ **Best Practice** - Keep conditions clear and simple\n",
                    "\n",
                    "## Resources\n",
                    "\n",
                    "- [Python Docs: if statements](https://docs.python.org/3/tutorial/controlflow.html)\n",
                    "- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)\n",
                    "- [W3Schools: Python if...else](https://www.w3schools.com/python/python_conditions.asp)"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab2_colab",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "## 📓 Run in Google Colab\n",
                    "\n",
                    "You can run this notebook directly in Google Colab by clicking the button below:\n",
                    "\n",
                    "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AhmadAlsaadi/ENCH320-Labs/blob/main/Notebook_02_Control_Flow.ipynb)"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return notebook

def create_looping_notebook():
    """Create Lab 3: Looping notebook."""
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "id": "lab3_title",
                "metadata": {},
                "source": [
                    "# Lab 3: Looping - Repeat Your Code\n",
                    "\n",
                    "Master iteration with `for` loops, `while` loops, and loop control statements.\n",
                    "\n",
                    "## Learning Objectives\n",
                    "By the end of this lab, you will:\n",
                    "- Use `for` loops to iterate over sequences\n",
                    "- Generate sequences with the `range()` function\n",
                    "- Loop through lists with `for` loops\n",
                    "- Use `while` loops for condition-based repetition\n",
                    "- Control loop flow with `break` and `continue` statements\n",
                    "- Write efficient, clean repetitive code\n",
                    "- Solve problems that require iteration"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept1_intro",
                "metadata": {},
                "source": [
                    "## Concept 1: for Loops - Counter-Based Repetition\n",
                    "\n",
                    "A `for` loop repeats a code block a specific number of times.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "for variable in sequence:\n",
                    "    # Code repeats for each item in sequence\n",
                    "```\n",
                    "\n",
                    "**How it works:**\n",
                    "1. The variable takes each value from the sequence\n",
                    "2. The code block executes for each value\n",
                    "3. After all values are processed, the loop ends\n",
                    "\n",
                    "**Key Points:**\n",
                    "- Best for a known number of iterations\n",
                    "- Variable automatically updates each iteration\n",
                    "- Sequence can be a list, string, or range\n",
                    "- Indentation is critical"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept1_arabic",
                "metadata": {},
                "source": [
                    "<details>\n",
                    "<summary style=\"cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;\">🌍 Arabic Translation / الترجمة العربية</summary>\n",
                    "\n",
                    "<div dir=\"rtl\" style=\"text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;\">\n",
                    "\n",
                    "<link href=\"https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap\" rel=\"stylesheet\">\n",
                    "\n",
                    "### العربية: حلقة for\n",
                    "\n",
                    "حلقة `for` تكرر كتلة كود عدداً معيناً من المرات.\n",
                    "\n",
                    "</div>\n",
                    "</details>"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept1_example",
                "metadata": {},
                "source": [
                    "### Example 1.1: Count to 5\n",
                    "\n",
                    "Simple counting loop:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept1_code1",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Count to 5\n",
                    "for i in range(1, 6):\n",
                    "    print(f\"Count: {i}\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept1_example2",
                "metadata": {},
                "source": [
                    "### Example 1.2: Multiplication Table\n",
                    "\n",
                    "Generate 5 times table:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept1_code2",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Multiplication table\n",
                    "num = 5\n",
                    "for i in range(1, 11):\n",
                    "    print(f\"{num} × {i} = {num * i}\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept1_task",
                "metadata": {},
                "source": [
                    "### Task 1: Print Even Numbers\n",
                    "\n",
                    "Write a `for` loop to print all even numbers from 2 to 20.\n",
                    "\n",
                    "**Expected Output:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept1_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Print even numbers from 2 to 20\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept2_intro",
                "metadata": {},
                "source": [
                    "## Concept 2: range() Function - Generating Sequences\n",
                    "\n",
                    "The `range()` function generates a sequence of numbers. It's commonly used with `for` loops.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "range(start, stop, step)  # All parameters except stop are optional\n",
                    "```\n",
                    "\n",
                    "**Parameters:**\n",
                    "- `start`: Beginning value (default: 0)\n",
                    "- `stop`: End value (exclusive, not included)\n",
                    "- `step`: Increment between values (default: 1)\n",
                    "\n",
                    "**Examples:**\n",
                    "- `range(5)` → 0, 1, 2, 3, 4\n",
                    "- `range(1, 5)` → 1, 2, 3, 4\n",
                    "- `range(0, 10, 2)` → 0, 2, 4, 6, 8"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept2_example",
                "metadata": {},
                "source": [
                    "### Example 2: Different range() Patterns\n",
                    "\n",
                    "Explore various range() uses:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept2_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Different range patterns\n",
                    "print(\"range(5):\")\n",
                    "for i in range(5):\n",
                    "    print(i, end=\" \")\n",
                    "\n",
                    "print(\"\\nrange(1, 6):\")\n",
                    "for i in range(1, 6):\n",
                    "    print(i, end=\" \")\n",
                    "\n",
                    "print(\"\\nrange(0, 10, 2):\")\n",
                    "for i in range(0, 10, 2):\n",
                    "    print(i, end=\" \")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept2_task",
                "metadata": {},
                "source": [
                    "### Task 2: Countdown\n",
                    "\n",
                    "Write a loop using `range()` to print a countdown from 10 to 1.\n",
                    "\n",
                    "**Hint:** Use negative step in range()\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept2_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Print countdown from 10 to 1\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept3_intro",
                "metadata": {},
                "source": [
                    "## Concept 3: for Loops with Lists - Iterating Collections\n",
                    "\n",
                    "One of the most common uses of `for` loops is iterating through lists.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "for item in list:\n",
                    "    # Code repeats for each item\n",
                    "```\n",
                    "\n",
                    "**Key Points:**\n",
                    "- The variable takes each element value\n",
                    "- Works with any sequence (list, string, tuple)\n",
                    "- No need to know list length in advance\n",
                    "- Clean and readable syntax"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept3_example",
                "metadata": {},
                "source": [
                    "### Example 3: Process a Shopping List\n",
                    "\n",
                    "Loop through and print items:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept3_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Shopping list\n",
                    "items = [\"milk\", \"bread\", \"eggs\", \"cheese\"]\n",
                    "\n",
                    "for item in items:\n",
                    "    print(f\"- {item}\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept3_task",
                "metadata": {},
                "source": [
                    "### Task 3: Calculate Total\n",
                    "\n",
                    "Given a list of numbers, calculate the total sum using a `for` loop.\n",
                    "\n",
                    "```python\n",
                    "numbers = [10, 20, 30, 40, 50]\n",
                    "```\n",
                    "\n",
                    "**Expected Output:** 150\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept3_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Calculate sum using for loop\n",
                    "numbers = [10, 20, 30, 40, 50]\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept4_intro",
                "metadata": {},
                "source": [
                    "## Concept 4: while Loops - Condition-Based Repetition\n",
                    "\n",
                    "A `while` loop repeats as long as a condition is True.\n",
                    "\n",
                    "**Syntax:**\n",
                    "```python\n",
                    "while condition:\n",
                    "    # Code repeats while condition is True\n",
                    "```\n",
                    "\n",
                    "**Key Points:**\n",
                    "- Best for unknown number of iterations\n",
                    "- Condition checked before each iteration\n",
                    "- Must eventually become False (avoid infinite loops)\n",
                    "- Variable must be updated inside the loop"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept4_example",
                "metadata": {},
                "source": [
                    "### Example 4: Countdown with while\n",
                    "\n",
                    "Count down from 5:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept4_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Countdown\n",
                    "count = 5\n",
                    "\n",
                    "while count > 0:\n",
                    "    print(f\"Countdown: {count}\")\n",
                    "    count -= 1\n",
                    "\n",
                    "print(\"Blastoff!\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept4_task",
                "metadata": {},
                "source": [
                    "### Task 4: Input Validation\n",
                    "\n",
                    "Use a `while` loop to ask for a number between 1 and 10.\n",
                    "Keep asking until valid input is received.\n",
                    "\n",
                    "**Hint:** Loop while number is not in valid range\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept4_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Input validation with while loop\n",
                    "# Keep asking for number between 1 and 10 until valid\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept5_intro",
                "metadata": {},
                "source": [
                    "## Concept 5: break and continue Statements - Loop Control\n",
                    "\n",
                    "Control loop flow with `break` and `continue` statements.\n",
                    "\n",
                    "**break Statement:**\n",
                    "- Exits the loop immediately\n",
                    "- Used when a condition is met\n",
                    "\n",
                    "**continue Statement:**\n",
                    "- Skips the rest of the current iteration\n",
                    "- Jumps to the next iteration\n",
                    "\n",
                    "**Key Points:**\n",
                    "- Use sparingly to keep code readable\n",
                    "- Helps handle special cases in loops\n",
                    "- Works with both `for` and `while` loops"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept5_example1",
                "metadata": {},
                "source": [
                    "### Example 5.1: break Statement\n",
                    "\n",
                    "Exit loop when condition is met:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept5_code1",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: break statement\n",
                    "for i in range(1, 11):\n",
                    "    if i == 5:\n",
                    "        print(\"Found 5! Stopping.\")\n",
                    "        break\n",
                    "    print(i)\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept5_example2",
                "metadata": {},
                "source": [
                    "### Example 5.2: continue Statement\n",
                    "\n",
                    "Skip odd numbers:\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept5_code2",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: continue statement\n",
                    "for i in range(1, 6):\n",
                    "    if i % 2 == 1:  # Skip odd numbers\n",
                    "        continue\n",
                    "    print(f\"Even: {i}\")\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_concept5_task",
                "metadata": {},
                "source": [
                    "### Task 5: Find Secret Number\n",
                    "\n",
                    "Use `break` to search for the secret number in a list.\n",
                    "\n",
                    "```python\n",
                    "secret = 7\n",
                    "numbers = [2, 5, 1, 8, 7, 3, 9]\n",
                    "```\n",
                    "\n",
                    "Print each number until you find the secret, then stop.\n"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_concept5_task_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Find secret number with break\n",
                    "secret = 7\n",
                    "numbers = [2, 5, 1, 8, 7, 3, 9]\n",
                    "\n",
                    "# Write your code here\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_mindmap",
                "metadata": {},
                "source": [
                    "## Looping Summary - Visual Mindmap\n",
                    "\n",
                    "```mermaid\n",
                    "mindmap\n",
                    "  root((Looping))\n",
                    "    for Loop\n",
                    "      Fixed iterations\n",
                    "      range() function\n",
                    "      Loop through sequences\n",
                    "    while Loop\n",
                    "      Condition-based\n",
                    "      Unknown count\n",
                    "      Must update variable\n",
                    "    range() Function\n",
                    "      Start, stop, step\n",
                    "      Generate sequences\n",
                    "      Common with for loops\n",
                    "    Loop Control\n",
                    "      break: Exit loop\n",
                    "      continue: Skip iteration\n",
                    "      Manage flow\n",
                    "    Best Practices\n",
                    "      Avoid infinite loops\n",
                    "      Keep logic simple\n",
                    "      Use appropriate loop type\n",
                    "```"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_capstone_intro",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "## Capstone Project: Multiplication Table Generator\n",
                    "\n",
                    "**Objective:** Build a comprehensive table generator using all looping concepts.\n",
                    "\n",
                    "**Requirements:**\n",
                    "1. Ask user for a number (validate it's between 1 and 12)\n",
                    "2. Ask for table size (how many multiples to show)\n",
                    "3. Generate multiplication table\n",
                    "4. Format output nicely with spacing\n",
                    "5. Ask if user wants another table\n",
                    "6. Repeat until user says \"no\"\n",
                    "\n",
                    "**Example Output:**\n",
                    "```\n",
                    "Multiplication Table for 5\n",
                    "5 × 1 = 5\n",
                    "5 × 2 = 10\n",
                    "5 × 3 = 15\n",
                    "5 × 4 = 20\n",
                    "5 × 5 = 25\n",
                    "```\n",
                    "\n",
                    "**Hints:**\n",
                    "- Use while loop for validation\n",
                    "- Use for loop with range() for table generation\n",
                    "- Use while loop to repeat for multiple tables"
                ]
            },
            {
                "cell_type": "python",
                "execution_count": None,
                "id": "lab3_capstone_code",
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Capstone: Multiplication Table Generator\n",
                    "# TODO: Implement the table generator\n",
                    "\n",
                    "# Starter code:\n",
                    "# while True:\n",
                    "#     # TODO: Get and validate number (1-12)\n",
                    "#     # TODO: Get table size\n",
                    "#     # TODO: Generate and display table\n",
                    "#     # TODO: Ask if user wants another table\n",
                    "#     # TODO: Break if no\n"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_resources",
                "metadata": {},
                "source": [
                    "## Key Takeaways\n",
                    "\n",
                    "✅ **for loops** - Iterate with known count  \n",
                    "✅ **while loops** - Iterate while condition is true  \n",
                    "✅ **range()** - Generate number sequences  \n",
                    "✅ **break** - Exit loop early  \n",
                    "✅ **continue** - Skip to next iteration  \n",
                    "✅ **Best Practice** - Choose right loop type for the job\n",
                    "\n",
                    "## Resources\n",
                    "\n",
                    "- [Python Docs: Loops](https://docs.python.org/3/tutorial/controlflow.html)\n",
                    "- [Real Python: For Loops](https://realpython.com/for-loop-python/)\n",
                    "- [Real Python: While Loops](https://realpython.com/while-loop/)\n",
                    "- [W3Schools: Python Loops](https://www.w3schools.com/python/python_for_loops.asp)"
                ]
            },
            {
                "cell_type": "markdown",
                "id": "lab3_colab",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "## 📓 Run in Google Colab\n",
                    "\n",
                    "You can run this notebook directly in Google Colab by clicking the button below:\n",
                    "\n",
                    "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AhmadAlsaadi/ENCH320-Labs/blob/main/Notebook_03_Looping.ipynb)"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return notebook

if __name__ == "__main__":
    import os
    
    workspace_dir = r"c:\Users\al7ak\Documents\gitRepo\ENCH320-Labs"
    
    # Generate Lab 2 (Control Flow)
    lab2 = create_control_flow_notebook()
    lab2_path = os.path.join(workspace_dir, "Notebook_02_Control_Flow.ipynb")
    with open(lab2_path, 'w', encoding='utf-8') as f:
        json.dump(lab2, f, indent=1, ensure_ascii=False)
    print(f"✓ Lab 2 (Control Flow) created: {len(lab2['cells'])} cells")
    
    # Generate Lab 3 (Looping)
    lab3 = create_looping_notebook()
    lab3_path = os.path.join(workspace_dir, "Notebook_03_Looping.ipynb")
    with open(lab3_path, 'w', encoding='utf-8') as f:
        json.dump(lab3, f, indent=1, ensure_ascii=False)
    print(f"✓ Lab 3 (Looping) created: {len(lab3['cells'])} cells")
    
    print("\n✓ Both notebooks generated successfully!")
