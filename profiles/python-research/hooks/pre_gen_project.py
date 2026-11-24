import keyword
import re
import sys


# JSON encoding preserves strings even when a supplied value contains quotes.
slug = {{ cookiecutter.project_slug | tojson }}
package = {{ cookiecutter.package_name | tojson }}
owner = {{ cookiecutter.quality_owner | tojson }}

if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", slug):
    sys.exit("project_slug must be a lowercase Git repository name with optional hyphens.")
if not re.fullmatch(r"[a-z][a-z0-9_]*", package) or keyword.iskeyword(package):
    sys.exit("package_name must be a valid lowercase Python import name.")
if owner != "CHANGE_ME" and not re.fullmatch(
    r"@[A-Za-z0-9-]+(?:/[A-Za-z0-9_-]+)?", owner
):
    sys.exit("quality_owner must be a GitHub @user or @org/team.")
