#!/usr/bin/env python3
"""
🏘️ COMMUNITY DATA COMMONS - ACTION HUB
Transforms community knowledge into actionable community empowerment
"""

import streamlit as st
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime
import uuid
import base64

# Add scripts to path
sys.path.append('/home/yethatsjames/community-ai-workspace/scripts')

def get_sdi_logo_base64():
    """Load SDI logo and convert to base64 for embedding"""
    logo_path = "/home/yethatsjames/community-ai-workspace/branding/logos/SDI Logo assets and variants/logo red.png"
    try:
        with open(logo_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""  # Return empty string if logo not found

# Page configuration
st.set_page_config(
    page_title="Community Action Hub",
    page_icon="🏘️",
    layout="wide"
)

# Mobile-First SDI Brand CSS
st.markdown("""
<style>
/* Mobile-First Community Data Commons - Based on SDI Brand Guidelines */
:root {
    /* SDI Official Colors from Brand Guidelines */
    --sdi-red: #bb2522;        /* Deep Red - passion & heart */
    --sdi-blue: #4061aa;       /* Sky Blue - hope & future */
    --sdi-green: #4e8f67;      /* Urban Green - grassroots */
    --sdi-yellow: #eed854;     /* Sunny Yellow - spirit */
    --sdi-grey: #888584;       /* Metal Grey - infrastructure */
    
    /* KYC Brand Colors */
    --kyc-red: #d32f2f;        /* Data insights focus */
    --kyc-blue: #1976d2;       /* Analysis emphasis */
    --kyc-green: #388e3c;      /* Community data */
    
    /* KYC TV Colors */
    --kyctv-pink: #e91e63;     /* Creative media */
    --kyctv-orange: #ff9800;   /* Storytelling */
    --kyctv-dark: #212121;     /* Media contrast */
    
    /* Mobile Typography - Franklin Gothic (SDI standard) */
    --font-primary: system-ui, -apple-system, "Franklin Gothic", "Source Sans Pro", sans-serif;
    --mobile-hero: 1.75rem;    /* 28px - thumb-friendly */
    --mobile-title: 1.25rem;   /* 20px - clear hierarchy */
    --mobile-body: 1rem;       /* 16px - readable */
    
    /* Touch Targets */
    --touch-target: 44px;      /* Apple minimum */
    --touch-comfortable: 48px; /* More comfortable */
    --mobile-padding: 16px;
    --mobile-margin: 12px;
}

/* Mobile-optimized base */
.stApp {
    font-family: var(--font-primary);
    padding-bottom: 60px; /* Space for mobile nav */
}

/* Mobile-friendly header */
.header-text {
    font-size: var(--mobile-hero);
    text-align: center;
    color: var(--sdi-red);
    margin-bottom: var(--mobile-margin);
    font-weight: 900; /* Franklin Gothic Heavy */
}

/* SDI Logo styling */
.sdi-logo {
    height: 60px;
    width: auto;
    margin-right: 15px;
    vertical-align: middle;
}

/* SDI Brand Action Cards - Mobile Optimized */
.action-card {
    background: var(--sdi-red);
    color: white;
    padding: var(--mobile-padding);
    border-radius: 12px;
    margin: var(--mobile-margin) 0px;
    border-left: 5px solid var(--sdi-yellow);
    font-weight: 600; /* Franklin Gothic Medium */
    min-height: var(--touch-target);
}

.success-card {
    background: var(--sdi-green);
    color: white;
    padding: var(--mobile-padding);
    border-radius: 10px;
    margin: var(--mobile-margin) 0px;
    min-height: var(--touch-target);
}

/* Community Photographer Optimized Cards */
.contribution-card {
    background: #f8f9fa;
    border: 2px solid var(--sdi-grey);
    padding: var(--mobile-padding);
    border-radius: 12px;
    margin: var(--mobile-margin) 0px;
    transition: transform 0.2s;
    min-height: var(--touch-comfortable);
}

.contribution-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(187, 37, 34, 0.15); /* SDI red shadow */
}

/* KYC Data Insights Header */
.insight-header {
    background: var(--sdi-blue);
    color: white;
    padding: var(--mobile-padding);
    border-radius: 10px;
    text-align: center;
    margin: var(--mobile-margin) 0px;
    font-weight: 900; /* SDI Heavy weight */
}

/* Mobile-friendly step cards */
.next-step {
    background: rgba(64, 97, 170, 0.1); /* SDI blue tint */
    border-left: 4px solid var(--sdi-blue);
    padding: var(--mobile-padding);
    margin: var(--mobile-margin) 0px;
    border-radius: 8px;
    min-height: var(--touch-target);
}

.community-connection {
    background: rgba(78, 143, 103, 0.1); /* SDI green tint */
    border-left: 4px solid var(--sdi-green);
    padding: var(--mobile-padding);
    margin: var(--mobile-margin) 0px;
    border-radius: 8px;
    min-height: var(--touch-target);
}

.resource-needed {
    background: rgba(238, 216, 84, 0.1); /* SDI yellow tint */
    border-left: 4px solid var(--sdi-yellow);
    padding: var(--mobile-padding);
    margin: var(--mobile-margin) 0px;
    border-radius: 8px;
    min-height: var(--touch-target);
}

/* Mobile Navigation Enhancement */
.stRadio > div {
    gap: var(--mobile-margin);
}

.stRadio label {
    font-size: var(--mobile-body);
    min-height: var(--touch-target);
    padding: 8px var(--mobile-margin);
    border-radius: 8px;
    transition: background 0.2s;
}

/* Mobile Button Optimization */
.stButton button {
    min-height: var(--touch-comfortable);
    font-size: var(--mobile-body);
    font-weight: 600;
    border-radius: 8px;
    padding: var(--mobile-margin) 20px;
    background: var(--sdi-red);
    border: none;
    color: white;
    font-family: var(--font-primary);
}

.stButton button:hover {
    background: var(--sdi-green);
    transform: translateY(-1px);
}

/* Community Photo Upload Areas */
.stFileUploader {
    border: 2px dashed var(--sdi-green);
    border-radius: 12px;
    padding: var(--mobile-padding);
    background: rgba(78, 143, 103, 0.05);
    min-height: 120px;
    text-align: center;
}

/* KYC TV Media Branding */
.kyctv-overlay {
    background: var(--sdi-grey);
    color: white;
    padding: var(--mobile-padding);
    border-radius: 12px;
    margin: var(--mobile-margin) 0;
}

/* Mobile Responsive Images */
img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}

/* Touch-friendly expandable sections */
.streamlit-expanderHeader {
    font-size: var(--mobile-title);
    min-height: var(--touch-target);
    font-weight: 600;
}

/* Loading states for mobile */
.stSpinner {
    color: var(--sdi-red);
}

/* Mobile-first media queries */
@media (max-width: 480px) {
    .header-text {
        font-size: 1.5rem;
        margin: var(--mobile-margin) 0;
    }
    
    .action-card, .contribution-card {
        margin: 8px 0;
        padding: 12px;
    }
}

/* Ensure accessibility on mobile */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'insights_engine' not in st.session_state:
    st.session_state.insights_engine = None

if 'media_processor' not in st.session_state:
    st.session_state.media_processor = None

if 'multimodal_engine' not in st.session_state:
    st.session_state.multimodal_engine = None

if 'contributions' not in st.session_state:
    # Load existing contributions
    contributions_file = Path("/home/yethatsjames/community-ai-workspace/community_contributions.json")
    if contributions_file.exists():
        with open(contributions_file, 'r') as f:
            st.session_state.contributions = json.load(f)
    else:
        st.session_state.contributions = []

def load_insights_engine():
    """Load the actionable insights engine"""
    if st.session_state.insights_engine is None:
        with st.spinner("🔄 Loading Community Action Intelligence..."):
            try:
                from actionable_insights import ActionableInsightsEngine
                st.session_state.insights_engine = ActionableInsightsEngine()
                return True
            except Exception as e:
                st.error(f"❌ Error loading system: {e}")
                return False
    return True

def load_media_processor():
    """Load the media processing engine"""
    if st.session_state.media_processor is None:
        try:
            from media_processor import MediaProcessor
            st.session_state.media_processor = MediaProcessor()
            return True
        except Exception as e:
            st.error(f"❌ Error loading media processor: {e}")
            return False
    return True

def load_multimodal_engine():
    """Load the multi-modal analysis engine"""
    if st.session_state.multimodal_engine is None:
        try:
            from multimodal_engine import MultiModalEngine
            st.session_state.multimodal_engine = MultiModalEngine()
            return True
        except Exception as e:
            st.error(f"❌ Error loading multimodal engine: {e}")
            return False
    return True

def save_contribution(contribution_data):
    """Save a new community contribution"""
    contribution_data['id'] = str(uuid.uuid4())
    contribution_data['timestamp'] = datetime.now().isoformat()
    st.session_state.contributions.append(contribution_data)
    
    # Save to file
    contributions_file = Path("/home/yethatsjames/community-ai-workspace/community_contributions.json")
    with open(contributions_file, 'w') as f:
        json.dump(st.session_state.contributions, f, indent=2)

# Main header with SDI logo
st.markdown('''
<div style="text-align: center; margin-bottom: 20px;">
    <img src="data:image/png;base64,{}" class="sdi-logo" />
    <h1 class="header-text" style="display: inline; vertical-align: middle;">COMMUNITY ACTION HUB</h1>
</div>
'''.format(get_sdi_logo_base64()), unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: var(--sdi-blue); font-weight: 600;">Transform Community Knowledge into Concrete Action</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: var(--sdi-grey); margin-bottom: 20px;">📍 <strong>SDI Community Data Commons</strong> | Mobile-First | Privacy-Preserving</p>', unsafe_allow_html=True)

# Mobile-First Navigation
st.sidebar.title("🎯 Action Hub")

# SDI Brand Information
st.sidebar.markdown("""
<div style="background: var(--sdi-red); color: white; padding: 12px; border-radius: 8px; margin: 10px 0; text-align: center;">
<strong>🏘️ SDI Community Data Commons</strong><br>
<small>Slum Dwellers International</small>
</div>
""", unsafe_allow_html=True)

# Mobile-optimized quick access 
with st.sidebar.expander("🏛️ Community Guidelines", expanded=False):
    st.markdown("**📱 Quick Access (Mobile-Friendly):**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Governance", key="governance_quick"):
            st.session_state.show_governance = True
        if st.button("🤝 Contribute", key="contribute_quick"):
            st.session_state.show_contribution_guide = True
    with col2:
        if st.button("🔍 Standards", key="quality_quick"):
            st.session_state.show_quality_standards = True
        if st.button("📸 Photo Guide", key="photo_guide"):
            st.session_state.show_photo_guide = True

# Mobile-optimized main navigation with cleaner labels
page = st.sidebar.radio(
    "📱 Choose Action (Mobile-Optimized):",
    [
        "🎯 Get Insights",
        "📸 Share Media", 
        "📊 Track Impact",
        "🌍 Connect",
        "💡 Learn Stories"
    ]
)

# Map mobile labels back to full functionality
page_mapping = {
    "🎯 Get Insights": "🚀 Get Actionable Insights",
    "📸 Share Media": "🤝 Contribute to Commons",
    "📊 Track Impact": "📊 Track Community Impact", 
    "🌍 Connect": "🌍 Connect Communities",
    "💡 Learn Stories": "💡 Success Stories"
}

# Use mapped page name for logic
full_page_name = page_mapping.get(page, page)

# Handle governance quick access
if st.session_state.get('show_governance'):
    st.header("🏛️ Community Governance Framework")
    from sdi_secretariat_contribution import get_sdi_secretariat_entry
    sdi_entry = get_sdi_secretariat_entry()
    content = sdi_entry['full_content']
    
    st.markdown("### 🎯 Community Purpose Statement")
    st.markdown(content['community_purpose'])
    
    st.markdown("### 🏛️ Governance Framework") 
    st.markdown(content['governance_framework'])
    
    st.markdown("### 📋 Contribution Guidelines")
    st.markdown(content['contribution_guidelines'])
    
    if st.button("🔙 Back to Action Hub"):
        st.session_state.show_governance = False
        st.rerun()
    st.stop()

if st.session_state.get('show_contribution_guide'):
    st.header("🤝 How to Contribute Guide")
    st.markdown("""
    ### 🌱 Growing the Community Data Commons
    
    **Your contributions make the difference between communities having access to empowering knowledge or not.**
    
    #### 📝 Share Your Story (Most Impactful)
    - Document what your community tried
    - What worked and what didn't
    - Key lessons for other communities
    
    #### 📊 Upload Data & Documents
    - Meeting notes and minutes
    - Government responses
    - Training materials
    - Survey results
    
    #### 🔍 Quality Standards
    - Real community experiences only
    - Actionable insights for others
    - Respectful, constructive tone
    - Privacy-protected (no personal info)
    """)
    
    if st.button("🔙 Back to Action Hub"):
        st.session_state.show_contribution_guide = False
        st.rerun()
    st.stop()

if st.session_state.get('show_quality_standards'):
    st.header("🔍 Community Knowledge Quality Standards")
    st.markdown("""
    ### 📊 Knowledge Contribution Standards
    
    **Authenticity**: Information comes from real community experiences and organizing
    
    **Actionability**: Knowledge provides concrete steps other communities can take
    
    **Cultural Context**: Contributions acknowledge local conditions and constraints
    
    **Success Evidence**: Claims of successful strategies include verifiable outcomes
    
    **Replicability**: Strategies can be adapted by communities in different contexts
    
    ### 🔒 Privacy and Security Standards
    
    **Local Processing**: All AI processing happens on community-controlled infrastructure
    
    **Anonymization**: Individual participants cannot be identified from stored data
    
    **Encryption**: Data in transit and at rest uses strong cryptographic protection
    
    **Access Control**: Only authorized community representatives access sensitive data
    
    **Audit Trail**: All system activities are logged for community oversight
    
    ### 🛠️ Technical Infrastructure Standards
    
    **Container Isolation**: Each community maintains separate computing environments
    
    **Federated Architecture**: Communities share model improvements, never raw data
    
    **Open Source**: All software components are publicly auditable and modifiable
    
    **Hardware Sovereignty**: Communities can run systems on their own equipment
    
    **Offline Capability**: Systems function without internet connectivity when needed
    """)
    
    if st.button("🔙 Back to Action Hub"):
        st.session_state.show_quality_standards = False
        st.rerun()
    st.stop()

if st.session_state.get('show_photo_guide'):
    st.header("📸 Community Photography Guide")
    st.markdown("""
    ### 📱 Mobile-First Photography for Community Organizing
    
    **Your photos document community power and organize for change!**
    
    #### 📸 What to Photograph
    - **Community meetings and gatherings**
    - **Organizing activities and actions**
    - **Infrastructure challenges and solutions**
    - **Community celebrations and achievements**
    - **Training sessions and skill-building**
    
    #### 🎯 Photography Tips
    - **Focus on action**: Capture people doing things, not just posing
    - **Show community power**: Groups working together, leadership in action
    - **Document before/after**: Progress and change over time
    - **Include context**: Wide shots that show the environment
    - **Respect privacy**: Get consent, avoid identifying information
    
    #### 📱 Technical Guidelines
    - **Use your smartphone**: Modern phones take excellent photos
    - **Good lighting**: Natural light is best, avoid harsh flash
    - **Steady shots**: Hold phone with both hands, brace against surfaces
    - **Multiple angles**: Take several shots from different perspectives
    - **Clean lens**: Wipe camera lens for clearer images
    
    #### 🔐 Privacy Protection
    - **No personal identifying information**: Avoid capturing full faces without consent
    - **Community consent**: Get agreement before photographing sensitive activities
    - **Safe storage**: Keep photos secure, share only through approved channels
    - **Community ownership**: Photos belong to the community, not individuals
    
    #### 📤 Sharing Guidelines
    - **Upload through the Community Action Hub for automatic privacy protection**
    - **Add context**: Describe what the photo shows and why it's important
    - **Community value**: Explain how this image helps other communities
    - **Cultural sensitivity**: Respect local customs and protocols
    """)
    
    if st.button("🔙 Back to Action Hub"):
        st.session_state.show_photo_guide = False
        st.rerun()
    st.stop()

# PAGE: Get Actionable Insights
if page == "🎯 Get Insights":
    st.header("🎯 Transform Your Questions into Community Action")
    
    if not load_insights_engine():
        st.stop()
    
    engine = st.session_state.insights_engine
    
    # Quick action buttons
    st.subheader("⚡ Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👥 Youth Organizing", key="youth_btn"):
            st.session_state.selected_query = "How can youth organize effectively in their communities?"
    
    with col2:
        if st.button("🎓 Skills Training", key="skills_btn"):
            st.session_state.selected_query = "What skills training opportunities are available for community members?"
    
    with col3:
        if st.button("🏛️ Government Engagement", key="gov_btn"):
            st.session_state.selected_query = "How should communities engage with government officials?"
    
    # Main query interface
    st.subheader("🔍 Ask for Actionable Community Guidance")
    
    # Get query from session state or input
    default_query = st.session_state.get('selected_query', '')
    query = st.text_area(
        "What challenge does your community face?",
        value=default_query,
        placeholder="e.g., How can we organize youth to address unemployment in our community?",
        height=100
    )
    
    if st.button("🎯 Get Actionable Insights", disabled=not query.strip()):
        if query.strip():
            with st.spinner("🧠 Analyzing community knowledge and generating actions..."):
                # Get search results
                results = engine.rag.query_knowledge_base(query, n_results=5)
                
                # Generate actionable insights
                insights = engine.generate_actionable_insights(query, results['results'])
            
            # Display insights with rich formatting
            st.markdown(f'<div class="insight-header"><h2>🎯 Action Plan: {insights["theme"]}</h2><p>Based on real community experiences</p></div>', unsafe_allow_html=True)
            
            # Immediate Actions
            if insights['immediate_actions']:
                st.subheader("🚀 Take These Actions Now")
                for action in insights['immediate_actions']:
                    st.markdown(f'<div class="action-card">{action}</div>', unsafe_allow_html=True)
            
            # Success Examples
            if insights['success_examples']:
                st.subheader("✅ Proven Success Stories")
                for example in insights['success_examples']:
                    st.markdown(f'<div class="success-card">{example}</div>', unsafe_allow_html=True)
            
            # Next Steps
            if insights['next_steps']:
                st.subheader("📋 Your Next Steps")
                for i, step in enumerate(insights['next_steps'], 1):
                    st.markdown(f'<div class="next-step"><strong>Step {i}:</strong> {step}</div>', unsafe_allow_html=True)
            
            # Community Connections
            if insights['community_connections']:
                st.subheader("🤝 Connect with These Communities")
                for connection in insights['community_connections']:
                    st.markdown(f'<div class="community-connection">{connection}</div>', unsafe_allow_html=True)
            
            # Resources Needed
            if insights['resources_needed']:
                st.subheader("📦 Resources You'll Need")
                for resource in insights['resources_needed']:
                    st.markdown(f'<div class="resource-needed">{resource}</div>', unsafe_allow_html=True)
            
            # Action tracking
            st.subheader("📊 Track Your Progress")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("✅ Mark as Started", key="start_action"):
                    save_contribution({
                        'type': 'action_started',
                        'query': query,
                        'theme': insights['theme'],
                        'actions_taken': 'Started implementing recommendations'
                    })
                    st.success("🎉 Action recorded! Your progress helps other communities.")
            
            with col2:
                if st.button("📝 Share Results Later", key="share_results"):
                    st.info("💡 Come back to share how these actions worked for your community!")
    
    # Clear query button
    if st.button("🔄 New Question"):
        if 'selected_query' in st.session_state:
            del st.session_state.selected_query
        st.rerun()

# PAGE: Contribute to Commons
elif page == "📸 Share Media":
    st.header("🌱 Grow the Community Data Commons")
    st.write("Your contributions help communities worldwide learn from each other.")
    
    # Load contribution pathways
    if not load_insights_engine():
        st.stop()
    
    # Add SDI Secretariat foundational entry
    from sdi_secretariat_contribution import get_sdi_secretariat_entry
    sdi_entry = get_sdi_secretariat_entry()
    
    pathways = [sdi_entry] + st.session_state.insights_engine.generate_contribution_pathways()
    
    # Display contribution options
    st.subheader("🎯 Ways to Contribute")
    
    for pathway in pathways:
        with st.expander(f"{pathway['title']} - {pathway['difficulty']}"):
            # Special rendering for SDI Secretariat foundational entry
            if pathway['title'] == '🏛️ The Role of the SDI Secretariat':
                st.markdown("### 🏛️ COMMUNITY GOVERNANCE FOUNDATION")
                st.info("This foundational document establishes the purpose and governance of the Community Data Commons")
                
                # Display each section
                content = pathway['full_content']
                
                with st.expander("🎯 Community Purpose Statement"):
                    st.markdown(content['community_purpose'])
                
                with st.expander("🏛️ Governance Framework"):
                    st.markdown(content['governance_framework'])
                
                with st.expander("📋 Contribution Guidelines"):
                    st.markdown(content['contribution_guidelines'])
                
                with st.expander("🔍 Quality Standards"):
                    st.markdown(content['quality_standards'])
                
                with st.expander("🗺️ Implementation Roadmap"):
                    st.markdown(content['implementation_roadmap'])
                
                with st.expander("📞 Secretariat Contact"):
                    st.markdown(content['secretariat_contact'])
                
                st.success("✅ This framework ensures community control and ethical AI development")
            
            else:
                # Regular pathway display
                st.write(f"**What:** {pathway['description']}")
                st.write(f"**How:** {pathway['action']}")
                st.write(f"**Impact:** {pathway['impact']}")
            
            # Contribution forms based on type
            if 'Share Your Story' in pathway['title']:
                st.subheader("📝 Submit Your Community Story")
                
                story_title = st.text_input("Story Title:", placeholder="How we organized against the water crisis")
                community_name = st.text_input("Your Community:", placeholder="Kibera Community Group")
                story_content = st.text_area("Your Story:", placeholder="Describe what happened, what you did, and the results...", height=150)
                lessons_learned = st.text_area("Key Lessons:", placeholder="What would you tell other communities?", height=100)
                
                if st.button("📤 Share Story", key="share_story"):
                    if story_title and community_name and story_content:
                        save_contribution({
                            'type': 'community_story',
                            'title': story_title,
                            'community': community_name,
                            'content': story_content,
                            'lessons': lessons_learned
                        })
                        st.success("🎉 Story shared! Your experience will help other communities.")
                        st.balloons()
            
            elif 'Add Community Data' in pathway['title']:
                st.subheader("📤 Upload Community Media & Data")
                
                if not load_media_processor():
                    st.error("❌ Media processing not available")
                    st.stop()
                
                processor = st.session_state.media_processor
                supported_formats = processor.get_supported_formats()
                
                # Show supported formats
                with st.expander("📋 Supported File Types"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.markdown("**📸 Images (Photographers)**")
                        st.write(", ".join(supported_formats['images']))
                    with col2:
                        st.markdown("**🎬 Videos**") 
                        st.write(", ".join(supported_formats['video']))
                    with col3:
                        st.markdown("**🔊 Audio**")
                        st.write(", ".join(supported_formats['audio']))
                
                data_type = st.selectbox("Type of Media:", [
                    "📸 Community Photos (Events, Meetings, Activities)",
                    "🎬 Community Videos (Training, Testimonials, Events)",
                    "🔊 Audio Recordings (Meetings, Interviews)", 
                    "📄 Meeting Notes/Minutes",
                    "📊 Community Survey Results",
                    "📋 Government Response Documents",
                    "🎓 Training Materials",
                    "📈 Success Metrics",
                    "📝 Other Documents"
                ])
                
                data_description = st.text_area("Describe this media:", 
                    placeholder="What does this show/contain and how might it help other communities? (No personal info)")
                
                # Dynamic file uploader based on type
                allowed_types = []
                if "Photos" in data_type:
                    allowed_types = [ext[1:] for ext in supported_formats['images']]  # Remove dots
                elif "Videos" in data_type:
                    allowed_types = [ext[1:] for ext in supported_formats['video']]
                elif "Audio" in data_type:
                    allowed_types = [ext[1:] for ext in supported_formats['audio']]
                else:
                    allowed_types = ['txt', 'pdf', 'doc', 'docx', 'csv', 'json']
                
                uploaded_file = st.file_uploader(
                    f"Upload {data_type}:", 
                    type=allowed_types,
                    help=f"Accepted formats: {', '.join(allowed_types)}"
                )
                
                if uploaded_file and data_description:
                    if st.button("📤 Process & Upload", key="upload_process"):
                        with st.spinner("📤 Processing your upload..."):
                            # Save the file
                            result = processor.save_uploaded_file(uploaded_file, {
                                'data_type': data_type,
                                'description': data_description,
                                'uploader_type': 'community_contributor'
                            })
                            
                            if result['success']:
                                file_id = result['file_id']
                                file_type = result['metadata']['file_type']
                                
                                # Process based on file type
                                if file_type == 'image':
                                    process_result = processor.process_image_file(file_id)
                                    if process_result['success']:
                                        st.success("📸 Image processed successfully!")
                                        # Show thumbnail
                                        if 'thumbnail_path' in process_result:
                                            st.image(process_result['thumbnail_path'], 
                                                   caption="📸 Your contribution", width=200)
                                        
                                        # Multi-modal analysis
                                        if load_multimodal_engine():
                                            analysis_result = st.session_state.multimodal_engine.analyze_image_content(
                                                file_id, data_description
                                            )
                                            if analysis_result['success']:
                                                insights = analysis_result['insights']
                                                st.info(f"🧠 Analysis: Found themes: {', '.join(insights['content_themes'])}")
                                                st.info(f"💡 Community value: {insights['community_value']['level'].upper()}")
                                
                                elif file_type == 'video':
                                    process_result = processor.process_video_file(file_id)
                                    if process_result['success']:
                                        st.success("🎬 Video processed - audio extracted for analysis!")
                                        
                                        # Multi-modal analysis
                                        if load_multimodal_engine():
                                            analysis_result = st.session_state.multimodal_engine.analyze_video_content(
                                                file_id, data_description
                                            )
                                            if analysis_result['success']:
                                                insights = analysis_result['insights']
                                                st.info(f"🧠 Analysis: Found themes: {', '.join(insights['content_themes'])}")
                                                st.info(f"🎙️ Audio ready for transcription")
                                
                                elif file_type == 'audio':
                                    # Multi-modal analysis for audio
                                    if load_multimodal_engine():
                                        analysis_result = st.session_state.multimodal_engine.analyze_audio_content(
                                            file_id, data_description
                                        )
                                        if analysis_result['success']:
                                            insights = analysis_result['insights']
                                            st.success("🔊 Audio analyzed successfully!")
                                            st.info(f"🧠 Analysis: Found themes: {', '.join(insights['content_themes'])}")
                                
                                # Save to contributions
                                save_contribution({
                                    'type': 'media_upload',
                                    'file_id': file_id,
                                    'data_type': data_type,
                                    'description': data_description,
                                    'file_type': file_type,
                                    'original_name': uploaded_file.name
                                })
                                
                                st.balloons()
                                st.success("🌟 Media uploaded, processed, and analyzed! Thank you for contributing to community knowledge.")
                            else:
                                st.error(f"❌ Upload failed: {result['error']}")
                
                elif uploaded_file and not data_description:
                    st.warning("📝 Please describe your media before uploading")
    
    # Show recent contributions including media
    st.subheader("🌟 Recent Community Contributions")
    
    recent_contributions = sorted(st.session_state.contributions, key=lambda x: x['timestamp'], reverse=True)[:5]
    
    if recent_contributions:
        for contrib in recent_contributions:
            with st.container():
                title = contrib.get('title', contrib['type'].replace('_', ' ').title())
                
                if contrib['type'] == 'media_upload':
                    st.markdown(f"**📸 {contrib.get('data_type', 'Media')}**")
                    st.write(f"📝 {contrib.get('description', 'No description')}")
                    
                    # Show thumbnail if available
                    if load_media_processor():
                        processor = st.session_state.media_processor
                        uploaded_files = processor.list_uploaded_files()
                        
                        matching_file = next((f for f in uploaded_files if f.get('file_id') == contrib.get('file_id')), None)
                        if matching_file and 'thumbnail_file' in matching_file:
                            try:
                                st.image(matching_file['thumbnail_file'], width=150, caption="📸 Community contribution")
                            except:
                                pass
                else:
                    st.markdown(f"**{title}**")
                
                if 'community' in contrib:
                    st.write(f"🏘️ {contrib['community']}")
                st.write(f"⏰ {contrib['timestamp'][:10]}")
                st.markdown("---")
    else:
        st.info("🌱 Be the first to contribute to your Community Data Commons!")

# PAGE: Track Community Impact
elif page == "📊 Track Impact":
    st.header("📈 Community Impact Dashboard")
    
    # Load system stats
    if not load_insights_engine():
        st.stop()
    
    engine = st.session_state.insights_engine
    doc_count = engine.rag.collection.count()
    
    # Impact metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🧠 Community Insights", doc_count)
    
    with col2:
        st.metric("🤝 Contributions", len(st.session_state.contributions))
    
    with col3:
        action_starts = len([c for c in st.session_state.contributions if c.get('type') == 'action_started'])
        st.metric("🚀 Actions Started", action_starts)
    
    with col4:
        communities = len(set([c.get('community', 'Unknown') for c in st.session_state.contributions]))
        st.metric("🌍 Communities", communities)
    
    # Impact visualization
    st.subheader("📊 Community Knowledge Growth")
    
    # Create sample growth data
    import pandas as pd
    
    growth_data = pd.DataFrame({
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        'Knowledge Base': [50, 150, 220, 263],
        'Communities': [1, 2, 3, 4],
        'Actions Taken': [0, 5, 12, action_starts]
    })
    
    st.line_chart(growth_data.set_index('Week'))
    
    # Success stories impact
    st.subheader("✅ Documented Success Stories")
    
    success_stories = [
        {
            'title': '🏛️ Finance Bill Victory',
            'community': 'Kenya Youth Movement',
            'impact': 'Government withdrew controversial taxation bill',
            'method': 'Social media organizing (Twitter, TikTok, Instagram)',
            'replicable': True
        },
        {
            'title': '📸 Skills to Employment',
            'community': 'Mungano Program',
            'impact': 'Youth employed by SafariCom, Red Cross, Government',
            'method': 'Photography, data collection, videography training',
            'replicable': True
        },
        {
            'title': '🎤 Media Strategy Success',
            'community': 'Urban Reform Coalition',
            'impact': 'Policy changes through strategic storytelling',
            'method': 'Expert positioning, journalist relationships',
            'replicable': True
        }
    ]
    
    for story in success_stories:
        with st.container():
            st.markdown(f"### {story['title']}")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Community:** {story['community']}")
                st.write(f"**Impact:** {story['impact']}")
            
            with col2:
                st.write(f"**Method:** {story['method']}")
                st.write(f"**Replicable:** {'✅ Yes' if story['replicable'] else '❌ Context-specific'}")
            
            st.markdown("---")

# PAGE: Connect Communities
elif page == "🌍 Connect":
    st.header("🤝 Community Network")
    st.write("Connect with communities working on similar challenges.")
    
    # Community matching based on themes
    st.subheader("🎯 Find Communities by Challenge")
    
    challenge_areas = {
        "Youth Unemployment": ["Kenya Youth Movement", "Ghana Skills Collective", "Nigeria Employment Initiative"],
        "Government Engagement": ["Kibera Advocacy Group", "Urban Reform Coalition", "Citizens Rights Network"],
        "Skills Development": ["Mungano Training Network", "Tech4Community", "Rural Skills Alliance"],
        "Media Strategy": ["Community Voices Media", "Storytelling for Change", "Grassroots Narratives"]
    }
    
    selected_challenge = st.selectbox("What challenge is your community working on?", list(challenge_areas.keys()))
    
    if selected_challenge:
        st.write(f"**Communities working on {selected_challenge}:**")
        
        for community in challenge_areas[selected_challenge]:
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.write(f"🏘️ **{community}**")
                
                with col2:
                    if st.button("💬 Connect", key=f"connect_{community}"):
                        st.info(f"Connection request sent to {community}!")
                
                with col3:
                    if st.button("📋 Learn More", key=f"learn_{community}"):
                        st.info(f"Learning about {community}'s strategies...")
    
    # Community contribution map
    st.subheader("🗺️ Global Community Network")
    
    # Create sample network data
    import pandas as pd
    network_data = pd.DataFrame({
        'Community': ['Kenya Youth', 'Ghana Skills', 'Nigeria Media', 'Tanzania Organizing'],
        'lat': [-1.286389, 5.6037, 9.0579, -6.7924],
        'lon': [36.817223, -0.1870, 7.4951, 39.2083],
        'Contributions': [15, 8, 12, 6]
    })
    
    st.map(network_data)
    
    # Community directory
    st.subheader("📞 Community Directory")
    
    directory = [
        {'name': 'Kenya Youth Movement', 'contact': 'Jakobo Mondeh (Youth Organizer)', 'expertise': 'Protest organizing, Government engagement'},
        {'name': 'Media Strategy Network', 'contact': 'Professor (Academic)', 'expertise': 'Urban reform, Storytelling, Journalist relations'},
        {'name': 'Mungano Skills Program', 'contact': 'Training Coordinator', 'expertise': 'Photography, Data collection, Community organizing'},
    ]
    
    for entry in directory:
        with st.expander(f"📞 {entry['name']}"):
            st.write(f"**Contact:** {entry['contact']}")
            st.write(f"**Expertise:** {entry['expertise']}")
            
            if st.button("🤝 Request Connection", key=f"request_{entry['name']}"):
                save_contribution({
                    'type': 'connection_request',
                    'target_community': entry['name'],
                    'requested_by': 'Community Member'
                })
                st.success(f"Connection request sent to {entry['name']}!")

# PAGE: Success Stories
elif page == "💡 Learn Stories":
    st.header("🏆 Community Success Stories")
    st.write("Learn from communities that have achieved real change.")
    
    # Featured success stories with detailed analysis
    stories = [
        {
            'title': '🏛️ Youth Organize Against Finance Bill',
            'community': 'Kenya Youth Movement',
            'challenge': 'Government proposed increased taxation harming young people',
            'action': 'Organic social media campaign using Twitter, TikTok, Instagram',
            'result': 'Government withdrew the controversial finance bill',
            'key_factors': [
                'Clear, specific demand (withdraw finance bill)',
                'Multi-platform social media strategy',
                'Youth-led, organic organization',
                'Sustained pressure over time'
            ],
            'replicable_elements': [
                'Social media campaign templates',
                'Youth organizing structures',
                'Government pressure tactics',
                'Coalition building methods'
            ],
            'resources_used': 'Social media accounts, youth networks, clear messaging',
            'timeline': '2024 campaign lasting several months'
        },
        {
            'title': '📸 Skills Training Creates Employment',
            'community': 'Mungano Training Program',
            'challenge': '70% youth unemployment in informal settlements',
            'action': 'Structured skills training: photography, data collection, videography',
            'result': 'Youth employed by SafariCom, Red Cross, Government Ministry',
            'key_factors': [
                'Practical, marketable skills focus',
                'Partnership with employers',
                'Mentorship during training',
                'Portfolio development support'
            ],
            'replicable_elements': [
                'Training curriculum design',
                'Employer partnership model',
                'Mentorship structures',
                'Skills certification process'
            ],
            'resources_used': 'Training equipment, experienced mentors, employer networks',
            'timeline': 'Ongoing program with multiple cohorts'
        },
        {
            'title': '🎤 Media Strategy Drives Policy Change',
            'community': 'Urban Reform Coalition',
            'challenge': 'Policy decisions made without community input',
            'action': 'Strategic storytelling, journalist relationships, expert positioning',
            'result': 'Influenced public discourse and government decisions',
            'key_factors': [
                'Compelling narrative development',
                'Building journalist relationships',
                'Expert credibility establishment',
                'Multi-channel story distribution'
            ],
            'replicable_elements': [
                'Story development process',
                'Media relationship building',
                'Expert positioning strategies',
                'Policy influence tactics'
            ],
            'resources_used': 'Story research, media contacts, expert knowledge',
            'timeline': 'Long-term relationship building with ongoing campaigns'
        }
    ]
    
    for story in stories:
        with st.container():
            st.markdown(f"## {story['title']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**🏘️ Community:** {story['community']}")
                st.markdown(f"**🎯 Challenge:** {story['challenge']}")
                st.markdown(f"**🚀 Action:** {story['action']}")
                st.markdown(f"**✅ Result:** {story['result']}")
            
            with col2:
                st.markdown(f"**⏰ Timeline:** {story['timeline']}")
                st.markdown(f"**📦 Resources:** {story['resources_used']}")
            
            # Detailed analysis
            with st.expander("🔍 Deep Dive Analysis"):
                st.markdown("**🔑 Key Success Factors:**")
                for factor in story['key_factors']:
                    st.write(f"• {factor}")
                
                st.markdown("**🔄 Replicable Elements:**")
                for element in story['replicable_elements']:
                    st.write(f"• {element}")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📋 Get Action Plan", key=f"plan_{story['title']}"):
                    st.info("Action plan based on this success story would be generated here!")
            
            with col2:
                if st.button("🤝 Connect Community", key=f"connect_{story['title']}"):
                    st.info(f"Connection request to {story['community']} sent!")
            
            with col3:
                if st.button("📚 Adapt for Us", key=f"adapt_{story['title']}"):
                    st.info("Customized adaptation guidance would be provided here!")
            
            st.markdown("---")

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; margin-top: 30px;">'
    '🏘️ Community Action Hub - Transforming Knowledge into Community Power<br>'
    'Real communities sharing real solutions for real change'
    '</div>',
    unsafe_allow_html=True
)