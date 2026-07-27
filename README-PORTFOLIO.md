# Mahee Noor Tayba - Portfolio Website

A professional portfolio website built with Jekyll and the Chirpy theme, showcasing academic and professional work in computer science.

## 🌟 Features

- **About Me**: Professional bio with education and research interests
- **Projects**: Detailed case studies of key projects
- **Publications**: Research papers with links and descriptions
- **Teaching Experience**: Comprehensive teaching history and philosophy
- **Research Experience**: Graduate research work and contributions
- **Blog**: Technical writing on machine learning, HCI, and education
- **Responsive Design**: Works beautifully on all devices
- **Dark/Light Theme**: Toggle between themes
- **Search**: Built-in search functionality
- **PWA**: Installable as a progressive web app

## 📁 Site Structure

```
copilot-resume-site/
├── _config.yml           # Site configuration
├── _tabs/                # Main navigation pages
│   ├── about.md         # About page
│   ├── projects.md      # Projects portfolio
│   ├── publications.md  # Research publications
│   ├── teaching.md      # Teaching experience
│   ├── research.md      # Research experience
│   ├── archives.md      # Blog archives
│   ├── categories.md    # Post categories
│   └── tags.md          # Post tags
├── _posts/              # Blog posts
├── assets/              # Static assets
│   └── resume-MaheeTayba.pdf # Downloadable resume
└── _site/               # Generated site (auto-created)
```

## 🚀 Local Development

### Prerequisites

- Ruby 3.3
- Bundler
- Jekyll

### Running Locally

1. Navigate to the site directory:
   ```bash
   cd /Users/maheetayba/Developer/copilot-resume-site
   ```

2. Set up Ruby environment:
   ```bash
   export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:$PATH"
   ```

3. Build the site:
   ```bash
   bundle exec jekyll build
   ```

4. Serve locally:
   ```bash
   bundle exec jekyll serve --host 127.0.0.1
   ```

5. Visit: http://127.0.0.1:4000

## 📝 Adding Content

### New Blog Post

Create a file in `_posts/` with format: `YYYY-MM-DD-title.md`

```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS -0600
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
---

Your content here...
```

### Update About Page

Edit `_tabs/about.md` to update your bio and information.

### Add New Project

Edit `_tabs/projects.md` and add your project details.

### Update Publications

Edit `_tabs/publications.md` to add new research papers.

## 🚢 Deployment to GitHub Pages

### Option 1: Username GitHub Pages Site

1. Create a repository named `maheetayba.github.io`
2. Push this code to the repository:
   ```bash
   cd /Users/maheetayba/Developer/copilot-resume-site
   git init
   git add -A
   git commit -m "Initial commit: Portfolio website"
   git branch -M main
   git remote add origin https://github.com/maheetayba/maheetayba.github.io.git
   git push -u origin main
   ```
3. Your site will be available at: `https://maheetayba.github.io`

### Option 2: Project GitHub Pages Site

1. Create any repository (e.g., `portfolio`)
2. Push this code to the repository
3. Go to Settings → Pages
4. Set source to "GitHub Actions"
5. The site will be available at: `https://maheetayba.github.io/portfolio`

**Note:** The Chirpy theme includes GitHub Actions workflow automatically! It will build and deploy on every push.

## 🔧 Configuration

### Update _config.yml

Key settings in `_config.yml`:

```yaml
title: Your Name
tagline: Your tagline
url: "https://maheetayba.github.io"  # Update this for deployment
github:
  username: maheetayba
social:
  name: Your Full Name
  email: your.email@example.com
```

### Adding Social Links

Uncomment and update social links in `_config.yml`:

```yaml
social:
  links:
    - https://github.com/maheetayba
    - https://www.linkedin.com/in/mahee-noor-tayba/
```

### Adding Google Analytics

Add your GA ID in `_config.yml`:

```yaml
analytics:
  google:
    id: 'G-XXXXXXXXXX'
```

## 📱 Custom Domain (Optional)

1. Add a `CNAME` file with your domain:
   ```bash
   echo "yourdomain.com" > CNAME
   ```

2. Configure DNS with your domain provider:
   - Add A records pointing to GitHub's IPs
   - Or add CNAME record pointing to `maheetayba.github.io`

3. In GitHub repo settings → Pages, add your custom domain

## 🎨 Customization

### Adding Profile Picture

1. Add your image to `assets/img/`
2. Update `_config.yml`:
   ```yaml
   avatar: /assets/img/yourphoto.jpg
   ```

### Changing Theme Colors

Create `assets/css/jekyll-theme-chirpy.scss` for custom styles (advanced).

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Chirpy Theme Wiki](https://github.com/cotes2020/jekyll-theme-chirpy/wiki)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

## ✅ What's Already Done

- ✓ Jekyll and Chirpy theme setup complete
- ✓ All content pages created (About, Projects, Publications, Teaching, Research)
- ✓ Three initial blog posts added
- ✓ Resume PDF available for download
- ✓ Site configuration completed
- ✓ SEO metadata configured
- ✓ Dark/light theme enabled
- ✓ Search functionality enabled
- ✓ PWA features enabled
- ✓ Responsive design working

## 🎯 Next Steps

1. **Review Content**: Check all pages and blog posts for accuracy
2. **Add Profile Picture**: Add your photo to assets/img/ and update config
3. **Create GitHub Repository**: Set up your repository
4. **Deploy**: Push to GitHub and enable GitHub Pages
5. **Test Live Site**: Verify everything works after deployment
6. **Optional**: Add Google Analytics, comment system, or custom domain
7. **Maintain**: Regularly add blog posts and update projects

## 📞 Support

For issues with:
- **Jekyll**: https://talk.jekyllrb.com/
- **Chirpy Theme**: https://github.com/cotes2020/jekyll-theme-chirpy/issues
- **GitHub Pages**: https://docs.github.com/en/pages

---

Built with ❤️ using Jekyll and Chirpy Theme
