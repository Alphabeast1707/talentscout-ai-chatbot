#!/bin/bash

echo "🚀 TalentScout AI Chatbot - Heroku Deployment"
echo "=============================================="
echo ""

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI is not installed. Please install it first:"
    echo "   brew tap heroku/brew && brew install heroku"
    exit 1
fi

# Check if user is logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "🔐 Please log in to Heroku first:"
    heroku login
    echo ""
fi

# Get app name from user
if [ -z "$1" ]; then
    echo "📝 Please provide your Heroku app name:"
    echo "Usage: ./deploy_to_heroku.sh <your-app-name>"
    echo ""
    echo "Example: ./deploy_to_heroku.sh talentscout-ai-harshit"
    echo ""
    echo "💡 App name must be unique across all Heroku apps"
    echo "   Suggested names:"
    echo "   - talentscout-ai-$(whoami)"
    echo "   - interview-ai-$(date +%Y%m%d)"
    echo "   - talentscout-$(random)"
    exit 1
fi

APP_NAME="$1"

echo "📋 Deployment Information:"
echo "   App Name: $APP_NAME"
echo "   Region: us (default)"
echo "   Stack: heroku-22"
echo ""

# Check if we're in the right directory
if [ ! -f "src/app.py" ]; then
    echo "❌ Error: Please run this script from the talentscout-chatbot project directory"
    exit 1
fi

# Check if all required files exist
echo "🔍 Checking deployment files..."
files_needed=("Procfile" "requirements.txt" "runtime.txt")
for file in "${files_needed[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Missing required file: $file"
        exit 1
    else
        echo "✅ Found: $file"
    fi
done

# Check if API key is set in environment
if [ -z "$GROQ_API_KEY" ]; then
    echo ""
    echo "⚠️  GROQ_API_KEY not found in environment variables"
    echo "   We'll need to set it on Heroku after deployment"
    echo ""
fi

echo ""
echo "🏗️  Creating Heroku app..."
heroku create "$APP_NAME" --region us

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Failed to create Heroku app. Possible reasons:"
    echo "   1. App name '$APP_NAME' is already taken"
    echo "   2. Invalid app name (must be lowercase, alphanumeric, dashes only)"
    echo "   3. Network connection issues"
    echo ""
    echo "💡 Try a different app name or check if the app already exists:"
    echo "   heroku apps | grep $APP_NAME"
    exit 1
fi

echo ""
echo "⚙️  Setting up configuration..."

# Set Python buildpack
heroku buildpacks:set heroku/python --app "$APP_NAME"

# Set environment variables
if [ -f ".env" ] && [ -n "$GROQ_API_KEY" ]; then
    echo "🔑 Setting GROQ_API_KEY..."
    heroku config:set GROQ_API_KEY="$GROQ_API_KEY" --app "$APP_NAME"
else
    echo "⚠️  Skipping API key setup (not found in environment)"
fi

# Add Heroku remote if it doesn't exist
if ! git remote | grep -q heroku; then
    echo "🔗 Adding Heroku remote..."
    heroku git:remote --app "$APP_NAME"
else
    echo "🔗 Heroku remote already exists"
fi

echo ""
echo "📤 Deploying to Heroku..."
git add .
git commit -m "Prepare for Heroku deployment

- Add Procfile for web dyno configuration
- Add runtime.txt specifying Python version
- Add pyproject.toml for project metadata
- Configure Streamlit for Heroku hosting" 2>/dev/null || echo "No changes to commit"

git push heroku main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your app has been deployed to Heroku!"
    echo ""
    echo "🌐 App URL: https://$APP_NAME.herokuapp.com"
    echo "📊 Dashboard: https://dashboard.heroku.com/apps/$APP_NAME"
    echo ""
    
    # Check if API key was set
    if [ -z "$GROQ_API_KEY" ]; then
        echo "⚠️  IMPORTANT: Set your Groq API key"
        echo "   Run: heroku config:set GROQ_API_KEY=\"your_api_key_here\" --app $APP_NAME"
        echo "   Or set it via the Heroku dashboard"
        echo ""
    fi
    
    echo "📝 Next steps:"
    echo "   1. Visit your app: https://$APP_NAME.herokuapp.com"
    echo "   2. Test the functionality"
    echo "   3. Monitor logs: heroku logs --tail --app $APP_NAME"
    echo "   4. Scale if needed: heroku ps:scale web=1 --app $APP_NAME"
    echo ""
    
    # Open the app in browser
    echo "🌐 Opening your app in browser..."
    heroku open --app "$APP_NAME"
    
else
    echo ""
    echo "❌ Deployment failed. Check the logs for details:"
    echo "   heroku logs --tail --app $APP_NAME"
    echo ""
    echo "🔧 Common issues and solutions:"
    echo "   1. Dependencies: Check requirements.txt"
    echo "   2. Python version: Verify runtime.txt"
    echo "   3. Port binding: Ensure Procfile uses \$PORT"
    echo "   4. API key: Set GROQ_API_KEY config var"
fi
