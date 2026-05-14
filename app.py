def render_projects():
    page_header(
        "Projects",
        "Selected work in marketing analytics, BI, and AI-assisted EDA.",
    )
    st.markdown(
        """
Use the selector below to explore individual projects.  
For each one, I highlight the context, data, methods, and most importantly the business impact.
        """.strip()
    )

    st.markdown("### Project gallery")
    selected_project = project_select_widget()
    st.write("")
    render_project_card(selected_project)

    st.markdown("### Project details")

    # Screenshots widget (no 'Code' options anymore)
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
                "Each screenshot gives a quick sense of the dashboard or app UI behind the analysis."
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
            st.markdown("#### Links & artifacts")  # <- fixed here
            for label, url in selected_project["links"].items():
                if url:
                    st.markdown(f"- [{label}]({url})")
