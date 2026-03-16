import os
import re

files = ['index.html', 'blog.html', 'contact.html', 'summary.html']
for filename in files:
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Body padding
    content = content.replace('p-6 md:p-12', 'p-4 md:p-12')

    # 2. Navigation
    nav_pattern = re.compile(r'<nav class="flex justify-between items-center mb-12( z-20 relative max-w-7xl mx-auto bg-\[var\(--klimt-cream\)\] border-4 border-\[var\(--klimt-black\)\] p-4 shadow-\[6px_6px_0px_var\(--klimt-gold\)\] w-full)">\s*<h1 class="text-3xl lg:text-4xl font-black tracking-wider m-0 text-\[var\(--klimt-red\)\]">Sruthi Korlakunta</h1>\s*<div class="space-x-6 text-xl">')
    
    nav_replacement = r'''<nav class="flex flex-col md:flex-row justify-between items-center mb-8 md:mb-12\1 gap-4">
        <h1 class="text-2xl md:text-3xl lg:text-4xl font-black tracking-wider m-0 text-[var(--klimt-red)] text-center">Sruthi Korlakunta</h1>
        <div class="flex flex-wrap justify-center gap-4 md:space-x-6 md:gap-0 text-base md:text-xl">'''
    
    content = re.sub(nav_pattern, nav_replacement, content)

    # 3. Bento Box Padding in CSS
    bento_pattern = re.compile(r'(\.bento-box\s*\{[^}]*?padding:\s*)(2\.5rem|3rem)(;[^}]*?\})')
    def bento_repl(m):
        orig_pad = m.group(2)
        return m.group(1) + '1.5rem' + m.group(3) + f'\n        @media (min-width: 768px) {{\n            .bento-box {{\n                padding: {orig_pad};\n            }}\n        }}'
    
    content = re.sub(bento_pattern, bento_repl, content)

    # 4. Stick figures mobile interactivity
    # Add a script at the end of body to handle touch for dancers and cards
    touch_script = """
    <script>
        // Mobile touch support for dancers
        document.querySelectorAll('.dancer').forEach(dancer => {
            dancer.addEventListener('touchstart', (e) => {
                dancer.style.zIndex = '100';
            });
        });
    </script>
</body>"""
    if '// Mobile touch support for dancers' not in content:
        content = content.replace('</body>', touch_script)

    if filename == 'index.html':
        # Pacman touch controls
        pacman_canvas = '<canvas id="pacman-canvas" width="400" height="400"></canvas>'
        pacman_canvas_mobile = '<canvas id="pacman-canvas" width="400" height="400" style="max-width: 100%; height: auto; touch-action: none;"></canvas>'
        content = content.replace(pacman_canvas, pacman_canvas_mobile)
        
        content = content.replace('Use Arrow Keys to Navigate.', 'Use Arrow Keys or Swipe to Navigate.')

        swipe_script = """
        let touchStartX = 0;
        let touchStartY = 0;
        canvas.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
        }, {passive: false});

        canvas.addEventListener('touchend', function(e) {
            if(gameOver) return;
            let touchEndX = e.changedTouches[0].screenX;
            let touchEndY = e.changedTouches[0].screenY;
            let dx = touchEndX - touchStartX;
            let dy = touchEndY - touchStartY;
            if (Math.abs(dx) > Math.abs(dy)) {
                if (dx > 30) { pacman.dx = 1; pacman.dy = 0; pacman.angle = 0; }
                else if (dx < -30) { pacman.dx = -1; pacman.dy = 0; pacman.angle = Math.PI; }
            } else {
                if (dy > 30) { pacman.dx = 0; pacman.dy = 1; pacman.angle = Math.PI/2; }
                else if (dy < -30) { pacman.dx = 0; pacman.dy = -1; pacman.angle = -Math.PI/2; }
            }
        }, {passive: false});
        
        // Prevent scrolling when touching canvas
        canvas.addEventListener('touchmove', function(e) {
            e.preventDefault();
        }, {passive: false});
        """
        if 'touchStartX = 0;' not in content:
            content = content.replace('document.addEventListener(\'keydown\'', swipe_script + '\n        document.addEventListener(\'keydown\'')

    if filename == 'summary.html':
        # Make the tree container responsive
        content = content.replace('class="tree-container"', 'class="tree-container overflow-x-auto"')
        
    with open(filename, 'w') as f:
        f.write(content)

print("Done")
