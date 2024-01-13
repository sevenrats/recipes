#!/usr/bin/python3
from recipe_scrapers import scrape_me

import json, sys

from pathlib import Path

DEFAULT_CONFIG = {
    "local": str(Path.home()/"recipes")
        }

APPLIED_CONFIG = {}
# load or create config
configPath = Path.home()/"recipes.conf"
if configPath.exists():
    if not configPath.is_file():
        raise Exception("Config path exists but is not a regular file!")
    try:
        config = json.loads(configPath.read_text())
    except:
        config = DEFAULT_CONFIG
else:
    config = DEFAULT_CONFIG
    configPath.write_text(json.dumps(config))

APPLIED_CONFIG = config

uri = sys.argv[1]
recipe = scrape_me(uri, wild_mode=True)

output = f"# {recipe.title()}\n\n"
if len(recipe.ingredient_groups()) > 1:
    raise Exception("multiple ingredient groups not yet implemented")
else:
    for ingredient in recipe.ingredients():
        output += f"- {ingredient}\n"
output += "\n## Instructions\n\n"
for instruction in recipe.instructions_list():
    output += f"{instruction}\n\n"

print(output)