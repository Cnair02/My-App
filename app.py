# app.py
# Streamlit portfolio app with improved tabs, subtle background, and widget-based project gallery
# Run with: streamlit run app.py

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
/* Overall page background (subtle dark slate) */
body {
    background-color: #020617;
}

/* Main content container */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

/* Make Streamlit main area use a softer panel color */
.main {
    background: linear-gradient(135deg, #020617 0%, #020617 20%, #020617 100%);
}

/* Tabs: pull them down a bit and make them readable */
.stTabs {
    margin-top: 0.5rem;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid #1f2937;
}
.stTabs [data-baseweb="tab"] {
    background-color: #111827;
    border-radius: 999px;
    padding: 0.2rem 1.0rem;
    color: #e5e7eb;
    font-weight: 500;
    border: 1px solid transparent;
}
.stTabs [aria-selected="true"] {
    background-color: #2563eb !important;
    color: #f9fafb !important;
    border-color: #2563eb !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: #e5e7eb;
}

/* Paragraph text */
p {
    color: #d1d5db;
}

/* Project card styling */
.project-card {
    padding: 1.0rem 1.2rem;
    border-radius: 0.9rem;
    background: radial-gradient(circle at top left, #111827 0%, #020617 60%);
    border: 1px solid #1f2937;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.6);
}

/* Snapshot pill */
.snapshot-pill {
    display: inline-block;
    padding: 0.18rem 0.6rem;
    border-radius: 999px;
    background-color: #1d4ed8;
    color: #e5e7eb;
    font-size: 0.8rem;
}

/* Tags pill */
.tag-pill {
    display: inline-block;
    padding: 0.12rem 0.5rem;
    border-radius: 999px;
    background-color: #0f172a;
    color: #9ca3af;
    font-size: 0.75rem;
    margin-right: 0.25rem;
    margin-bottom: 0.15rem;
}

/* Screenshot image rounding */
img {
    border-radius: 0.6rem;
}

/* Make selectbox/radio labels a bit brighter */
.stSelectbox label, .stRadio label {
    color: #e5e7eb;
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
        "screenshots": {
            # TODO: replace with real image paths or leave empty
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
        ],
        "how_i_work": [
            "I connect performance metrics directly to budget decisions instead of stopping at descriptive reporting.",
            "I combine Python-based EDA with stakeholder-friendly dashboards so non-technical partners can self-serve answers and drill into the data.",
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
        ],
        "results_impact": [
            "Uncovered a $17.7K net loss in the Tables sub-category driven by an average 26.13% discount rate across 1,241 units—an issue invisible in top-line reporting.",
            "Flagged Copiers as a high-margin opportunity (~$55.6K profit on relatively low volume) compared with Phones (~$44.5K profit on higher volume).",
        ],
        "how_i_work": [
            "I focus on profitability and margin drivers, not just revenue, when analyzing commercial performance.",
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
            "Built dynamic univariate and bivariate views using Pandas, Seaborn, and Streamlit charts.",
            "Engineered a data profiling layer to parse dates, coerce numeric metrics, and enforce basic ID integrity before analysis.",
            "Integrated a Gemini-based EDA assistant via Google ADK that consumes the compact profiling summary and returns structured markdown insights.",
        ],
        "results_impact": [
            "Delivered a plug-and-play EDA tool that lets analysts and PMs upload a dataset and get initial visualizations and AI-generated insights without writing code.",
            "Demonstrated safe, repeatable AI integration by separating core EDA logic from AI calls and enforcing a consistent prompt template.",
        ],
        "how_i_work": [
            "I build tools that scale my own analysis workflow and make EDA accessible to non-technical collaborators.",
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
        ],
        "results_impact": [
            "Surfaced a sharp divergence in credit-bureau performance: Equifax’s relief rate collapsed from 54% to 8.5% while Experian’s rose from 32% to 48%, creating a ~45-pp gap by 2015.",
            "Identified a near system-wide deterioration in mortgage-servicer outcomes by 2015, highlighting a potential area for regulatory or operational intervention.",
        ],
        "how_i_work": [
            "I design analyses with methodological discipline—predefined questions, guardrails, and explicit checks for confounders.",
            "I translate large, complex datasets and multi-year trends into concise narratives and monitoring KPIs for decision-makers.",
        ],
        "links": {
            "GitHub": "https://github.com/Cnair02/CFPB-Complaint-Analysis",
            "Dashboard": "",
        },
    },
]


# -----------------------
# Helpers
# -----------------------
def page_header(title: str, subtitle: str):
    st.markdown(f"## {title}")
    if subtitle:
        st.caption(subtitle)
    st.markdown("---")


def project_snapshot_row():
    st.markdown("### Project snapshots")
    cols = st.columns(4)
    for idx, proj in enumerate(PROJECTS[:4]):
        with cols[idx]:
            st.markdown(f"**{proj['title']}**")
            st.markdown(
                f'<span class="snapshot-pill">{proj["snapshot"]}</span>',
                unsafe_allow_html=True,
            )


def project_select_widget():
    options = {p["title"]: p for p in PROJECTS}
    selected_title = st.selectbox(
        "Choose a project to explore:",
        options=list(options.keys()),
    )
    return options[selected_title]


def render_project_card(project: dict):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown(f"### {project['title']}")
    st.markdown(project["tagline"])
    st.markdown(
        f'<span class="snapshot-pill">{project["snapshot"]}</span>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.caption("Tools: " + ", ".join(project["tools"]))
    if project.get("tags"):
        tag_html = " ".join(
            f'<span class="tag-pill">{t}</span>' for t in project["tags"]
        )
        st.markdown(tag_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# Pages
# -----------------------
def render_home():
    page_header(
        "Data & Analytics Portfolio",
        "Data Analyst / Analytics Engineer (ex-Data Engineer)",
    )
    st.markdown(
        """
I help teams turn messy data into clear, business-ready insights using SQL, Python, and modern BI tools.  
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
Use the selector below to explore individual projects.  
Each project card is followed by detailed context, methods, and impact.
        """.strip()
    )

    st.markdown("### Project gallery")
    selected_project = project_select_widget()
    st.write("")
    render_project_card(selected_project)

    st.markdown("### Project details")

    # Screenshots widget
    screenshots = selected_project.get("screenshots", {})
    if screenshots:
        st.markdown("#### Screenshots")
        col_img, col_info = st.columns([2, 1])
        with col_img:
            choice = st.radio(
                "View:",
                options=list(screenshots.keys()),
                horizontal=True,
                key=f"radio_{selected_project['id']}",
            )
            img_path = screenshots.get(choice)
            if img_path:
                st.image(img_path, use_column_width=True, caption=choice)
        with col_info:
            st.caption(
                "Screenshots give a quick sense of the code, dashboard, or app UI behind the analysis."
            )

    st.markdown("#### Context & objective")
    st.markdown(selected_project["context_objective"])

    st.markdown("#### Data & tools")
    st.markdown(selected_project["data_tools"])

    st.markdown("#### Analysis steps")
    for step in selected_project["analysis_steps"]:
        st.markdown(f"- {step}")

    st.markdown("#### Results & business impact")
    for result in selected_project["results_impact"]:
        st.markdown(f"- {result}")

    st.markdown("#### What this shows about how I work")
    for item in selected_project["how_i_work"]:
        st.markdown(f"- {item}")

    if selected_project.get("links"):
        any_link = any(selected_project["links"].values())
        if any_link:
            st.markdown("#### Links & artifacts")
            for label, url in selected_project["links"].items():
                if url:
                    st.markdown(f"- [{label}]({url})")


def render_about():
    page_header("About", "Who I am and how I work.")
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
    st.markdown(
        """
If you’d like to talk about data/marketing analytics, BI, or analytics engineering roles, I’d be happy to connect.  
I’m open to roles in Canada and remote opportunities.
        """.strip()
    )

    st.markdown("### Links")
    # TODO: replace with real links
    st.markdown("- LinkedIn: [Your LinkedIn URL](https://www.linkedin.com/)")
    st.markdown("- GitHub: [Your GitHub profile](https://github.com/Cnair02)")
    st.markdown("- Tableau / BI Gallery: [Your Tableau or Power BI link](https://public.tableau.com/)")
    st.markdown("- Email: your.email@example.com")


# -----------------------
# Main with tabs
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
