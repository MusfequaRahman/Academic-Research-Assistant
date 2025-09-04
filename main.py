from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

import json
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load environment variables
load_dotenv()

# Initialize LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1
)

# Initialize search tool (you'll need SerperDev API key)
search_tool = SerperDevTool()


class ResearchAssistant:
    def __init__(self):
        self.llm = llm
        self.search_tool = search_tool
        self.setup_agents()

    def setup_agents(self):
        """Initialize all research agents"""

        # Agent 1: Research Paper Finder
        self.paper_finder = Agent(
            role="Academic Paper Research Specialist",
            goal="Find relevant academic papers and research articles on given topics",
            backstory="""You are an expert academic researcher who specializes in finding 
            high-quality research papers, journal articles, and conference proceedings. 
            You know how to search for the most relevant and recent papers in any field.""",
            verbose=True,
            llm=self.llm,
            tools=[self.search_tool]
        )

        # Agent 2: Research Question Extractor
        self.question_extractor = Agent(
            role="Research Question Analysis Expert",
            goal="Extract and analyze research questions, problems, and gaps from academic papers",
            backstory="""You are skilled at reading academic papers and identifying 
            the core research questions, methodology, and research gaps. You can 
            summarize complex research into clear, understandable insights.""",
            verbose=True,
            llm=self.llm
        )

        # Agent 3: Project Proposal Writer
        self.proposal_writer = Agent(
            role="Academic Project Proposal Writer",
            goal="Create comprehensive project proposals based on research analysis",
            backstory="""You are an experienced academic writer who creates compelling 
            project proposals. You know how to structure proposals with clear objectives, 
            methodology, timeline, and expected outcomes.""",
            verbose=True,
            llm=self.llm
        )

    def research_and_propose(self, topic: str):
        """Main function to research topic and create proposal"""

        # Task 1: Find relevant papers
        find_papers_task = Task(
            description=f"""
            Search for the most relevant and recent academic papers on the topic: "{topic}"

            Focus on:
            1. Recent papers (2020-2024)
            2. High-impact journals and conferences
            3. Papers with clear research questions
            4. Diverse perspectives on the topic

            Find at least 5-7 relevant papers and provide:
            - Paper titles
            - Authors
            - Publication year
            - Brief summary of each paper
            - Key findings or contributions
            """,
            agent=self.paper_finder,
            expected_output="List of relevant academic papers with summaries and key details"
        )

        # Task 2: Extract research questions and gaps
        extract_questions_task = Task(
            description=f"""
            Based on the papers found, analyze and extract:

            1. Main research questions being addressed
            2. Research methodologies used
            3. Key findings and conclusions
            4. Identified research gaps or limitations
            5. Future work suggestions
            6. Common themes across papers

            Create a comprehensive analysis that identifies what has been done 
            and what opportunities exist for new research in "{topic}".
            """,
            agent=self.question_extractor,
            expected_output="Detailed analysis of research questions, gaps, and opportunities",
            context=[find_papers_task]
        )

        # Task 3: Create project proposal
        create_proposal_task = Task(
            description=f"""
            Based on the research analysis, create a comprehensive project proposal for "{topic}".

            The proposal should include:

            1. **Title**: Clear and descriptive project title
            2. **Abstract**: 150-200 word summary
            3. **Introduction**: Background and motivation
            4. **Literature Review**: Summary of existing research
            5. **Research Questions**: 2-3 specific research questions
            6. **Methodology**: Proposed research approach
            7. **Timeline**: Project phases and milestones
            8. **Expected Outcomes**: What the project will deliver
            9. **Significance**: Why this research matters
            10. **Resources Needed**: Tools, data, equipment

            Make it suitable for academic submission (thesis, grant application, etc.)
            """,
            agent=self.proposal_writer,
            expected_output="Complete academic project proposal with all required sections",
            context=[find_papers_task, extract_questions_task]
        )

        # Create and execute crew
        crew = Crew(
            agents=[self.paper_finder, self.question_extractor, self.proposal_writer],
            tasks=[find_papers_task, extract_questions_task, create_proposal_task],
            verbose=True
        )

        return crew.kickoff()

    def save_results(self, result, topic: str):
        """Save the research results to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"research_proposal_{topic.replace(' ', '_')}_{timestamp}.md"

        try:
            with open(f"outputs/{filename}", 'w', encoding='utf-8') as f:
                f.write(f"# Research Proposal: {topic}\n\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("---\n\n")
                f.write(str(result))

            print(f"✅ Results saved to: outputs/{filename}")
            return filename
        except Exception as e:
            print(f"❌ Error saving results: {e}")
            return None


def main():
    print("🔬 Academic Research Assistant")
    print("=" * 50)

    # Create output directory
    os.makedirs("outputs", exist_ok=True)

    # Initialize research assistant
    assistant = ResearchAssistant()

    # Get topic from user
    topic = input("\n📝 Enter your research topic: ").strip()

    if not topic:
        print("❌ Please provide a valid topic.")
        return

    print(f"\n🚀 Starting research on: '{topic}'")
    print("This may take a few minutes...\n")

    try:
        # Run research and proposal generation
        result = assistant.research_and_propose(topic)

        print("\n" + "=" * 50)
        print("📋 RESEARCH PROPOSAL GENERATED")
        print("=" * 50)
        print(result)

        # Save results
        filename = assistant.save_results(result, topic)

        if filename:
            print(f"\n💾 Full proposal saved as: {filename}")

    except Exception as e:
        print(f"❌ Error during research: {e}")
        print("Please check your API keys and internet connection.")


if __name__ == "__main__":
    main()
