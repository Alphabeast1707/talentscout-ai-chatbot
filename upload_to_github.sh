#!/bin/bash

echo "🚀 TalentScout AI Chatbot - GitHub Upload Helper"
echo "================================================="
echo ""

# Check if GitHub username is provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide your GitHub username"
    echo "Usage: ./upload_to_github.sh <your-github-username>"
    echo ""
    echo "Example: ./upload_to_github.sh Alphabeast1707"
    exit 1
fi

GITHUB_USERNAME="$1"
REPO_NAME="talentscout-ai-chatbot"

echo "📋 Repository Information:"
echo "   GitHub Username: $GITHUB_USERNAME"
echo "   Repository Name: $REPO_NAME"
echo "   Repository URL: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""

# Check if we're in the right directory
if [ ! -f "src/app.py" ]; then
    echo "❌ Error: Please run this script from the talentscout-chatbot project directory"
    exit 1
fi

echo "🔗 Adding GitHub remote..."
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

if [ $? -eq 0 ]; then
    echo "✅ Remote origin added successfully"
else
    echo "⚠️  Remote might already exist, continuing..."
fi

echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your project has been uploaded to GitHub!"
    echo "🌐 View your repository at: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    echo ""
    echo "📝 Next steps:"
    echo "   1. Visit your repository on GitHub"
    echo "   2. Add a proper description if needed"
    echo "   3. Add topics/tags for better discoverability"
    echo "   4. Consider adding a license"
    echo ""
else
    echo ""
    echo "❌ Upload failed. Please check:"
    echo "   1. Repository exists on GitHub"
    echo "   2. Repository name is correct"
    echo "   3. You have push permissions"
    echo "   4. Your GitHub credentials are correct"
fi
