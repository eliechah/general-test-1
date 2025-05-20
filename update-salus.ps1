# Update Salus submodule and sync scanner files into root

Set-Location salus
git pull origin main
Set-Location ..

# Copy scanner workflow and configs from submodule into main repo
Copy-Item -Recurse -Force salus\.github .\
Copy-Item -Recurse -Force salus\configs .\

# Commit and push updated files
git add .github configs
git commit -m "Update Salus scanner files"
git push



# Any permission errors, run the following:
#
#   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned