# app.py
# Streamlit portfolio app with red theme, IMDB project, and cover banner
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
/* Overall page background */
body {
    background-color: #fef2f2;
}

/* Main content container: top padding so tabs are fully visible */
.block-container {
    padding-top: 3.2rem;
    padding-bottom: 1.5rem;
}

/* Main content gradient */
.main {
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 45%, #ffffff 100%);
}

/* Cover banner */
.cover-banner {
    border-radius: 1.2rem;
    padding: 1.2rem 1.4rem;
    background: radial-gradient(circle at top left, #fecaca 0%, #fee2e2 40%, #ffffff 100%);
    border: 1px solid #fecaca;
    box-shadow: 0 16px 40px rgba(248, 113, 113, 0.22);
    margin-bottom: 1.5rem;
}
.cover-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #7f1d1d;
}
.cover-subtitle {
    font-size: 0.95rem;
    color: #b91c1c;
}
.cover-tags {
    margin-top: 0.5rem;
}
.cover-tag-pill {
    display: inline-block;
    padding: 0.15rem 0.6rem;
    border-radius: 999px;
    background: #fee2e2;
    color: #7f1d1d;
    font-size: 0.8rem;
    margin-right: 0.25rem;
}

/* Tabs styling */
.stTabs {
    margin-top: 0.75rem;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 0.6rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid #fecaca;
}
.stTabs [data-baseweb="tab"] {
    background-color: #fee2e2;
    border-radius: 999px;
    padding: 0.25rem 1.1rem;
    color: #7f1d1d;
    font-weight: 500;
    border: 1px solid transparent;
}
.stTabs [aria-selected="true"] {
    background-color: #f97373 !important;
    color: #fef2f2 !important;
    border-color: #fb7185 !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: #7f1d1d;
}

/* Body text */
p {
    color: #374151;
}

/* Project card styling */
.project-card {
    padding: 1.0rem 1.2rem;
    border-radius: 0.9rem;
    background: #fef2f2;
    border: 1px solid #fecaca;
    box-shadow: 0 10px 25px rgba(248, 113, 113, 0.25);
}

/* Snapshot widgets: rectangular pop-out */
.snapshot-widget {
    padding: 0.8rem 0.9rem;
    border-radius: 0.75rem;
    background: #fee2e2;
    border: 1px solid #fecaca;
    box-shadow: 0 6px 18px rgba(239, 68, 68, 0.25);
    height: 100%;
}
.snapshot-title {
    font-weight: 600;
    color: #7f1d1d;
    margin-bottom: 0.2rem;
}
.snapshot-metric {
    font-size: 0.9rem;
    color: #b91c1c;
}

/* Tags pill */
.tag-pill {
    display: inline-block;
    padding: 0.12rem 0.5rem;
    border-radius: 999px;
    background-color: #fee2e2;
    color: #7f1d1d;
    font-size: 0.8rem;
    margin-right: 0.25rem;
    margin-bottom: 0.15rem;
}

/* Screenshot image rounding */
img {
    border-radius: 0.6rem;
}

/* Selectbox (project gallery) styled in red theme */
.stSelectbox > div > div {
    border-radius: 999px !important;
    border: 1px solid #fecaca !important;
    background-color: #fee2e2 !important;
}
.stSelectbox > div > div > div {
    color: #7f1d1d !important;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------
# Project data (5 projects including IMDB)
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
            "Dashboard": "images/marketing_dashboard.png",  # TODO: update or leave empty
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
            "Standardized spend and revenue fields and engineered ROAS, CPC, CTR, and CVR metrics by channel and country.",
            "Benchmarked channel efficiency in Python to identify underperforming platforms and saturation points.",
            "Segmented performance by holiday vs non-holiday periods to quantify seasonal uplift.",
            "Built Tableau dashboards with filters for channel, country, and time period so stakeholders could explore ROAS and CPC interactively.",
        ],
        "results_impact": [
            "Identified a 6× CPC inefficiency in LinkedIn (3.73) versus Meta (0.59), supporting budget cuts to low-ROI channels.",
            "Improved overall campaign ROAS by 34% (0.89 → 1.19) on reduced total spend via budget reallocation.",
            "Showed that holiday campaigns delivered roughly 2× higher ROAS, supporting a more seasonal, peak-focused investment strategy.",
        ],
        "how_i_work": [
            "I connect performance metrics directly to budget decisions instead of stopping at descriptive reporting.",
            "I combine Python-based EDA with stakeholder-friendly dashboards so non-technical partners can self-serve answers.",
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
            "Aggregated transaction-level data by category, sub-category, region, and segment, computing discount rates, margins, and profit ratios.",
            "Compared revenue vs profit at multiple aggregation levels to identify categories where discounting or cost structure destroyed margins.",
            "Built Tableau dashboards with dual-axis views and filters to visualize sales, profit, and discount patterns side by side.",
        ],
        "results_impact": [
            "Uncovered a $17.7K net loss in the Tables sub-category driven by an average 26.13% discount rate across 1,241 units.",
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
            "Dashboard": "images/ai_eda_app.png",
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
        },
        "context_objective": """
The CFPB Consumer Complaint Database provides a rich view into how well financial institutions resolve customer issues over time.
The objective was to understand how outcomes evolved from 2012–2015 across products and major firms, while explicitly avoiding analytical traps like reverse causality and confounding.
I treated this as both a substantive analysis and a testbed for a disciplined, AI-supported EDA process.
        """.strip(),
        "data_tools": """
165,242 complaints and 19 fields covering product, company, geography, and resolution outcomes.
Python and an AI coding assistant used as a pair-programmer for hypothesis generation, code review, and edge-case detection.
GitHub repo: https://github.com/Cnair02/CFPB-Complaint-Analysis
        """.strip(),
        "analysis_steps": [
            "Defined eight business-relevant questions and created an EDA checklist with guardrails against reverse causality, sample-size artifacts, and product-mix confounding.",
            "Conducted EDA across product mix, geography, company performance, and resolution speed, including year-over-year decomposition at system and company level.",
            "Used the AI assistant to suggest hypotheses, review code for edge cases, and co-draft documentation while keeping final judgment human-owned.",
        ],
        "results_impact": [
            "Surfaced a sharp divergence in credit-bureau performance, highlighting risk signals that multi-year averages would have hidden.",
            "Identified a near system-wide deterioration in mortgage-servicer outcomes by 2015, suggesting areas for regulatory or operational intervention.",
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
    {
        "id": "imdb_cleaning",
        "title": "IMDB Data Processing & Cleaning",
        "tagline": "Standardized a messy IMDB movies dataset into an analysis-ready table using Python and PySpark.",
        "tools": ["Python", "PySpark", "Pandas"],
        "tags": ["Data Cleaning", "ETL", "IMDB"],
        "snapshot": "Multiple raw CSVs • Schema fixes • Clean, typed dataset",
        "screenshots": {
            "Dashboard": "images/imdb_before_after.png",
        },
        "context_objective": """
This project focuses on data cleaning and preprocessing for IMDB-like movie data, turning inconsistent raw files into a single, reliable dataset.
The objective was to demonstrate practical data engineering and cleaning skills: handling missing values, inconsistent types, and messy categorical fields so that downstream analysis becomes straightforward.
        """.strip(),
        "data_tools": """
Raw IMDB-style movie data across multiple CSVs with inconsistent types, missing values, and noisy fields.
Python, Pandas, and PySpark DataFrames used to profile, clean, and standardize the dataset.
GitHub repo: https://github.com/Cnair02/IMDB-DataProcessing
        """.strip(),
        "analysis_steps": [
            "Loaded multiple raw IMDB datasets into PySpark DataFrames and inspected schema, null patterns, and basic distributions.",
            "Standardized column types (e.g., dates, numeric fields), handled missing and invalid values, and normalized categorical fields like genres.",
            "Removed duplicates and reconciled inconsistent IDs to produce a single, coherent movie table suitable for analysis and modeling.",
        ],
        "results_impact": [
            "Produced an analysis-ready IMDB dataset with a consistent schema and types, reducing friction for downstream EDA and modeling.",
            "Demonstrated practical data-cleaning workflows similar to real-world ingestion and preprocessing tasks.",
        ],
        "how_i_work": [
            "I treat data cleaning and preprocessing as first-class work, not an afterthought.",
            "I’m comfortable using both Pandas and PySpark to clean and standardize messy real-world datasets.",
        ],
        "links": {
            "GitHub": "https://github.com/Cnair02/IMDB-DataProcessing",
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


def render_cover_banner():
    """LinkedIn-style cover banner on Home."""
    st.markdown(
        """
        <div class="cover-banner">
            <div class="cover-title">Data Analyst & Analytics Engineer</div>
            <div class="cover-subtitle">
                Turning marketing, product, and customer data into clear decisions — with solid data engineering under the hood.
            </div>
            <div class="cover-tags">
                <span class="cover-tag-pill">SQL & Python</span>
                <span class="cover-tag-pill">Marketing ROI</span>
                <span class="cover-tag-pill">BI Dashboards</span>
                <span class="cover-tag-pill">Data Cleaning</span>
                <span class="cover-tag-pill">AI-assisted Analytics</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def project_snapshot_row():
    st.markdown("### Project snapshots")
    cols = st.columns(4)
    # show the first 4 projects as snapshots (you can reorder PROJECTS to pick which)
    for idx, proj in enumerate(PROJECTS[:4]):
        with cols[idx]:
            st.markdown(
                f'<div class="snapshot-widget">'
                f'<div class="snapshot-title">{proj["title"]}</div>'
                f'<div class="snapshot-metric">{proj["snapshot"]}</div>'
                f"</div>",
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
    # Safety check: show debug if project is missing
    if not project:
        st.warning("No project selected.")
        return

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown(f"### {project['title']}")
    st.markdown(project["tagline"])
    st.markdown(f"**Snapshot:** {project['snapshot']}")
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
    render_cover_banner()
    page_header(
        "Data & Analytics Portfolio",
        "Data Analyst / Analytics Engineer (ex-Data Engineer)",
    )
    st.markdown(
        """
I help teams turn messy data into clear, business-ready insights using SQL, Python, and modern BI tools.  
Over the last few years I’ve moved from building production data pipelines in banking to using that foundation to answer business questions for marketing, product, and operations teams.  
I enjoy taking ambiguous questions like “Which campaigns should we cut?” or “Which customers are at risk?” and turning them into structured analysis, dashboards, and concrete recommendations.
        """.strip()
    )
    st.markdown(
        """
This portfolio focuses on a handful of projects that represent how I work day to day:  
- Optimizing multi-channel marketing budgets and improving ROAS.  
- Finding hidden margin issues in retail sales data.  
- Building reusable EDA tools with LLMs and Streamlit.  
- Cleaning messy IMDB-style movie data into a reliable asset.  
- Investigating large regulatory datasets and turning them into clear, executive-ready narratives.
        """.strip()
    )
    project_snapshot_row()


def render_projects():
    page_header(
        "Projects",
        "Selected work in marketing analytics, BI, data cleaning, and AI-assisted EDA.",
    )
    st.markdown(
        """
Use the selector below to explore individual projects.  
For each one, I highlight the context, data, methods, and the measurable impact.
        """.strip()
    )

    st.markdown("### Project gallery")

    # SELECT ONE PROJECT
    selected_project = project_select_widget()

    # Optional debug – uncomment once to confirm you get a dict
    # st.write("DEBUG selected_project:", selected_project)

    st.write("")  # spacing
    render_project_card(selected_project)  # Renders a single, non-blank card

    st.markdown("### Project details")

    # Single screenshot per project
    screenshots = selected_project.get("screenshots", {})
    img_path = screenshots.get("Dashboard")
    if img_path:
        st.markdown("#### Screenshot")
        st.image(img_path, use_column_width=True, caption="Dashboard")

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
Early in my career I focused on keeping data flowing reliably: building ETL pipelines, migrating workloads to the cloud, and maintaining thousands of feeds in a production banking environment.  
That experience taught me how fragile data can be and why trustworthy pipelines matter for every analysis.
        """.strip()
    )

    st.markdown(
        """
Today I apply that foundation to analytics work: marketing ROI, product and customer behavior, BI reporting, and data quality.  
I like being close to the decision—partnering with marketers, product managers, and operations leaders to understand their goals, translate them into metrics, and then build analyses and dashboards that move the needle.  
I’m comfortable going from ad-hoc deep dives in Python to polished Tableau or Power BI views that non-technical stakeholders can own and update.
        """.strip()
    )

    st.markdown("### How I work")
    st.markdown(
        """
When I start a project, I usually begin with a short problem framing: what decision are we trying to make, which levers can we realistically pull, and how will we know if the change worked.  
From there I design the data model and KPIs, run exploratory analysis to find patterns and edge cases, and then iterate on visuals and recommendations with stakeholders.  
I’m deliberate about avoiding common analytical traps (confounding, reverse causality, cherry-picking) and I document assumptions so decisions are traceable.
        """.strip()
    )

    st.markdown("### Skills snapshot")
    st.markdown(
        """
- SQL, Python (Pandas, NumPy, visualization)  
- Tableau, Power BI, Streamlit  
- Data modeling, ETL, cloud data platforms  
- Marketing analytics (ROAS, CAC, funnels, seasonality)  
- Data cleaning and preprocessing (IMDB-style datasets)  
- AI/LLM tooling and agent-based analytics workflows
        """.strip()
    )


def render_contact():
    page_header("Contact & Links", "How to reach me and explore more work.")
    st.markdown(
        """
If you’d like to talk about data/marketing analytics, BI, data engineering, or analytics engineering roles, I’d be happy to connect.  
I’m especially interested in roles where I can combine hands-on analysis with close collaboration with marketing or product teams, and keep learning from real-world experiments.  
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
