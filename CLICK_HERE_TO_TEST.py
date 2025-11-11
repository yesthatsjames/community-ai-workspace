#!/usr/bin/env python3
"""
🎯 CLICK HERE TO TEST THE COMMUNITY AI
Just run this file to test the system yourself!
"""

import sys
sys.path.append('/home/yethatsjames/community-ai-workspace/scripts')
from privacy_rag import CommunityRAG

print("🏘️  COMMUNITY DATA COMMONS - INTERACTIVE TEST")
print("=" * 50)
print()

# Initialize the system
print("Loading your community knowledge base...")
rag = CommunityRAG()
print(f"✅ Ready! {rag.collection.count()} community insights loaded")
print()

# Interactive testing
while True:
    print("🔍 ASK THE COMMUNITY KNOWLEDGE BASE ANYTHING:")
    print("   Examples:")
    print("   - How do youth organize in their communities?")
    print("   - What skills training is available?")
    print("   - How does media help communities?")
    print("   - What are the barriers to organizing?")
    print()
    
    query = input("Your question (or 'quit' to exit): ")
    
    if query.lower() in ['quit', 'exit', 'q']:
        break
    
    if not query.strip():
        continue
    
    print(f"\n🧠 Searching community knowledge for: '{query}'")
    print("-" * 40)
    
    results = rag.query_knowledge_base(query, n_results=3)
    
    for i, result in enumerate(results['results'], 1):
        similarity = result['similarity']
        community = result['metadata']['community']
        participant = result['metadata']['participant_id']
        content = result['content']
        
        print(f"\n{i}. [{similarity:.3f} match] {community} - {participant}")
        print(f"   \"{content[:200]}{'...' if len(content) > 200 else ''}\"")
    
    print("\n" + "="*50)

print("\n👋 Thanks for testing the Community Data Commons!")