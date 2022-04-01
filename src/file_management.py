from pathlib import Path
from json import load

def homepath():
    return Path.home()/"Documents"/"MusicProgrammes"

def sourcepath():
    return Path.cwd()/"src"

def jsontemplates():
    return Path.cwd()/"json_templates"

def validate(filepath):
    if not Path.exists(filepath):
        Path.mkdir(filepath)

validate(homepath())