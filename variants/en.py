from variants._common import (
    BOT_ALLERT_URL, CERTIFICATIONS_EN, CONTACT_EN, DRIVER_BOT_URL, EDUCATION_EN, EXTRA_EN, INBULK_EN, LANGUAGES_EN,
    NAME, PRESS_URL, SHOWCASE_API_URL, SHOWCASE_GRAFANA_URL, SHOWCASE_REPO_URL, TALK_EN, TEKRA_EN,
)

RESUME_DATA = {
    "lang": "en",
    "file_name": "Vladyslav_Skopenko_CV",
    "name": NAME,
    "title": "Python Backend Engineer · FastAPI, PostgreSQL, LLM integrations, CI/CD & Cloud",
    "contact": CONTACT_EN,
    "summary": (
        "Python backend engineer with 2.5+ years of commercial experience. At INBULK, a B2B grain-trading and "
        "logistics platform, from early stage to production: top contributor by commits and code (35% of all "
        "commits). Owns the logistics domain (deliveries, truck and vessel voyages, waybills, laytime), the document "
        "pipelines and the market price data, with LLM features inside. Runs delivery end to end on a public "
        "showcase: GitHub Actions CI/CD, Docker images promoted by digest, Terraform on Oracle Cloud, Grafana. "
        "A finance degree helps with invoices, VAT and multi-currency. Works spec-first with AI coding agents and "
        "writes tests before code."
    ),
    "skills": {
        "Backend": ["Python", "FastAPI", "Pydantic v2", "SQLAlchemy 2.0 (async)", "Alembic", "REST API", "WebSocket",
                    "OAuth 2.0", "JWT", "background workers", "pytest", "TDD"],
        "Databases and data": ["PostgreSQL (CTE, JSONB, query optimization)", "SQL analytics", "PDF and Excel pipelines",
                               "S3 / Object Storage"],
        "AI / LLM": ["OpenAI API", "LangChain (tool calling)", "structured extraction", "eval harnesses", "prompt design",
                     "Claude Code", "BMAD", "spec-driven development"],
        "CI/CD and cloud": ["GitHub Actions", "Docker (multi-stage)", "Docker Compose", "GHCR", "Trivy", "Terraform",
                            "Oracle Cloud (OCI)", "cloud-init", "Caddy", "nginx", "Tailscale", "Grafana", "n8n"],
        "Code quality": ["ruff", "mypy", "import-linter", "ADRs", "Git", "code review"],
        "Integrations": ["Telegram bots (aiogram, Telethon)", "Google Maps API", "Slack", "Postman"],
        "Frontend": ["React", "TypeScript (fixes in the web app)"],
    },
    "experience": [
        {
            **INBULK_EN,
            "achievements": [
                "<strong>Logistics domain end to end:</strong> deliveries, truck voyages with weighing, vessel voyages and "
                "nominations, laytime and demurrage; PDF waybills (TTN), Excel import, S3 storage. "
                f"A <a href='{DRIVER_BOT_URL}'>Telegram bot</a> through which drivers report their trips instead of calling dispatchers.",
                "<strong>Deal execution and terminals:</strong> the flow after a deal is closed: counter offers with deadlines and "
                "extensions, settlement and prepayment, VAT rates for multi-quality contracts, IBAN handling, disputed payments, "
                "two-sided closing, shipment document drafts shared through chat with notifications; order rules such as "
                "auto-stopping a multi-order once its volume is sold out and allowing Fixed Price only where the incoterm fits; "
                "terminal appointments with lab checks, quality sampling and Excel registries; ports reference data with admin endpoints.",
                "<strong>Data model:</strong> async SQLAlchemy 2.0 models and more than half of the ~550 Alembic migrations, "
                "including a refactor that moved logistics data out of deals into a dedicated delivery aggregate, "
                "so deals and deliveries evolve independently.",
                "<strong>LLM document features:</strong> NOR and SOF port documents parsed by an LLM into typed schemas and "
                "turned by a deterministic builder into the laytime timeline, verified by an eval harness against reference "
                "voyages; vessel certificates extracted into validated Pydantic models; domain tools for the LangChain "
                "tool-calling assistant on OpenAI.",
                "<strong>Market price pipeline on n8n:</strong> 10 workflows on Data Tables that scrape three grain marketplaces and "
                "Telegram channels, normalize offers (LLM for free-text Telegram posts, NBU exchange rates), post a Slack digest "
                "and a “market today” summary to the staff group and feed the backend's public price aggregations; Code nodes "
                "kept as JavaScript files with 270+ node tests and golden fixtures, and a generator that builds the workflow JSON from them.",
                "<strong>Analytics:</strong> warehouse stocks and dashboards on PostgreSQL CTE and JSONB queries with "
                "multi-currency totals; quality of each delivery precomputed by a background worker; buy and sell product charts "
                "with class and protein filters.",
                "<strong>Performance:</strong> cut waybill download from ~10 s to 0.2 s by dropping line-by-line streaming of "
                "in-memory PDFs, sharing one 140 KB font subset and rendering off the event loop.",
                "<strong>Auth and security:</strong> in-house OAuth 2.0 with Google and LinkedIn replacing Auth0; phone and "
                "email sign-up; WebSocket auth moved from JWT in the URL to one-time tickets.",
                "<strong>DevOps:</strong> GitHub Actions deploy of the monitoring stack over Tailscale with SSH keys; "
                "a Dockerized Telegram reader service behind nginx; n8n through Compose.",
                "<strong>Agentic development:</strong> introduced spec-driven development with Claude Code and BMAD to the "
                "team: 80+ specs, tests before code, multi-agent code review.",
            ],
        },
        TEKRA_EN,
    ],
    "extra_experience": EXTRA_EN,
    "projects": [
        {
            "name": "Backend Showcase",
            "period": "2026",
            "stack": "FastAPI · PostgreSQL · Terraform · GitHub Actions",
            "description": (
                "REST API for a restaurant chain built to show delivery end to end. CI runs ruff, mypy, import-linter, an "
                "Alembic round-trip and pytest on a real PostgreSQL; multi-stage Docker images are built once per git tree, "
                "scanned with Trivy and promoted by digest from GHCR; Terraform provisions the Oracle Cloud VM, network, "
                "volumes and Object Storage, cloud-init the OS, and the server is replaced, not patched; Caddy with HTTPS; "
                "deploys over Tailscale through an entrypoint that verifies the commit; an n8n booking simulator; public "
                "Grafana dashboards over a least-privilege database role; 18 ADRs."
            ),
            "links": [
                {"text": "GitHub", "url": SHOWCASE_REPO_URL},
                {"text": "API docs", "url": SHOWCASE_API_URL},
                {"text": "Grafana", "url": SHOWCASE_GRAFANA_URL},
            ],
        },
        {
            "name": "bot_allert",
            "period": "2026",
            "stack": "Python · Telethon · Docker",
            "description": (
                "Self-hosted Telegram bot that merges air-alert channels into one feed and respects each channel's mute "
                "setting; runs in about 100 MB on Oracle Cloud's free tier. Featured on dev.ua."
            ),
            "links": [
                {"text": "GitHub", "url": BOT_ALLERT_URL},
                {"text": "dev.ua article", "url": PRESS_URL},
            ],
        },
    ],
    "education": EDUCATION_EN,
    "certifications": CERTIFICATIONS_EN,
    "languages": LANGUAGES_EN,
    "talks": [TALK_EN],
}
