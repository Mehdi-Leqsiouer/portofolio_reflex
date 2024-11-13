import reflex as rx


def create_hover_link(href, text):
    """Create a link element with hover effect and custom color."""
    return rx.el.a(
        text,
        href=href,
        _hover={"color": "#4F46E5"},
        color="#374151",
    )


def create_h2_heading(font_size, line_height, margin_bottom, text):
    """Create an h2 heading with custom font size, line height, and margin."""
    return rx.heading(
        text,
        font_weight="700",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height=line_height,
        as_="h2",
    )


def create_h3_heading(font_size, line_height, margin_bottom, text):
    """Create an h3 heading with custom font size, line height, and margin."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom=margin_bottom,
        font_size=font_size,
        line_height=line_height,
        as_="h3",
    )


def create_icon(tag):
    """Create an icon with specified tag and default styling."""
    return rx.icon(
        tag=tag,
        height="1.5rem",
        margin_right="0.5rem",
        width="1.5rem",
    )


def create_text_span(text):
    """Create a text span element."""
    return rx.text.span(text)


def create_icon_with_text(icon_tag, text):
    """Create a flex container with an icon and text."""
    return rx.flex(
        create_icon(tag=icon_tag),
        create_text_span(text=text),
        display="flex",
        align_items="center",
    )


def create_icon_link(href, icon_tag, text):
    """Create a link with an icon and text, opening in a new tab."""
    return rx.el.a(
        create_icon(tag=icon_tag),
        create_text_span(text=text),
        href=href,
        target="_blank",
        rel="noopener noreferrer",
        display="flex",
        align_items="center",
    )


def create_image(alt, height, src, width):
    """Create an image element with specified attributes."""
    return rx.image(
        alt=alt,
        src=src,
        height=height,
        margin_right="1rem",
        width=width,
    )


def create_h3_title(text):
    """Create an h3 title with predefined styling."""
    return rx.heading(
        text,
        font_weight="600",
        font_size="1.5rem",
        line_height="2rem",
        as_="h3",
    )


def create_image_with_title(image_alt, image_src, title_text):
    """Create a flex container with an image and a title."""
    return rx.flex(
        create_image(
            alt=image_alt,
            height="3rem",
            src=image_src,
            width="3rem",
        ),
        create_h3_title(text=title_text),
        display="flex",
        align_items="center",
        margin_bottom="0.5rem",
    )


def create_body_text(text):
    """Create a paragraph of body text with predefined styling."""
    return rx.text(
        text,
        margin_bottom="1rem",
        color="#4B5563",
        font_size="1.125rem",
        line_height="1.75rem",
    )


def create_list_item(text):
    """Create a list item element."""
    return rx.el.li(text)


def create_bullet_list(item1, item2, item3, item4):
    """Create a bullet list with four items."""
    return rx.list(
        create_list_item(text=item1),
        create_list_item(text=item2),
        create_list_item(text=item3),
        create_list_item(text=item4),
        list_style_type="disc",
        list_style_position="inside",
        font_size="1.125rem",
        line_height="1.75rem",
    )


def create_logo_image(alt, src):
    """Create a logo image with predefined styling."""
    return rx.image(
        alt=alt,
        src=src,
        height="4rem",
        margin_bottom="0.5rem",
        width="4rem",
    )


def create_h4_title(text):
    """Create an h4 title with predefined styling."""
    return rx.heading(text, font_weight="600", as_="h4", size="3")


def create_skill_card(logo_alt, logo_src, skill_name):
    """Create a skill card with a logo and skill name."""
    return rx.flex(
        create_logo_image(alt=logo_alt, src=logo_src),
        create_h4_title(text=skill_name),
        background_color="#ffffff",
        display="flex",
        flex_direction="column",
        align_items="center",
        padding="1rem",
        border_radius="0.25rem",
        box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
    )


def create_description_text(text):
    """Create a description text with predefined styling."""
    return rx.text(text, margin_bottom="1rem")


def create_tag(text):
    """Create a tag element with predefined styling."""
    return rx.text.span(
        text,
        background_color="#E0E7FF",
        font_weight="500",
        padding_left="0.625rem",
        padding_right="0.625rem",
        padding_top="0.125rem",
        padding_bottom="0.125rem",
        border_radius="0.25rem",
        color="#3730A3",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_tag_group(tag1, tag2, tag3):
    """Create a group of three tags."""
    return rx.flex(
        create_tag(text=tag1),
        create_tag(text=tag2),
        create_tag(text=tag3),
        display="flex",
        column_gap="0.5rem",
    )


def create_subtext(text):
    """Create a subtext element with predefined styling."""
    return rx.text(text, color="#4B5563")


def create_title_with_subtext(title, subtext):
    """Create a box with a title and subtext."""
    return rx.box(
        create_h3_heading(
            font_size="1.25rem",
            line_height="1.75rem",
            margin_bottom="0.5rem",
            text=title,
        ),
        create_subtext(text=subtext),
    )


def create_certification_card(logo_alt, logo_src, title, description):
    """Create a certification card with logo, title, and description."""
    return rx.flex(
        create_image(
            alt=logo_alt,
            height="4rem",
            src=logo_src,
            width="4rem",
        ),
        create_title_with_subtext(title=title, subtext=description),
        background_color="#ffffff",
        display="flex",
        align_items="center",
        padding="1.5rem",
        border_radius="0.25rem",
        box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
    )


def create_form_label(text):
    """Create a form label with predefined styling."""
    return rx.el.label(
        text,
        display="block",
        font_weight="600",
        margin_bottom="0.5rem",
        color="#374151",
    )


def create_form_input(id, name, type):
    """Create a form input field with predefined styling."""
    return rx.el.input(
        id=id,
        name=name,
        required=True,
        type=type,
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#6366F1",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        width="100%",
    )


def create_form_field(label, input_id, input_name, input_type):
    """Create a form field with label and input."""
    return rx.box(
        create_form_label(text=label),
        create_form_input(id=input_id, name=input_name, type=input_type),
        margin_bottom="1rem",
    )


def create_small_icon(tag):
    """Create a small icon with specified tag."""
    return rx.icon(tag=tag, height="1.5rem", width="1.5rem")


def create_social_link(href, icon_tag):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_small_icon(tag=icon_tag),
        href=href,
        target="_blank",
        rel="noopener noreferrer",
        _hover={"color": "#818CF8"},
    )


def create_profile_header():
    """Create the profile header with name and image."""
    return rx.flex(
        rx.image(
            alt="Mehdi Leqsiouer profile picture",
            src="/photo_mehdi.jpg",
            height="3rem",
            margin_right="1rem",
            border_radius="9999px",
            width="3rem",
        ),
        rx.heading(
            "Mehdi Leqsiouer",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#4F46E5",
            as_="h1",
        ),
        display="flex",
        align_items="center",
    )


def create_navigation_bar():
    """Create the navigation bar with profile and links."""
    return rx.flex(
        create_profile_header(),
        rx.flex(
            create_hover_link(href="#about", text="About"),
            create_hover_link(href="#experience", text="Experience"),
            create_hover_link(href="#skills", text="Skills"),
            create_hover_link(href="#projects", text="Projects"),
            create_hover_link(
                href="#certifications",
                text="Certifications",
            ),
            create_hover_link(href="#contact", text="Contact"),
            display="flex",
            column_gap="1rem",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
    )


def create_contact_button():
    """Create a 'Get in Touch' button."""
    return rx.el.a(
        "test",
        href="#contact",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#E0E7FF"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        color="#4338CA",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_section():
    """Create the hero section with title, subtitle, and button."""
    return rx.box(
        create_h2_heading(
            font_size="2.25rem",
            line_height="2.5rem",
            margin_bottom="0.5rem",
            text="Mehdi Leqsiouer",
        ),
        rx.heading(
            "Data Engineer",
            margin_bottom="2rem",
            font_size="1.5rem",
            line_height="2rem",
            as_="h3",
        ),
        rx.text(
            "Transforming raw data into actionable insights",
            margin_bottom="2rem",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_contact_button(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        text_align="center",
    )


def create_about_content():
    """Create the content for the About Me section."""
    return rx.flex(
        rx.image(
            alt="Mehdi Leqsiouer working on a laptop",
            src="/photo_mehdi.jpg",
            margin_right="1.5rem",
            border_radius="0.5rem",
            width="33.333333%",
        ),
        rx.text(
            "Hello! I'm Mehdi Leqsiouer, a Data Engineer at Orange based in Paris. With a robust background in both data science and data engineering acquired through diverse experiences, I specialize in implementing best practices in DevOps and MLOps to successfully drive various data projects.",
            line_height="1.75rem",
            font_size="1.25rem",
        ),
        display="flex",
        align_items="center",
        margin_bottom="1.5rem",
    )


def create_about_section():
    """Create the About Me section with title and content."""
    return rx.box(
        create_h2_heading(
            font_size="1.875rem",
            line_height="2.25rem",
            margin_bottom="1.5rem",
            text="About Me",
        ),
        create_about_content(),
        rx.flex(
            create_icon_with_text(icon_tag="mail", text="leqsiouer.mehdi@outlook.com"),
            create_icon_with_text(icon_tag="phone", text="+33 6 62 64 90 29"),
            create_icon_with_text(icon_tag="map-pin", text="Paris, France"),
            create_icon_link(
                href="https://github.com/Mehdi-Leqsiouer",
                icon_tag="github",
                text="GitHub",
            ),
            create_icon_link(
                href="https://www.linkedin.com/in/mehdi-leqsiouer",
                icon_tag="linkedin",
                text="LinkedIn",
            ),
            display="flex",
            align_items="center",
            column_gap="1.5rem",
        ),
        id="about",
        margin_bottom="5rem",
    )


def create_experience_section():
    """Create the Work Experience section with job details."""
    return rx.box(
        create_h2_heading(
            font_size="1.875rem",
            line_height="2.25rem",
            margin_bottom="1.5rem",
            text="Work Experience",
        ),
        rx.box(
            create_image_with_title(
                image_alt="Orange Logo",
                image_src="/orange_logo",
                title_text="Data Engineer",
            ),
            create_body_text(text="Orange S.A | January 2024 - Present"),
            create_bullet_list(
                item1="Designed and implemented scalable data pipelines using Apache Spark and Airflow",
                item2="Optimized data warehouse performance, reducing query times by 40%",
                item3="Led the migration of on-premises data infrastructure to AWS cloud services",
                item4="Collaborated with data science teams to productionize machine learning models",
            ),
            margin_bottom="2rem",
        ),
        rx.box(
            create_image_with_title(
                image_alt="DataSolutions Co. logo",
                image_src="https://replicate.delivery/xezq/cyuPSoHeSZxqFy9LhQIsoLuIRGefp0jxBRhGffYGlAPhNVEeE/out-0.webp",
                title_text="Data Engineer",
            ),
            create_body_text(text="DataSolutions Co. | 2015 - 2018"),
            create_bullet_list(
                item1="Developed and maintained ETL processes using Python and SQL",
                item2="Implemented data quality checks and monitoring systems",
                item3="Assisted in the design of data models for various business domains",
                item4="Provided technical support and documentation for data-related projects",
            ),
        ),
        id="experience",
        margin_bottom="5rem",
    )


def create_skills_grid():
    """Create a grid of skill cards."""
    return rx.box(
        create_skill_card(
            logo_alt="Python logo",
            logo_src="https://replicate.delivery/xezq/MGql59oK6f3CGK3mF3AHcNuSSc8GRlvmRv6G6ZkGK7J2UR4JA/out-0.webp",
            skill_name="Python",
        ),
        create_skill_card(
            logo_alt="SQL logo",
            logo_src="https://replicate.delivery/xezq/vdyaYiTKR5JGNZasgMn0QG1NBvjYpzJdrc2hEhTbxRxaqI8E/out-0.webp",
            skill_name="SQL",
        ),
        create_skill_card(
            logo_alt="Apache Spark logo",
            logo_src="https://replicate.delivery/xezq/Yxspvat9D6q7C53tOqmqYqBCKJOLPfCbBpjJnMgD1mZ2UR4JA/out-0.webp",
            skill_name="Apache Spark",
        ),
        create_skill_card(
            logo_alt="Airflow logo",
            logo_src="https://replicate.delivery/xezq/L2g2ExpagBoEHlrggh749kg0ru9wrv3R8egTde9SSjfZTFhnA/out-0.webp",
            skill_name="Airflow",
        ),
        create_skill_card(
            logo_alt="AWS logo",
            logo_src="https://replicate.delivery/xezq/uZqUULFfWfgprUMnel64P77lTonLWyH7hWfCiBWQIffMbqI8E/out-0.webp",
            skill_name="AWS",
        ),
        create_skill_card(
            logo_alt="Hadoop logo",
            logo_src="https://replicate.delivery/xezq/22flquQ8Ax3JOSilf53oMDRHehhrO5XBcjosQnihOovXTFhnA/out-0.webp",
            skill_name="Hadoop",
        ),
        create_skill_card(
            logo_alt="Kafka logo",
            logo_src="https://replicate.delivery/xezq/kxRSvs6HEhLgLdxyexucyj11xQ3SHIstjKqLdnI1cQT2UR4JA/out-0.webp",
            skill_name="Kafka",
        ),
        create_skill_card(
            logo_alt="Docker logo",
            logo_src="https://replicate.delivery/xezq/qHBUfz2CMiQtPSJY8DTZJuDOfa0b3leTaQ11uO1IEvfxmKCPB/out-0.webp",
            skill_name="Docker",
        ),
        gap="1rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(2, minmax(0, 1fr))",
                "768px": "repeat(4, minmax(0, 1fr))",
            }
        ),
    )


def create_projects_grid():
    """Create a grid of featured projects."""
    return rx.box(
        rx.box(
            create_h3_heading(
                font_size="1.25rem",
                line_height="1.75rem",
                margin_bottom="1rem",
                text="Real-time Data Processing Pipeline",
            ),
            create_description_text(
                text="Developed a high-throughput, fault-tolerant data processing pipeline using Apache Kafka and Spark Streaming, capable of handling millions of events per second."
            ),
            create_tag_group(tag1="Kafka", tag2="Spark", tag3="AWS"),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.25rem",
            box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
        ),
        rx.box(
            create_h3_heading(
                font_size="1.25rem",
                line_height="1.75rem",
                margin_bottom="1rem",
                text="Data Warehouse Optimization",
            ),
            create_description_text(
                text="Redesigned and optimized a large-scale data warehouse, resulting in a 60% reduction in storage costs and 40% improvement in query performance."
            ),
            create_tag_group(tag1="SQL", tag2="Redshift", tag3="Python"),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.25rem",
            box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(2, minmax(0, 1fr))",
            }
        ),
    )


def create_message_textarea():
    """Create a textarea for message input in the contact form."""
    return rx.el.textarea(
        id="message",
        name="message",
        required=True,
        rows="4",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#6366F1",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        width="100%",
    )


def create_submit_button():
    """Create a submit button for the contact form."""
    return rx.el.button(
        "Send Message",
        type="submit",
        background_color="#4F46E5",
        transition_duration="300ms",
        _hover={"background-color": "#4338CA"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_contact_form():
    """Create the contact form with input fields and submit button."""
    return rx.form(
        create_form_field(
            label="Name",
            input_id="name",
            input_name="name",
            input_type="text",
        ),
        create_form_field(
            label="Email",
            input_id="email",
            input_name="email",
            input_type="email",
        ),
        rx.box(
            create_form_label(text="Message"),
            create_message_textarea(),
            margin_bottom="1rem",
        ),
        create_submit_button(),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.25rem",
        box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
    )


def create_main_content():
    """Create the main content of the portfolio including all sections."""
    return rx.box(
        create_about_section(),
        create_experience_section(),
        rx.box(
            create_h2_heading(
                font_size="1.875rem",
                line_height="2.25rem",
                margin_bottom="1.5rem",
                text="Skills",
            ),
            create_skills_grid(),
            id="skills",
            margin_bottom="5rem",
        ),
        rx.box(
            create_h2_heading(
                font_size="1.875rem",
                line_height="2.25rem",
                margin_bottom="1.5rem",
                text="Featured Projects",
            ),
            create_projects_grid(),
            id="projects",
            margin_bottom="5rem",
        ),
        rx.box(
            create_h2_heading(
                font_size="1.875rem",
                line_height="2.25rem",
                margin_bottom="1.5rem",
                text="Certifications & Achievements",
            ),
            rx.box(
                create_certification_card(
                    logo_alt="AWS Certified Data Analytics - Specialty",
                    logo_src="https://replicate.delivery/xezq/ySvDDTmaHT7mApzoVrhADOve4DGqtIMeUM7SMuxAafQYTFhnA/out-0.webp",
                    title="AWS Certified Data Analytics - Specialty",
                    description="Issued by Amazon Web Services, 2022",
                ),
                create_certification_card(
                    logo_alt="Databricks Certified Associate Developer for Apache Spark",
                    logo_src="https://replicate.delivery/xezq/Zmhgh0mWKDbLEdX17bHQ71sR8XAy4O3CzBFpV1rwCnIbqI8E/out-0.webp",
                    title="Databricks Certified Associate Developer for Apache Spark",
                    description="Issued by Databricks, 2021",
                ),
                gap="2rem",
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "768px": "repeat(2, minmax(0, 1fr))",
                    }
                ),
            ),
            id="certifications",
            margin_bottom="5rem",
        ),
        rx.box(
            create_h2_heading(
                font_size="1.875rem",
                line_height="2.25rem",
                margin_bottom="1.5rem",
                text="Get in Touch",
            ),
            create_contact_form(),
            id="contact",
            margin_bottom="5rem",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="3rem",
        padding_bottom="3rem",
    )


def create_social_links():
    """Create social media links for the footer."""
    return rx.flex(
        create_social_link(
            href="https://www.linkedin.com/in/johndoe",
            icon_tag="linkedin",
        ),
        create_social_link(
            href="https://github.com/johndoe",
            icon_tag="github",
        ),
        rx.el.a(
            create_small_icon(tag="twitter"),
            href="#",
            _hover={"color": "#818CF8"},
        ),
        display="flex",
        justify_content="center",
        margin_top="1rem",
        column_gap="1rem",
    )


def create_footer():
    """Create the footer with copyright and social links."""
    return rx.box(
        rx.text("© 2024 Mehdi Leqsiouer. All rights reserved."),
        create_social_links(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        text_align="center",
    )


def create_page_layout():
    """Create the overall page layout including header, content, and footer."""
    return rx.box(
        rx.box(
            create_navigation_bar(),
            background_color="#ffffff",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        rx.box(
            create_hero_section(),
            class_name="bg-gradient-to-r from-indigo-600 to-purple-600",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        create_main_content(),
        rx.box(
            create_footer(),
            background_color="#1F2937",
            padding_top="2rem",
            padding_bottom="2rem",
            color="#ffffff",
        ),
        class_name="bg-gradient-to-br from-blue-100 to-pink-200 via-purple-100",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        color="#1F2937",
    )


def create_portfolio_page():
    """Create the main portfolio page with all components."""
    return rx.fragment(
        rx.script(src="https://cdn.tailwindcss.com"),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        create_page_layout(),
    )
