import os

icon_svg = '''        <svg class="gemma-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="face-grad" cx="40%" cy="40%" r="70%">
                    <stop offset="0%" stop-color="#FFD1E3"/>
                    <stop offset="60%" stop-color="#FF9EBB"/>
                    <stop offset="100%" stop-color="#E86A92"/>
                </radialGradient>
                <radialGradient id="gill-grad" cx="30%" cy="30%" r="70%">
                    <stop offset="0%" stop-color="#FF9EBB"/>
                    <stop offset="100%" stop-color="#E86A92"/>
                </radialGradient>
                <radialGradient id="eye-grad" cx="40%" cy="40%" r="60%">
                    <stop offset="0%" stop-color="#3A3A3A"/>
                    <stop offset="100%" stop-color="#1A1A1A"/>
                </radialGradient>
                <filter id="drop-shadow" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#4A0E17" flood-opacity="0.3"/>
                </filter>
            </defs>
            <g filter="url(#drop-shadow)">
                <path d="M 25 35 Q 5 25 15 15 Q 25 25 30 38" fill="url(#gill-grad)" />
                <path d="M 22 45 Q -5 45 5 30 Q 18 35 25 48" fill="url(#gill-grad)" />
                <path d="M 25 55 Q 5 65 15 75 Q 25 65 30 52" fill="url(#gill-grad)" />
                <path d="M 75 35 Q 95 25 85 15 Q 75 25 70 38" fill="url(#gill-grad)" />
                <path d="M 78 45 Q 105 45 95 30 Q 82 35 75 48" fill="url(#gill-grad)" />
                <path d="M 75 55 Q 95 65 85 75 Q 75 65 70 52" fill="url(#gill-grad)" />
                <ellipse cx="50" cy="50" rx="35" ry="28" fill="url(#face-grad)" />
                <ellipse cx="35" cy="46" rx="8" ry="10" fill="url(#eye-grad)" />
                <ellipse cx="65" cy="46" rx="8" ry="10" fill="url(#eye-grad)" />
                <circle cx="33" cy="42" r="3.5" fill="#FFFFFF" />
                <circle cx="37" cy="48" r="1.5" fill="#FFFFFF" opacity="0.8"/>
                <circle cx="63" cy="42" r="3.5" fill="#FFFFFF" />
                <circle cx="67" cy="48" r="1.5" fill="#FFFFFF" opacity="0.8"/>
                <ellipse cx="25" cy="54" rx="6" ry="4" fill="#E86A92" opacity="0.4" />
                <ellipse cx="75" cy="54" rx="6" ry="4" fill="#E86A92" opacity="0.4" />
                <path d="M 45 58 Q 50 64 55 58" fill="none" stroke="#A33258" stroke-width="2.5" stroke-linecap="round" />
            </g>
        </svg>'''

css_old = '''        .gemma-label {
            display: block;
            font-family: 'Cinzel Decorative', serif;
            font-weight: 900;
            font-size: 0.8rem;
            text-transform: uppercase;
            color: var(--klimt-black);
            margin-bottom: 0.5rem;
            border-bottom: 1px solid var(--klimt-red);
            padding-bottom: 2px;
        }'''

css_new = '''        .gemma-label {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-family: 'Cinzel Decorative', serif;
            font-weight: 900;
            font-size: 0.8rem;
            text-transform: uppercase;
            color: var(--klimt-black);
            margin-bottom: 0.5rem;
            border-bottom: 1px solid var(--klimt-red);
            padding-bottom: 2px;
        }
        .gemma-icon {
            width: 35px;
            height: 35px;
            flex-shrink: 0;
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-3px); }
        }'''

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    with open(filename, 'r') as f:
        content = f.read()

    if css_old in content or '<span class="gemma-label">Gemma says:</span>' in content:
        content = content.replace(css_old, css_new)
        
        replacement = f'<span class="gemma-label">\n{icon_svg}\n            Gemma says:\n        </span>'
        content = content.replace('<span class="gemma-label">Gemma says:</span>', replacement)

        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")

