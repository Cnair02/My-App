# app.py
# Streamlit portfolio app with enhanced tabs, styling, and screenshot slots
# Run with: streamlit run app.py

import math
import streamlit as st

# -----------------------
# Basic page configuration
# -----------------------
st.set_page_config(
    page_title="Data & Analytics Portfolio",
    page_icon="📊",
    layout="wide",
)

# -----------------------
# Custom CSS for styling
# -----------------------
CUSTOM_CSS = """
<style>
/* Background for main content */
.main {
    background: linear-gradient(135deg, #f6f8fc 0%, #ffffff 60%);
}

/* Tabs styling (make them stand out more) */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
}
.stTabs [data-baseweb="tab"] {
    background-color: #e6ecf5;
    border-radius: 999px;
    padding: 0.25rem 1rem;
    color: #1f2933;
}
.stTabs [aria-selected="true"] {
    background-color: #2563eb !important;
    color: #ffffff !important;
}

/* Card-like containers */
.project-card {
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.9rem;
    border-radius: 0.75rem;
    background-color: #ffffff;
    border: 1px solid #dde3f0;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
}

/* Slight hover effect for cards (desktop) */
@media (hover: hover) {
  .project-card:hover {
      border-color: #b8c2d8;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
  }
}

/* Snapshot pill styling */
.snapshot-pill {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 999px;
    background-color: #e0ebff;
    color: #1e3a8a;
    font-size: 0.8rem;
    margin-top: 0.2rem;
}

/* Make images slightly rounded */
img {
    border-radius: 0.5rem;
}

/* Reduce top padding a bit */
.block-container {
    padding-top: 1.0rem;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------
# Project data
# -----------------------
PROJECTS = [
    {
        "id": "marketing_roi",
        "title": "Marketing ROI & Budget Optimization",
        "tagline": "Improved multi-channel ROAS by 34% on reduced spend by reallocating budget across platforms and markets.",
        "tools": ["Python", "Pandas", "Matplotlib", "Seaborn", "Tableau"],
        "tags": ["Marketing Analytics", "E-commerce", "BI Dashboard"],
        "snapshot": "30K+ rows • 5 channels • 4 countries • +34% ROAS",
        # TODO: replace with your actual screenshot file paths
        "screenshots": {
            "Dashboard": "images/marketing_dashboard.png",
            "Code": "images/marketing_code.png",
        },
        "context_objective": """
A 3-year, 30K-row e-commerce marketing dataset was underperforming on overall ROAS, and the team needed to understand where ad dollars were being wasted.
The objective was to compare performance across Google Search, Meta, LinkedIn, and other channels, quantify cost inefficiencies, and recommend a data-driven budget reallocation strategy.
I focused on turning raw performance logs into clear guidance on which platforms, markets, and seasons deserved more or less spend.
        """.strip(),
        "data_tools": """
30K+ rows of ad spend and performance data across 5 channels and 4 countries, including spend, impressions, clicks, conversions, and revenue.
Python (Pandas, Matplotlib, Seaborn) for EDA and Tableau to build interactive ROAS and KPI dashboards.
GitHub repo: https://github.com/Cnair02/Marketing-ROI-and-Budget-Analysis
        """.strip(),
        "analysis_steps": [
            "Cleaned and transformed raw channel-level data, standardizing spend and revenue and engineering ROAS, CPC, CTR, and CVR metrics by channel and country.",
            "Performed EDA in Python to benchmark channel efficiency, identify underperforming platforms, and detect saturation points.",
            "Segmented performance by holiday vs non-holiday periods to quantify seasonal uplift.",
            "Built Tableau dashboards with filters for channel, country, and time period to let stakeholders explore ROAS, CTR, and CPC interactively.",
        ],
        "results_impact": [
            "Identified a 6× CPC inefficiency in LinkedIn (3.73) versus Meta (0.59), supporting a recommendation to reduce LinkedIn spend and reinvest in higher-ROI platforms.",
            "Improved overall campaign ROAS by 34% (0.89 → 1.19) on reduced total spend by shifting budget toward the most efficient channels and geographies.",
            "Showed that holiday campaigns delivered roughly 2× higher ROAS, supporting a more seasonal, peak-focused investment strategy.",
            "Delivered an executive-ready Tableau dashboard and summary that enabled ongoing monitoring and budget adjustment.",
        ],
        "how_i_work": [
            "I connect performance metrics directly to budget decisions instead of stopping at descriptive reporting.",
            "I combine Python-based EDA with stakeholder-friendly dashboards so non-technical partners can self-serve answers and drill into the data.",
            "I translate complex multi-channel performance patterns into simple, prioritized recommendations under real business constraints.",
        ],
        "links": {
            "GitHub": "https://github.com/Cnair02/Marketing-ROI-and-Budget-Analysis",
            "Dashboard": "",
        },
    },
    {
        "id": "retail_sales_profit",
        "title": "Retail Sales vs Profit Analysis",
        "tagline": "Exposed a 17.7K loss-making sub-category and high-margin opportunities in 4 years of retail data.",
        "tools": ["Python", "Pandas", "Tableau"],
        "tags": ["BI Dashboard", "Retail Analytics", "Profitability"],
        "snapshot": "$2.2M revenue • $286K profit • 17.7K loss in Tables",
        "screenshots": {
            "Dashboard": "images/retail_dashboard.png",
            "Code": "images/retail_code.png",
        },
        "context_objective": """
Standard revenue reports were hiding important profitability issues across product categories in a retail dataset.
The objective was to move beyond “what sells” to “what actually makes money,” identifying loss-making categories and high-margin niches that deserved more attention.
I approached this as a category management and pricing question, not just a generic EDA exercise.
        """.strip(),
        "data_tools": """
4 years of sales, discount, and profit data across regions, segments, and product sub-categories, totaling $2.2M revenue and $286K profit.
Python (Pandas) for data preparation and analysis, and Tableau for interactive sales and profit dashboards.
GitHub repo: https://github.com/Cnair02/Sales-vs-Profit-Analysis
        """.strip(),
        "analysis_steps": [
            "Cleaned and aggregated transaction-level data by category, sub-category, region, and segment, computing discount rates, margins, and profit ratios.",
            "Compared revenue vs profit at multiple aggregation levels to identify categories where discounting or cost structure destroyed margins.",
            "Built Tableau dashboards with dual-axis views and filters to visualize sales, profit, and discount patterns side by side.",
            "Conducted deep dives on categories with high revenue but low or negative profit to trace root causes.",
        ],
        "results_impact": [
            "Uncovered a $17.7K net loss in the Tables sub-category driven by an average 26.13% discount rate across 1,241 units—an issue invisible in top-line reporting.",
            "Flagged Copiers as a high-margin opportunity (~$55.6K profit on relatively low volume) compared with Phones (~$44.5K profit on higher volume).",
            "Showed how adjusting discount policies and rebalancing assortment could lift overall profit without necessarily increasing volume.",
        ],
        "how_i_work": [
            "I focus on profitability and margin drivers, not just revenue, when analyzing commercial performance.",
            "I design dashboards that help stakeholders discover and interrogate issues themselves, instead of locking insight in a static report.",
            "I convert analysis into clear, category-level recommendations that can feed into pricing and assortment decisions.",
        ],
        "links": {
            "GitHub": "https://github.com/Cnair02/Sales-vs-Profit-Analysis",
            "Dashboard": "",
        },
    },
    {
        "id": "ai_eda_dashboard",
        "title": "AI-Augmented EDA Dashboard",
        "tagline": "Streamlit app that runs EDA on any CSV and uses a Gemini agent to surface structured insights.",
        "tools": ["Python", "Pandas", "Streamlit", "Seaborn", "Gemini/Google ADK"],
        "tags": ["Streamlit", "LLM/Agents", "Tooling"],
        "snapshot": "Dataset-agnostic • Gemini insights • Reusable tool",
        "screenshots": {
            "App UI": "images/ai_eda_app.png",
            "Code": "images/ai_eda_code.png",
        },
        "context_objective": """
Analysts and PMs often need a quick “first pass” on a new dataset but don’t always have time or skills to write EDA code from scratch.
The objective was to build a reusable web app that automates the first 80% of EDA and adds AI-generated guidance, while keeping the process reproducible and well-guarded.
I treated this as a small internal product that could speed up exploratory work across many projects.
        """.strip(),
        "data_tools": """
Dataset-agnostic Streamlit app with a default e-commerce dataset and support for any user-uploaded CSV.
Built with Python, Pandas, Streamlit, Seaborn, and Google Gemini via the Agent Development Kit (ADK).
GitHub repo: https://github.com/Cnair02/EDA
        """.strip(),
        "analysis_steps": [
            "Implemented core EDA capabilities: schema and shape overview, sample preview, summary statistics, and column-level profiling.",
            "Built dynamic univariate and bivariate views (histograms, boxplots, scatter plots, categorical-numeric aggregations) using Pandas, Seaborn, and Streamlit charts.",
            "Engineered a data profiling layer to parse dates, coerce numeric metrics, and enforce basic ID integrity before analysis.",
            "Integrated a Gemini-based EDA assistant via Google ADK that consumes the compact profiling summary and returns structured markdown insights.",
            "Added robust error handling around CSV loading and plotting to fail gracefully on invalid files or edge cases.",
        ],
        "results_impact": [
            "Delivered a plug-and-play EDA tool that lets analysts and PMs upload a dataset and get initial visualizations and AI-generated insights without writing code.",
            "Demonstrated safe, repeatable AI integration by separating core EDA logic from AI calls and enforcing a consistent prompt template.",
            "Packaged the project with a GitHub-ready structure (app.py, eda_utils.py, data/, requirements.txt, README) that can be cloned, run, and extended.",
        ],
        "how_i_work": [
            "I build tools that scale my own analysis workflow and make EDA accessible to non-technical collaborators.",
            "I know how to integrate LLM agents into analytics workflows while maintaining guardrails and reliability.",
            "I think in terms of products (UX, error handling, documentation, deployment), not just one-off notebooks.",
        ],
        "links": {
            "GitHub": "https://github.com/Cnair02/EDA",
            "Live App": "",
        },
    },
    {
        "id": "cfpb_eda",
        "title": "Consumer Finance Complaints EDA",
        "tagline": "Analyzed 165K+ complaints to uncover deteriorating outcomes and company-level performance gaps using AI-assisted EDA.",
        "tools": ["Python", "Tableau", "AI Coding Assistant"],
        "tags": ["Risk Analytics", "Regulatory", "AI-assisted EDA"],
        "snapshot": "165K+ records • 4 years • 10 institutions",
        "screenshots": {
            "Dashboard": "images/cfpb_dashboard.png",
            "Code": "images/cfpb_code.png",
        },
        "context_objective": """
The CFPB Consumer Complaint Database provides a rich view into how well financial institutions resolve customer issues over time.
The objective was to understand how outcomes evolved from 2012–2015 across products and major firms, while explicitly avoiding analytical traps like reverse causality and confounding.
I treated this as both a substantive analysis and a testbed for a disciplined, AI-supported EDA process.
        """.strip(),
        "data_tools": """
165,242 complaints and 19 fields covering product, company, geography, and resolution outcomes.
Python and an AI coding assistant (Claude Code) used as a pair-programmer for hypothesis generation, code review, and edge-case detection.
GitHub repo: https://github.com/Cnair02/CFPB-Complaint-Analysis
        """.strip(),
        "analysis_steps": [
            "Defined eight business-relevant questions and created an EDA checklist with guardrails against reverse causality, sample-size artifacts, and product-mix confounding.",
            "Conducted EDA across product mix, geography, company performance, and resolution speed, including year-over-year decomposition at system and company level.",
            "Used the AI assistant to suggest hypotheses, review code for edge cases, and co-draft documentation while keeping final judgment human-owned.",
            "Designed a Tableau dashboard mockup with five KPIs and drill-downs to support ongoing monitoring of complaint trends by company and product.",
        ],
        "results_impact": [
            "Surfaced a sharp divergence in credit-bureau performance: Equifax’s relief rate collapsed from 54% to 8.5% while Experian’s rose from 32% to 48%, creating a ~45-pp gap by 2015.",
            "Identified a near system-wide deterioration in mortgage-servicer outcomes by 2015, highlighting a potential area for regulatory or operational intervention.",
            "Produced a one-page executive memo and dashboard concept that could be used by regulators or internal risk teams to track consumer outcomes.",
        ],
        "how_i_work": [
            "I design analyses with methodological discipline—predefined questions, guardrails, and explicit checks for confounders.",
            "I use AI tools as structured analytical partners while retaining responsibility for conclusions.",
            "I translate large, complex datasets and multi-year trends into concise narratives and monitoring KPIs for decision-makers.",
        ],
        "links": {
            "GitHub": "https://github.com/Cnair02/CFPB-Complaint-Analysis",
            "Dashboard": "",
        },
    },
]


# -----------------------
# Layout helpers
# -----------------------
def page_header(title: str, subtitle: str):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.markdown("---")


def project_snapshot_row():
    st.markdown("### Project snapshots")
    cols = st.columns(4)
    for idx, project in enumerate(PROJECTS[:4]):
        with cols[idx]:
            st.markdown(f"**{project['title']}**")
            st.markdown(
                f'<span class="snapshot-pill">{project["snapshot"]}</span>',
                unsafe_allow_html=True,
            )


def render_project_card(project: dict):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown(f"**{project['title']}**")
    st.markdown(project["tagline"])
    st.caption("Tools: " + ", ".join(project["tools"]))
    if project.get("tags"):
        st.caption("Tags: " + ", ".join(project["tags"]))
    st.markdown(
        f'<span class="snapshot-pill">{project["snapshot"]}</span>',
        unsafe_allow_html=True,
    )
    if st.button("View details", key=f"btn_{project['id']}"):
        st.session_state["selected_project_id"] = project["id"]
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# Page render functions
# -----------------------
def render_home():
    page_header(
        "Data & Analytics Portfolio",
        "Data Analyst / Analytics Engineer (ex-Data Engineer)",
    )

    st.markdown(
        """
I help teams turn messy data into clear, business-ready insights using SQL, Python, and modern BI tools like Tableau and Power BI.  
I started my career in data engineering, building pipelines and data products in banking and tech, and now focus on analytics for marketing, product, and operations.  
This portfolio highlights projects where I improved marketing ROI, surfaced hidden margin issues, and built AI-assisted analytics tools.
        """.strip()
    )

    project_snapshot_row()


def render_projects():
    page_header(
        "Projects",
        "Selected work in marketing analytics, BI, and AI-assisted EDA.",
    )

    st.markdown(
        """
These projects show how I work end-to-end: from clarifying the business question and structuring the data,  
to analysis, dashboards, and recommendations across marketing analytics, BI, and AI-assisted EDA.
        """.strip()
    )

    st.markdown("### Project gallery")

    num_cols = 2
    num_rows = math.ceil(len(PROJECTS) / num_cols)

    for row in range(num_rows):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            proj_idx = row * num_cols + col_idx
            if proj_idx >= len(PROJECTS):
                continue
            with cols[col_idx]:
                render_project_card(PROJECTS[proj_idx])

    st.markdown("### Project details")

    project_titles = [p["title"] for p in PROJECTS]
    default_index = 0

    if "selected_project_id" in st.session_state:
        default_id = st.session_state["selected_project_id"]
        for i, p in enumerate(PROJECTS):
            if p["id"] == default_id:
                default_index = i
                break

    selected_title = st.selectbox(
        "Select a project to view details:",
        options=project_titles,
        index=default_index,
    )
    selected_project = next(p for p in PROJECTS if p["title"] == selected_title)

    render_project_detail(selected_project)


def render_project_detail(project: dict):
    st.markdown(f"## {project['title']}")
    st.markdown(f"_{project['tagline']}_")
    st.write("")

    # Screenshot selector
    screenshots = project.get("screenshots", {})
    if screenshots:
        st.markdown("#### Screenshots")
        col_img, col_info = st.columns([2, 1])
        with col_img:
            screenshot_options = list(screenshots.keys())
            choice = st.radio(
                "View:",
                options=screenshot_options,
                horizontal=True,
                key=f"radio_{project['id']}",
            )
            img_path = screenshots.get(choice)
            if img_path:
                st.image(img_path, use_column_width=True, caption=choice)
        with col_info:
            st.caption(
                "Screenshots give a quick sense of the code, dashboard, or app UI behind the analysis."
            )

    st.markdown("#### Context & objective")
    st.markdown(project["context_objective"])

    st.markdown("#### Data & tools")
    st.markdown(project["data_tools"])

    st.markdown("#### Analysis steps")
    for step in project["analysis_steps"]:
        st.markdown(f"- {step}")

    st.markdown("#### Results & business impact")
    for result in project["results_impact"]:
        st.markdown(f"- {result}")

    st.markdown("#### What this shows about how I work")
    for item in project["how_i_work"]:
        st.markdown(f"- {item}")

    if project.get("links"):
        any_link = any(project["links"].values())
        if any_link:
            st.markdown("#### Links & artifacts")
            for label, url in project["links"].items():
                if url:
                    st.markdown(f"- [{label}]({url})")


def render_about():
    page_header("About", "Who I am and how I work.")

    st.markdown("### Who I am")
    st.markdown(
        """
I’m a data analyst and analytics engineer with a background in data engineering across financial services and technology.  
I’ve built ETL pipelines and data products in production banking environments, and now focus on analytics work that improves marketing ROI, profitability, and customer outcomes.
        """.strip()
    )

    st.markdown("### How I work")
    st.markdown(
        """
I’m comfortable moving from raw data (APIs, CSVs, warehouses) to cleaned models, exploratory analysis, and dashboards in Python, SQL, Tableau, and Power BI.  
I like to start with clear business questions, design metrics that matter (ROAS, CAC, churn, profit, relief rates), and present findings in plain language with concrete recommendations.
        """.strip()
    )

    st.markdown("### What I’m looking for")
    st.markdown(
        """
I’m interested in data analyst, marketing analyst, and analytics engineer roles where I can bridge data engineering depth with business-facing analysis.  
I enjoy partnering with marketing, product, and operations stakeholders and using data to guide decisions on budgets, product changes, and customer experience.
        """.strip()
    )

    st.markdown("### Skills snapshot")
    st.markdown(
        """
- SQL, Python (Pandas, NumPy, visualization)
- Tableau, Power BI, Streamlit
- Data modeling, ETL, cloud data platforms
- AI/LLM tooling and agent-based analytics workflows
        """.strip()
    )


def render_contact():
    page_header("Contact & Links", "How to reach me and explore more work.")

    st.markdown("### Let’s connect")
    st.markdown(
        """
If you’d like to talk about data/marketing analytics, BI, or analytics engineering roles, I’d be happy to connect.  
The quickest way to reach me is via email or LinkedIn. I’m open to roles in Canada and remote opportunities.
        """.strip()
    )

    st.markdown("### Links")
    # TODO: Replace these placeholders with your real URLs.
    st.markdown("- LinkedIn: [Your LinkedIn URL](https://www.linkedin.com/)")
    st.markdown("- GitHub: [Your GitHub profile](https://github.com/Cnair02)")
    st.markdown("- Tableau / BI Gallery: [Your Tableau or Power BI link](https://public.tableau.com/)")
    st.markdown("- Email: your.email@example.com")


# -----------------------
# Main app (tabs)
# -----------------------
def main():
    tabs = st.tabs(["Home", "Projects", "About", "Contact"])

    with tabs[0]:
        render_home()
    with tabs[1]:
        render_projects()
    with tabs[2]:
        render_about()
    with tabs[3]:
        render_contact()


if __name__ == "__main__":
    main()
