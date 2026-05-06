import os
import re

files_to_update = ['index.html', 'about.html', 'events.html', 'gallery.html', 'training.html']
base_dir = r'e:\chinharimodels'

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements that are safe
    # Navbar links
    content = content.replace('>Training<', '>Chinhari Academy<')
    # Footer links
    content = content.replace('>Training Academy<', '>Chinhari Academy<')
    
    # Specific buttons and titles
    content = content.replace('>Join Academy<', '>Join Chinhari Academy<')
    content = content.replace('>Model Training<', '>Chinhari Academy<')
    content = content.replace('training academy', 'Chinhari Academy')
    content = content.replace('Training - Chinhari Models', 'Chinhari Academy - Chinhari Models')
    content = content.replace('Register via Training Academy', 'Register via Chinhari Academy')
    content = content.replace('Chinhari Models Training Academy', 'Chinhari Academy')
    content = content.replace('Join Our <em>Training Academy</em>', 'Join <em>Chinhari Academy</em>')
    
    # Any other leftover "training academy" case variations
    content = content.replace('Training academy', 'Chinhari Academy')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement complete.")
