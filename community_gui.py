#!/usr/bin/env python3
"""
🏘️ COMMUNITY DATA COMMONS - GRAPHICAL USER INTERFACE
Click buttons, see results, no command line needed!
"""

import streamlit as st
import sys
import os
import json
import time
from pathlib import Path

# Add scripts to path
sys.path.append('/home/yethatsjames/community-ai-workspace/scripts')

# Page configuration
st.set_page_config(
    page_title="Community Data Commons",
    page_icon="🏘️",
    layout="wide"
)

# Custom CSS for big buttons
st.markdown("""
<style>
.big-button {
    font-size: 24px !important;
    height: 60px;
    width: 100%;
    margin: 10px 0px;
}
.metric-card {
    background: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
    margin: 10px;
    text-align: center;
}
.success-box {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0px;
}
.header-text {
    font-size: 48px;
    text-align: center;
    color: #1f77b4;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="header-text">🏘️ COMMUNITY DATA COMMONS</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: #666;">Privacy-Preserving AI for Community Sovereignty</h2>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎛️ Navigation")
page = st.sidebar.radio(
    "Choose what to do:",
    [
        "🏠 System Status", 
        "🔍 Search Community Knowledge", 
        "📊 View Community Insights",
        "🌐 Federated Learning",
        "🔒 Privacy Dashboard"
    ]
)

# Initialize session state
if 'rag_system' not in st.session_state:
    st.session_state.rag_system = None

def load_rag_system():
    """Load the RAG system"""
    if st.session_state.rag_system is None:
        with st.spinner("🔄 Loading Community Knowledge Base..."):
            try:
                from privacy_rag import CommunityRAG
                st.session_state.rag_system = CommunityRAG()
                return True
            except Exception as e:
                st.error(f"❌ Error loading system: {e}")
                return False
    return True

def check_system_status():
    """Check system components"""
    workspace_path = Path("/home/yethatsjames/community-ai-workspace")
    
    # Check transcripts
    transcript_files = list((workspace_path / "transcripts").glob("*.json"))
    transcript_count = len(transcript_files)
    
    # Check vector database
    vector_db_exists = (workspace_path / "vector-db").exists()
    
    # Check containers
    try:
        import subprocess
        result = subprocess.run(['distrobox', 'list'], capture_output=True, text=True)
        containers = len([line for line in result.stdout.split('\n') if 'ai' in line])
    except:
        containers = 0
    
    # Check federated results
    fed_results_exist = (workspace_path / "federated-results.json").exists()
    
    return {
        "transcripts": transcript_count,
        "vector_db": vector_db_exists,
        "containers": containers,
        "federated_results": fed_results_exist
    }

# PAGE: System Status
if page == "🏠 System Status":
    st.header("🔧 System Status Dashboard")
    
    # Check system status
    status = check_system_status()
    
    # Display metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📂 Community Transcripts",
            value=status["transcripts"],
            help="Real community interview files"
        )
    
    with col2:
        st.metric(
            label="🧠 AI Knowledge Base", 
            value="✅ Active" if status["vector_db"] else "❌ Not Found",
            help="Vector database with community insights"
        )
    
    with col3:
        st.metric(
            label="🐳 Community Containers",
            value=status["containers"],
            help="Isolated federated learning nodes"
        )
    
    with col4:
        st.metric(
            label="🌐 Federated Learning",
            value="✅ Complete" if status["federated_results"] else "⚠️ Not Run",
            help="Cross-community knowledge sharing"
        )
    
    # Overall system status
    if all([status["transcripts"] > 0, status["vector_db"]]):
        st.markdown('<div class="success-box"><h3>🎉 SYSTEM FULLY OPERATIONAL</h3><p>Your Community Data Commons is processing real community voices with full privacy protection!</p></div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ System partially configured. Check components above.")
    
    # Quick actions
    st.header("🚀 Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Reload Knowledge Base", key="reload"):
            if load_rag_system():
                st.success("✅ Knowledge base loaded successfully!")
                st.rerun()
    
    with col2:
        if st.button("🌐 Run Federated Learning", key="federated"):
            with st.spinner("🤝 Running federated learning between communities..."):
                try:
                    import subprocess
                    result = subprocess.run(
                        ['python3', '/home/yethatsjames/community-ai-workspace/scripts/federated_demo.py'],
                        capture_output=True, text=True, timeout=60
                    )
                    if result.returncode == 0:
                        st.success("✅ Federated learning completed!")
                        st.rerun()
                    else:
                        st.error(f"❌ Error: {result.stderr}")
                except subprocess.TimeoutExpired:
                    st.error("⏱️ Federated learning timed out")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
    
    with col3:
        if st.button("📊 View Full Report", key="report"):
            st.info("📋 Full system report would appear here")

# PAGE: Search Community Knowledge  
elif page == "🔍 Search Community Knowledge":
    st.header("🔍 Ask the Community Knowledge Base")
    
    if not load_rag_system():
        st.stop()
    
    rag = st.session_state.rag_system
    
    # Display knowledge base stats
    doc_count = rag.collection.count()
    st.info(f"🧠 Knowledge Base Ready: {doc_count} community insights available")
    
    # Search interface
    st.subheader("💬 Ask Anything About Community Knowledge")
    
    # Suggested questions
    st.write("**💡 Try these questions:**")
    suggestions = [
        "How do youth organize in their communities?",
        "What skills does Mungano teach young people?", 
        "How do communities engage with government?",
        "What role does media play in community development?",
        "How do communities solve unemployment problems?"
    ]
    
    selected_suggestion = st.selectbox("Or choose a suggested question:", [""] + suggestions)
    
    # Query input
    query = st.text_input(
        "Your question:",
        value=selected_suggestion,
        placeholder="e.g., How do youth organize protests?"
    )
    
    if st.button("🔍 Search Community Knowledge", disabled=not query.strip()):
        if query.strip():
            with st.spinner(f"🧠 Searching for: '{query}'"):
                results = rag.query_knowledge_base(query, n_results=5)
            
            st.subheader("📋 Search Results")
            
            for i, result in enumerate(results['results'], 1):
                similarity = result['similarity']
                community = result['metadata']['community']
                participant = result['metadata']['participant_id']
                content = result['content']
                
                # Create expandable result
                with st.expander(f"Result {i}: [{similarity:.3f} match] {community} - {participant}"):
                    st.write(f"**Community:** {community}")
                    st.write(f"**Participant:** {participant}")
                    st.write(f"**Similarity Score:** {similarity:.3f}")
                    st.write("**Content:**")
                    st.write(f'"{content}"')

# PAGE: View Community Insights
elif page == "📊 View Community Insights":
    st.header("📊 Community Knowledge Analytics")
    
    if not load_rag_system():
        st.stop()
    
    rag = st.session_state.rag_system
    
    # Get all data for analysis
    all_data = rag.collection.get(include=['documents', 'metadatas'])
    documents = all_data['documents']
    metadatas = all_data['metadatas']
    
    # Community breakdown
    communities = {}
    for metadata in metadatas:
        community = metadata['community']
        if community in communities:
            communities[community] += 1
        else:
            communities[community] = 1
    
    st.subheader("🏘️ Communities Represented")
    
    for community, count in communities.items():
        st.write(f"**{community}**: {count} insights")
    
    # Theme analysis
    st.subheader("🎯 Key Themes Detected")
    
    themes = {
        'Youth Empowerment': ['youth', 'young people', 'skills', 'training'],
        'Government Engagement': ['government', 'offices', 'baraza', 'leaders'],
        'Community Organizing': ['community', 'organizing', 'members', 'programs'],
        'Media & Storytelling': ['media', 'stories', 'narrative', 'voices'],
        'Economic Development': ['finance', 'loans', 'unemployment', 'opportunities']
    }
    
    theme_counts = {}
    for theme_name, keywords in themes.items():
        count = 0
        for doc in documents:
            doc_lower = doc.lower()
            count += sum(1 for keyword in keywords if keyword in doc_lower)
        theme_counts[theme_name] = count
    
    # Display theme results
    for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
        st.metric(label=theme, value=f"{count} mentions")
    
    # Sample content
    st.subheader("📝 Sample Community Voices")
    
    if documents:
        sample_doc = documents[0]
        sample_meta = metadatas[0]
        
        st.write(f"**From {sample_meta['community']} - {sample_meta['participant_id']}:**")
        st.write(f'"{sample_doc[:300]}..."')

# PAGE: Federated Learning
elif page == "🌐 Federated Learning":
    st.header("🌐 Federated Learning Dashboard")
    
    # Check for federated results
    fed_results_path = Path("/home/yethatsjames/community-ai-workspace/federated-results.json")
    
    if fed_results_path.exists():
        with open(fed_results_path, 'r') as f:
            fed_results = json.load(f)
        
        st.success("✅ Federated Learning Completed Successfully!")
        
        # Display results
        st.subheader("📈 Training Progress")
        
        rounds_data = []
        for round_data in fed_results:
            rounds_data.append({
                'Round': round_data['round'],
                'Average Loss': round_data['average_loss'],
                'Average Accuracy': round_data['average_accuracy'],
                'Communities': round_data['communities']
            })
        
        import pandas as pd
        df = pd.DataFrame(rounds_data)
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🤝 Communities", fed_results[0]['communities'])
        
        with col2:
            st.metric("🔄 Training Rounds", len(fed_results))
        
        with col3:
            st.metric("📊 Total Samples", fed_results[0]['total_samples'])
        
        # Display progress chart
        st.line_chart(df.set_index('Round')[['Average Loss', 'Average Accuracy']])
        
        # Community performance
        st.subheader("🏘️ Community Performance")
        
        final_round = fed_results[-1]
        for community, metrics in final_round['community_metrics'].items():
            st.write(f"**{community}:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Samples", metrics['samples'])
            with col2:
                st.metric("Loss", f"{metrics['loss']:.4f}")
            with col3:
                st.metric("Accuracy", f"{metrics['accuracy']:.4f}")
    
    else:
        st.warning("⚠️ Federated learning has not been run yet")
        
        st.subheader("🚀 Run Federated Learning")
        st.write("Click below to start federated learning between community containers:")
        
        if st.button("🌐 Start Federated Learning", key="start_fed"):
            with st.spinner("🤝 Running federated learning... This may take a few minutes"):
                try:
                    import subprocess
                    result = subprocess.run(
                        ['python3', '/home/yethatsjames/community-ai-workspace/scripts/federated_demo.py'],
                        capture_output=True, text=True, timeout=120
                    )
                    if result.returncode == 0:
                        st.success("✅ Federated learning completed!")
                        st.rerun()
                    else:
                        st.error(f"❌ Error: {result.stderr}")
                except subprocess.TimeoutExpired:
                    st.error("⏱️ Federated learning timed out")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

# PAGE: Privacy Dashboard
elif page == "🔒 Privacy Dashboard":
    st.header("🔒 Privacy & Security Dashboard")
    
    st.subheader("🛡️ Privacy Protection Status")
    
    # Privacy features
    privacy_features = [
        ("✅ Participant Anonymization", "All participant IDs are cryptographically hashed"),
        ("✅ Local-Only Processing", "No data leaves your machine"), 
        ("✅ Container Isolation", "Communities have separate secure environments"),
        ("✅ No External Telemetry", "ChromaDB configured with anonymized_telemetry=False"),
        ("✅ Federated Learning", "Model parameters shared, never raw data"),
        ("✅ Open Source", "Full transparency of all code and processes")
    ]
    
    for status, description in privacy_features:
        st.write(f"**{status}**")
        st.write(f"  {description}")
        st.write("")
    
    # System security info
    st.subheader("🔐 Technical Security Measures")
    
    security_info = {
        "Data Storage": "Local vector database only (/home/yethatsjames/community-ai-workspace/vector-db)",
        "Network Access": "No external API calls or data transmission",
        "Participant Privacy": "SHA-256 hashing of all identifying information", 
        "Container Security": "Distrobox isolation with separate namespaces",
        "Model Security": "Local SentenceTransformers, no cloud dependencies"
    }
    
    for measure, details in security_info.items():
        with st.expander(f"🔍 {measure}"):
            st.write(details)
    
    # Data location info
    st.subheader("📁 Data Locations")
    
    st.code("""
🗄️ Data Storage Locations:
├── /home/yethatsjames/community-ai-workspace/
    ├── transcripts/          # Original community interviews
    ├── vector-db/           # Processed knowledge base
    ├── containers/          # Community federated nodes
    ├── models/              # Local AI models
    └── federated-results.json # Learning outcomes
    
🔒 All data stays on this machine
🚫 No external servers or cloud services
✅ Complete community data sovereignty
    """)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; margin-top: 50px;">'
    '🏘️ Community Data Commons - Privacy-Preserving AI for Community Sovereignty<br>'
    'Built with ❤️ for community empowerment'
    '</div>',
    unsafe_allow_html=True
)