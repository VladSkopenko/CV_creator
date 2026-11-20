from variants._common import (
    BOT_ALLERT_URL, CERTIFICATIONS_EN, CONTACT_EN, DRIVER_BOT_URL, EDUCATION_EN, INBULK_EN, LANGUAGES_EN,
    NAME, PRESS_URL, SHOWCASE_API_URL, SHOWCASE_GRAFANA_URL, SHOWCASE_REPO_URL, TALK_EN, TEKRA_EN,
)

# Wording follows the terms Python backend vacancies on Djinni and DOU use (11/2026); numbers only where they show
# a result.
INBULK_ACHIEVEMENTS = [
    "<strong>Performance:</strong> waybill PDF download cut from ~10 s to 0.2 s and the file from ~1 MB to under "
    "300 KB: one shared font subset, whole-body responses instead of streaming, S3 I/O moved off the asyncio event loop.",
    "<strong>Logistics domain, main author:</strong> split deliveries out of deals into their own domain model and "
    "migrated live PostgreSQL data with reversible Alembic migrations; truck and sea shipments, waybills, VAT, a "
    "registry of 13,754 world ports; drivers get a Telegram invite to the terminal gate instead of a guard searching "
    f"the parking lot (<a href='{DRIVER_BOT_URL}'>t.me/inbulk_drivers_bot</a>).",
    "<strong>LLM document processing:</strong> an LLM (OpenAI API, structured outputs) reads scanned port documents "
    "and rule-based code calculates waiting time and penalties (laytime and demurrage), checked by an evaluation "
    "script; vessel forms filled from certificate PDFs; tool calling for the team's LangChain AI assistant.",
    "<strong>Market price data on n8n:</strong> n8n workflows collect prices from grain marketplaces, a trader's "
    "price list and Telegram channels, normalize them (LLM for free text and photos, NBU exchange rates) and feed a "
    "public REST API of prices by region and a daily market summary for the team.",
    "<strong>Auth and security:</strong> in-house OAuth 2.0 (Google, LinkedIn) with JWT sessions; WebSocket auth "
    "moved to single-use 30-second tickets, so access tokens no longer land in proxy and CDN logs.",
]
SPEC_BULLET = (
    "<strong>AI-assisted development:</strong> introduced a team process where AI coding agents (Claude Code) write "
    "code from a written spec, tests come first and every change passes code review; reviews stopped defects before "
    "release, such as deals whose penalties could never be calculated."
)
SUMMARY_HEAD = (
    "Python backend developer at INBULK, a B2B grain-trading and logistics platform, from early stage to production. "
)
SUMMARY_TAIL = (
    "Ships with Docker and CI/CD on GitHub Actions, shown end to end on a public showcase project. A finance degree "
    "helps with invoices, VAT and multi-currency. "
)

STACK_LINE = "FastAPI, PostgreSQL, LLM integrations, CI/CD"

RESUME_DATA = {
    "lang": "en",
    "file_name": "Vladyslav_Skopenko",
    "name": NAME,
    # One PDF per headline, titles as Djinni and DOU vacancies name the role; the content is the same.
    "headlines": {
        "Python_Developer": f"Python Developer · {STACK_LINE}",
        "Python_Backend_Developer": f"Python Backend Developer · {STACK_LINE}",
        "Backend_Developer_Python": f"Backend Developer (Python) · {STACK_LINE}",
        "Python_AI_Developer": "Python Developer (AI / LLM) · OpenAI API, LangChain, FastAPI, PostgreSQL",
        "AI_Automation_Developer": "AI Automation Developer · Python, n8n, LLM, FastAPI",
    },
    "contact": CONTACT_EN,
    "summary": (
        SUMMARY_HEAD
        + "Builds REST APIs on FastAPI, PostgreSQL and asyncio, and LLM features on the OpenAI API with structured "
        "outputs, tool calling and evaluation. Main author of the logistics domain, document processing and market "
        "price data. "
        + SUMMARY_TAIL
        + "Works with AI coding agents under code review and tests first, so quality does not depend on who writes "
        "the code."
    ),
    "skills": {
        "Backend": ["Python", "FastAPI", "Django", "REST API", "asyncio", "SQLAlchemy 2.0 (async)", "Alembic",
                    "Pydantic v2", "WebSocket", "OAuth 2.0", "JWT", "pytest", "TDD", "Git"],
        "Databases": ["PostgreSQL (CTE, JSONB, query optimization)", "SQL", "Redis", "S3 / Object Storage",
                      "PDF and Excel processing"],
        "AI / LLM": ["LLM", "OpenAI API", "LangChain", "tool calling", "structured outputs", "prompt engineering",
                     "prompt design", "LLM evaluation", "AI agents", "AI coding tools (Claude Code)"],
        "CI/CD and cloud": ["GitHub Actions", "Docker (multi-stage)", "Docker Compose", "Terraform",
                            "Oracle Cloud (OCI)", "Linux", "nginx", "Prometheus", "Grafana"],
        "Code quality": ["code review", "ruff", "mypy"],
        "Automation and integrations": ["n8n", "Telegram bots (aiogram, Telethon)", "Google Maps API"],
    },
    "experience": [
        {
            **INBULK_EN,
            "achievements": [*INBULK_ACHIEVEMENTS, SPEC_BULLET],
        },
        TEKRA_EN,
    ],
    "projects": [
        {
            "name": "Backend Showcase",
            "period": "2026",
            "stack": "FastAPI · PostgreSQL · LangChain · Docker · Terraform",
            "description": (
                "Built alone with AI agents in under a month: a live cloud REST API for a restaurant chain with "
                "automatic deploys, monitoring and an AI assistant. Reviews stopped real bugs before release, such as "
                "logins silently dropping their session cookie and a monitoring change that would have kept the "
                "service down after a crash."
            ),
            "bullets": [
                "<strong>API:</strong> FastAPI, async SQLAlchemy and PostgreSQL; table booking where row locks and an "
                "exclusion constraint prevent double booking; JWT with refresh-token rotation, Google sign-in.",
                "<strong>AI assistant:</strong> LangChain tool calling on the OpenAI API with answers streamed over "
                "SSE; it changes bookings only through cards the guest confirms, under a daily spending budget.",
                "<strong>CI/CD:</strong> GitHub Actions runs linters, type checks, migration checks and pytest on a "
                "real PostgreSQL; Docker images are built once, security-scanned and promoted by digest; a merge "
                "deploys with no manual steps.",
                "<strong>Infrastructure:</strong> Terraform on Oracle Cloud, a Linux server replaced rather than "
                "patched, HTTPS, Prometheus metrics and public Grafana dashboards, an n8n simulator of guest traffic; "
                "runs for $0.",
            ],
            "links": [
                {"text": "Code", "url": SHOWCASE_REPO_URL},
                {"text": "API", "url": SHOWCASE_API_URL},
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
                {"text": "Code", "url": BOT_ALLERT_URL},
                {"text": "Article", "url": PRESS_URL},
            ],
        },
    ],
    "education": EDUCATION_EN,
    "certifications": CERTIFICATIONS_EN,
    "languages": LANGUAGES_EN,
    "talks": [TALK_EN],
}
