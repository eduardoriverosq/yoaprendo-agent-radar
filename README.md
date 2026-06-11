\# 🚀 YoAprendo - Autonomous AI Prospecting Radar



An autonomous, multi-agent intelligence system built for the \*\*Google Agents Hackathon\*\*. This platform utilizes the next-generation `google-genai` SDK and `gemini-2.5-flash` to crawl the live web via native Google Search Grounding. Its mission is to scan, detect, analyze, and convert institutional resistance and pedagogical friction regarding Artificial Intelligence into high-value B2B sales opportunities for \*\*YoAprendo\*\* training workshops.



\---



\## 💡 The Core Problem \& Strategic Concept



Most B2B sales tools look for standard corporate signals, missing the human and emotional triggers that drive educational budget allocations. In the academic sector, \*\*fear, institutional friction, and complaints about AI plagiarism\*\* are not barriers to entry—they are the most powerful commercial triggers available.



Where there is public anxiety about AI plagiarism or academic integrity, there is an immediate, unbudgeted crisis that requires urgent faculty training. 



The \*\*YoAprendo Autonomous Radar\*\* acts as an AI-powered smoke detector:

1\. \*\*Scans\*\* the chaotic surface of the live web (news, academic forums, public debates, community boards).

2\. \*\*Translates\*\* institutional panic or teacher resistance into a structured pedagogical pain point.

3\. \*\*Calculates\*\* a commercial urgency score (\*Lead Scoring\*).

4\. \*\*Generates\*\* a tailored B2B value proposition (\*Sales Pitch\*) designed to convert institutional fear into an adaptation opportunity.



\---



\## 🛠️ Tech Stack \& Google Architecture



This project is built natively on top of Google's newest and most advanced agentic infrastructure:



\*   \*\*Core LLM:\*\* `gemini-2.5-flash` — Chosen for its ultra-low latency, vast context window, and exceptional reasoning capabilities in processing multi-layered system instructions.

\*   \*\*Orchestration SDK:\*\* The modern, official `google-genai` SDK, utilizing native configuration object schemas (`types.GenerateContentConfig`).

\*   \*\*Live Web Intelligence:\*\* Native \*\*Google Search Grounding Tool\*\* (`types.GoogleSearch()`). Instead of relying on static training data or brittle third-party scraping APIs, the agent dynamically queries Google's live web index to analyze real-time discussions.

\*   \*\*User Interface:\*\* A minimalist, futuristic interactive web dashboard built with \*\*Streamlit\*\*, optimized for real-time sales operations and cross-device local network casting.



\---



\## 📦 Project Structure



```bash

├── app\_interface.py     # Main Streamlit Application \& Autonomous Agent Core

├── requirements.txt     # Local environment dependencies

├── .env                 # Secret file for API Keys (DO NOT UPLOAD TO GITHUB)

└── README.md            # Hackathon documentation

\## Technical Access Note for Judges:
Due to the security perimeters and federated token constraints (ACCESS_TOKEN_TYPE_UNSUPPORTED for tokens starting with AQ...) managed under the hackathon's dedicated Google Cloud project sandbox (yoaprendo-agents-challenge), the native Google Search Grounding module restricts outbound API handshakes when executed from generic public cloud runtimes like Streamlit Cloud.

To evaluate the full agent lifecycle without authentication boundaries, the repository is fully optimized to run instantly on a local runtime environment where your authenticated project session is inherited. You can run it locally by cloning the repository and executing:
python -m streamlit run app_interface.py

All core cognitive workflows, agent scouting mechanisms, and calculus-based scoring outputs are completely operational and can be fully verified in real-time within the attached demonstration video.
