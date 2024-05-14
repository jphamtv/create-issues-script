import subprocess

# Script for quickly creating issues
# Run file with 'python create-multiple-issues.py' using GH CLI

repo = "your-username/your-repository"

# Create 1 Prework Checklist issue
for i in range(1):
    title = "Pre-work Checklist: Developer: Test"
    description = "This is a checklist."
    labels = "Complexity: Prework,role: front end,role: back end/devOps,size: 1pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 3 Good first issues with any roles
for i in range(3):
    title = "Good first issue"
    description = "This is a good first issue."
    labels = "P-Feature: Home page,good first issue,role: front end,role: back end/devOps,size: 1pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Small Issues with front end role
for i in range(2):
    title = "Small issue"
    description = "This is a small issue."
    labels = "P-Feature: Home page,Complexity: Small,role: front end,size: 1pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Small issues with back end role
for i in range(2):
    title = "Small issue"
    description = "This is a small issue."
    labels = "P-Feature: Home page,Complexity: Small,role: back end/devOps,size: 1pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Small issues with both roles
for i in range(2):
    title = "Small issue"
    description = "This is a small issue."
    labels = "P-Feature: Home page,Complexity: Small,role: front end,role: back end/devOps,size: 1pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Medium Issues with front end role
for i in range(2):
    title = "Medium issue"
    description = "This is a medium issue."
    labels = "P-Feature: Home page,Complexity: Medium,role: front end,size: 2pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Medium issues with back end role
for i in range(2):
    title = "Medium issue"
    description = "This is a medium issue."
    labels = "P-Feature: Home page,Complexity: Medium,role: back end/devOps,size: 2pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Medium issues with both roles
for i in range(2):
    title = "Medium issue"
    description = "This is a medium issue."
    labels = "P-Feature: Home page,Complexity: Medium,role: front end,role: back end/devOps,size: 2pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")

# Create 2 Large Issues with any roles
for i in range(2):
    title = "Large issue"
    description = "This is a large issue."
    labels = "P-Feature: Home page,Complexity: Large,role: front end,role: back end/devOps,size: 5pt"
    command = f'gh issue create --repo {repo} --title "{title}" --body "{description}" --label "{labels}"'
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
    print("----------------------")
