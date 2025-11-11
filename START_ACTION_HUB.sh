#!/bin/bash

echo "🚀 LAUNCHING COMMUNITY ACTION HUB..."
echo "====================================="
echo
echo "🎯 Opening actionable community empowerment interface..."
echo "💪 Transform knowledge into concrete community action!"
echo
echo "➡️  Your Action Hub will open at: http://localhost:8502"
echo
echo "🔥 Starting in 3 seconds..."
sleep 3

cd /home/yethatsjames/community-ai-workspace
streamlit run community_action_hub.py --server.port 8502 --server.address localhost