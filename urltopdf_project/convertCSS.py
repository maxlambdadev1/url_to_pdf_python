import sass

compiled_css = sass.compile(filename='custom.alchemix-finance.gitbook.io.css')

with open('output.css', 'w') as f:
    f.write(compiled_css)