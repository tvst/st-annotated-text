import os
import sys
from urllib.parse import quote

from github import Github

# Authenticate with GitHub
access_token = os.getenv("GITHUB_TOKEN")
g = Github(access_token)


repo_name = "tvst/st-annotated-text"
commit_sha = sys.argv[1]  # e.g d39677a321bca34df41ecc87ff7e539b450207f2
run_id = sys.argv[2]  # e.g 1324, usually obtained via ${{ github.run_id }} or ${{ github.event.workflow_run.id }} in GitHub Actions workflow files
type = "streamlit"  # streamlit/dash/vizro/solara/panel

# take the code from the PR/commit, not master
code = f"https://github.com/tvst/st-annotated-text/raw/{commit_sha}/example.py"

artifact_name = "st-annotated-text-wheel"  # name given in the GitHub Actions workflow file for the artifact


# parse the version from the setup.py file, i.e.
#    version="4.0.1",

path = "setup.py"
import re
content = open(path).read()
version = re.search(r'version="(.*)",', content).group(1)
print(f"Version: {version}")

requirements = f"""
https://py.cafe/gh/artifact/{repo_name}/actions/runs/{run_id}/{artifact_name}/st_annotated_text-{version}-py3-none-any.whl
"""

# GitHub Python API
repo = g.get_repo(repo_name)

base_url = f"https://py.cafe/snippet/{type}/v1"
url = f"{base_url}#code={quote(code)}&requirements={quote(requirements)}"

# Define the deployment status
state = "success"  # Options: 'error', 'failure', 'pending', 'success'
description = "Test out this PR on a PyCafe playground environment"
context = "PyCafe"

# Create the status on the commit
commit = repo.get_commit(commit_sha)
commit.create_status(state="success", target_url=url, description=description, context="PyCafe")
print(f"Deployment status added to commit {commit_sha}")
