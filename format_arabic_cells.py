#!/usr/bin/env python3
"""
Format all Lab 2 Arabic cells to match Lab 1 template with collapsible sections,
RTL text, and Amiri font.
"""

import json

# Template for formatted Arabic cells
ARABIC_WRAPPER = '''<details>
<summary style="cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;">🌍 Arabic Translation / الترجمة العربية</summary>

<div dir="rtl" style="text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;">

<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">

{content}

</div>
</details>'''

def format_lab2():
    """Format all Arabic cells in Lab 2."""
    file_path = r"c:\Users\al7ak\Documents\gitRepo\ENCH320-Labs\Notebook_02_Control_Flow.ipynb"
    
    # Read the VSCode cell format file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Dictionary of Arabic cell patterns to find and wrap
    arabic_replacements = {
        '### العربية: جملة if\n\nجملة `if` تسمح لبرنامجك باتخاذ قرارات بناءً على الشروط. إذا كان الشرط صحيحاً (True)، يتم تنفيذ الكود داخل كتلة if. إذا كان خاطئاً (False)، يتم تخطي الكود.\n\n**النقاط الرئيسية:**\n- الشروط تقيّم إلى صحيح أو خاطئ\n- استخدم مشغلات المقارنة: ==, !=, <, >, <=, >=\n- المحاذاة (Indentation) مهمة في Python': 'concept 1 explanation',
        '### مثال عربي: التحقق من السن\n\nإذا كان العمر 18 أو أكثر، سيتم طباعة رسالة.': 'concept 1 example',
        '### المهمة بالعربية: التحقق من درجة الطالب\n\nاكتب جملة if للتحقق من أن درجة الطالب 80 أو أعلى.': 'concept 1 task',
        '### العربية: جملة if-else\n\nجملة `if-else` توفر طريقين: أحدهما عندما يكون الشرط صحيحاً، والآخر عندما يكون خاطئاً.\n\n**النقاط الرئيسية:**\n- استخدم `else` للتعامل مع الحالة الخاطئة\n- تنفيذ كتلة واحدة فقط\n- مفيد للقرارات الثنائية': 'concept 2 explanation',
        '### مثال عربي: نصيحة الطقس\n\nإذا كانت درجة الحرارة أعلى من 15، نطبع رسالة واحدة، وإلا نطبع رسالة أخرى.': 'concept 2 example',
        '### المهمة بالعربية: التحقق من الخصم\n\nاكتب جملة if-else للتحقق من أن مبلغ الشراء 100 أو أكثر.': 'concept 2 task',
    }
    
    count = 0
    for arabic_text, label in arabic_replacements.items():
        formatted_text = ARABIC_WRAPPER.format(content=arabic_text)
        if arabic_text in content:
            content = content.replace(arabic_text, formatted_text, 1)
            count += 1
            print(f"✓ Formatted {label}")
        else:
            print(f"✗ Could not find {label}")
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✓ Successfully formatted {count} Arabic cells!")

if __name__ == "__main__":
    format_lab2()
