
# 🔬 Academic Research Assistant

A Python-based research assistant built using **CrewAI** that helps researchers, students, and academics search for relevant academic papers and generate comprehensive project proposals automatically.


<img width="1476" height="695" alt="1" src="https://github.com/user-attachments/assets/cb4069e3-10d8-4d4d-b328-c5f4791da9be" />
<img width="1371" height="895" alt="2" src="https://github.com/user-attachments/assets/9fe41156-565e-47b6-acfc-2a197451359c" />
<img width="1251" height="225" alt="3" src="https://github.com/user-attachments/assets/3a6cc5dd-0558-4bd9-af30-6a22f0d1c686" />


## 📝 Features

- **Automated Paper Search:** Find recent (2020–2024) and high-impact academic papers from trusted sources such as ArXiv, IEEE, ACM, Springer, Elsevier, and Google Scholar.  
- **Research Question Analysis:** Extract research questions, methodologies, key findings, and research gaps from papers.  
- **Project Proposal Generation:** Generate structured academic proposals suitable for thesis, grants, or project submissions.  
- **Markdown Output:** Save results in clean, well-formatted Markdown files for easy sharing and documentation.  
- **Configurable Parameters:** Customize maximum number of papers, preferred sources, and output format.  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Pip package manager
- API Keys for:
  - **Gemini API** (Google AI Studio)
  - **Serper Dev API** (for search functionality)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/academic-research-assistant.git
cd academic-research-assistant
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file** in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SERPER_DEV_API_KEY=your_serper_dev_api_key_here

# Optional parameters
MAX_PAPERS=7
MIN_PUBLICATION_YEAR=2020
OUTPUT_FORMAT=markdown
```

4. **Validate API keys**

```python
from config import APIKeys

APIKeys.validate_keys()
```

---

## 🧩 Usage

Run the main script:

```bash
python main.py
```

1. Enter your research topic when prompted.
2. The assistant will:

   * Search for relevant papers.
   * Analyze research questions and gaps.
   * Generate a complete project proposal.
3. The proposal will be displayed in the console and saved in `outputs/` as a Markdown file.

---

## 📁 Project Structure

```
academic-research-assistant/
│
├─ main.py                  # Main application entry
├─ config.py                # Configuration and API key management
├─ utils.py                 # Output formatting and project templates
├─ requirements.txt         # Project dependencies
├─ .env                     # API keys and optional config
├─ outputs/                 # Generated proposals will be saved here
└─ README.md                # Project documentation
```

---

## ⚙️ Configuration

You can customize research behavior in `config.py` or via `.env`:

* `MAX_PAPERS` – Maximum number of papers to retrieve (default: 7)
* `MIN_PUBLICATION_YEAR` – Filter papers published after this year (default: 2020)
* `OUTPUT_FORMAT` – Format of the generated output (`markdown` or `txt`)

---

## 🛠 Dependencies

* [CrewAI](https://pypi.org/project/crewai/) – AI agent orchestration
* [python-dotenv](https://pypi.org/project/python-dotenv/) – Load environment variables
* [requests](https://pypi.org/project/requests/) – HTTP requests
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) – HTML parsing
* [markdown](https://pypi.org/project/Markdown/) – Markdown generation

---

## ⚡ Example Workflow

1. User enters topic: `"AI in Healthcare"`
2. The assistant:

   * Searches for 5–7 recent papers on AI in healthcare.
   * Extracts research questions and gaps.
   * Generates a full proposal with abstract, methodology, timeline, and expected outcomes.
3. Proposal saved as `outputs/research_proposal_AI_in_Healthcare_<timestamp>.md`

---

## 💡 Future Improvements

* Add integration with **Zotero** or **Mendeley** for automatic reference management.
* Support for **LaTeX output** for academic submissions.
* Add **interactive CLI** for selecting preferred journals and filters.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

##  Acknowledgements

* Built with [CrewAI](https://www.crewai.com) for AI agent orchestration.
* Powered by [Gemini API](https://developers.google.com/ai) and [Serper Dev API](https://serper.dev/) for search capabilities.

