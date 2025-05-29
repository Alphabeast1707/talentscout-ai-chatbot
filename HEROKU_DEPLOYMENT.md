# Heroku Deployment Guide for TalentScout AI Chatbot

## Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git repository set up
- Groq API key

## Quick Deployment

### Option 1: Automated Script (Recommended)
```bash
# Use the deployment script
./deploy_to_heroku.sh your-unique-app-name

# Example:
./deploy_to_heroku.sh talentscout-ai-harshit
```

### Option 2: Manual Deployment
```bash
# 1. Login to Heroku
heroku login

# 2. Create Heroku app
heroku create your-app-name --region us

# 3. Set environment variables
heroku config:set GROQ_API_KEY="your_groq_api_key_here" --app your-app-name

# 4. Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# 5. Open your app
heroku open --app your-app-name
```

## Configuration Files Added

### Procfile
Tells Heroku how to run your app:
```
web: streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0
```

### runtime.txt
Specifies Python version:
```
python-3.11.9
```

### .streamlit/config.toml
Optimizes Streamlit for production:
- Headless mode enabled
- CORS disabled for security
- Custom theme colors
- Error details enabled for debugging

## Environment Variables
Set these in Heroku dashboard or via CLI:
- `GROQ_API_KEY`: Your Groq API key (required)

## Monitoring & Maintenance

### View Logs
```bash
heroku logs --tail --app your-app-name
```

### Scale Dynos
```bash
# Scale up
heroku ps:scale web=1 --app your-app-name

# Scale down (save costs)
heroku ps:scale web=0 --app your-app-name
```

### Update App
```bash
# Make changes, then:
git add .
git commit -m "Update description"
git push heroku main
```

## Troubleshooting

### Common Issues

1. **App crashes on startup**
   - Check logs: `heroku logs --app your-app-name`
   - Verify GROQ_API_KEY is set
   - Check Python version in runtime.txt

2. **Port binding errors**
   - Ensure Procfile uses $PORT variable
   - Verify Streamlit config uses 0.0.0.0 address

3. **API key not working**
   - Set via CLI: `heroku config:set GROQ_API_KEY="key" --app name`
   - Or via dashboard: Settings → Config Vars

4. **Build failures**
   - Check requirements.txt dependencies
   - Verify Python version compatibility

### Performance Tips

1. **Free Tier Limitations**
   - Sleeps after 30 minutes of inactivity
   - 550 dyno hours per month
   - Consider upgrading for production use

2. **Optimization**
   - Use caching in Streamlit (@st.cache_data)
   - Minimize API calls where possible
   - Consider using faster Groq models for quick responses

## Cost Optimization

### Free Tier Usage
- Monitor dyno hours in dashboard
- Scale down when not in use
- Use sleep/wake cycle efficiently

### Paid Plans
- Hobby ($7/month): No sleep, custom domains
- Standard ($25/month): Better performance, metrics
- Performance ($250/month): Dedicated resources

## Security Considerations

1. **API Keys**
   - Never commit API keys to Git
   - Use Heroku config vars only
   - Rotate keys regularly

2. **HTTPS**
   - Heroku provides SSL by default
   - Custom domains need SSL certificates

3. **Access Control**
   - Consider adding authentication for production
   - Monitor usage and set rate limits

## Support Resources

- **Heroku Documentation**: https://devcenter.heroku.com/
- **Streamlit Deployment**: https://docs.streamlit.io/knowledge-base/deploy/
- **TalentScout Issues**: https://github.com/Alphabeast1707/talentscout-ai-chatbot/issues
