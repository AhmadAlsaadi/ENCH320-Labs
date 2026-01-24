#!/usr/bin/env python3
"""Format Lab 2 Arabic cells to match Lab 1 template."""

import json

ARABIC_WRAPPER = '''<details>
<summary style="cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;">🌍 Arabic Translation / الترجمة العربية</summary>

<div dir="rtl" style="text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;">

<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">

{content}

</div>
</details>'''

def format_arabic_cells():
    """Format all Arabic cells in Lab 2."""
    file_path = r"c:\Users\al7ak\Documents\gitRepo\ENCH320-Labs\Notebook_02_Control_Flow.ipynb"
    
    # Load as JSON
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    count = 0
    for cell in notebook['cells']:
        if cell['cell_type'] != 'markdown':
            continue
        
        # Join source if it's a list
        source = cell['source']
        if isinstance(source, list):
            source_text = ''.join(source)
        else:
            source_text = source
        
        # Check if this is an Arabic cell
        if any(marker in source_text for marker in ['### العربية:', '### مثال عربي:', '### المهمة بالعربية:']):
            # Remove the markdown heading if it starts with ###
            if source_text.startswith('###'):
                lines = source_text.split('\n')
                # Keep the heading but wrap everything
                wrapped = ARABIC_WRAPPER.format(content=source_text)
            else:
                wrapped = ARABIC_WRAPPER.format(content=source_text)
            
            # Update cell source - keep as list format if it was a list
            if isinstance(cell['source'], list):
                cell['source'] = [wrapped]
            else:
                cell['source'] = wrapped
            
            count += 1
            # Extract label for logging
            if '### العربية:' in source_text:
                label_line = [l for l in source_text.split('\n') if '###' in l][0]
                print(f"✓ Formatted: {label_line}")
            else:
                print(f"✓ Formatted Arabic cell {count}")
    
    # Write back as JSON
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"\n✓ Successfully formatted {count} Arabic cells!")

if __name__ == "__main__":
    format_arabic_cells()
