# � Google Colab Notebook Guide

> **Master Google Colab interface and features through hands-on exercises**

---

## 📚 Table of Contents

1. [What is Google Colab?](#what-is-google-colab)
2. [Getting Started](#getting-started)
3. [Your First Notebook](#your-first-notebook)
4. [Understanding the Interface](#understanding-the-interface)
5. [Working with Code Cells](#working-with-code-cells)
6. [Working with Text Cells](#working-with-text-cells)
7. [Managing Your Notebook](#managing-your-notebook)
8. [Formatting & Organization](#formatting--organization)
9. [Sharing Your Work](#sharing-your-work)
10. [Tips & Tricks](#tips--tricks)
11. [Final Project: Create Your Learning Portfolio](#-final-project-create-your-learning-portfolio)

---

## What is Google Colab?

### 📖 The Concept

**Google Colab** (short for "Colaboratory") is a free, cloud-based platform for creating and sharing interactive notebooks.

**What is a Jupyter Notebook?**
A Jupyter Notebook is a document that combines:
- **Text cells:** For explanations, instructions, and documentation
- **Code cells:** For writing and executing code
- **Output areas:** For displaying results, graphs, and messages

**Why use Google Colab?**
- ✅ Free and easy to use
- ✅ No software installation required
- ✅ Access from any device with a browser
- ✅ Built-in cloud storage integration
- ✅ Easy sharing and collaboration
- ✅ Perfect for learning and teaching

**Who uses it?**
- Students following course materials
- Educators creating interactive lessons
- Researchers documenting their work
- Anyone needing to share code and explanations together

---

## Getting Started

### Step 1: Access Google Colab

**Instructions:**
1. Open your browser and go to [colab.research.google.com](https://colab.research.google.com)
2. You'll see the Colab homepage with options to create or open notebooks

**✋ Exercise 1: Navigate to Colab**
- Open Google Colab in your browser
- Take 30 seconds to look around the interface
- **Checkpoint:** You should see a page with "New Notebook" and "Recent Notebooks" options

---

### Step 2: Create Your First Notebook

**Instructions:**
1. Click the **"+ New Notebook"** button
2. A new notebook will open in a new tab
3. You'll see a blank notebook titled "Untitled0.ipynb"

**✋ Exercise 2: Create Your First Notebook**
- Create a new notebook
- Look at the top where it says "Untitled0" - this is your notebook name
- **Checkpoint:** You should have a blank notebook open with a code cell ready to edit

---

### Step 3: Rename Your Notebook

**Instructions:**
1. Click on the notebook name at the top left ("Untitled0")
2. Type a new name: `My_First_Colab_Notebook`
3. Press Enter to save

**✋ Exercise 3: Rename Your Notebook**
- Rename your notebook to something meaningful
- Examples: `Python_Learning`, `Data_Analysis`, `My_Project`
- **Checkpoint:** The notebook title should reflect your new name

---

---

## Your First Notebook

### Understanding the Notebook Layout

```
┌─────────────────────────────────────────────────┐
│  File  Edit  View  Insert  Runtime  Tools  Help │  ← Menu Bar
├─────────────────────────────────────────────────┤
│  Notebook Name    Share    Open in Drive  ...   │  ← Toolbar
├─────────────────────────────────────────────────┤
│  📝 Text Cell (Markdown formatted text)        │
│                                                 │
├─────────────────────────────────────────────────┤
│  💻 Code Cell (Ready for input)                 │
│  [ ▶ ]  Your code goes here                     │  ← Run Button
│                                                 │
├─────────────────────────────────────────────────┤
│  Output Area                                    │
│  (Results appear here when you run the cell)   │
└─────────────────────────────────────────────────┘
```

**Key Areas:**
- **Menu Bar:** File, Edit, View, Insert, Runtime, Tools, Help
- **Toolbar:** Quick access buttons for common tasks
- **Cells:** The main content area (text or code)
- **Run Button:** The ▶ button that executes code cells
- **Output Area:** Where results, errors, and messages appear



---

## Working with Code Cells

### Identifying a Code Cell

**What is a Code Cell?**
A code cell is a box where you can type code and execute it. Code cells have:
- A cell number on the left: `[ 1 ]`
- A run button (▶) on the left side
- A light gray background
- An empty text area for input

---

### Running Code Cells

**Instruction:**
There are multiple ways to execute a code cell:

**Method 1: Click the Run Button**
1. Click the ▶ button on the left side of the code cell
2. Wait a moment for execution
3. Results appear below the cell

**Method 2: Keyboard Shortcut**
- `Ctrl + Enter` - Run the current cell and stay in it
- `Shift + Enter` - Run the current cell and move to the next cell

**✋ Exercise 4: Run Your First Cell**
1. Find the empty code cell in your notebook
2. Try both methods:
   - Method 1: Click the ▶ button
   - Method 2: Place cursor in cell and press `Ctrl + Enter`
3. Notice the cell number appears (e.g., `[1]`)
4. **Checkpoint:** You see `[ ]` changes to `[1]` when you run the cell

---

### Creating New Code Cells

**Instruction:**
1. Hover your cursor between cells or below a cell
2. Click the **"+ Code"** button that appears
3. A new code cell is inserted at that position

**Keyboard Shortcut:**
- `Ctrl + M + B` - Insert code cell below
- `Ctrl + M + A` - Insert code cell above

**✋ Exercise 5: Create Multiple Code Cells**
1. Create 5 new code cells using the "+ Code" button
2. Notice each new cell is empty and ready for input
3. Try using the keyboard shortcut `Ctrl + M + B` to add another cell
4. **Checkpoint:** You have multiple code cells in your notebook

---

### Moving and Deleting Code Cells

**Instruction:**
**Moving a Cell:**
1. Hover over the cell number on the left side
2. Click the up (↑) or down (↓) arrow buttons
3. The cell moves to the new position

**Deleting a Cell:**
1. Click the three dots (⋮) menu on the right side of the cell
2. Select "Delete cell" from the menu
3. The cell is removed (cannot be undone - be careful!)

**✋ Exercise 6: Organize Code Cells**
1. Create 3 code cells
2. Use the up/down arrows to rearrange them (try moving the second cell to the bottom)
3. Delete one cell using the three-dots menu
4. **Checkpoint:** Your cells are in a different order than they were created

---

### Clearing Output

**Instruction:**
When you run a cell multiple times, old output may accumulate. To clear it:

1. Click the three dots (⋮) menu on the right side
2. Select "Clear output" 
3. The output area is cleared but the cell code remains

**Clear All Output:**
1. Go to **Edit → Clear all outputs**
2. All output in the notebook is cleared

**✋ Exercise 7: Clear Cell Output**
1. Create a code cell
2. Run it (even if there's no output)
3. Click the three-dots menu
4. Select "Clear output"
5. **Checkpoint:** Any previous output is removed

---

## Working with Text Cells

### What is a Text Cell?

**Text Cell Characteristics:**
- Contains formatted text, not code
- Used for explanations, instructions, headings, and documentation
- Uses **Markdown** formatting (special syntax for formatting)
- Has a light background when editing, disappears when finished

---

### Creating a Text Cell

**Instruction:**
1. Hover between cells or above/below existing cells
2. Click **"+ Text"** button (next to "+ Code")
3. An empty text cell appears
4. Start typing your content

**Keyboard Shortcut:**
- `Ctrl + M + D` - Insert text cell below

**✋ Exercise 8: Create Your First Text Cell**
1. Click "+ Text" to create a new text cell
2. Type any sentence, for example: "This is my first text cell"
3. Click outside the cell or press `Ctrl + Enter`
4. Notice the text is now formatted and the cell is complete
5. **Checkpoint:** Your text cell is created and displayed

---

### Markdown Formatting Basics

**What is Markdown?**
Markdown is a simple way to format text using special characters. In Google Colab text cells, you can use these formatting options:

| Element | Syntax | How It Looks |
|---------|--------|--------------|
| Heading 1 | `# Text` | # Big Title |
| Heading 2 | `## Text` | ## Medium Title |
| Heading 3 | `### Text` | ### Smaller Title |
| Bold | `**Text**` | **Bold** |
| Italic | `*Text*` | *Italic* |
| Bold + Italic | `***Text***` | ***Bold Italic*** |
| Bullet Point | `- Item` | • Item |
| Numbered List | `1. Item` | 1. Item |
| Code | `` `code` `` | `code` |

---

### Creating Formatted Text

**Instruction:**
You can combine different formatting elements in one text cell.

**✋ Exercise 9: Create a Formatted Text Cell**
1. Create a new text cell
2. Type the following:
```markdown
# My First Notebook

## Introduction
This notebook contains my learning materials.

### Key Topics
- Topic 1: Getting started
- Topic 2: Using cells
- Topic 3: Saving work

**Important:** Save your work regularly!
```
3. Click outside the cell
4. **Checkpoint:** Your text is now formatted with headings, lists, and bold text

---

### Editing Existing Text Cells

**Instruction:**
To edit a text cell after you've finished typing:

1. Click on the text cell (double-click if needed)
2. The cell enters editing mode
3. Make your changes
4. Click outside or press `Ctrl + Enter` when done

**✋ Exercise 10: Edit a Text Cell**
1. Find a text cell you created earlier
2. Double-click it to enter edit mode
3. Add more content or change existing text
4. Click outside to finish
5. **Checkpoint:** Your changes are saved in the text cell

---

### Deleting Text Cells

**Instruction:**
1. Click the three dots (⋮) menu on the right side of the text cell
2. Select "Delete cell"
3. The cell is removed

**✋ Exercise 11: Delete a Text Cell**
1. Create a text cell
2. Click the three-dots menu
3. Select "Delete cell"
4. **Checkpoint:** The text cell is removed from the notebook

---

## Managing Your Notebook

### Saving Your Notebook

**Important:** Google Colab doesn't automatically save to your personal files. You must manually save your work!

**Option 1: Save to Google Drive (Recommended)**
1. Click **File → Save a copy in Drive**
2. Colab saves your notebook to your Google Drive
3. You can now access it anytime from Google Drive
4. Changes are auto-saved while you're working

**Option 2: Download Notebook**
1. Click **File → Download** 
2. Your notebook downloads as `.ipynb` file
3. You can upload it to Google Colab later

**✋ Exercise 12: Save Your Notebook**
1. Click **File → Save a copy in Drive**
2. A dialog appears asking where to save
3. Choose a folder or create a new one
4. Click **Save**
5. Open your Google Drive in another tab to verify
6. **Checkpoint:** Your notebook appears in your Google Drive

---

### Finding Your Notebook

**Instruction:**
After saving to Google Drive, locate your notebook:

**Method 1: From Colab**
1. Click **File → Open notebook** (or go to colab.research.google.com)
2. Click "Google Drive" tab
3. Browse your files to find your notebook
4. Click on it to open

**Method 2: From Google Drive**
1. Go to drive.google.com
2. Find your notebook file (ends in `.ipynb`)
3. Double-click to open in Colab

**✋ Exercise 13: Find Your Notebook**
1. Open Google Drive
2. Look for your recently saved notebook
3. Click on it to open in Colab
4. Verify it's the same notebook you saved
5. **Checkpoint:** You can find your notebook in Google Drive

---

### Renaming Your Notebook

**Instruction:**
1. Click on the notebook name at the top left
2. Type the new name
3. Press Enter to confirm

**✋ Exercise 14: Rename Your Notebook**
1. Look at the notebook name at the top
2. Click on it (it should become editable)
3. Change the name to something descriptive
4. Press Enter
5. **Checkpoint:** The notebook title has changed

---

### Checking Notebook File Size

**Instruction:**
1. Click **File → View notebook details**
2. See information about the notebook:
   - Size (in MB or KB)
   - Last modified date
   - Location
3. Click elsewhere to close

**✋ Exercise 15: View Notebook Details**
1. Open **File → View notebook details**
2. Note the file size and location
3. **Checkpoint:** You know how large your notebook is

---

## Formatting & Organization

### Adding Sections to Your Notebook

**Instruction:**
Organize your notebook with clear sections using text cells with headings.

**Structure Example:**
```
# Main Title (Heading 1)

## Section 1 (Heading 2)
[Text cells and code cells for section 1]

## Section 2 (Heading 2)
[Text cells and code cells for section 2]
```

**✋ Exercise 16: Create a Structured Notebook**
1. Create a new notebook and rename it "My Structured Notebook"
2. Add a text cell at the top: `# My Project`
3. Add another text cell: `## Section A`
4. Add a code cell below it
5. Add another text cell: `## Section B`
6. Add another code cell
7. **Checkpoint:** Your notebook has clear sections with headings

---

### Creating Tables in Text Cells

**Instruction:**
You can add tables using Markdown:

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Item 1   | Data 1   | Value 1  |
| Item 2   | Data 2   | Value 2  |
```

**✋ Exercise 17: Add a Table to Your Notebook**
1. Create a text cell
2. Copy the table structure above
3. Modify it with your own data:
   - Change column names
   - Add your own rows
4. Click outside to see the formatted table
5. **Checkpoint:** A formatted table appears in your notebook

---

### Creating Lists in Text Cells

**Bullet Points:**
```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3
```

**Numbered Lists:**
```markdown
1. First step
2. Second step
3. Third step
```

**✋ Exercise 18: Create Organized Lists**
1. Create a text cell
2. Add a bullet point list with at least 3 items
3. Add a nested item (indent with spaces)
4. Below that, add a numbered list
5. **Checkpoint:** Both bullet and numbered lists display correctly

---

### Adding Line Breaks and Dividers

**Instruction:**
- Single line break: Press Enter once
- Paragraph break: Press Enter twice
- Horizontal line divider: `---` or `***`

**✋ Exercise 19: Format Text with Breaks**
1. Create a text cell
2. Type some text
3. Press Enter twice to create a paragraph break
4. Type more text
5. Add `---` on a new line to create a divider
6. **Checkpoint:** Your text has proper spacing and a visual divider

---

## Sharing Your Work

### How to Share Your Notebook

**Instruction:**
1. Click **Share** button (top-right corner)
2. A dialog box appears
3. In the text field, enter email addresses of people to share with
4. Choose permission level:
   - **Viewer** - Can only read (no editing)
   - **Commenter** - Can read and add comments
   - **Editor** - Can read, edit, and make changes
5. Click **Share**

**✋ Exercise 20: Share Your Notebook**
1. Create or open a notebook
2. Click the **Share** button
3. Enter an email address (use a test email or classmate's email)
4. Select "Viewer" permission
5. Click **Share**
6. **Checkpoint:** The notebook has been shared (verify by checking the Share button)

---

### Creating a Shareable Link

**Instruction:**
Instead of typing individual emails, create a link anyone can use:

1. Click **Share** button
2. Look for "Get link" section
3. Change setting from "Restricted" to "Anyone with the link"
4. Copy the URL that appears
5. Share this link with others

**✋ Exercise 21: Create and Copy a Share Link**
1. Open **Share**
2. Find "Get link" section
3. Click the permission dropdown ("Restricted")
4. Select "Anyone with the link"
5. Click the copy button to copy the link
6. **Checkpoint:** You have a shareable link in your clipboard

---

### Changing Share Permissions

**Instruction:**
You can change or revoke access at any time:

1. Click **Share** button
2. Find the person's name in the shared list
3. Click the dropdown next to their name
4. Change permission level or click trash icon to remove

**✋ Exercise 22: Manage Shared Access**
1. Open **Share**
2. Look at people you've shared with
3. Click the dropdown next to one person's name
4. Change their permission from "Viewer" to "Commenter"
5. **Checkpoint:** Permissions have been updated

---

### Publishing to the Web

**Instruction:**
Make your notebook available as a read-only web page:

1. Click **File → Publish to web**
2. A dialog appears with a shareable link
3. Copy the link
4. Anyone can view it as a webpage (no Colab account needed)

**✋ Exercise 23: Publish Your Notebook**
1. Click **File → Publish to web**
2. Review the shareable link
3. Copy the link
4. Open it in a new browser tab to see how it looks
5. **Checkpoint:** Your notebook is published as a web page

---

## Tips & Tricks

### 🎯 Essential Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + Enter` | Run current cell |
| `Shift + Enter` | Run cell and move to next |
| `Ctrl + M + B` | Insert code cell below |
| `Ctrl + M + A` | Insert code cell above |
| `Ctrl + M + D` | Insert text cell below |
| `Ctrl + /` | Comment/uncomment code |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` | Redo |

**✋ Exercise 24: Practice Keyboard Shortcuts**
1. Create a code cell using `Ctrl + M + B`
2. Run it with `Ctrl + Enter`
3. Create a text cell using `Ctrl + M + D`
4. Try undoing something with `Ctrl + Z`
5. **Checkpoint:** You're comfortable using keyboard shortcuts

---

### Using the Table of Contents

**Instruction:**
Google Colab can automatically create a table of contents from your headings:

1. Click the **table of contents icon** (three horizontal lines on left sidebar)
2. Your text cell headings appear as a navigation menu
3. Click any heading to jump to that section

**✋ Exercise 25: Use Table of Contents**
1. Create several text cells with different headings (# H1, ## H2)
2. Click the table of contents icon on the left
3. Watch your headings appear in the menu
4. Click on a heading to jump to it
5. **Checkpoint:** You can navigate using the table of contents

---

### Using the Search Function

**Instruction:**
Find text in your notebook:

1. Press `Ctrl + F` (or `Cmd + F` on Mac)
2. Type what you're looking for
3. Results highlight in yellow
4. Use arrows to navigate between matches

**✋ Exercise 26: Search in Your Notebook**
1. Press `Ctrl + F`
2. Type a word that appears multiple times in your notebook
3. Notice the highlighting
4. Use the navigation arrows to move between matches
5. Press Escape to close the search
6. **Checkpoint:** You found text using search

---

### Collapsing Cells

**Instruction:**
Hide cell content to focus on other areas:

1. Click the **arrow** next to the cell number
2. The cell collapses (code/content is hidden)
3. Click again to expand

**✋ Exercise 27: Collapse and Expand Cells**
1. Find several cells in your notebook
2. Click the arrow next to one cell's number to collapse it
3. Click again to expand
4. Try collapsing multiple cells
5. **Checkpoint:** Cells can be collapsed and expanded

---

### Duplicating Cells

**Instruction:**
Make a copy of a cell:

1. Click the three dots (⋮) menu on the right
2. Select "Duplicate cell"
3. An identical copy appears below the original

**✋ Exercise 28: Duplicate a Cell**
1. Create a code or text cell with content
2. Click the three-dots menu
3. Select "Duplicate cell"
4. Verify that a copy appears below
5. **Checkpoint:** Cell duplication works

---

### Code Cell Settings

**Instruction:**
Change how code cells behave:

1. Click the three dots (⋮) menu on the code cell
2. Options include:
   - "Hide code" - Output visible, code hidden
   - "Hide output" - Code visible, output hidden
   - "Show form" - Turn code into an interactive form
   - "Allow output scrolling" - Limit output height

**✋ Exercise 29: Hide Cell Code or Output**
1. Create a code cell
2. Click the three-dots menu
3. Select "Hide code"
4. Notice only output is visible
5. Click the menu again and select "Show code"
6. **Checkpoint:** You can control what's visible in cells

---

## 🎯 Final Project: Create Your Learning Portfolio

Now that you've mastered Google Colab, let's create something meaningful - a **Learning Portfolio Notebook** that you can share with others, use for reference, and build upon throughout your studies.

### Project Goal

By the end of this project, you will have created a professional notebook that:
- Showcases your Google Colab skills
- Documents your learning journey
- Serves as a reference guide you can return to
- Can be shared with instructors, peers, or future employers

---

### Step 1: Set Up Your Portfolio Structure

**✋ Exercise 30: Create Your Portfolio Notebook**

1. Create a new notebook and name it: `[YourName]_Google_Colab_Portfolio`
2. Create the first text cell with this content:

```markdown
# My Google Colab Learning Portfolio
**Created by:** [Your Name]  
**Date:** [Today's Date]  
**Purpose:** Demonstrate mastery of Google Colab notebook features

---

## 📚 Table of Contents
1. About Me
2. Skills I've Learned
3. Code Cell Demonstrations
4. Useful Code Snippets
5. Markdown Showcase
6. Interactive Examples
7. Future Goals
```

3. Save your notebook to Google Drive
4. **Checkpoint:** You have a professionally titled portfolio with a table of contents

---

### Step 2: Add Your Personal Introduction

**✋ Exercise 31: Create an "About Me" Section**

1. Create a text cell with a heading: `## About Me`
2. Write 3-5 sentences about yourself:
   - Your academic background
   - Why you're learning Google Colab
   - What interests you about programming or data analysis
3. Format your text with **bold** for your major and *italics* for course names
4. Add a horizontal divider (`---`) at the end
5. **Checkpoint:** You have a personalized introduction with formatted text

**Example:**
```markdown
## About Me

I am a **Chemical Engineering** student learning to use Google Colab for *ENCH320: Computational Methods*. I'm excited about using notebooks to document my work and share results with my study group. My goal is to become proficient in creating professional, well-organized computational notebooks.

---
```

---

### Step 3: Document Your Skills

**✋ Exercise 32: Create a Skills Inventory**

1. Create a text cell with heading: `## Skills I've Learned`
2. Create two subsections with bullet points:

```markdown
### Notebook Management
- Creating and renaming notebooks
- Saving to Google Drive
- Opening and organizing saved notebooks
- Managing cell layout and order

### Cell Operations
- Creating and running code cells
- Creating formatted text cells
- Moving and deleting cells
- Using keyboard shortcuts for efficiency

### Collaboration & Sharing
- Sharing notebooks with specific users
- Creating shareable links
- Managing view and edit permissions
- Commenting and version control
```

3. **Checkpoint:** You have a structured list showcasing everything you learned

---

### Step 4: Demonstrate Code Cell Mastery

**✋ Exercise 33: Create Code Cell Examples**

1. Create a text cell: `## Code Cell Demonstrations`
2. Add a subtitle: `### Basic Operations`
3. Create a **code cell** below it and type:

```python
# Simple arithmetic
print("Hello from my portfolio!")
print("2 + 2 =", 2 + 2)
print("10 * 5 =", 10 * 5)
```

4. Run the code cell and observe the output
5. Create another text cell: `### Working with Variables`
6. Create a **code cell** and type:

```python
# Variables and calculations
my_name = "[Your Name]"
my_course = "ENCH320"
year = 2026

print(f"My name is {my_name}")
print(f"I'm taking {my_course} in {year}")
```

7. Run this code cell
8. **Checkpoint:** You have working code cells with output demonstrating your understanding

---

### Step 5: Create a Reference Library

**✋ Exercise 34: Build a Markdown Quick Reference**

1. Create a text cell: `## Markdown Quick Reference`
2. Create a table showing markdown syntax you use most often:

```markdown
| What I Want | Markdown Syntax | Result |
|-------------|-----------------|--------|
| Main Heading | `# Text` | # Big Title |
| Subheading | `## Text` | ## Medium Title |
| Bold | `**Text**` | **Bold Text** |
| Italic | `*Text*` | *Italic Text* |
| Bullet List | `- Item` | • Item |
| Numbered List | `1. Item` | 1. Item |
| Code | `` `code` `` | `code` |
| Link | `[Text](url)` | [Link](#) |
```

3. Add a note below explaining why this reference is useful to you
4. **Checkpoint:** You've created a personal reference you can return to anytime

---

### Step 6: Build a Code Snippet Library

**✋ Exercise 35: Create Reusable Code Examples**

1. Create a text cell: `## Useful Code Snippets`
2. Add explanation text:

```markdown
These are code patterns I can reuse in future notebooks:

### Displaying Information
```

3. Create a **code cell** with:

```python
# Print multiple items nicely
print("=" * 40)
print("     MY RESULTS")
print("=" * 40)
print("Value 1:", 100)
print("Value 2:", 200)
print("=" * 40)
```

4. Run the cell to see formatted output
5. Create another text cell: `### Creating Lists`
6. Create a **code cell** with:

```python
# Working with lists
my_skills = ["Creating notebooks", "Using markdown", "Running code cells", "Sharing work"]

print("Skills I've learned:")
for i, skill in enumerate(my_skills, 1):
    print(f"{i}. {skill}")
```

7. Run this cell
8. **Checkpoint:** You have reusable code patterns you can reference

---

### Step 7: Create Interactive Examples

**✋ Exercise 36: Combine Markdown and Code Cells**

1. Create a text cell: `## Interactive Examples`
2. Add this content:

```markdown
### Example 1: Simple Calculator

This demonstrates how code cells can perform calculations:
```

3. Create a **code cell** below:

```python
# Interactive calculator example
number1 = 15
number2 = 7

print(f"Number 1: {number1}")
print(f"Number 2: {number2}")
print(f"Sum: {number1 + number2}")
print(f"Difference: {number1 - number2}")
print(f"Product: {number1 * number2}")
print(f"Division: {number1 / number2:.2f}")
```

4. Run the code cell
5. Create another text cell:

```markdown
### Example 2: Text Processing

This shows how to work with text data:
```

6. Create a **code cell**:

```python
# Text processing example
sentence = "Google Colab is an amazing tool for learning"

print("Original:", sentence)
print("Uppercase:", sentence.upper())
print("Word count:", len(sentence.split()))
print("Character count:", len(sentence))
print("Contains 'Colab':", "Colab" in sentence)
```

7. Run this code cell
8. **Checkpoint:** You've created a section that combines explanatory text with executable code

---

### Step 8: Showcase Keyboard Shortcuts

**✋ Exercise 37: Document Your Efficiency Tools**

1. Create a text cell: `## Keyboard Shortcuts I Use`
2. List the shortcuts you find most helpful:

```markdown
### Most Useful Shortcuts

**Cell Execution:**
- `Ctrl + Enter` - Run current cell
- `Shift + Enter` - Run and move to next cell

**Cell Creation:**
- `Ctrl + M + B` - Insert code cell below
- `Ctrl + M + A` - Insert code cell above

**Navigation:**
- `Ctrl + M + H` - Show keyboard shortcuts
- `Ctrl + /` - Comment/uncomment code
```

3. Add a personal note about which shortcut saves you the most time
4. **Checkpoint:** You have a personalized shortcut reference guide

---

### Step 9: Set Your Future Goals

**✋ Exercise 38: Define Your Learning Path**

1. Create a text cell: `## My Future Goals with Google Colab`
2. Write about what you want to accomplish:

```markdown
### Short-term Goals (This Semester)
- [ ] Complete all course lab notebooks
- [ ] Create study notes in notebook format
- [ ] Share notebooks with study group
- [ ] Use notebooks for project documentation

### Long-term Goals
- [ ] Build a portfolio of data analysis projects
- [ ] Learn advanced visualization techniques
- [ ] Collaborate on research projects using notebooks
- [ ] Teach others what I've learned

### Why This Matters to Me
[Write 2-3 sentences about why mastering Colab is important for your academic or career goals]
```

3. **Checkpoint:** You've set clear, actionable goals for your continued learning

---

### Step 10: Finalize and Share Your Portfolio

**✋ Exercise 39: Polish and Share Your Work**

1. Review your entire portfolio notebook
2. Make sure all sections have:
   - Clear headings (using `#`, `##`, `###`)
   - Proper formatting (bold, italics, lists)
   - Consistent style throughout
3. Add a final text cell at the bottom:

```markdown
---

## 🏆 Portfolio Complete!

**Created:** [Date]  
**Skills Demonstrated:** Notebook creation, Markdown formatting, code cell execution, organization, documentation  
**Cell Types Used:** Both text (markdown) and code cells  
**Status:** Ready to share

*This portfolio represents my journey in mastering Google Colab. I will continue to update it as I learn new skills and complete new projects.*
```

4. Save your portfolio to Google Drive
5. Create a shareable link (Anyone with the link can view)
6. Test the link in a private/incognito browser window
7. **Checkpoint:** You have a complete, shareable portfolio demonstrating both markdown and code skills!

---

### Step 11: Optional - Take It Further

**✋ Exercise 40: Enhance Your Portfolio (Optional)**

Consider adding these sections to make your portfolio even more impressive:

1. **Data Visualization:** Add code cells that create simple charts or graphs
2. **Mini Projects:** Include small coding challenges you've solved
3. **Code vs Output Comparison:** Show how changing code affects output
4. **Commented Code Examples:** Demonstrate your understanding with well-commented code
5. **Resources Section:** Links to helpful tutorials and guides
6. **Tips for Beginners:** Advice based on your learning experience

---

## 🎓 Your Learning Journey

### What You've Accomplished

You've completed **40 hands-on exercises** and created a **professional learning portfolio** that combines both markdown and code cells! Here's what you can now do:

- ✅ Create, rename, and organize notebooks
- ✅ Create and run code cells
- ✅ Create and format text cells using Markdown
- ✅ Combine code and markdown cells effectively
- ✅ Document code with explanatory text
- ✅ Insert cells above and below existing cells
- ✅ Move, duplicate, and delete cells
- ✅ Save notebooks to Google Drive
- ✅ Share notebooks with specific people
- ✅ Create shareable links for public access
- ✅ Change and manage sharing permissions
- ✅ Use keyboard shortcuts efficiently
- ✅ Navigate using table of contents
- ✅ Search for content in notebooks
- ✅ Control what's visible in cells (hide/show)
- ✅ **Create a professional learning portfolio**
- ✅ **Document your skills and progress**
- ✅ **Set goals for future learning**

---

### Next Steps

**Now that you've created your Learning Portfolio:**

1. **Use Your Portfolio**
   - Keep it as a reference when working on future projects
   - Update it with new skills as you learn them
   - Show it to instructors when submitting coursework
   - Share it with study partners to help them learn

2. **Build on Your Skills**
   - Create notebooks for each course assignment
   - Document your problem-solving approaches
   - Organize notebooks in Google Drive folders by topic
   - Practice formatting and organization in every notebook

3. **Help Others Learn**
   - Share your portfolio with classmates who are just starting
   - Create tutorial notebooks for topics you master
   - Collaborate on group projects using notebooks
   - Provide feedback on others' work through comments

4. **Keep Growing**
   - Set a goal to create one well-documented notebook per week
   - Experiment with advanced Markdown features
   - Try creating educational content in notebook format
   - Build a collection of reusable code snippets and templates

---

### 💡 Why This Portfolio Matters

This portfolio is more than just practice - it's a tangible demonstration of your ability to:
- **Learn new tools independently** - You taught yourself Google Colab
- **Document your work professionally** - Essential for engineering and research
- **Organize information clearly** - Critical for communicating technical concepts
- **Create shareable resources** - Valuable for collaboration and teaching

These are skills that will serve you throughout your academic career and beyond. Your portfolio proves you can master a tool and create something useful with it.

---

### 💡 Learning Mindset Tips

1. **Save Often:** Don't wait until the end - save regularly to Google Drive
2. **Use Descriptive Names:** Name your notebooks so you can find them later
3. **Organize with Text Cells:** Use headings and sections to make notebooks clear
4. **Document As You Go:** Add explanations while working, not after
5. **Share for Feedback:** Get input from others to improve your work
6. **Build a Reference Library:** Keep useful notebooks for future reference
7. **Set Learning Goals:** Use your portfolio to track what you want to achieve
8. **Create, Don't Just Consume:** Build notebooks that demonstrate your understanding

---

## 🆘 Quick Reference

### Most Important Commands

**File Management:**
- `File → Save a copy in Drive` - Permanent save
- `File → Open notebook` - Open existing notebook
- `File → Download` - Download as .ipynb file

**Cell Operations:**
- `+ Code` button - Add code cell
- `+ Text` button - Add text cell
- Click up/down arrows - Move cells
- Click three dots - Delete, duplicate, hide cells

**Running & Execution:**
- `Ctrl + Enter` - Run cell
- `Shift + Enter` - Run and move to next
- `Runtime → Run all` - Execute all cells
- `Runtime → Restart runtime` - Reset environment

**Sharing & Saving:**
- `Share` button - Share with specific people
- `Get link` - Create shareable link
- `Publish to web` - Make publicly available

---

### Markdown Quick Reference

```markdown
# Heading 1          → Largest heading
## Heading 2         → Medium heading
### Heading 3        → Smaller heading

**Bold Text**        → Makes text bold
*Italic Text*        → Makes text italic

- Bullet point       → Creates list
  - Nested bullet    → Indented item
1. Numbered item     → Creates numbered list

`code`               → Inline code formatting

---                  → Horizontal divider

| Col 1 | Col 2 |    → Creates table
|-------|-------|
| Data1 | Data2 |
```

---

### Essential Links

- [Google Colab Home](https://colab.research.google.com)
- [Colab Official Notebooks](https://colab.research.google.com/notebooks/)
- [Markdown Guide](https://www.markdownguide.org)
- [Google Drive](https://drive.google.com)

---

## 🏆 Conclusion

**Congratulations!** You've completed the Google Colab Notebook Guide and created your own **Learning Portfolio**. You now have:

- ✅ Mastered Google Colab navigation and features
- ✅ Created well-organized, professional notebooks
- ✅ Built a portfolio showcasing your skills
- ✅ Developed documentation and organization skills
- ✅ Set clear goals for continued learning

**Your Portfolio Is Just the Beginning:** The notebook you created is a living document that demonstrates your ability to combine explanatory text with executable code. As you progress through your courses and learn new skills, continue updating it. Add sections for:
- New code techniques you master
- Projects combining analysis and documentation
- Problems you solve with code examples
- Reusable code snippets and patterns
- Resources you find helpful

**Remember:** The most valuable skill you've gained isn't just using Colab - it's the ability to document your learning, organize your work, and create resources that benefit both you and others. These skills will serve you throughout your academic and professional career.

Keep creating, keep learning, and keep building your portfolio! 🚀

---

**Document Information:**
- **Version:** 3.0 (Portfolio-Driven Learning)
- **Last Updated:** January 25, 2026
- **Difficulty Level:** Beginner to Intermediate
- **Estimated Time:** 2-3 hours (including portfolio creation)
- **Prerequisites:** None - start from the beginning
- **Focus:** Google Colab mastery through meaningful project creation
- **Outcome:** Professional learning portfolio demonstrating Colab proficiency
