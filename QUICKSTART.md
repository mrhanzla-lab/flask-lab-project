# Quick Start Guide for CI/CD Submission

## What I've Set Up For You

✅ **Fixed Issues:**
- Fixed `__name__` typo in `main/app.py`
- Added werkzeug compatibility shim
- All unit tests passing (3/3)

✅ **CI/CD Pipeline:**
- Updated `.github/workflows/ci-cd.yml` with full pipeline
- Runs tests automatically on push/PR
- Builds multi-platform Docker image (amd64/arm64)
- Pushes to GitHub Container Registry (GHCR)
- Uses caching for faster builds

✅ **Documentation:**
- Comprehensive README with badges, screenshots sections, and troubleshooting
- Created `docs/images/` folder for screenshots
- Created `docs/logs/` folder for optional logs

## Next Steps (To Complete Your Submission)

### 1. Push Changes to GitHub
```powershell
# From repository root
cd C:\Users\hanzl\OneDrive\Desktop\flask-lab-project

# Add all changes
git add .

# Commit
git commit -m "Add complete CI/CD pipeline and documentation"

# Push to trigger workflow
git push origin main
```

### 2. Wait for CI/CD to Complete
- Go to: https://github.com/mrhanzla-lab/flask-lab-project/actions
- Watch the workflow run (takes ~5-10 minutes)
- All jobs should show green checkmarks

### 3. Capture Screenshots

**Screenshot 1: GitHub Actions**
- Location: https://github.com/mrhanzla-lab/flask-lab-project/actions
- Click latest workflow run
- Screenshot showing:
  - Workflow name: "CI/CD Pipeline"
  - Status: All checks passed
  - Both jobs (test, build-and-push) with green checks
- Save as: `docs/images/ci-github-actions.png`

**Screenshot 2: GHCR Image**
- Location: https://github.com/mrhanzla-lab?tab=packages
- Click "flask-lab" package
- Screenshot showing:
  - Image name and tags (latest, SHA)
  - "Published X minutes ago"
- Save as: `docs/images/ci-ghcr-image.png`

**Screenshot 3: Running App**
```powershell
# Pull and run the published image
docker pull ghcr.io/mrhanzla-lab/flask-lab:latest
docker run --rm -p 5000:5000 ghcr.io/mrhanzla-lab/flask-lab:latest
```
- Open browser: http://localhost:5000
- Screenshot showing the app homepage with URL bar visible
- Save as: `docs/images/app-running.png`

### 4. Add Screenshots to Repo
```powershell
# From repository root
git add docs/images/*.png
git commit -m "Add CI/CD screenshots for submission"
git push origin main
```

### 5. Verify README
- Open: https://github.com/mrhanzla-lab/flask-lab-project
- Scroll through README to verify:
  - CI/CD badge shows "passing"
  - Screenshots display correctly
  - All sections are complete

## Submission Checklist

- [ ] Code pushed to GitHub
- [ ] CI/CD workflow ran successfully
- [ ] Screenshot 1: GitHub Actions success (captured)
- [ ] Screenshot 2: GHCR image published (captured)
- [ ] Screenshot 3: App running (captured)
- [ ] Screenshots added to `docs/images/` and committed
- [ ] README displays all screenshots correctly
- [ ] Submission includes GitHub repo link

## Quick Commands Reference

### Build Locally (from repo root)
```powershell
docker build -t flask-lab:latest -f main/Dockerfile .
```

### Run Tests
```powershell
cd main
pytest -q
```

### Run App Locally
```powershell
docker run --rm -p 5000:5000 flask-lab:latest
```

### Check Image Pushed to GHCR
```powershell
docker pull ghcr.io/mrhanzla-lab/flask-lab:latest
```

## Troubleshooting

### Workflow Fails on Push
- Check: Repository Settings → Actions → General → Workflow permissions
- Ensure: "Read and write permissions" is selected
- Re-run failed workflow from Actions tab

### Image Not Visible in GHCR
- Package might be private by default
- Go to: Package settings → Change visibility to Public (optional)

### Docker Build Fails Locally
- Make sure you're in repository root (not `main` folder)
- Check Docker is running: `docker --version`

## Files Modified/Created

### Modified:
- `main/app.py` - Fixed __name__ typo, added werkzeug compatibility
- `main/.github/workflows/ci-cd.yml` - Complete CI/CD pipeline
- `README.md` - Comprehensive documentation

### Created:
- `docs/images/.gitkeep` - Placeholder for screenshots
- `docs/logs/.gitkeep` - Placeholder for logs
- `QUICKSTART.md` - This file

---

**Ready to submit!** Follow the steps above to complete your CI/CD submission.
