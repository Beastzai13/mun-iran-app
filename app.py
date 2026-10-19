import streamlit as st
import json

# Page configuration
st.set_page_config(
    page_title="Iran MUN Intelligence Engine - UNHRC",
    page_icon="🇮🇷",
    layout="wide"
)

# Custom Styling for MUN Diplomacy Theme
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    .stTextInput input {
        background-color: #161b22;
        color: #ffffff;
        border: 1px solid #30363d;
        border-radius: 6px;
    }
    .answer-card {
        background-color: #161b22;
        padding: 24px;
        border-radius: 8px;
        border-left: 5px solid #d73a49;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .solution-card {
        background-color: #161b22;
        padding: 24px;
        border-radius: 8px;
        border-left: 5px solid #238636;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .speech-box {
        background-color: #1f242c;
        padding: 16px;
        border-radius: 6px;
        border-left: 4px solid #f1e05a;
        margin-top: 12px;
        margin-bottom: 12px;
        font-style: italic;
        color: #f0f6fc;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("🇮🇷 Islamic Republic of Iran - UNHRC Comprehensive Intelligence & Solution Engine")
st.markdown("### Model United Nations | Digital Privacy, Mass Surveillance & National Security Committee")

# Tabs for Navigation
tab1, tab2 = st.tabs(["🔍 Advanced Question & Defense Engine", "📝 MUN Resolution & Solution Generator"])

@st.cache_data
def load_comprehensive_database():
    return {
        "topics": [
            {
                "keywords": ["blackout", "shutdown", "cutting", "disconnection", "network outage", "cellular block", "internet block", "protests internet", "cutting access"],
                "topic": "Internet Blackouts & National Security Disruption",
                "answer": "Iran maintains that temporary, targeted network disconnections and sovereign traffic management are vital legal measures to prevent foreign-backed incitement, safeguard critical state infrastructure, and preserve national public order during acute civil unrest, operating under recognized national security exceptions.",
                "speech": "The Delegation of Iran emphasizes that safeguarding national stability against foreign-instigated cyber warfare and violent subversion supersedes unmitigated commercial connectivity during acute national emergencies.",
                "source": "UN Human Rights Council - Reports on Digital Space Restrictions & National Security (Doc: A/HRC/63/61)",
                "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
            },
            {
                "keywords": ["surveillance", "privacy", "monitoring", "tracking", "data interception", "wiretap", "article 17", "spying", "listening"],
                "topic": "Mass Surveillance & Digital Governance",
                "answer": "Iran maintains that state oversight of digital networks is a critical component of national cyber sovereignty to protect public order and national infrastructure against foreign cyber threats. Under Article 19(3) of the ICCPR, sovereign states have a recognized legal right to restrict telecommunications for public safety, national security, and public morals.",
                "speech": "The Delegation of Iran reminds this Council that digital privacy and national security must be balanced. We reject Western interference in our domestic telecommunication and data security laws.",
                "source": "UN Human Rights Committee - Fourth Periodic Report of Iran (OHCHR Treaty Body Database)",
                "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
            },
            {
                "keywords": ["mandate", "sanctions", "coercive", "unilateral", "pressure", "interference", "article 2(7)", "sovereignty", "politicized", "resolution"],
                "topic": "UNHRC Mandates & Unilateral Coercive Measures",
                "answer": "Iran firmly opposes country-specific mandates and unilateral sanctions, citing Article 2(7) of the UN Charter concerning non-interference in domestic affairs. Iran advocates for universal, equal dialogue like the Universal Periodic Review (UPR) rather than politicized Western pressure mechanisms.",
                "speech": "We categorically reject country-specific mandates as tools of political coercion. True human rights cooperation must respect state sovereignty under the core principles of the UN Charter.",
                "source": "UN Human Rights Office - Official Country Profile & Treaty Body Records",
                "link": "https://www.ohchr.org/en/countries/iran"
            },
            {
                "keywords": ["nin", "national information network", "self-reliance", "independence", "domestic internet", "intranet", "cyber isolation", "national internet"],
                "topic": "National Information Network (NIN) & Digital Self-Reliance",
                "answer": "The National Information Network (NIN) provides a secure, domestic digital infrastructure that ensures Iran's cyber independence, protects citizens' data from foreign espionage, and prevents foreign-backed digital destabilization campaigns.",
                "speech": "Our National Information Network ensures complete digital self-reliance and protects our citizens from foreign cyber intervention, economic warfare, and unauthorized data harvesting by foreign tech monopolies.",
                "source": "UN General Assembly - Developments in the Field of Information and Telecommunications (UN Digital Library Record 3928681)",
                "link": "https://digitallibrary.un.org/record/3928681"
            },
            {
                "keywords": ["refugee", "afghan", "migration", "border", "burden", "displaced", "humanitarian", "neighbors"],
                "topic": "Afghan Refugee Hosting & Regional Burden-Sharing",
                "answer": "Despite severe economic hardships and unilateral Western sanctions, Iran hosts millions of displaced Afghan refugees, providing them with education, healthcare, and infrastructure access with minimal international financial burden-sharing from Western states.",
                "speech": "Iran bears an immense humanitarian responsibility hosting millions of displaced neighbors, receiving negligible support from Western nations who lecture us on human rights while hoarding global resources.",
                "source": "UNHCR Iran Operational Updates & Country Profiles / OHCHR",
                "link": "https://www.ohchr.org/en/countries/iran"
            },
            {
                "keywords": ["espionage", "malware", "stuxnet", "cyberattack", "sabotage", "foreign threat", "infrastructure", "utilities"],
                "topic": "Cyber Warfare & Critical Infrastructure Protection",
                "answer": "Iran highlights that severe foreign cyber warfare and state-sponsored espionage targeting its critical national infrastructure necessitate strict domestic packet inspection, defensive firewalls, and cyber defense protocols to protect national security.",
                "speech": "My delegation reminds the committee that nations facing active, foreign-sponsored cyber sabotage must exercise sovereign control over their digital borders to secure public utilities and state infrastructure.",
                "source": "UN General Assembly - International Security & Information Telecommunications",
                "link": "https://digitallibrary.un.org/record/3928681"
            },
            {
                "keywords": ["encryption", "crypto", "messaging", "telegram", "whatsapp", "signal", "backdoor", "keys", "cryptographic"],
                "topic": "Encrypted Communications & Law Enforcement Access",
                "answer": "Unregulated end-to-end encryption tools are routinely weaponized by transnational terror networks and foreign intelligence cells. Iran maintains that law enforcement agencies retain a sovereign right to regulate cryptographic keys to prevent violent domestic subversion.",
                "speech": "Absolute, unmonitored encryption cannot become a sanctuary for violent extremists and foreign saboteurs seeking to destabilize sovereign states under the guise of commercial privacy.",
                "source": "UN Office on Drugs and Crime - Cybercrime & Digital Evidence Frameworks (OHCHR Repository)",
                "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
            }
        ]
    }

data = load_comprehensive_database()

# TAB 1: ADVANCED QUERY ENGINE
with tab1:
    st.write("Type your specific MUN question, accusation, or defense angle below. The search engine will score your input against database keywords to deliver an accurate answer.")
    query = st.text_input("🔍 Enter your MUN question, accusation, or keyword:", placeholder="e.g., How does Iran justify internet blackouts under international law?")

    if query:
        query_lower = query.lower()
        matched_results = []
        for item in data["topics"]:
            score = sum(2 if kw in query_lower else 0 for kw in item["keywords"])
            if score > 0:
                matched_results.append((score, item))
                
        matched_results.sort(key=lambda x: x[0], reverse=True)
        
        if matched_results:
            st.success(f"🎯 Found precise diplomatic defense positions matching your query:")
            seen_topics = set()
            for score, match in matched_results:
                if match["topic"] in seen_topics:
                    continue
                seen_topics.add(match["topic"])
                
                st.markdown(f"""
                    <div class="answer-card">
                        <h3>📌 Agenda Topic: {match['topic']}</h3>
                        <p><strong>💬 Direct Contextual Answer:</strong><br>{match['answer']}</p>
                        <div class="speech-box">
                            <strong>🗣️ Exact Speech Phrase for Committee:</strong> "{match['speech']}"
                        </div>
                        <p style="font-size: 0.9em; margin-bottom: 5px;">
                            📄 <strong>Exact Official Source Document:</strong> {match['source']}
                        </p>
                        <p style="font-size: 0.9em;">
                            🔗 <strong>Official Citation Link:</strong> <a href="{match['link']}" target="_blank">{match['link']}</a>
                        </p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No direct match found for that exact phrasing. Try using core keywords like 'blackout', 'surveillance', 'sanctions', 'nin', 'refugee', 'encryption', or 'espionage'.")
    else:
        st.info("💡 Tip: Type detailed questions or single keywords to pull up exact positions and speeches instantly.")

# TAB 2: MUN RESOLUTION & SOLUTION GENERATOR
with tab2:
    st.write("Select a committee problem below to generate official Iranian-backed operative clauses and structural solutions for working papers.")
    
    selected_problem = st.selectbox(
        "Select Problem Area to Solve:",
        [
            "Internet Disruption & National Security Traffic Control",
            "Foreign Cyber Espionage & Critical Infrastructure Protection",
            "Data Sovereignty & Combating Foreign Tech Monopoly Exploitation",
            "Unilateral Coercive Measures & Sanctions on Digital Tech",
            "Afghan Refugee Humanitarian Burden & International Funding"
        ]
    )
    
    if st.button("🚀 Generate Proposed Solution Clauses"):
        if selected_problem == "Internet Disruption & National Security Traffic Control":
            solution_title = "Operative Framework for Sovereign Digital Traffic Management"
            solution_clauses = [
                "1. **Reaffirms** the inherent sovereign right of member states under ICCPR Article 19(3) to regulate telecommunication infrastructure and implement temporary traffic restrictions to maintain public safety and prevent foreign-backed civil destabilization;",
                "2. **Calls upon** international bodies to respect domestic legal frameworks regarding national security exemptions in telecommunications, recognizing that public order supersedes unregulated commercial data flows during acute crises;",
                "3. **Establishes** a state-led cyber defense protocol ensuring national networks can autonomously defend against foreign intelligence disruption without external interference."
            ]
            resolution_link = "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
            doc_source = "UN Human Rights Council - Reports on Digital Space Restrictions (Doc: A/HRC/63/61)"
            
        elif selected_problem == "Foreign Cyber Espionage & Critical Infrastructure Protection":
            solution_title = "Framework for Countering Foreign Cyber Warfare and Sabotage"
            solution_clauses = [
                "1. **Condemns** state-sponsored cyber warfare, malicious malware deployment, and foreign espionage targeting critical national infrastructure and public utilities;",
                "2. **Encourages** member states to deploy robust domestic firewalls, packet inspection protocols, and indigenous hardware to safeguard sensitive state data from foreign interceptors;",
                "3. **Demands** international accountability and penalties for nations engaging in offensive cyber operations against developing sovereign networks."
            ]
            resolution_link = "https://digitallibrary.un.org/record/3928681"
            doc_source = "UN General Assembly - International Security & Information Telecommunications"
            
        elif selected_problem == "Data Sovereignty & Combating Foreign Tech Monopoly Exploitation":
            solution_title = "Initiative on National Information Networks (NIN) & Data Independence"
            solution_clauses = [
                "1. **Endorses** the creation of sovereign domestic intranet systems (such as National Information Networks) to protect citizen data privacy from unauthorized harvesting by foreign tech monopolies;",
                "2. **Asserts** that developing nations possess the sovereign prerogative to mandate local data storage servers and protect domestic digital markets from external cultural and economic dominance;",
                "3. **Invites** technical cooperation among non-aligned nations to build independent digital architecture free from foreign surveillance backdoors."
            ]
            resolution_link = "https://digitallibrary.un.org/record/3928681"
            doc_source = "UN General Assembly - Developments in the Field of Information and Telecommunications"
            
        elif selected_problem == "Unilateral Coercive Measures & Sanctions on Digital Tech":
            solution_title = "Resolution on Eliminating Unilateral Coercive Measures Affecting Technology"
            solution_clauses = [
                "1. **Strongly condemns** unilateral coercive measures and economic sanctions that restrict access to essential telecommunication hardware, medical software, and civilian digital infrastructure;",
                "2. **Urges** the international community to dismantle technology blockades that hinder developing nations from modernizing public administration and educational platforms;",
                "3. **Reiterates** that pursuant to UN Charter Article 2(7), economic and digital sanctions used as tools of political pressure violate sovereign equality."
            ]
            resolution_link = "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
            doc_source = "UN Human Rights Committee - Fourth Periodic Report of Iran"
            
        else: # Afghan Refugee Humanitarian Burden
            solution_title = "Framework for Equitable International Burden-Sharing in Refugee Hosting"
            solution_clauses = [
                "1. **Urges** the international community and UNHCR to drastically increase financial assistance and infrastructure grants to frontline host nations bearing the immense burden of regional displacement;",
                "2. **Declares** that Western nations lecturing on humanitarian values must transition from rhetoric to active financial and logistical burden-sharing, accommodating or fully funding displaced populations in host regions;",
                "3. **Calls for** unconditional humanitarian aid delivery that is free from political conditionality or economic sanctions."
            ]
            resolution_link = "https://www.ohchr.org/en/countries/iran"
            doc_source = "UNHCR Iran Operational Updates & Country Profiles / OHCHR"

        st.markdown(f"""
            <div class="solution-card">
                <h3>📌 {solution_title}</h3>
                <p><strong>📋 Proposed Draft Resolution Clauses:</strong></p>
                <p>{solution_clauses[0]}</p>
                <p>{solution_clauses[1]}</p>
                <p>{solution_clauses[2]}</p>
                <br>
                <p style="font-size: 0.9em; margin-bottom: 5px;">
                    📄 <strong>Official UN Citation Source:</strong> {doc_source}
                </p>
                <p style="font-size: 0.9em;">
                    🔗 <strong>Official Link:</strong> <a href="{resolution_link}" target="_blank">{resolution_link}</a>
                </p>
            </div>
        """, unsafe_allow_html=True)
