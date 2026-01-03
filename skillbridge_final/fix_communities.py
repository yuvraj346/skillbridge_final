with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace main.communities with service.browse
content = content.replace("url_for('main.communities')", "url_for('service.browse')")

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed main.communities references in index.html")
