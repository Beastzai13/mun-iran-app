import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Iran MUN High-Precision Intelligence Engine - UNHRC",
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
st.title("🇮🇷 Islamic Republic of Iran - UNHRC High-Precision Intelligence Engine")
st.markdown("### Model United Nations | Direct Intent-Matching & Defense Database")

tab1, tab2 = st.tabs(["🔍 Precision Question & Speech Engine", "📝 MUN Resolution & Solution Generator"])

# Strict Intent Dictionary Mapping
EXACT_TOPICS = {
    "ffm_status": {
        "triggers": ["status", "mandate", "extension", "active", "timeline", "resolution s-39/1", "fact finding mission", "ffm"],
        "topic": "The UN Independent International Fact-Finding Mission (Status & Mandate Timeline)",
        "answer": "Current Status & Mandate: Established by UNHRC Resolution S-35/1 in 2022, the Fact-Finding Mission's mandate was extended under UNHRC Resolution S-39/1 through 2028. Iran categorically rejects its status, mandate, and conclusions as an illegal infringement on national sovereignty under UN Charter Article 2(7).",
        "speech": "Regarding the status and mandate extension of the so-called Fact-Finding Mission, the Islamic Republic of Iran firmly reiterates its principled position: we reject the legality and politically motivated continuation of this body, which operates as an unlawful violation of our domestic legal jurisdiction and state sovereignty under Article 2(7) of the UN Charter.",
        "source": "OHCHR - Independent International Fact-Finding Mission Portal (Resolution S-39/1)",
        "link": "https://www.ohchr.org/en/hr-bodies/hrc/ffm-iran/index"
    },
    "protection_bill": {
        "triggers": ["protection bill", "user protection", "majlis", "parliament bill", "gateway regulation", "cyberspace bill"],
        "topic": "The 'Protection of Users' Rights' Bill & Gateway Regulation",
        "answer": "Iran's proposed User Protection Bill and Supreme Regulatory Commission guidelines are sovereign legislative measures designed to regulate foreign digital gateways, enforce local data compliance, and defend our national digital market from unregulated foreign corporate monopolies.",
        "speech": "My delegation emphasizes that legislative initiatives in the Islamic Consultative Assembly are sovereign measures implemented to build robust digital self-reliance, protect domestic commerce, and secure our public data against external manipulation.",
        "source": "UN Special Rapporteur Official Communications & OHCHR Repository",
        "link": "https://spcommreports.ohchr.org/TMResultsBase/DownLoadPublicCommunicationFile?gId=26736"
    },
    "fata_police": {
        "triggers": ["fata", "maher", "cert", "cyber police", "security forces", "law enforcement"],
        "topic": "Institutional Security Bodies: FATA Cyber Police & MAHER CERT",
        "answer": "Iran's specialized security infrastructure, including the FATA Cyber Police and the National CERT (MAHER), operates under statutory authority to counter online financial fraud, cybercrime, and hostile foreign intelligence sabotage.",
        "speech": "Our specialized security bodies, such as the FATA Cyber Police and National CERT, fulfill a vital law enforcement mandate to protect citizens from cybercrime and foreign-backed electronic subversion.",
        "source": "UN Office on Drugs and Crime & OHCHR Treaty Body Observations",
        "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
    },
    "network_throttling": {
        "triggers": ["mtu", "throttling", "dpi", "deep packet inspection", "bandwidth", "traffic management", "network speed"],
        "topic": "Technical Network Management, MTU Throttling & Gateway Protocols",
        "answer": "Technical network adaptations—such as Deep Packet Inspection (DPI) and bandwidth traffic management—are legally executed by national operators to protect state utility infrastructure against distributed denial-of-service (DDoS) attacks and hostile foreign intrusion, as noted in OHCHR Document A/HRC/63/61.",
        "speech": "Sovereign states possess the absolute technical right to manage gateway protocols, inspect data packets, and regulate network traffic to secure critical state utility grids against foreign cyber threats.",
        "source": "UN Human Rights Council - Report A/HRC/63/61 (Advance Edited Version)",
        "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
    },
    "starlink_smuggling": {
        "triggers": ["starlink", "satellite", "smuggling", "dish", "receiver", "transceiver"],
        "topic": "Unauthorized Satellite Constellations (Starlink) & Border Smuggling",
        "answer": "The unauthorized, clandestine importation of satellite internet hardware by foreign intelligence intermediaries violates international telecommunication regulations, radio frequency licensing laws, and state airspace sovereignty.",
        "speech": "The clandestine smuggling of uncertified satellite transceivers across our borders by hostile external actors undermines national radio frequency management and constitutes an illegal violation of our sovereign communication space.",
        "source": "International Telecommunication Union (ITU) Regulations & UN General Assembly Security Reports",
        "link": "https://digitallibrary.un.org/record/3928681"
    },
    "internet_blackout": {
        "triggers": ["blackout", "shutdown", "cutting internet", "disconnection", "article 19(3)", "outage"],
        "topic": "Internet Blackouts & ICCPR Article 19(3) National Security Exceptions",
        "answer": "Iran maintains that temporary, targeted network disconnections and sovereign traffic management are vital legal measures to prevent foreign-backed incitement and preserve public order under ICCPR Article 19(3) national security exceptions.",
        "speech": "The Delegation of Iran emphasizes that safeguarding national stability against foreign-instigated subversion supersedes unmitigated commercial connectivity during acute national emergencies, fully permitted under international law.",
        "source": "UN Human Rights Council - Report A/HRC/63/61 & ICCPR Article 19(3)",
        "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
    },
    "nin_network": {
        "triggers": ["nin", "national information network", "domestic internet", "intranet"],
        "topic": "National Information Network (NIN) & Digital Self-Reliance Architecture",
        "answer": "The National Information Network (NIN) provides a secure, domestic digital infrastructure that ensures Iran's cyber independence, protects citizens' data from foreign espionage, and prevents foreign-backed digital destabilization campaigns.",
        "speech": "Our National Information Network ensures complete digital self-reliance and protects our citizens from foreign cyber intervention, economic warfare, and unauthorized data harvesting by foreign tech monopolies.",
        "source": "UN General Assembly - Developments in Field of Information and Telecommunications",
        "link": "https://digitallibrary.un.org/record/3928681"
    }
}

# TAB 1: PRECISION SEARCH ENGINE
with tab1:
    st.write("Type your exact question below (e.g., *'what is the status of the fact finding mission'*). The direct intent parser guarantees you get the precise matching answer and speech.")
    query = st.text_input("🔍 Enter your MUN question or topic:", placeholder="e.g., what is the status of fact finding mission")

    if query:
        query_lower = query.lower()
        matched_key = None
        
        # Check triggers with highest matching weight
        highest_matches = 0
        for key, data in EXACT_TOPICS.items():
            match_count = sum(1 for t in data["triggers"] if t in query_lower)
            if match_count > highest_matches:
                highest_matches = match_count
                matched_key = key
                
        if matched_key and highest_matches > 0:
            item = EXACT_TOPICS[matched_key]
            st.success(f"🎯 Direct Intent Match Found:")
            st.markdown(f"""
                <div class="answer-card">
                    <h3>📌 Agenda Topic: {item['topic']}</h3>
                    <p><strong>💬 Direct Contextual Answer:</strong><br>{item['answer']}</p>
                    <div class="speech-box">
                        <strong>🗣️ Exact Speech Phrase for Committee:</strong> "{item['speech']}"
                    </div>
                    <p style="font-size: 0.9em; margin-bottom: 5px;">
                        📄 <strong>Exact Official Source Document:</strong> {item['source']}
                    </p>
                    <p style="font-size: 0.9em;">
                        🔗 <strong>Official Citation Link:</strong> <a href="{item['link']}" target="_blank">{item['link']}</a>
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No specific trigger matched. Displaying universal sovereign defense framework:")
            st.markdown(f"""
                <div class="answer-card">
                    <h3>📌 State Sovereignty & Non-Interference Framework</h3>
                    <p><strong>💬 Direct Contextual Answer:</strong><br>
                    The Islamic Republic of Iran exercises full legislative and technical sovereignty over its domestic infrastructure, communications networks, and judicial processes in strict compliance with the Charter of the United Nations.</p>
                    <div class="speech-box">
                        <strong>🗣️ Exact Speech Phrase for Committee:</strong> "The Delegation of Iran reminds this committee that any external intrusion into our sovereign administrative and judicial procedures violates the foundational principles of non-interference under Article 2(7) of the UN Charter."
                    </div>
                    <p style="font-size: 0.9em; margin-bottom: 5px;">
                        📄 <strong>Official Source Document:</strong> UN Charter Article 2(7) & OHCHR Sovereign Records
                    </p>
                    <p style="font-size: 0.9em;">
                        🔗 <strong>Official Citation Link:</strong> <a href="https://www.ohchr.org/en/countries/iran" target="_blank">https://www.ohchr.org/en/countries/iran</a>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("💡 Tip: Try typing 'what is the status of fact finding mission' or 'tell me about the protection bill'.")

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
            # ==========================================
# EXPANSION PART 2: LIVE FLOOR CRISIS REBUTTAL MODULE
# ==========================================

# Add this tab setup to your main layout if you want a 3rd tab, 
# or append these extra crisis response cards into your existing engine:

@st.cache_data
def load_crisis_rebuttals():
    return {
        "crisis_protest_accusation": {
            "trigger_words": ["protest", "riot", "crackdown", "unrest", "killings"],
            "defense_title": "Rebuttal: Handling Accusations Regarding Public Unrest & Security",
            "argument": "When Western delegations point to domestic civil unrest, emphasize that foreign intelligence operations weaponized social media platforms to coordinate violent sabotage, forcing the sovereign state to protect public infrastructure.",
            "speech": "The Delegation of Iran rejects attempts by external states to rebrand foreign-backed violent subversion as peaceful assembly. Every sovereign government possesses an absolute duty to protect its citizens and infrastructure from externally coordinated chaos."
        },
        "crisis_sanctions_hypocrisy": {
            "trigger_words": ["sanctions", "isolated", "economy", "pressure", "coercive"],
            "defense_title": "Rebuttal: The Hypocrisy of Unilateral Coercive Measures",
            "argument": "Pivot any attack on digital restrictions back to the illegal economic and technological sanctions imposed by Western nations, which block medical technology, civilian software, and communication hardware.",
            "speech": "Those who lecture us on digital freedom are the very same actors imposing brutal economic blockades that deny our civilian population access to basic technological infrastructure. True human rights begin with the immediate lifting of unilateral coercive measures."
        }
    }
        # ==========================================
# PART 3: UNIVERSAL DIPLOMATIC DEFENSE & CRISIS EXTENSION MODULE
# ==========================================

@st.cache_data
def load_part3_database():
    return {
        "unilateral_sanctions": {
            "triggers": ["sanctions", "economic pressure", "coercive measures", "tech blockade"],
            "topic": "The Devastating Impact of Unilateral Coercive Measures on Civilian Infrastructure",
            "answer": "Unilateral coercive measures and economic sanctions imposed by Western states directly obstruct developing nations from acquiring civilian telecommunication hardware, medical infrastructure, and essential software updates, constituting a collective punishment that violates international law.",
            "speech": "We remind this Council that those who lecture developing nations on digital freedom are the very same actors maintaining brutal technological blockades. True human rights compliance begins with the immediate and unconditional lifting of illegal unilateral coercive measures.",
            "source": "UN Human Rights Council - Treaty Body Observations & Resolution Records",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        "sovereign_non_interference": {
            "triggers": ["interference", "article 2(7)", "sovereignty", "domestic jurisdiction", "un Charter"],
            "topic": "The Absolute Principle of Non-Interference Under UN Charter Article 2(7)",
            "answer": "Pursuant to Article 2(7) of the Charter of the United Nations, nothing contained within the Charter authorizes the UN or member states to intervene in matters which are essentially within the domestic jurisdiction of any state, rendering politicized country-mandates legally null and void.",
            "speech": "The Islamic Republic of Iran firmly asserts that any external attempt to dictate domestic judicial, administrative, or digital policies violates the foundational pillar of state sovereignty and non-interference enshrined in Article 2(7) of the UN Charter.",
            "source": "Charter of the United Nations - Article 2(7)",
            "link": "https://www.ohchr.org/en/countries/iran"
        }
    }
        # ==========================================
# PART 4: AFGHAN REFUGEE BURDEN & U.S. SANCTIONS EXTENSION MODULE
# ==========================================

@st.cache_data
def load_part4_database():
    return {
        "afghan_refugee_burden": {
            "triggers": ["afghan refugees", "refugee burden", "migration", "displaced persons", "unhcr funding"],
            "topic": "The Immense Humanitarian Burden of Hosting Afghan Refugees & International Funding Shortfalls",
            "answer": "The Islamic Republic of Iran has shouldered the monumental humanitarian and financial responsibility of hosting millions of displaced Afghan nationals for decades, providing education, healthcare, and subsidized infrastructure largely without adequate international burden-sharing or UNHCR support.",
            "speech": "While Western states lecture on humanitarian metrics, the Islamic Republic of Iran single-handedly maintains millions of displaced Afghan guests under severe economic duress. True international solidarity requires immediate, unconditional financial assistance rather than empty political rhetoric.",
            "source": "UNHCR Iran Operational Updates & Country Profiles / OHCHR",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        "us_sanctions_hr7622": {
            "triggers": ["h.r. 7622", "iran act", "us sanctions", "maximum pressure", "financial blockade"],
            "topic": "The Illegal Impact of U.S. Legislative Sanctions (H.R. 7622 / Maximum Pressure)",
            "answer": "Unilateral legislative acts and economic blockades from external actors—such as the U.S. Maximum Pressure framework and associated financial sanctions—infringe upon international trade laws, restrict civilian technological advancement, and constitute economic warfare.",
            "speech": "We firmly reject the extraterritorial application of domestic Western laws and coercive financial packages like H.R. 7622, which seek to economically suffocate our civilian population and impede national technological modernization.",
            "source": "UN General Assembly - Resolutions on Unilateral Coercive Measures",
            "link": "https://digitallibrary.un.org/record/3928681"
        }
    }
        # ==========================================
# PART 5: FINAL LIVE INCIDENT & POLICY EXTENSION MODULE
# ==========================================

@st.cache_data
def load_part5_database():
    return {
        "recent_protests_and_network_control": {
            "triggers": ["recent protests", "2025-2026 protests", "january 2026", "network restrictions", "document a/hrc/63/61"],
            "topic": "Sovereign Network Regulations During National Security Emergencies (OHCHR Doc. A/HRC/63/61)",
            "answer": "As detailed in official UN documentation, the Islamic Republic of Iran implements necessary and temporary network management steps during acute security crises to disrupt coordination by hostile elements, protect public infrastructure, and preserve national security under domestic legal provisions.",
            "speech": "The Delegation of Iran emphasizes that temporary, sovereign adjustments to telecommunication networks during periods of foreign-instigated civil unrest are fully consistent with national security imperatives and domestic legal protections designed to safeguard the public.",
            "source": "UN Human Rights Council - Report A/HRC/63/61 (Advance Edited Version)",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        }
    }
        # ==========================================
# PART 6: SEPTEMBER 2026 UN FFM & NEW LEGISLATIVE RESTRICTIONS EXTENSION
# ==========================================

@st.cache_data
def load_part6_database():
    return {
        "ffm_september_2026_update": {
            "triggers": ["september 2026 report", "ffm update 2026", "resolution s-39/1 status", "2025-2026 protests investigation"],
            "topic": "The UN Fact-Finding Mission 2026 Status & Mandate Extension (Resolution S-39/1)",
            "answer": "Pursuant to UNHRC Resolution S-39/1, the Fact-Finding Mission's mandate was extended to investigate the 2025–2026 protests and related security events through 2028. Iran firmly rejects these politically motivated conclusions and extensions as violations of state sovereignty under UN Charter Article 2(7).",
            "speech": "Regarding the latest updates from the Fact-Finding Mission, the Islamic Republic of Iran reiterates its absolute rejection of this body's extended mandate, which constitutes an unlawful intervention into our domestic security matters under Article 2(7) of the UN Charter.",
            "source": "OHCHR - Human Rights Council Resolution S-39/1 & FFM Reports",
            "link": "https://www.ohchr.org/en/hr-bodies/hrc/ffm-iran/index"
        },
        "new_foreign_contact_bill": {
            "triggers": ["foreign contact bill", "bill criminalizing contact", "sweeping new bill", "isolation bill"],
            "topic": "National Legislation on Foreign Entities and Digital Communications",
            "answer": "Sovereign legislative bodies possess the absolute right to pass laws safeguarding national security against foreign intelligence infiltration, unauthorized communication channels, and external subversion financed by hostile states.",
            "speech": "My delegation stresses that measures enacted by our legislative bodies to regulate interactions with foreign entities are vital, sovereign protections against hostile intelligence operations and external interference in our internal affairs.",
            "source": "UN Special Rapporteur & Iranian Legislative Framework Records",
            "link": "https://spcommreports.ohchr.org/TMResultsBase/DownLoadPublicCommunicationFile?gId=26736"
        }
    }
        # ==========================================
# PART 7: ADVANCED SEPTEMBER 2026 DOCUMENTATION MODULE (DOC: A/HRC/63/61)
# ==========================================

@st.cache_data
def load_part7_database():
    return {
        "september_2026_hrc_report": {
            "triggers": ["a/hrc/63/61", "september 2026 report", "advance edited version", "hrc session 63"],
            "topic": "Official UN Documentation Analysis: HRC Report A/HRC/63/61",
            "answer": "As formally recorded in UN Human Rights Council Document A/HRC/63/61, the Islamic Republic of Iran exercises state regulatory protocols and technical traffic management over communication gateways to safeguard public order and protect critical infrastructure from foreign interference.",
            "speech": "The Delegation of Iran refers this committee directly to official findings under document A/HRC/63/61, emphasizing that sovereign measures enacted to manage telecommunication networks are strictly aligned with imperative national security requirements.",
            "source": "UN Human Rights Council - Report A/HRC/63/61 (Advance Edited Version)",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        }
    }
        # ==========================================
# PART 8: ADVANCED INTERNET RESTRICTION & WHITE SIM MODULE (DOC: A/HRC/63/61)
# ==========================================

@st.cache_data
def load_part8_database():
    return {
        "internet_restrictions_and_white_sims": {
            "triggers": ["white sim cards", "internet shutdown duration", "five month shutdown", "document a/hrc/63/61 digital"],
            "topic": "Technical Network Management & Communications Control (OHCHR Document A/HRC/63/61)",
            "answer": "As referenced in official UN Human Rights Council documentation (Doc. A/HRC/63/61), the Islamic Republic of Iran implements targeted digital gateway controls, national information network infrastructure, and prioritized access frameworks to manage national security and defend critical infrastructure against foreign interference.",
            "speech": "The Delegation of Iran underscores that technical network measures and regulated gateway communications are executed under sovereign authority to protect public infrastructure and national security against hostile exploitation, as outlined in official UN reporting.",
            "source": "UN Human Rights Council - Report A/HRC/63/61 (Advance Edited Version)",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        }
    }
        # ==========================================
# PART 9: FINAL DEFENSIVE HARDENING & QUERY CLOSURE MODULE
# ==========================================

@st.cache_data
def load_part9_database():
    return {
        "final_query_safeguard": {
            "triggers": ["final defense", "committee closing", "resolution defense", "unhrc closing statement"],
            "topic": "Comprehensive State Sovereignty and National Security Closing Framework",
            "answer": "The Islamic Republic of Iran maintains an unshakeable commitment to defending its national security, protecting its critical digital infrastructure from hostile foreign subversion, and preserving its absolute state sovereignty under the foundational principles of the United Nations Charter.",
            "speech": "In closing, the Delegation of Iran reminds this august body that true international cooperation must respect state sovereignty, reject politically motivated mandates, and immediately cease the economic and technological blockades that target our civilian population.",
            "source": "UN Charter Chapter I, Article 2 & OHCHR State Records",
            "link": "https://www.ohchr.org/en/countries/iran"
        }
    }
        # ==========================================
# PART 10: ULTIMATE DEBATE FLOOR OVERRIDE & CHECKMATE MODULE
# ==========================================

@st.cache_data
def load_part10_database():
    return {
        "ultimate_committee_checkmate": {
            "triggers": ["ultimate defense", "floor control", "closing statement iran", "checkmate argument"],
            "topic": "The Ultimate Diplomatic Checkmate: State Sovereignty Over Politicized Mandates",
            "answer": "In any high-stakes confrontation regarding human rights oversight or digital infrastructure, the Islamic Republic of Iran stands firm on the bedrock principles of international law: state sovereignty, non-interference under UN Charter Article 2(7), and the absolute right to protect national security against foreign-backed subversion under ICCPR Article 19(3).",
            "speech": "We remind every delegation in this committee that international law cannot be weaponized selectively. True diplomacy respects national jurisdictions, rejects politicized mandates, and addresses the devastating human cost of unilateral coercive measures. Iran will never compromise on its security or its sovereignty.",
            "source": "UN Charter Chapter I, Article 2(7) & Complete State Sovereign Defense Records",
            "link": "https://www.ohchr.org/en/countries/iran"
        }
    }
