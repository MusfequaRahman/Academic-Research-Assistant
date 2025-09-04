import re
import json
from typing import Dict, List
from datetime import datetime


class OutputFormatter:
    """Utility class for formatting research outputs"""

    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and format text output"""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters that might cause issues
        text = re.sub(r'[^\w\s\-\.\,\:\;\!\?\(\)\[\]\"\'\/]', '', text)
        return text.strip()

    @staticmethod
    def format_proposal(proposal_text: str) -> str:
        """Format the proposal with better structure"""
        lines = proposal_text.split('\n')
        formatted_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append("")
                continue

            # Add proper heading formatting
            if any(heading in line.lower() for heading in
                   ['title:', 'abstract:', 'introduction:', 'methodology:',
                    'timeline:', 'expected outcomes:', 'significance:']):
                formatted_lines.append(f"\n## {line}")
            else:
                formatted_lines.append(line)

        return '\n'.join(formatted_lines)

    @staticmethod
    def generate_summary_stats(result: str) -> Dict:
        """Generate summary statistics about the research"""
        stats = {
            "generated_at": datetime.now().isoformat(),
            "word_count": len(result.split()),
            "character_count": len(result),
            "sections_found": len(re.findall(r'##?\s+\w+', result))
        }
        return stats


class ProjectTemplates:
    """Templates for different types of projects"""

    @staticmethod
    def get_template(project_type: str = "general") -> str:
        """Get proposal template based on project type"""
        templates = {
            "general": """
# Project Proposal: {title}

## Abstract
{abstract}

## 1. Introduction and Background
{introduction}

## 2. Literature Review
{literature_review}

## 3. Research Questions
{research_questions}

## 4. Methodology
{methodology}

## 5. Timeline and Milestones
{timeline}

## 6. Expected Outcomes
{outcomes}

## 7. Significance and Impact
{significance}

## 8. Resources Required
{resources}

## 9. References
{references}
            """,

            "thesis": """
# Master's/PhD Thesis Proposal: {title}

## Executive Summary
{abstract}

## Problem Statement
{problem}

## Literature Survey
{literature}

## Research Objectives
{objectives}

## Proposed Methodology
{methodology}

## Work Plan and Timeline
{timeline}

## Expected Contributions
{contributions}

## Evaluation Plan
{evaluation}

## Bibliography
{references}
            """
        }

        return templates.get(project_type, templates["general"])

