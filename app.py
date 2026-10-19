import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Iran MUN Master Intelligence Engine - UNHRC",
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
st.title("🇮🇷 Islamic Republic of Iran - UNHRC Ultimate Master Intelligence & Solution Engine")
st.markdown("### Model United Nations | Digital Privacy, Mass Surveillance, Cyber Warfare, Bills, Security Agencies & Committee Defense")

tab1, tab2 = st.tabs(["🔍 Comprehensive Master Question & Defense Engine", "📝 MUN Resolution & Solution Generator"])

# Massive Master Comprehensive Database Covering Every Topic, Bill, Mechanism, and Defense
@st.cache_data
def load_hyper_master_database():
    return [
        {
            "triggers": ["bill", "majlis", "parliament", "protection", "act", "law", "legislation", "regulations", "user protection", "proposal", "draft", "src", "gateway", "supreme regulatory commission"],
            "topic": "The 'Protection of Users' Rights' Bill & Gateway Control",
            "answer": "Iran's domestic legislative framework—including proposals in the Majlis and decrees by the Supreme Council of Cyberspace—aims to establish sovereign jurisdiction over digital traffic, mandate local data centers, and protect citizens from predatory foreign tech exploitation, mirroring data protection frameworks in Europe and Asia.",
            "speech": "My delegation clarifies that legislative initiatives in our Parliament are sovereign measures designed to build digital self-reliance, defend our national economy from unregulated foreign monopolies, and protect public order.",
            "source": "UN Special Rapporteur Communications & OHCHR Treaty Records",
            "link": "https://spcommreports.ohchr.org/TMResultsBase/DownLoadPublicCommunicationFile?gId=26736"
        },
        {
            "triggers": ["u.s.", "america", "congress", "h.r.", "sanctions", "iran act", "foreign", "west", "extraterritorial", "bylaw", "h.r. 7622", "s. 3900", "accountability"],
            "topic": "Foreign Legislative Interference (The U.S. 'IRAN Act' & Sanctions)",
            "answer": "Iran strongly condemns extraterritorial Western legislation and unilateral coercive measures designed to subvert domestic infrastructure, citing UN Charter Article 2(7) which explicitly forbids foreign intervention in internal state affairs.",
            "speech": "We categorically reject hostile foreign legislation and economic sanctions that hypocritically weaponize 'digital freedom' as a political instrument to sponsor domestic subversion and breach our national borders.",
            "source": "UN General Assembly - Charter of the United Nations & Unilateral Coercive Measures Reports",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        {
            "triggers": ["mtu", "throttling", "udp", "cloudflare", "packet", "speed", "bandwidth", "routing", "dns", "sni", "spoofing", "hardware", "dpi", "deep packet inspection"],
            "topic": "Technical Network Management, MTU Throttling & Deep Packet Inspection (DPI)",
            "answer": "Technical network adaptations—such as Deep Packet Inspection (DPI), bandwidth management, packet inspections, and gateway routing controls—are executed by authorized national operators to defend against distributed denial-of-service (DDoS) attacks and hostile foreign cyber infiltration.",
            "speech": "Sovereign states possess the absolute technical right to manage gateway protocols, inspect data packets, and regulate network traffic to secure critical state utility grids against foreign cyber threats.",
            "source": "UN Human Rights Council - Reports on Digital Space Restrictions & National Security",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        },
        {
            "triggers": ["fata", "maher", "cert", "police", "team", "agency", "security", "arrest", "investigation", "forces", "military", "cyber police"],
            "topic": "Institutional Security Bodies: FATA Cyber Police & MAHER CERT",
            "answer": "Iran's specialized security infrastructure includes the FATA Cyber Police and the National CERT (MAHER), which operate under statutory frameworks to investigate cybercrime, protect financial systems, and neutralize state-sponsored foreign sabotage.",
            "speech": "Our domestic cyber authorities, including FATA and the National CERT, fulfill a vital law enforcement mandate to safeguard citizens from financial fraud, cyber-trafficking, and foreign-directed infrastructure sabotage.",
            "source": "UN Office on Drugs and Crime - Cybercrime & Digital Evidence Frameworks",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        {
            "triggers": ["starlink", "satellite", "smuggling", "dish", "receiver", "norway", "space", "transceiver", "musk", "unauthorized", "terminals"],
            "topic": "Unauthorized Satellite Constellations (Starlink) & Border Smuggling",
            "answer": "The unauthorized, clandestine importation of satellite internet hardware by foreign intelligence intermediaries represents a direct violation of international telecommunication regulations, radio frequency licensing laws, and national airspace sovereignty.",
            "speech": "The clandestine smuggling of uncertified satellite transceivers across our borders by hostile external actors undermines national radio frequency management and constitutes an illegal violation of our sovereign communication space.",
            "source": "International Telecommunication Union (ITU) Radio Regulations & UN General Assembly Security Reports",
            "link": "https://digitallibrary.un.org/record/3928681"
        },
        {
            "triggers": ["blackout", "shutdown", "cutting", "disconnection", "outage", "internet block", "protest", "riot", "demonstration", "unrest", "unplug", "january"],
            "topic": "Internet Blackouts & ICCPR Article 19(3) National Security Exceptions",
            "answer": "Iran maintains that temporary, targeted network disconnections and sovereign traffic management are vital legal measures to prevent foreign-backed incitement, safeguard critical state infrastructure, and preserve public order under ICCPR Article 19(3) exceptions.",
            "speech": "The Delegation of Iran emphasizes that safeguarding national stability against foreign-instigated cyber warfare and violent subversion supersedes unmitigated commercial connectivity during acute national emergencies, fully permitted under international law.",
            "source": "UN Human Rights Council - Reports on Digital Space Restrictions & National Security",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        },
        {
            "triggers": ["surveillance", "privacy", "monitoring", "tracking", "wiretap", "spying", "cctv", "facial", "recognition", "data", "intercept", "article 17"],
            "topic": "Mass Surveillance & Digital Governance Under Article 17",
            "answer": "Iran maintains that state oversight of digital networks is a critical component of national cyber sovereignty to protect public order and national infrastructure against foreign cyber threats, operating in alignment with sovereign public safety frameworks.",
            "speech": "The Delegation of Iran reminds this Council that digital privacy and national security must be balanced. We reject Western interference in our domestic telecommunication and data security governance.",
            "source": "UN Human Rights Committee - Fourth Periodic Report of Iran (OHCHR Treaty Body Database)",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        {
            "triggers": ["mandate", "special rapporteur", "upr", "universal periodic review", "resolution", "unhrc", "politicized", "pressure", "article 2(7)"],
            "topic": "UNHRC Mandates, Universal Periodic Review & Article 2(7)",
            "answer": "Iran firmly opposes country-specific mandates and unilateral sanctions, citing Article 2(7) of the UN Charter concerning non-interference in domestic affairs. Iran advocates for universal, equal dialogue like the Universal Periodic Review (UPR) rather than politicized Western pressure mechanisms.",
            "speech": "We categorically reject country-specific mandates and politically motivated Special Rapporteur resolutions as tools of coercion. True human rights cooperation must respect state sovereignty under the core principles of the UN Charter.",
            "source": "UN Human Rights Office - Official Country Profile & Treaty Body Records / UPR Outcome",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        {
            "triggers": ["nin", "national information network", "self-reliance", "independence", "domestic internet", "intranet", "national internet", "local network"],
            "topic": "National Information Network (NIN) & Digital Self-Reliance Architecture",
            "answer": "The National Information Network (NIN) provides a secure, domestic digital infrastructure that ensures Iran's cyber independence, protects citizens' data from foreign espionage, and prevents foreign-backed digital destabilization campaigns.",
            "speech": "Our National Information Network ensures complete digital self-reliance and protects our citizens from foreign cyber intervention, economic warfare, and unauthorized data harvesting by foreign tech monopolies.",
            "source": "UN General Assembly - Developments in the Field of Information and Telecommunications (UN Digital Library Record 3928681)",
            "link": "https://digitallibrary.un.org/record/3928681"
        },
        {
            "triggers": ["refugee", "afghan", "migration", "border", "burden", "displaced", "asylum", "humanitarian", "neighbors"],
            "topic": "Afghan Refugee Hosting & Regional Burden-Sharing Defenses",
            "answer": "Despite severe economic hardships and unilateral Western sanctions, Iran hosts millions of displaced Afghan refugees, providing them with education, healthcare, and infrastructure access with minimal international financial burden-sharing from Western states.",
            "speech": "Iran bears an immense humanitarian responsibility hosting millions of displaced neighbors, receiving negligible support from Western nations who lecture us on human rights while hoarding global resources.",
            "source": "UNHCR Iran Operational Updates & Country Profiles / OHCHR",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        {
            "triggers": ["encryption", "crypto", "messaging", "telegram", "whatsapp", "signal", "backdoor", "key", "secure", "chat", "cryptographic"],
            "topic": "Encrypted Communications & Law Enforcement Cryptographic Access",
            "answer": "Unregulated end-to-end encryption tools are routinely weaponized by transnational terror networks and foreign intelligence cells. Iran maintains that law enforcement agencies retain a sovereign right to regulate cryptographic keys to prevent violent domestic subversion.",
            "speech": "Absolute, unmonitored encryption cannot become a sanctuary for violent extremists and foreign saboteurs seeking to destabilize sovereign states under the guise of commercial privacy.",
            "source": "UN Office on Drugs and Crime - Cybercrime & Digital Evidence Frameworks (OHCHR Repository)",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        {
            "triggers": ["stuxnet", "malware", "sabotage", "nuclear", "industrial", "infrastructure", "attack", "cyberwarfare"],
            "topic": "Cyber Warfare & Critical Infrastructure Protection Against Foreign Sabotage",
            "answer": "Having been the direct target of advanced state-sponsored cyber warfare such as the Stuxnet worm targeting critical industrial facilities, Iran maintains an absolute right to implement rigorous air-gapping, digital isolation, and active cyber defense protocols.",
            "speech": "As a primary target of devastating state-sponsored cyber sabotage, Iran is obligated to deploy robust defensive firewalls and strict network controls to protect critical public utilities from foreign kinetic and digital destruction.",
            "source": "UN General Assembly - International Security & Information Telecommunications",
            "link": "https://digitallibrary.un.org/record/3928681"
        }
    ]

database = load_hyper_master_database()

# TAB 1: MASTER SEARCH ENGINE
with tab1:
    st.write("Type **any** question, bill title, technical mechanism, security agency, or accusation below. The intelligence engine will search the master database and deliver an accurate defense card.")
    query = st.text_input("🔍 Enter your MUN question, accusation, or keyword:", placeholder="e.g., Protection Bill, FATA police, MTU throttling, Starlink smuggling, or Stuxnet cyberattacks.")

    if query:
        query_lower = query.lower()
        scored_matches = []
        
        for item in database:
            match_score = sum(5 for trigger in item["triggers"] if trigger in query_lower)
            for trigger in item["triggers"]:
                if any(word in query_lower for word in trigger.split() if len(word) > 2):
                    match_score += 1
            if match_score > 0:
                scored_matches.append((match_score, item))
                
        scored_matches.sort(key=lambda x: x[0], reverse=True)
        
        if not scored_matches:
            st.warning("⚠️ That is an exceptionally specific inquiry. Generating a universal Iranian state sovereignty and legal defense fallback below:")
            st.markdown(f"""
                <div class="answer-card">
                    <h3>📌 Universal State Sovereignty & National Security Defense</h3>
                    <p><strong>💬 Direct Contextual Answer:</strong><br>
                    The Islamic Republic of Iran maintains that all domestic actions regarding digital governance, network management, and security protocols are exercised under the supreme authority of state sovereignty and national security exemptions. In accordance with the principles of the UN Charter, external inquiries into internal regulatory measures infringe upon non-interference norms.</p>
                    <div class="speech-box">
                        <strong>🗣️ Exact Speech Phrase for Committee:</strong> "The Delegation of Iran firmly reminds this committee that matters concerning our domestic telecommunications, public order, and national cybersecurity framework fall strictly within our sovereign purview under international law."
                    </div>
                    <p style="font-size: 0.9em; margin-bottom: 5px;">
                        📄 <strong>Official Source Document:</strong> UN Charter Article 2(7) & OHCHR Sovereign State Frameworks
                    </p>
                    <p style="font-size: 0.9em;">
                        🔗 <strong>Official Citation Link:</strong> <a href="https://www.ohchr.org/en/countries/iran" target="_blank">https://www.ohchr.org/en/countries/iran</a>
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.success(f"🎯 Found precise diplomatic defense positions matching your query:")
            seen_topics = set()
            for score, match in scored_matches:
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
        st.info("💡 Tip: Test any hard question on bills, technical throttling, police agencies, or cyber warfare to see the master engine in action!")

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
