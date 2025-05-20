#!/bin/bash
cd salus
git pull origin main
cd ..
cp -r salus/.github .
cp -r salus/configs .
git add .github configs
git commit -m "Update Salus scanner files"
git push