import re

with open('art_nouveau.css', 'r', encoding='utf-8') as f:
    content = f.read()

colors = {
    "--vivid-purple: #8A2BE2": "--vivid-purple: #35524A",
    "--hot-pink: #FF69B4": "--hot-pink: #C2A36B",
    "--teal: #008080": "--teal: #1E2320",
    "--gold: #FFD700": "--gold: #E6CE9C",
    "--parchment: #fcf5e5": "--parchment: #FAF7F2",
    "--text-color: #3a2d22": "--text-color: #1A1F1A",
    "%23FF69B4": "%23C2A36B", # from SVG stroke
    "%238A2BE2": "%2335524A", # from SVG stroke
}

for old, new in colors.items():
    content = content.replace(old, new)

# Remove cursor: none
content = re.sub(r'cursor:\s*none;', '', content)

# Change hover to active
content = content.replace('.main-nav a:hover', '.main-nav a:active')

# Remove animation that might be desktop only? 
# "Use only animation styles that work on a mobile phone"
# Continuous CSS animations DO work on a mobile phone (e.g. animation: rotate 20s linear infinite).
# But mouse features don't. So removing cursor: none; and :hover is sufficient.

with open('art_nouveau.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("art_nouveau.css updated.")