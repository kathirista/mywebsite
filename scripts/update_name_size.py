import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Old size: text-6xl md:text-8xl lg:text-9xl
    # New size (approx 50%): text-3xl md:text-4xl lg:text-5xl
    old_h1 = 'class="text-6xl md:text-8xl lg:text-9xl font-serif-custom font-bold m-0 text-black tracking-tight"'
    new_h1 = 'class="text-3xl md:text-4xl lg:text-5xl font-serif-custom font-bold m-0 text-black tracking-tight"'
    
    if old_h1 in content:
        content = content.replace(old_h1, new_h1)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

