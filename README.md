# Iniva

**A confidential, open-source assistant that answers girls' and young women's questions about periods, contraception, STIs and pregnancy, and refers them to youth-friendly health services in Gabon.**

Iniva is being developed by **OSSIA Digital** (Libreville, Gabon) with **APSAD** (Alliance pour la Promotion Sociale et l'Aide au Développement), whose President, a medical doctor, validates all health content. Target users: girls and young women aged 15–24 in Greater Libreville. Interface language: French.

> **Status: pilot demonstration 11 November 2026.** APSAD medical approval has been communicated; signed sign-off must be archived. Pilot access is limited to ages 18–24. No deployed LLM/WhatsApp is claimed.

## What it does

- Answers free-text questions in French from a curated sexual and reproductive health (SRH) knowledge base (41 entries across periods, contraception, STIs/HIV, pregnancy, consent and wellbeing).
- Detects safety-critical messages (sexual violence, violence, suicidal thoughts, medical emergencies) **before** any answer and shows an immediate support message with helpline contacts.
- Refers users to health services filtered by need (contraception, emergency contraception, HIV PEP, testing, antenatal care, violence support).
- Collects anonymous, in-memory feedback ("this helped / not really") for user testing.

## Safety and privacy by design

- No name, phone number or account. No cookies, no analytics, no server-side storage.
- Questions stay in the browser tab and disappear when it is closed.
- Age-appropriate entry screen with consent; users under 18 are not admitted to the pilot to trusted adults and support contacts.
- A "Quick exit" button immediately leaves the page.
- Answers never diagnose and never give medication doses; every answer encourages consultation where relevant.
- See [SAFETY.md](SAFETY.md) and [PRIVACY.md](PRIVACY.md).

## Architecture

```
data/knowledge_base.json   validated Q&A entries (French), CC BY 4.0
data/safety.json           crisis triggers, support messages, helpline contacts
data/clinics.json          service directory (Greater Libreville)
src/index.template.html    the app (HTML/CSS/vanilla JS, no dependencies)
build.py                   embeds the data into a single file
dist/index.html            the built, self-contained app (works offline)
```

**Retrieval mode (default):** keyword and phrase matching over the knowledge base; answers are returned verbatim as validated by the medical reviewer. No AI model or network connection is required, which suits low-bandwidth settings.

**Open-source LLM mode (optional):** set `INIVA_CONFIG.llmEndpoint` to an Ollama-compatible endpoint running an open-weight model (e.g. Mistral or Llama). The model only rephrases the top three validated entries for the user's question and is instructed never to go beyond them; on any error Iniva falls back to retrieval mode. No proprietary API is used.

## Run it

```bash
python3 build.py          # rebuild after editing data/
open dist/index.html      # or serve the folder with any static web server
```

Test mode for user-testing sessions: open `dist/index.html#test`. A bar shows aggregate counts (questions, answered, unanswered, safety alerts, helpfulness votes) and exports them as CSV. No question text is exported.

## Roadmap (12 months)

1. Medical validation of all content by APSAD's President; child-safeguarding, consent and privacy review.
2. Pilot with 1,000 girls aged 15–24 in Greater Libreville via APSAD; WhatsApp channel.
3. Local-language voice input/output; verified map of youth-friendly services.
4. Scale to 5,000 users; publish aggregated, anonymous insights on unmet information needs.

## Content governance

Every entry in `data/knowledge_base.json` must be approved by the medical reviewer before release. Changes to health content go through a pull request reviewed by APSAD. Set `contentValidated: true` and `validatedBy` in `INIVA_CONFIG` only after sign-off.

## Licence

Code: MIT. Knowledge base: CC BY 4.0. The name "Iniva" is not licensed. Copyright © 2026 OSSIA Digital, APSAD and Arthur Rodrigue Assamba.
