from variants._common import (
    BOT_ALLERT_URL, CERTIFICATIONS_UK, CONTACT_UK, DRIVER_BOT_URL, EDUCATION_UK, EXTRA_UK, INBULK_UK, LANGUAGES_UK,
    NAME, PRESS_URL, SHOWCASE_API_URL, SHOWCASE_GRAFANA_URL, SHOWCASE_REPO_URL, TALK_UK, TEKRA_UK,
)

RESUME_DATA = {
    "lang": "uk",
    "file_name": "Vladyslav_Skopenko_CV_UA",
    "name": NAME,
    "title": "Python Backend Engineer · FastAPI, PostgreSQL, LLM-інтеграції, CI/CD та хмара",
    "contact": CONTACT_UK,
    "summary": (
        "Python backend-інженер з 2,5+ роками комерційного досвіду. В INBULK, B2B-платформі для торгівлі зерном і "
        "логістики, від ранньої стадії до продакшну: головний контриб'ютор за комітами й кодом (35% усіх комітів). "
        "Відповідаю за домен логістики (поставки, автомобільні й морські рейси, ТТН, laytime), пайплайни документів і "
        "ринкові ціни, з LLM-функціями всередині. На публічному showcase веду delivery від і до: CI/CD у GitHub Actions, "
        "Docker-образи з промоушеном за digest, Terraform в Oracle Cloud, Grafana. Фінансова освіта допомагає з "
        "інвойсами, ПДВ і мультивалютністю. Працюю за специфікаціями з AI-агентами, тести пишу до коду."
    ),
    "skills": {
        "Backend": ["Python", "FastAPI", "Pydantic v2", "SQLAlchemy 2.0 (async)", "Alembic", "REST API", "WebSocket",
                    "OAuth 2.0", "JWT", "фонові воркери", "pytest", "TDD"],
        "Бази даних і дані": ["PostgreSQL (CTE, JSONB, оптимізація запитів)", "SQL-аналітика", "PDF- та Excel-пайплайни",
                              "S3 / Object Storage"],
        "AI / LLM": ["OpenAI API", "LangChain (tool calling)", "структурований витяг даних", "eval-харнеси", "промпт-дизайн",
                     "Claude Code", "BMAD", "розробка за специфікаціями"],
        "CI/CD і хмара": ["GitHub Actions", "Docker (multi-stage)", "Docker Compose", "GHCR", "Trivy", "Terraform",
                          "Oracle Cloud (OCI)", "cloud-init", "Caddy", "nginx", "Tailscale", "Grafana", "n8n"],
        "Якість коду": ["ruff", "mypy", "import-linter", "ADR", "Git", "код-рев'ю"],
        "Інтеграції": ["Telegram-боти (aiogram, Telethon)", "Google Maps API", "Slack", "Postman"],
        "Frontend": ["React", "TypeScript (правки у вебзастосунку)"],
    },
    "experience": [
        {
            **INBULK_UK,
            "achievements": [
                "<strong>Домен логістики від і до:</strong> поставки, автомобільні рейси зі зважуванням, морські рейси й "
                "номінації суден, laytime і демередж; PDF-ТТН, імпорт з Excel, зберігання в S3. "
                f"<a href='{DRIVER_BOT_URL}'>Telegram-бот</a>, через який водії звітують про рейси замість дзвінків диспетчеру.",
                "<strong>Виконання угод і термінали:</strong> процес після укладення угоди: зустрічні пропозиції з дедлайнами й "
                "продовженнями, розрахунки й передоплата, ставки ПДВ для мультиякісних контрактів, робота з IBAN, спірні платежі, "
                "двостороннє закриття, чернетки відвантажувальних документів із шерингом у чаті та сповіщеннями; правила ордерів, "
                "як-от автостоп мультиордера після розпродажу обсягу і Fixed Price лише там, де дозволяє інкотерм; записи на "
                "термінал з лабораторною перевіркою, відбором проб і Excel-реєстрами; довідник портів з адмін-ендпоінтами.",
                "<strong>Модель даних:</strong> моделі на async SQLAlchemy 2.0 і більше половини з ~550 міграцій Alembic, "
                "зокрема рефакторинг, що виніс логістичні дані з угод в окремий агрегат поставки, щоб угоди й поставки "
                "розвивалися незалежно.",
                "<strong>LLM-функції для документів:</strong> портові документи NOR і SOF LLM розбирає у типізовані схеми, "
                "детермінований builder будує з них хронологію laytime, eval-харнес звіряє результат з еталонними рейсами; "
                "витяг даних із суднових сертифікатів у валідовані Pydantic-моделі; доменні інструменти для LangChain-асистента "
                "з tool calling на OpenAI.",
                "<strong>Пайплайн ринкових цін на n8n:</strong> 10 воркфлоу на Data Tables, що збирають ціни з трьох зернових "
                "майданчиків і Telegram-каналів, нормалізують пропозиції (LLM для вільного тексту з Telegram, курси НБУ), "
                "надсилають дайджест у Slack і зведення «ринок сьогодні» у групу команди та живлять публічні цінові агрегації "
                "бекенду; Code-ноди зберігаються як JavaScript-файли з 270+ node-тестами й golden-фікстурами, а генератор "
                "збирає з них JSON воркфлоу.",
                "<strong>Аналітика:</strong> залишки на складах і дашборди на PostgreSQL (CTE, JSONB) з мультивалютними "
                "підсумками; якість по кожній поставці заздалегідь рахує фоновий воркер; графіки продуктів купівлі та продажу "
                "з фільтрами за класом і протеїном.",
                "<strong>Продуктивність:</strong> завантаження ТТН прискорено з ~10 с до 0,2 с: без построкового стрімінгу "
                "PDF з пам'яті, з одним спільним шрифтом на 140 КБ і рендером поза event loop.",
                "<strong>Авторизація й безпека:</strong> власний OAuth 2.0 з Google і LinkedIn замість Auth0; реєстрація за "
                "телефоном і email; авторизація WebSocket через одноразові тікети замість JWT в URL.",
                "<strong>DevOps:</strong> деплой стеку моніторингу з GitHub Actions через Tailscale з SSH-ключами; сервіс "
                "Telegram-рідера в Docker за nginx; n8n через Compose.",
                "<strong>Розробка з агентами:</strong> запровадив у команді розробку за специфікаціями з Claude Code і BMAD: "
                "80+ специфікацій, тести до коду, рев'ю коду кількома агентами.",
            ],
        },
        TEKRA_UK,
    ],
    "extra_experience": EXTRA_UK,
    "projects": [
        {
            "name": "Backend Showcase",
            "period": "2026",
            "stack": "FastAPI · PostgreSQL · Terraform · GitHub Actions",
            "description": (
                "REST API для мережі ресторанів, побудований, щоб показати delivery від і до. CI запускає ruff, mypy, "
                "import-linter, round-trip міграцій Alembic і pytest на справжньому PostgreSQL; multi-stage Docker-образи "
                "збираються один раз на git tree, скануються Trivy і промоутяться за digest з GHCR; Terraform створює VM в "
                "Oracle Cloud, мережу, диски й Object Storage, cloud-init налаштовує ОС, сервер замінюється, а не латається; "
                "Caddy з HTTPS; деплой через Tailscale через entrypoint, що перевіряє коміт; симулятор бронювань на n8n; "
                "публічні дашборди Grafana через роль БД з мінімальними правами; 18 ADR."
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
                "Self-hosted Telegram-бот, що зводить канали тривог в одну стрічку і враховує, які канали заглушені; "
                "працює в ~100 МБ на безкоштовній VM Oracle Cloud. Про нього написав dev.ua."
            ),
            "links": [
                {"text": "GitHub", "url": BOT_ALLERT_URL},
                {"text": "стаття dev.ua", "url": PRESS_URL},
            ],
        },
    ],
    "education": EDUCATION_UK,
    "certifications": CERTIFICATIONS_UK,
    "languages": LANGUAGES_UK,
    "talks": [TALK_UK],
}
