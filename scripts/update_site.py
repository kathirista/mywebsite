import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Increase font size of the name
    old_h1 = '<h1 class="text-2xl font-serif-custom m-0 text-black tracking-tight"><a href="index.html">Sruthi Korlakunta</a></h1>'
    new_h1 = '<h1 class="text-6xl md:text-8xl lg:text-9xl font-serif-custom font-bold m-0 text-black tracking-tight"><a href="index.html">Sruthi Korlakunta</a></h1>'
    content = content.replace(old_h1, new_h1)

    # 2. Gemma size
    content = content.replace('width: 20px;\n            height: 20px;', 'width: 80px;\n            height: 80px;')
    content = content.replace('font-size: 10px;', 'font-size: 40px;')

    # 3. Headers: remove italics, keep bold
    # First, specific italic span inside h2 in index.html
    content = content.replace('<span class="text-cyan italic">', '<span class="text-cyan font-bold">')
    
    # Let's add font-bold to all h1-h6 tags if they don't have it, and remove italic
    def process_header(match):
        tag = match.group(1)
        classes_match = re.search(r'class="([^"]*)"', match.group(0))
        if classes_match:
            classes = classes_match.group(1)
            # Remove italic
            classes = re.sub(r'\bitalic\b', '', classes)
            # Add font-bold if not present
            if 'font-bold' not in classes and 'font-black' not in classes:
                classes += ' font-bold'
            # Clean up extra spaces
            classes = re.sub(r'\s+', ' ', classes).strip()
            
            # Replace the old class with the new class
            new_tag = re.sub(r'class="[^"]*"', f'class="{classes}"', match.group(0))
            return new_tag
        return match.group(0)

    content = re.sub(r'(<h[1-6][^>]*>)', process_header, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated all HTML files successfully.")
