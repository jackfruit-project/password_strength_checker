
  # Contributing Guide
 Follow the steps below tomake changes using the Fork → Clone → Edit → Push → Pull Request workflow.
  ## 1. Fork the Repository
  1. Open the repository on GitHub.
  2. Click the Fork button (top right corner).
  3. GitHub will create a copy of the repository in your GitHub account.
  ## 2. Clone Your Fork
  Run:
      git clone https://github.com/<your-username>/<repo-name>.git
  Replace <your-username> and <repo-name> accordingly.
  ## 3. Navigate Into the Project Folder
      cd <repo-name>
  ## 4. Create a New Branch (Recommended)
      git checkout -b feature-name
  Examples: fix-typo, add-auth-api, ui-improvements
  ## 5. Make Your Changes
  Modify code, fix bugs, add features, or improve documentation.
  ## 6. Stage and Commit Your Changes
      git add .
      git commit -m "Describe your changes here"
  ## 7. Push Your Branch to Your Fork
      git push origin feature-name
  ## 8. Create a Pull Request (PR)
  1. Open your fork on GitHub.
  2. Click Compare & Pull Request.
  3. Add a title and description.
  4. Submit the PR.
  ## 9. (Optional) Keep Your Fork Updated
      git remote add upstream https://github.com/<original-owner>/<repo-name>.git
      git fetch upstream
      git merge upstream/main
  
