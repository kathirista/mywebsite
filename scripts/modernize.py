import os
import re

files = ["index.html", "summary.html", "blog.html", "contact.html"]

colors = {
    "--klimt-gold: #B38B36": "--klimt-gold: #C2A36B",
    "--klimt-yellow: #D4AF37": "--klimt-yellow: #E6CE9C",
    "--klimt-red: #4A0E17": "--klimt-red: #35524A",
    "--klimt-black: #0F0C0C": "--klimt-black: #1E2320",
    "--klimt-cream: #EFE6D5": "--klimt-cream: #FAF7F2",
    # SVG colors encoded
    "%23B38B36": "%23C2A36B",
    "%23E5C158": "%23E6CE9C",
    "%234A0E17": "%2335524A",
    "%23D4AF37": "%23E6CE9C",
    "%230F0C0C": "%231E2320"
}

for file in files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply color replacements
    for old, new in colors.items():
        content = content.replace(old, new)
        
    # Replace CSS hover with active
    content = content.replace('.bento-box:hover', '.bento-box:active')
    content = content.replace('.link-hover:hover', '.link-hover:active')
    content = content.replace('.tree-node:hover', '.tree-node:active')
    
    # Make dancers animate continuously by removing :hover pseudo-class
    content = content.replace('.dancer:hover', '.dancer')
    
    # Replace Tailwind hover with active
    content = re.sub(r'\bhover:', 'active:', content)
    content = re.sub(r'\bgroup-hover:', 'group-active:', content)
    
    # Remove javascript mousemove and mouseleave blocks
    content = re.sub(r"\s*wrapper\.addEventListener\('mousemove'[\s\S]*?\}\);", "", content)
    content = re.sub(r"\s*wrapper\.addEventListener\('mouseleave'[\s\S]*?\}\);", "", content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML updated.")