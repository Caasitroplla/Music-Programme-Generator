from pathlib import Path

def homepath():
    return Path.home()/"Documents"/"Programme Generator"

def sourcepath():
    return Path.cwd()/"src"

def jsontemplates():
    return Path.cwd()/"json_templates"

def validate(filepath):
    if not Path.exists(filepath):
        try:
            Path.mkdir(filepath)
        except FileNotFoundError:
            validate(Path(filepath).parent)
            Path.mkdir(filepath)

validate(homepath())