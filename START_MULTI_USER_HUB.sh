#!/bin/bash

echo "🌐 STARTING COMMUNITY ACTION HUB - MULTI-USER ACCESS"
echo "===================================================="
echo
echo "👥 Multiple colleagues can access simultaneously!"
echo "🔒 All processing stays local on your machine"
echo
echo "📱 SHARE THESE URLS WITH YOUR TEAM:"
echo "   Network Access: http://192.168.10.134:8502"
echo "   Local Access:   http://localhost:8502"
echo
echo "🚀 Starting in 3 seconds..."
sleep 3

cd /home/yethatsjames/community-ai-workspace

# Start with network access enabled
streamlit run community_action_hub.py \
    --server.port 8502 \
    --server.address 0.0.0.0 \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --browser.gatherUsageStats false
