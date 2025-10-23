# 🧪 Flask Lab Project

![CI/CD Pipeline](https://github.com/mrhanzla-lab/flask-lab-project/actions/workflows/ci-cd.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

Collaborative Flask application with Docker and CI/CD pipeline using GitHub Actions.

## 📁 Project Structure

```
flask-lab-project/
├── main/                    # Main application directory
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Docker configuration
│   ├── tests/              # Unit tests
│   │   └── test_app.py
│   ├── templates/          # HTML templates
│   │   └── index.html
│   ├── static/             # CSS/JS files
│   │   └── style.css
│   └── .github/
│       └── workflows/
│           └── ci-cd.yml   # GitHub Actions CI/CD pipeline
├── docs/                   # Documentation & screenshots
│   ├── images/             # CI/CD screenshots for submission
│   └── logs/               # Build & test logs (optional)
├── member1_backend/        # Backend member workspace
├── member2_frontend/       # Frontend member workspace
└── member3_devops/         # DevOps member workspace
```

## 👥 Team Roles

- **Member 1 (Backend)**: Flask app implementation and API endpoints
- **Member 2 (Frontend)**: HTML templates and CSS styling
- **Member 3 (DevOps)**: Docker configuration and CI/CD pipeline

## 🚀 How to Run

### Run Locally

1. **Clone repository:**
   ```bash
   git clone https://github.com/mrhanzla-lab/flask-lab-project.git
   cd flask-lab-project
   ```

2. **Install dependencies:**
   ```bash
   cd main
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run Flask app:**
   ```bash
   python app.py
   ```
   Visit: http://localhost:5000

### Run with Docker

**Important:** Build from repository root (not from `main` directory)

1. **Build image:**
   ```bash
   # Run from repository root
   docker build -t flask-lab:latest -f main/Dockerfile .
   ```

2. **Run container:**
   ```bash
   docker run --rm -p 5000:5000 flask-lab:latest
   ```
   Visit: http://localhost:5000

### Run Tests

```bash
cd main
pytest -q
```

## 📡 API Endpoints

- **GET /** - Homepage with UI
- **GET /health** - Health check (returns "OK")
- **POST /data** - Echo JSON data back

Example:
```bash
curl -X POST http://localhost:5000/data \
  -H "Content-Type: application/json" \
  -d '{"name":"test"}'
```

## 🔄 CI/CD Pipeline

The project uses **GitHub Actions** for automated testing, building, and publishing Docker images.

### Pipeline Overview

```
┌─────────────┐      ┌──────────────┐      ┌─────────────────┐
│   Push to   │ ───> │  Run Tests   │ ───> │  Build & Push   │
│    main     │      │  (pytest)    │      │  Docker Image   │
└─────────────┘      └──────────────┘      └─────────────────┘
```

### Workflow Steps

1. **Test Job:**
   - Checkout code
   - Set up Python 3.11
   - Cache pip dependencies
   - Install requirements
   - Run pytest tests

2. **Build & Push Job:**
   - Checkout code
   - Set up Docker Buildx
   - Login to GitHub Container Registry (GHCR)
   - Build multi-platform image (amd64/arm64)
   - Push to `ghcr.io/mrhanzla-lab/flask-lab:latest`
   - Cache Docker layers for faster builds

### Required Repository Settings

#### Permissions
- Ensure Actions has package write permissions (already configured in workflow)
- Go to: Repository Settings → Actions → General → Workflow permissions
- Select: "Read and write permissions"

#### Secrets (if using Docker Hub - optional)
- Add repository secrets at: Settings → Secrets and variables → Actions
- Required secrets for Docker Hub:
  - `DOCKERHUB_USERNAME` - Your Docker Hub username
  - `DOCKERHUB_TOKEN` - Docker Hub access token or password

**Note:** GHCR (GitHub Container Registry) uses `GITHUB_TOKEN` automatically - no additional secrets needed!

### Triggering the Pipeline

The CI/CD pipeline runs automatically on:
- Push to `main` branch
- Pull requests to `main` branch

Manual trigger:
```bash
git add .
git commit -m "Trigger CI/CD pipeline"
git push origin main
```

### Viewing Pipeline Results

1. Go to: https://github.com/mrhanzla-lab/flask-lab-project/actions
2. Click on the latest workflow run
3. View test results and build logs
4. Check published image at: https://github.com/mrhanzla-lab?tab=packages

## 📸 CI/CD Proof (Screenshots)

### 1. GitHub Actions Workflow Run
![CI/CD Pipeline Success](docs/images/ci-github-actions.png)
*Screenshot showing successful test and build jobs in GitHub Actions*

### 2. Published Docker Image
![Docker Image on GHCR](docs/images/ci-ghcr-image.png)
*Screenshot showing published image on GitHub Container Registry*

### 3. Running Application
![App Running](docs/images/app-running.png)
*Screenshot showing Flask app running in browser at http://localhost:5000*

## 📋 Submission Checklist

- ✅ GitHub repository: https://github.com/mrhanzla-lab/flask-lab-project
- ✅ CI/CD pipeline configured and passing
- ✅ Docker image builds and runs successfully
- ✅ Unit tests passing (pytest)
- ✅ Screenshots captured and documented
- ✅ README with complete documentation

## 🐛 Common Issues & Solutions

### Docker Build Error: "CreateFile main: The system cannot find the file specified"

**Problem:** Running `docker build -f main/Dockerfile .` from inside the `main` directory.

**Solution:** Always build from repository root:
```bash
# Navigate to repository root first
cd /path/to/flask-lab-project
# Then build
docker build -t flask-lab:latest -f main/Dockerfile .
```

### Tests Failing Locally

**Problem:** Missing dependencies or wrong Python version.

**Solution:**
```bash
cd main
python --version  # Should be 3.11.x
pip install -r requirements.txt
pytest -v  # Verbose output to see which tests fail
```

### Image Not Pushing to GHCR

**Problem:** Insufficient permissions or GITHUB_TOKEN not available.

**Solution:**
- Check workflow permissions (Settings → Actions → General)
- Ensure `permissions: packages: write` is in workflow file
- For pull requests, image push is skipped (by design)

## 🔗 Useful Links

- [GitHub Repository](https://github.com/mrhanzla-lab/flask-lab-project)
- [GitHub Actions Runs](https://github.com/mrhanzla-lab/flask-lab-project/actions)
- [Docker Image (GHCR)](https://github.com/mrhanzla-lab?tab=packages)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

## 📝 How to Capture Screenshots for Submission

### Screenshot 1: GitHub Actions Success
1. Push code to trigger workflow: `git push origin main`
2. Go to: Repository → Actions tab
3. Click on latest workflow run
4. Expand jobs to show green checkmarks
5. Screenshot showing workflow name, branch, and "All checks passed"
6. Save as: `docs/images/ci-github-actions.png`

### Screenshot 2: Docker Image Published
1. After workflow completes, go to: https://github.com/mrhanzla-lab?tab=packages
2. Click on `flask-lab` package
3. Screenshot showing image tags and "Published X minutes ago"
4. Save as: `docs/images/ci-ghcr-image.png`

### Screenshot 3: Running Application
1. Run: `docker run --rm -p 5000:5000 flask-lab:latest`
2. Open browser to: http://localhost:5000
3. Screenshot showing the Flask app homepage with URL visible
4. Save as: `docs/images/app-running.png`

### Adding Screenshots to Repository
```bash
# From repository root
git add docs/images/*.png
git commit -m "Add CI/CD screenshots for submission"
git push origin main
```

## 👨‍💻 Contributors

- **Backend Team**: API implementation and testing
- **Frontend Team**: UI/UX design and templates
- **DevOps Team**: Docker, CI/CD, and deployment

---

**License:** MIT  
**Maintainer:** mrhanzla-lab  
**Last Updated:** October 2025