#!/bin/bash

echo "🚀 STARTING COMMUNITY DATA COMMONS GUI..."
echo "========================================="
echo
echo "🌐 Opening web browser interface..."
echo "📱 Click buttons instead of typing commands!"
echo
echo "➡️  Your GUI will open at: http://localhost:8501"
echo
echo "🔥 Starting in 3 seconds..."
sleep 3

cd /home/yethatsjames/community-ai-workspace
streamlit run community_gui.py --server.port 8501 --server.address localhost