
css_content = """
/* ============================================================================
   Category Cards - New_SkillBridge Style Match
   ============================================================================ */

/* Category Icons - Solid Colors + Rounded Square */
.category-icon {
    width: 64px !important;
    height: 64px !important;
    border-radius: 16px !important; /* Rounded square */
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin: 0 auto 1rem !important;
    font-size: 2rem !important;
    transition: transform 0.3s ease;
}

/* Category Specific Styles */
/* Development - Blue */
.category-icon.development {
    background-color: #3b82f6 !important;
    color: white !important;
}

/* Design - Red */
.category-icon.design {
    background-color: #ef4444 !important;
    color: white !important;
}

/* Writing - Yellow */
.category-icon.writing {
    background-color: #f59e0b !important;
    color: white !important;
}

/* Video - Cyan */
.category-icon.video {
    background-color: #06b6d4 !important;
    color: white !important;
}

/* Audio - Green */
.category-icon.audio {
    background-color: #10b981 !important;
    color: white !important;
}

/* Photography - Dark */
.category-icon.photography {
    background-color: #1e293b !important;
    color: white !important;
}

/* Marketing - Blue */
.category-icon.marketing {
    background-color: #2563eb !important;
    color: white !important;
}

/* Business - Indigo */
.category-icon.business {
    background-color: #4f46e5 !important;
    color: white !important;
}

/* Tutoring - Green */
.category-icon.tutoring {
    background-color: #16a34a !important;
    color: white !important;
}

/* Hover Effect */
.category-card:hover .category-icon {
    transform: scale(1.1);
}
"""

with open('static/css/custom.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("Appended category styles to custom.css")
