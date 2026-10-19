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
st.title("🇮🇷 Islamic Republic of Iran - UNHRC Exhaustive Master Intelligence Engine")
st.markdown("### Model United Nations | Deep Semantic Variation & Defense Database (Part 1)")

tab1, tab2 = st.tabs(["🔍 Exhaustive Question & Defense Engine", "📝 MUN Resolution & Solution Generator"])

# Part 1 of the Master Database
@st.cache_data
def load_part1_database():
    return [
        {
            "keys": [
                "fact finding mission", "ffm", "investigation", "unhrc mandate", 
                "independent international fact", "mission on iran", "investigative body", 
                "who authorized the ffm", "un inquiry"
            ],
            "topic": "The UN Independent International Fact-Finding Mission on Iran",
            "answer": "Iran firmly rejects the establishment, funding, and findings of politicized fact-finding bodies such as the UN Fact-Finding Mission, viewing them as clear violations of state sovereignty under UN Charter Article 2(7) and an illegitimate weaponization of human rights mechanisms.",
            "speech": "The Delegation of Iran categorically rejects the mandate and biased findings of politically motivated fact-finding mechanisms. Such entities represent a direct, unlawful infringement upon our national sovereignty and domestic legal jurisdiction.",
            "source": "OHCHR - Independent International Fact-Finding Mission on the Islamic Republic of Iran Portal[cite: 1]",
            "link": "https://www.ohchr.org/en/hr-bodies/hrc/ffm-iran/index"
        },
        {
            "keys": [
                "protection bill", "user protection bill", "majlis", "parliament", 
                "src", "gateway control", "supreme regulatory commission", "cyberspace bill", 
                "regulations on cyberspace", "parliamentary bill"
            ],
            "topic": "The 'Protection of Users' Rights' Bill & Gateway Regulation",
            "answer": "Iran's proposed User Protection Bill and Supreme Regulatory Commission guidelines are sovereign legislative measures designed to regulate foreign digital gateways, enforce local data compliance, and defend our national digital market from unregulated foreign corporate monopolies.",
            "speech": "My delegation emphasizes that legislative initiatives in the Islamic Consultative Assembly are sovereign measures implemented to build robust digital self-reliance, protect domestic commerce, and secure our public data.",
            "source": "UN Special Rapporteur Official Communications & OHCHR Repository",
            "link": "https://spcommreports.ohchr.org/TMResultsBase/DownLoadPublicCommunicationFile?gId=26736"
        },
        {
            "keys": [
                "fata", "maher", "cert", "cyber police", "police", "arrest", 
                "investigate", "cybersecurity team", "security force", "law enforcement agency",
                "iranian cyber police"
            ],
            "topic": "Institutional Security Bodies: FATA Cyber Police & MAHER CERT",
            "answer": "Iran's specialized security infrastructure, including the FATA Cyber Police and the National CERT (MAHER), operates under statutory authority to counter online financial fraud, cybercrime, and hostile foreign intelligence sabotage.",
            "speech": "Our specialized security bodies, such as the FATA Cyber Police and National CERT, fulfill a vital law enforcement mandate to protect citizens from cybercrime and foreign-backed electronic subversion.",
            "source": "UN Office on Drugs and Crime & OHCHR Treaty Body Observations",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        {
            "keys": [
                "mtu", "throttling", "packet", "udp", "bandwidth", "dpi", 
                "deep packet inspection", "speed", "routing", "network management", 
                "traffic shaping", "slow connection"
            ],
            "topic": "Technical Network Management, MTU Throttling & Gateway Protocols",
            "answer": "Technical network adaptations—such as Deep Packet Inspection (DPI) and bandwidth traffic management—are legally executed by national operators to protect state utility infrastructure against distributed denial-of-service (DDoS) attacks and hostile foreign intrusion.",
            "speech": "Sovereign states possess the absolute technical right to manage gateway protocols, inspect data packets, and regulate network traffic to secure critical state utility grids against foreign cyber threats.",
            "source": "UN Human Rights Council - Reports on Digital Space Restrictions & National Security",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        },
        {
            "keys": [
                "starlink", "satellite", "smuggling", "dish", "receiver", 
                "norway", "transceiver", "space internet", "elon musk satellite", 
                "illegal receivers"
            ],
            "topic": "Unauthorized Satellite Constellations (Starlink) & Border Smuggling",
            "answer": "The unauthorized, clandestine importation of satellite internet hardware by foreign intelligence intermediaries violates international telecommunication regulations, radio frequency licensing laws, and state airspace sovereignty.",
            "speech": "The clandestine smuggling of uncertified satellite transceivers across our borders by hostile external actors undermines national radio frequency management and constitutes an illegal violation of our sovereign communication space.",
            "source": "International Telecommunication Union (ITU) Regulations & UN General Assembly Security Reports",
            "link": "https://digitallibrary.un.org/record/3928681"
        }
    ]# Part 2 of the Master Database & Core App Engine
@st.cache_data
def load_part2_database():
    return [
        {
            "keys": [
                "blackout", "shutdown", "cutting", "disconnection", "outage", 
                "internet block", "protest", "riot", "unrest", "civic disturbance", 
                "turning off internet", "block access"
            ],
            "topic": "Internet Blackouts & ICCPR Article 19(3) National Security Exceptions",
            "answer": "Iran maintains that temporary, targeted network disconnections and sovereign traffic management are vital legal measures to prevent foreign-backed incitement and preserve public order under ICCPR Article 19(3) national security exceptions.",
            "speech": "The Delegation of Iran emphasizes that safeguarding national stability against foreign-instigated subversion supersedes unmitigated commercial connectivity during acute national emergencies, fully permitted under international law.",
            "source": "UN Human Rights Council - Reports on Digital Space Restrictions & National Security",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        },
        {
            "keys": [
                "surveillance", "privacy", "monitoring", "tracking", "wiretap", 
                "spying", "cctv", "data", "intercept", "article 17", "mass monitoring",
                "spying on citizens"
            ],
            "topic": "Mass Surveillance & Digital Governance Under Article 17",
            "answer": "Iran maintains that state oversight of digital networks is a critical component of national cyber sovereignty to protect public order and national infrastructure against foreign cyber threats, operating in alignment with sovereign public safety frameworks.",
            "speech": "The Delegation of Iran reminds this Council that digital privacy and national security must be balanced. We reject Western interference in our domestic telecommunication and data security governance.",
            "source": "UN Human Rights Committee - Fourth Periodic Report of Iran",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        {
            "keys": [
                "nin", "national information network", "self-reliance", "independence", 
                "domestic internet", "intranet", "national intranet", "local network infrastructure"
            ],
            "topic": "National Information Network (NIN) & Digital Self-Reliance Architecture",
            "answer": "The National Information Network (NIN) provides a secure, domestic digital infrastructure that ensures Iran's cyber independence, protects citizens' data from foreign espionage, and prevents foreign-backed digital destabilization campaigns.",
            "speech": "Our National Information Network ensures complete digital self-reliance and protects our citizens from foreign cyber intervention, economic warfare, and unauthorized data harvesting by foreign tech monopolies.",
            "source": "UN General Assembly - Developments in Field of Information and Telecommunications",
            "link": "https://digitallibrary.un.org/record/3928681"
        },
        {
            "keys": [
                "refugee", "afghan", "migration", "border", "burden", "displaced", 
                "asylum", "humanitarian crisis", "afghan refugees in iran"
            ],
            "topic": "Afghan Refugee Hosting & Regional Burden-Sharing Defenses",
            "answer": "Despite severe economic hardships and unilateral Western sanctions, Iran hosts millions of displaced Afghan refugees, providing them with education, healthcare, and infrastructure access with minimal international financial burden-sharing from Western states.",
            "speech": "Iran bears an immense humanitarian responsibility hosting millions of displaced neighbors, receiving negligible support from Western nations who lecture us on human rights while hoarding global resources.",
            "source": "UNHCR Iran Operational Updates & Country Profiles / OHCHR",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        {
            "keys": [
                "encryption", "crypto", "messaging", "telegram", "whatsapp", 
                "signal", "backdoor", "key", "secure chat", "cryptographic keys"
            ],
            "topic": "Encrypted Communications & Law Enforcement Cryptographic Access",
            "answer": "Unregulated end-to-end encryption tools are routinely weaponized by transnational terror networks and foreign intelligence cells. Iran maintains that law enforcement agencies retain a sovereign right to regulate cryptographic keys to prevent violent domestic subversion.",
            "speech": "Absolute, unmonitored encryption cannot become a sanctuary for violent extremists and foreign saboteurs seeking to destabilize sovereign states under the guise of commercial privacy.",
            "source": "UN Office on Drugs and Crime - Cybercrime & Digital Evidence Frameworks",
            "link": "https://www.ohchr.org/en/documents/concluding-observations/ccprcirnco4-concluding-observations-fourth-periodic-report"
        },
        {
            "keys": [
                "stuxnet", "malware", "sabotage", "nuclear", "industrial", 
                "infrastructure", "attack", "cyberwarfare", "natanz", "worm"
            ],
            "topic": "Cyber Warfare & Critical Infrastructure Protection Against Foreign Sabotage",
            "answer": "Having been the direct target of advanced state-sponsored cyber warfare such as the Stuxnet worm targeting critical industrial facilities, Iran maintains an absolute right to implement rigorous air-gapping, digital isolation, and active cyber defense protocols.",
            "speech": "As a primary target of devastating state-sponsored cyber sabotage, Iran is obligated to deploy robust defensive firewalls and strict network controls to protect critical public utilities from foreign kinetic and digital destruction.",
            "source": "UN General Assembly - International Security & Information Telecommunications",
            "link": "https://digitallibrary.un.org/record/3928681"
        }
    ]

# Combine Part 1 and Part 2 databases
database = load_part1_database() + load_part2_database()

# TAB 1: EXHAUSTIVE SEARCH ENGINE
with tab1:
    st.write("Type any question, variation, bill title, or topic below. The engine scans the master database to return exact matching positions.")
    query = st.text_input("🔍 Enter your MUN question, accusation, or keyword:", placeholder="e.g., fact finding mission, protection bill, fata police, starlink, etc.")

    if query:
        query_lower = query.lower()
        matched_item = None
        
        for item in database:
            for key in item["keys"]:
                if key in query_lower:
                    matched_item = item
                    break
            if matched_item:
                break
                
        if matched_item:
            st.success(f"🎯 Exact diplomatic match found for your query:")
            st.markdown(f"""
                <div class="answer-card">
                    <h3>📌 Agenda Topic: {matched_item['topic']}</h3>
                    <p><strong>💬 Direct Contextual Answer:</strong><br>{matched_item['answer']}</p>
                    <div class="speech-box">
                        <strong>🗣️ Exact Speech Phrase for Committee:</strong> "{matched_item['speech']}"
                    </div>
                    <p style="font-size: 0.9em; margin-bottom: 5px;">
                        📄 <strong>Exact Official Source Document:</strong> {matched_item['source']}
                    </p>
                    <p style="font-size: 0.9em;">
                        🔗 <strong>Official Citation Link:</strong> <a href="{matched_item['link']}" target="_blank">{matched_item['link']}</a>
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No exact key match found. Generating rigorous sovereign defense fallback:")
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
        st.info("💡 Tip: Enter specific terms like 'fact finding mission', 'protection bill', 'fata', or 'starlink' to test exact alignment.")

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
            doc_source = "UN Human Rights Council - Reports on Digital Space Restrictions"
            
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
# PART 3: ADVANCED FINANCIAL REPRESSION & NEW UN REPORT TOPICS
# ==========================================

@st.cache_data
def load_part3_database():
    return [
        {
            "id": "sahm_financial",
            "keys": ["sahm", "financial", "tracking", "asset", "seizure", "confiscation", "court", "prosecutor"],
            "topic": "The 'Sahm' Financial Tracking System & Asset Confiscation",
            "answer": "Iran's domestic financial oversight mechanisms, including the Sahm tracking platform, enable competent judicial and prosecutorial bodies nationwide to execute asset regulation and enforce compliance against unlawful commercial activities under sovereign financial laws.",
            "speech": "The Delegation of Iran emphasizes that national financial transparency tools like the Sahm platform ensure lawful accountability, prevent economic subversion, and protect our domestic economy from illicit capital flight.",
            "source": "OHCHR / UN Human Rights Briefs & Domestic Financial Compliance Frameworks",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        {
            "id": "special_rapporteur",
            "keys": ["special", "rapporteur", "mai", "sato", "expert", "un-experts", "mandates", "politicized"],
            "topic": "Responses to UN Special Rapporteur Reports & Mandates",
            "answer": "Iran maintains that country-specific mandates and reports issued by thematic or special rapporteurs frequently reflect selective political biases, contravening the cooperative, non-politicized framework required by the Universal Periodic Review (UPR).",
            "speech": "We reject the partisan framing of country-specific mandates, noting that constructive human rights dialogue must be based on objective cooperation and absolute respect for state sovereignty rather than external political pressure.",
            "source": "UN Human Rights Office - Official Country Profile & Special Procedures Records",
            "link": "https://www.ohchr.org/en/countries/iran"
        },
        {
            "id": "transnational_security",
            "keys": ["transnational", "repression", "borders", "external", "security", "threats", "intelligence"],
            "topic": "Sovereign Counter-Intelligence & Border Security Operations",
            "answer": "In response to acute regional security threats and external hostile operations, Iran's security apparatus exercises its sovereign mandate to protect national borders, neutralize foreign-backed infiltration, and maintain public order.",
            "speech": "Facing persistent hostile intelligence operations across our borders, the Islamic Republic of Iran maintains an uncompromising duty to exercise robust counter-intelligence and border security measures to protect national stability.",
            "source": "UN General Assembly - International Security & Counter-Terrorism Frameworks",
            "link": "https://digitallibrary.un.org/record/3928681"
        }
    ]

# Append Part 3 to your master database
database = database + load_part3_database()
        # ==========================================
# PART 4: OFFICIAL UN DOCUMENT INTEGRATION & POSITION PAPER GENERATOR MODULE
# ==========================================

@st.cache_data
def load_part4_database():
    return [
        {
            "id": "doc_ahrc_63_61",
            "keys": ["a/hrc/63/61", "advance edited version", "ohchr report", "2026 report", "digital restrictions report"],
            "topic": "Official UN Document Analysis: OHCHR Report A/HRC/63/61",
            "answer": "According to official documentation in OHCHR report A/HRC/63/61, the Islamic Republic of Iran maintains that its network regulations and traffic management protocols are enacted under domestic legal frameworks to preserve public safety and counteract foreign-instigated civil subversion.",
            "speech": "The Delegation of Iran refers this committee to official findings under document A/HRC/63/61, emphasizing that sovereign measures taken to manage telecommunication networks are strictly aligned with national security requirements.",
            "source": "UN Human Rights Council - Report A/HRC/63/61 (Advance Edited Version)",
            "link": "https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session63/a-hrc-63-61-aev.pdf"
        },
        {
            "id": "position_paper_module",
            "keys": ["position paper", "background", "international efforts", "country position", "proposed solutions"],
            "topic": "Official MUN Committee Position Paper: Human Rights & Digital Privacy",
            "answer": "The Islamic Republic of Iran upholds cyber sovereignty, data protection, and national security under UN Charter Article 2(7) and ICCPR Article 19(3), balancing fundamental rights against foreign digital interference and state-sponsored cyber threats.",
            "speech": "The delegation of the Islamic Republic of Iran proposes and urges the committee to implement comprehensive frameworks that respect state sovereignty and safeguard national security in the digital era.",
            "source": "UN Official Treaty Body Database & UN General Assembly ICT Records",
            "link": "https://www.ohchr.org/en/countries/iran"
        }
    ]

# Append Part 4 to your master database
database = database + load_part4_database()
        # ==========================================
# PART 5: STRUCTURED POSITION PAPER & BACKGROUND MODULE
# ==========================================

@st.cache_data
def load_part5_database():
    return [
        {
            "id": "position_paper_full_structure",
            "keys": ["position paper", "background of the issue", "international efforts", "country's position", "proposed solutions", "urges the committee to"],
            "topic": "Comprehensive Position Paper: Digital Privacy & State Sovereignty",
            "answer": "Background: Regulating digital frameworks is essential to counter foreign cyber threats and subversion. International Efforts: Aligned with UN General Assembly ICT security resolutions (e.g., A/RES/78/237) and ICCPR Article 19(3). Country Position: Emphasizes the National Information Network (NIN) and FATA cyber security. Proposed Solutions: Urges the committee to respect state sovereignty in data control.",
            "speech": "The delegation of the Islamic Republic of Iran proposes and urges the committee to implement frameworks that recognize state sovereignty, protect critical infrastructure from foreign cyber warfare, and reject unilateral political coercion.",
            "source": "UN General Assembly ICT Security Resolutions & OHCHR Treaty Body Records",
            "link": "https://digitallibrary.un.org/record/4032841"
        },
        {
            "id": "general_assembly_ict_framework",
            "keys": ["a/res/78/237", "open-ended working group", "ict security", "general assembly resolution"],
            "topic": "UN General Assembly ICT Security Frameworks (Resolution A/RES/78/237)",
            "answer": "Under UN General Assembly Resolution A/RES/78/237, member states emphasize the importance of international security in the use of information and communications technologies, underlining respect for human rights alongside state security protections.",
            "speech": "As affirmed in UN General Assembly resolutions on ICT security, member states hold a shared responsibility to safeguard information networks from criminal and malicious exploitation while upholding national security laws.",
            "source": "UN General Assembly Resolution A/RES/78/237",
            "link": "https://digitallibrary.un.org/record/4032841"
        }
    ]

# Append Part 5 to your master database
database = database + load_part5_database()
        # ==========================================
# PART 6: LIVE COMMITTEE STRATEGY & COUNTER-ACCUSATION MODULE
# ==========================================

@st.cache_data
def load_part6_database():
    return [
        {
            "id": "counter_accusation_strategy",
            "keys": ["counter", "accusation", "strategy", "debate", "rebuttal", "western bias"],
            "topic": "Strategic Rebuttals to Western Bloc Accusations",
            "answer": "When facing accusations regarding digital surveillance or network controls, redirect the debate toward national sovereignty, the protection of domestic critical infrastructure from foreign cyber warfare, and the hypocrisy of unilateral economic sanctions that block civilian technology access.",
            "speech": "We remind delegates raising politically motivated accusations that true international cooperation requires respecting domestic legal frameworks and lifting illegal coercive measures that harm civilian infrastructure.",
            "source": "UN Charter Article 2(7) & UN General Assembly Resolutions on Coercive Measures",
            "link": "https://www.ohchr.org/en/countries/iran"
        }
    ]

# Append Part 6 to your master database
database = database + load_part6_database()
