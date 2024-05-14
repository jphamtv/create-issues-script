### Quick Issue Creation Script

1. Install the GitHub CLI (gh) by following the instructions at https://cli.github.com.
2. Authenticate with GitHub using the command:
```
gh auth login
```
3. Save the code to a file named create-multiple-issues.py.
4. Replace `repo` on line 6 in the code with your own GitHub username and repository:
```
repo = "your-username/your-repository"
```
5. Open a terminal or command prompt, navigate to the directory where you saved the file, and run the following command:
```
python create-multiple-issues.py
```
The script will execute and create the specified issues in your repository using the GitHub CLI.
