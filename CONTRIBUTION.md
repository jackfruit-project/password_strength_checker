
  # Contributing Guide
  This repository belongs to an organization, and all four members have Owner access. Contributors may use either the fork workflow or direct contribution workflow (owners only). Both are detailed below.
  # 🪝 Option 1: Fork the Repository (Recommended for External Contributors)
  ## 1. Fork the Repository
  Click the Fork button on GitHub to create a copy under your account.
  ## 2. Clone Your Fork
      git clone https://github.com/<your-username>/<repo-name>.git
  ## 3. Enter the Project Directory
      cd <repo-name>
  ## 4. Create a New Branch
      git checkout -b feature-name
  ## 5. Make Your Changes
  Modify code, documentation, or features as needed.
  ## 6. Stage & Commit
      git add .
      git commit -m "Describe your changes"
  ## 7. Push to Your Fork
      git push origin feature-name
  ## 8. Open a Pull Request
  Go to your fork → Compare & Pull Request → Submit.
  # 🔓 Option 2: Contribute Directly to the Organization Repository (Owners Only)
  ## 1. Clone the Main Repository
      git clone https://github.com/<org-name>/<repo-name>.git
  ## 2. Enter the Project Directory
      cd <repo-name>
  ## 3. Create a New Branch (Never push directly to main)
      git checkout -b feature-name
  Examples: add-login-route, fix-db-connection, update-readme, implement-ui-endpoints
  ## 4. Make Your Changes
  Implement updates, fixes, or features.
  ## 5. Stage & Commit
      git add .
      git commit -m "Describe your changes"
  ## 6. Push Branch to Main Repo
      git push origin feature-name
  ## 7. Open a Pull Request
  Go to the organization repo → Switch to your branch → Open Pull Request → Add title & description → Submit.
  # 🔄 Keeping Your Local Repo Updated
  ## For organization members:
      git checkout main
      git pull origin main
  ## For fork users:
      git remote add upstream https://github.com/<org-name>/<repo-name>.git
      git fetch upstream
      git merge upstream/main
  # 🤝 Contribution Rules
  - Never push directly to main (even Owners)
  - All changes must go through a Pull Request
  - PR descriptions must be clear
  - At least one teammate review before merging
  # 🎉 Thank You
  Whether you're a core member or an external contributor, your contributions help strengthen this project!

