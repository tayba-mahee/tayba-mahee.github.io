# Quick Deployment Guide

## 🚀 Deploy Your Portfolio to GitHub Pages

Follow these steps to get your portfolio live on the web!

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `maheetayba.github.io` (or any name for project pages)
3. Make it Public
4. Don't initialize with README (we already have content)
5. Click "Create repository"

### Step 2: Push Your Code

Open Terminal and run these commands:

```bash
# Navigate to your site directory
cd /Users/maheetayba/Developer/copilot-resume-site

# Initialize git (if not already done)
git init

# Add all files
git add -A

# Commit
git commit -m "Initial commit: Professional portfolio website"

# Add remote (replace with your actual repo URL)
git remote add origin https://github.com/maheetayba/maheetayba.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

The Chirpy theme includes GitHub Actions that will automatically build and deploy your site!

1. Go to your repository on GitHub
2. Click **Settings** (gear icon)
3. Click **Pages** in the left sidebar
4. Under "Source", select **GitHub Actions**
5. Wait 1-2 minutes for the first deployment

### Step 4: Update Configuration

Before or after deployment, update `_config.yml`:

```yaml
# Update this line with your actual GitHub Pages URL
url: "https://maheetayba.github.io"

# If using a custom repo name (not username.github.io):
# url: "https://maheetayba.github.io"
# baseurl: "/your-repo-name"
```

Then commit and push:

```bash
git add _config.yml
git commit -m "Update site URL"
git push
```

### Step 5: View Your Live Site

**For username.github.io:**
- Your site will be at: https://maheetayba.github.io

**For project repository:**
- Your site will be at: https://maheetayba.github.io/repository-name

## 🔍 Troubleshooting

### Build Failed?

1. Check the **Actions** tab in your GitHub repository
2. Click on the failed workflow to see error details
3. Common issues:
   - `_config.yml` syntax error
   - Invalid markdown in posts
   - Missing frontmatter in posts

### Site Not Showing?

1. Check if GitHub Actions workflow completed (green checkmark)
2. Verify GitHub Pages is enabled in Settings → Pages
3. Try hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
4. Wait a few minutes - initial deployment can take 5-10 minutes

### 404 Error?

- Make sure `baseurl` in `_config.yml` is correct:
  - Empty for username.github.io: `baseurl: ""`
  - Repository name for project pages: `baseurl: "/repo-name"`

## ✨ Optional Enhancements

### Add LinkedIn Badge

Edit `_config.yml`:

```yaml
social:
  links:
    - https://github.com/maheetayba
    - https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME
```

### Add Profile Picture

1. Add image to `assets/img/avatar.jpg`
2. Edit `_config.yml`:
   ```yaml
   avatar: /assets/img/avatar.jpg
   ```
3. Commit and push

### Enable Comments

Choose a comment system (Giscus recommended):

1. Go to https://giscus.app
2. Follow setup instructions
3. Update `_config.yml` with your Giscus settings
4. Commit and push

### Add Google Analytics

1. Create GA4 property at https://analytics.google.com
2. Copy your Measurement ID (G-XXXXXXXXXX)
3. Edit `_config.yml`:
   ```yaml
   analytics:
     google:
       id: 'G-XXXXXXXXXX'
   ```
4. Commit and push

## 📝 Updating Your Site

Whenever you want to update content:

```bash
cd /Users/maheetayba/Developer/copilot-resume-site

# Edit files (posts, pages, etc.)

# Test locally
export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:$PATH"
bundle exec jekyll serve --host 127.0.0.1

# When ready, commit and push
git add -A
git commit -m "Description of changes"
git push
```

GitHub Actions will automatically rebuild and redeploy your site!

## 🎉 You're Done!

Your professional portfolio is now live! Share it with:
- Potential employers
- Academic colleagues
- Research collaborators
- On your LinkedIn profile
- In your email signature

---

**Need Help?** Check README-PORTFOLIO.md for more detailed documentation.
