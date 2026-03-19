# Disease information: treatment, severity, and multilingual names
# Format: class_name -> {treatment, severity, name_hi, name_mr}

DISEASE_INFO = {
    # ── Tomato ─────────────────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "name_hi": "टमाटर बैक्टीरियल स्पॉट",
        "name_mr": "टोमॅटो बॅक्टेरियल स्पॉट",
        "severity": "medium",
        "treatment_en": (
            "1. Remove and destroy infected leaves immediately.\n"
            "2. Apply copper-based bactericide (e.g., Blitox 50 WP) every 7-10 days.\n"
            "3. Avoid overhead watering — use drip irrigation.\n"
            "4. Rotate crops — do not plant tomato in same field for 2 years.\n"
            "5. Use disease-free certified seeds next season."
        ),
        "treatment_hi": (
            "1. संक्रमित पत्तियों को तुरंत हटा दें और नष्ट करें।\n"
            "2. कॉपर-आधारित बैक्टीरीसाइड (जैसे ब्लिटॉक्स 50 WP) हर 7-10 दिनों में लगाएं।\n"
            "3. ऊपर से पानी देने से बचें — ड्रिप सिंचाई का उपयोग करें।\n"
            "4. फसल चक्र अपनाएं — 2 साल तक उसी खेत में टमाटर न लगाएं।"
        ),
        "treatment_mr": (
            "1. संक्रमित पाने ताबडतोब काढून नष्ट करा.\n"
            "2. तांबे-आधारित बॅक्टेरीसाइड (ब्लिटॉक्स 50 WP) दर 7-10 दिवसांनी फवारा.\n"
            "3. वरून पाणी देणे टाळा — ठिबक सिंचन वापरा.\n"
            "4. पीक फेरपालट करा — 2 वर्षे त्याच शेतात टोमॅटो लावू नका."
        )
    },
    "Tomato___Early_blight": {
        "name": "Tomato Early Blight",
        "name_hi": "टमाटर अर्ली ब्लाइट",
        "name_mr": "टोमॅटो अर्ली ब्लाइट",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Mancozeb (Dithane M-45) @ 2.5g/L water every 10 days.\n"
            "2. Remove lower infected leaves — improve airflow.\n"
            "3. Mulch around plants to prevent soil splash.\n"
            "4. Maintain proper plant spacing (45-60cm).\n"
            "5. Avoid working in field when plants are wet."
        ),
        "treatment_hi": (
            "1. मैंकोजेब (Dithane M-45) @ 2.5g/L पानी में हर 10 दिन में छिड़कें।\n"
            "2. निचली संक्रमित पत्तियां हटाएं — हवा का प्रवाह बढ़ाएं।\n"
            "3. मिट्टी के छींटे रोकने के लिए पौधों के चारों ओर मल्च लगाएं।"
        ),
        "treatment_mr": (
            "1. मॅन्कोझेब (Dithane M-45) @ 2.5g/L पाण्यात दर 10 दिवसांनी फवारा.\n"
            "2. खालची संक्रमित पाने काढा — हवा खेळती ठेवा.\n"
            "3. माती उडू नये म्हणून झाडांभोवती आच्छादन घाला."
        )
    },
    "Tomato___Late_blight": {
        "name": "Tomato Late Blight",
        "name_hi": "टमाटर लेट ब्लाइट",
        "name_mr": "टोमॅटो लेट ब्लाइट",
        "severity": "high",
        "treatment_en": (
            "⚠️ HIGH PRIORITY — spreads very fast!\n"
            "1. Apply Ridomil Gold MZ or Cymoxanil + Mancozeb immediately.\n"
            "2. Remove ALL infected plant material and burn it.\n"
            "3. Do NOT compost infected plants.\n"
            "4. Spray every 5-7 days during wet/cool weather.\n"
            "5. Consider destroying heavily infected crop to protect neighbors."
        ),
        "treatment_hi": (
            "⚠️ उच्च प्राथमिकता — बहुत तेजी से फैलता है!\n"
            "1. Ridomil Gold MZ या Cymoxanil + Mancozeb तुरंत लगाएं।\n"
            "2. सभी संक्रमित पौधों को हटाएं और जलाएं।\n"
            "3. संक्रमित पौधों को कंपोस्ट न करें।"
        ),
        "treatment_mr": (
            "⚠️ उच्च प्राधान्य — खूप वेगाने पसरतो!\n"
            "1. Ridomil Gold MZ किंवा Cymoxanil + Mancozeb ताबडतोब फवारा.\n"
            "2. सर्व संक्रमित झाडे काढून जाळा.\n"
            "3. संक्रमित झाडे कंपोस्ट करू नका."
        )
    },
    "Tomato___Leaf_Mold": {
        "name": "Tomato Leaf Mold",
        "name_hi": "टमाटर लीफ मोल्ड",
        "name_mr": "टोमॅटो पानावरील बुरशी",
        "severity": "medium",
        "treatment_en": (
            "1. Improve greenhouse/tunnel ventilation to reduce humidity.\n"
            "2. Apply Chlorothalonil (Kavach) or Copper oxychloride spray.\n"
            "3. Avoid wetting leaves when watering.\n"
            "4. Keep humidity below 85% if growing in protected conditions."
        ),
        "treatment_hi": (
            "1. आर्द्रता कम करने के लिए वेंटिलेशन बेहतर करें।\n"
            "2. क्लोरोथालोनिल (कवच) या कॉपर ऑक्सीक्लोराइड स्प्रे करें।\n"
            "3. पानी देते समय पत्तियों को गीला न करें।"
        ),
        "treatment_mr": (
            "1. आर्द्रता कमी करण्यासाठी वायुवीजन सुधारा.\n"
            "2. क्लोरोथालोनिल (कवच) किंवा कॉपर ऑक्सिक्लोराइड फवारा.\n"
            "3. पाणी देताना पाने ओली होणार नाहीत याची काळजी घ्या."
        )
    },
    "Tomato___Septoria_leaf_spot": {
        "name": "Tomato Septoria Leaf Spot",
        "name_hi": "टमाटर सेप्टोरिया लीफ स्पॉट",
        "name_mr": "टोमॅटो सेप्टोरिया पान ठिपके",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Mancozeb or Chlorothalonil every 7-10 days.\n"
            "2. Remove and destroy infected lower leaves.\n"
            "3. Stake plants to improve air circulation.\n"
            "4. Avoid working in wet fields — disease spreads by touch."
        ),
        "treatment_hi": (
            "1. मैंकोजेब या क्लोरोथालोनिल हर 7-10 दिन में लगाएं।\n"
            "2. संक्रमित निचली पत्तियां हटाकर नष्ट करें।\n"
            "3. हवा प्रवाह बढ़ाने के लिए पौधों को सहारा दें।"
        ),
        "treatment_mr": (
            "1. मॅन्कोझेब किंवा क्लोरोथालोनिल दर 7-10 दिवसांनी फवारा.\n"
            "2. संक्रमित खालची पाने काढून नष्ट करा.\n"
            "3. हवा खेळती राहण्यासाठी झाडांना आधार द्या."
        )
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "name": "Spider Mites on Tomato",
        "name_hi": "टमाटर स्पाइडर माइट्स",
        "name_mr": "टोमॅटो कोळी माइट",
        "severity": "medium",
        "treatment_en": (
            "1. Spray water forcefully on leaf undersides to dislodge mites.\n"
            "2. Apply Abamectin (Vertimec) or Spiromesifen (Oberon) miticide.\n"
            "3. Neem oil spray (5ml/L) — good organic option.\n"
            "4. Introduce predatory mites (Phytoseiulus persimilis) if available.\n"
            "5. Mites thrive in dry/hot weather — maintain soil moisture."
        ),
        "treatment_hi": (
            "1. माइट्स हटाने के लिए पत्ती के नीचे जोर से पानी छिड़कें।\n"
            "2. Abamectin (Vertimec) या Spiromesifen (Oberon) माइटीसाइड लगाएं।\n"
            "3. नीम तेल (5ml/L) — अच्छा जैविक विकल्प।"
        ),
        "treatment_mr": (
            "1. माइट्स काढण्यासाठी पानाच्या खालून जोरात पाणी फवारा.\n"
            "2. Abamectin (Vertimec) किंवा Spiromesifen (Oberon) माइटीसाइड वापरा.\n"
            "3. कडुनिंब तेल (5ml/L) — चांगला सेंद्रिय पर्याय."
        )
    },
    "Tomato___Target_Spot": {
        "name": "Tomato Target Spot",
        "name_hi": "टमाटर टार्गेट स्पॉट",
        "name_mr": "टोमॅटो टार्गेट स्पॉट",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Azoxystrobin (Amistar) or Tebuconazole fungicide.\n"
            "2. Remove infected leaves promptly.\n"
            "3. Improve air circulation through pruning.\n"
            "4. Avoid excessive nitrogen fertilization."
        ),
        "treatment_hi": (
            "1. Azoxystrobin (Amistar) या Tebuconazole फफूंदनाशक लगाएं।\n"
            "2. संक्रमित पत्तियां जल्दी हटाएं।\n"
            "3. छंटाई से हवा प्रवाह बेहतर करें।"
        ),
        "treatment_mr": (
            "1. Azoxystrobin (Amistar) किंवा Tebuconazole बुरशीनाशक फवारा.\n"
            "2. संक्रमित पाने लवकर काढा.\n"
            "3. छाटणीद्वारे हवा खेळती ठेवा."
        )
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "name": "Tomato Yellow Leaf Curl Virus",
        "name_hi": "टमाटर येलो लीफ कर्ल वायरस",
        "name_mr": "टोमॅटो पिवळी पानगुंडाळी विषाणू",
        "severity": "high",
        "treatment_en": (
            "⚠️ VIRAL DISEASE — No direct cure!\n"
            "1. Remove and destroy infected plants immediately.\n"
            "2. Control whitefly (vector) using Imidacloprid (Confidor) spray.\n"
            "3. Use yellow sticky traps to monitor/catch whiteflies.\n"
            "4. Install 50-mesh insect-proof netting in nursery.\n"
            "5. Plant resistant varieties: Arka Rakshak, H-24 (for your region)."
        ),
        "treatment_hi": (
            "⚠️ वायरल रोग — सीधा इलाज नहीं!\n"
            "1. संक्रमित पौधे तुरंत हटाएं और नष्ट करें।\n"
            "2. सफेद मक्खी नियंत्रण: Imidacloprid (Confidor) छिड़काव।\n"
            "3. पीले चिपचिपे ट्रैप का उपयोग करें।\n"
            "4. प्रतिरोधी किस्में लगाएं: अर्का रक्षक, H-24।"
        ),
        "treatment_mr": (
            "⚠️ विषाणूजन्य रोग — थेट उपाय नाही!\n"
            "1. संक्रमित झाडे ताबडतोब काढून नष्ट करा.\n"
            "2. पांढरी माशी नियंत्रण: Imidacloprid (Confidor) फवारा.\n"
            "3. पिवळे चिकट सापळे वापरा.\n"
            "4. प्रतिरोधक वाण लावा: अर्का रक्षक, H-24."
        )
    },
    "Tomato___Tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "name_hi": "टमाटर मोजेक वायरस",
        "name_mr": "टोमॅटो मोज़ेक विषाणू",
        "severity": "high",
        "treatment_en": (
            "⚠️ VIRAL DISEASE — No cure once infected!\n"
            "1. Remove and destroy infected plants.\n"
            "2. Disinfect tools with 10% bleach solution between plants.\n"
            "3. Control aphids (main vector) with Imidacloprid spray.\n"
            "4. Do NOT smoke near tomato plants (tobacco mosaic virus).\n"
            "5. Use certified virus-free seeds."
        ),
        "treatment_hi": (
            "⚠️ वायरल रोग — एक बार संक्रमित होने पर कोई इलाज नहीं!\n"
            "1. संक्रमित पौधे हटाएं और नष्ट करें।\n"
            "2. पौधों के बीच 10% ब्लीच से उपकरण साफ करें।\n"
            "3. माहू नियंत्रण के लिए Imidacloprid छिड़कें।"
        ),
        "treatment_mr": (
            "⚠️ विषाणूजन्य रोग — एकदा संसर्ग झाल्यावर उपाय नाही!\n"
            "1. संक्रमित झाडे काढून नष्ट करा.\n"
            "2. झाडांमध्ये 10% ब्लीचने साधने निर्जंतुक करा.\n"
            "3. माव्या नियंत्रणासाठी Imidacloprid फवारा."
        )
    },
    "Tomato___healthy": {
        "name": "Tomato — Healthy",
        "name_hi": "टमाटर — स्वस्थ",
        "name_mr": "टोमॅटो — निरोगी",
        "severity": "none",
        "treatment_en": "✅ Plant looks healthy! Keep doing: regular watering, balanced fertilization, and weekly scouting for early signs of disease.",
        "treatment_hi": "✅ पौधा स्वस्थ दिखता है! नियमित देखभाल जारी रखें।",
        "treatment_mr": "✅ झाड निरोगी दिसते! नियमित काळजी सुरू ठेवा."
    },

    # ── Potato ─────────────────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "name": "Potato Early Blight",
        "name_hi": "आलू अर्ली ब्लाइट",
        "name_mr": "बटाटा अर्ली ब्लाइट",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Mancozeb (2.5g/L) or Chlorothalonil every 7-10 days.\n"
            "2. Ensure proper plant nutrition — nitrogen deficiency worsens blight.\n"
            "3. Remove infected leaves to slow spread.\n"
            "4. Avoid late-evening watering.\n"
            "5. Hill up soil around plants to protect developing tubers."
        ),
        "treatment_hi": (
            "1. मैंकोजेब (2.5g/L) या क्लोरोथालोनिल हर 7-10 दिन में लगाएं।\n"
            "2. उचित पोषण सुनिश्चित करें — नाइट्रोजन की कमी से रोग बढ़ता है।\n"
            "3. संक्रमित पत्तियां हटाएं।"
        ),
        "treatment_mr": (
            "1. मॅन्कोझेब (2.5g/L) किंवा क्लोरोथालोनिल दर 7-10 दिवसांनी फवारा.\n"
            "2. योग्य पोषण द्या — नायट्रोजनच्या कमतरतेने रोग वाढतो.\n"
            "3. संक्रमित पाने काढा."
        )
    },
    "Potato___Late_blight": {
        "name": "Potato Late Blight",
        "name_hi": "आलू लेट ब्लाइट",
        "name_mr": "बटाटा उशीरा करपा",
        "severity": "high",
        "treatment_en": (
            "⚠️ EMERGENCY — This caused the Irish Famine. Acts fast!\n"
            "1. Apply Metalaxyl + Mancozeb (Ridomil Gold MZ) IMMEDIATELY.\n"
            "2. Spray every 5 days in cool/wet weather.\n"
            "3. Remove and destroy ALL infected foliage.\n"
            "4. Destroy tubers showing infection — do not sell/store.\n"
            "5. Harvest early if >30% of crop is infected."
        ),
        "treatment_hi": (
            "⚠️ आपातकाल — यह रोग बहुत तेजी से फैलता है!\n"
            "1. Metalaxyl + Mancozeb (Ridomil Gold MZ) तुरंत लगाएं।\n"
            "2. ठंडे/बरसाती मौसम में हर 5 दिन में छिड़काव करें।\n"
            "3. सभी संक्रमित पत्तियां हटाएं और जलाएं।"
        ),
        "treatment_mr": (
            "⚠️ आपत्कालीन — हा रोग खूप वेगाने पसरतो!\n"
            "1. Metalaxyl + Mancozeb (Ridomil Gold MZ) ताबडतोब फवारा.\n"
            "2. थंड/पावसाळी हवामानात दर 5 दिवसांनी फवारा.\n"
            "3. सर्व संक्रमित पाने काढून जाळा."
        )
    },
    "Potato___healthy": {
        "name": "Potato — Healthy",
        "name_hi": "आलू — स्वस्थ",
        "name_mr": "बटाटा — निरोगी",
        "severity": "none",
        "treatment_en": "✅ Potato plant looks healthy! Maintain regular hilling, watering, and weekly scouting.",
        "treatment_hi": "✅ आलू का पौधा स्वस्थ है! नियमित देखभाल जारी रखें।",
        "treatment_mr": "✅ बटाट्याचे झाड निरोगी आहे! नियमित काळजी सुरू ठेवा."
    },

    # ── Pepper ─────────────────────────────────────────────────────────────────
    "Pepper,_bell___Bacterial_spot": {
        "name": "Pepper Bacterial Spot",
        "name_hi": "मिर्च बैक्टीरियल स्पॉट",
        "name_mr": "मिरची बॅक्टेरियल स्पॉट",
        "severity": "medium",
        "treatment_en": (
            "1. Apply copper hydroxide (Kocide) spray every 7 days.\n"
            "2. Avoid overhead irrigation.\n"
            "3. Remove infected plant parts.\n"
            "4. Do not work in wet fields.\n"
            "5. Use disease-free transplants."
        ),
        "treatment_hi": (
            "1. कॉपर हाइड्रॉक्साइड (Kocide) हर 7 दिन में लगाएं।\n"
            "2. ऊपर से सिंचाई से बचें।\n"
            "3. संक्रमित भाग हटाएं।"
        ),
        "treatment_mr": (
            "1. कॉपर हायड्रॉक्साइड (Kocide) दर 7 दिवसांनी फवारा.\n"
            "2. वरून सिंचन टाळा.\n"
            "3. संक्रमित भाग काढा."
        )
    },
    "Pepper,_bell___healthy": {
        "name": "Pepper — Healthy",
        "name_hi": "मिर्च — स्वस्थ",
        "name_mr": "मिरची — निरोगी",
        "severity": "none",
        "treatment_en": "✅ Pepper plant looks healthy!",
        "treatment_hi": "✅ मिर्च का पौधा स्वस्थ है!",
        "treatment_mr": "✅ मिरचीचे झाड निरोगी आहे!"
    },

    # ── Apple ──────────────────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "name": "Apple Scab",
        "name_hi": "सेब स्कैब",
        "name_mr": "सफरचंद स्कॅब",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Captan or Mancozeb fungicide from bud break.\n"
            "2. Rake and destroy fallen leaves (primary inoculum source).\n"
            "3. Prune for better airflow.\n"
            "4. Apply lime sulfur during dormant season.\n"
            "5. Use scab-resistant varieties for new planting."
        ),
        "treatment_hi": (
            "1. कली खुलने से Captan या Mancozeb फफूंदनाशक लगाएं।\n"
            "2. गिरी पत्तियों को रेक करके नष्ट करें।\n"
            "3. हवा प्रवाह के लिए छंटाई करें।"
        ),
        "treatment_mr": (
            "1. कळी उघडण्यापासून Captan किंवा Mancozeb बुरशीनाशक फवारा.\n"
            "2. गळलेली पाने गोळा करून नष्ट करा.\n"
            "3. हवा खेळती राहण्यासाठी छाटणी करा."
        )
    },
    "Apple___Black_rot": {
        "name": "Apple Black Rot",
        "name_hi": "सेब ब्लैक रॉट",
        "name_mr": "सफरचंद काळी कूज",
        "severity": "high",
        "treatment_en": (
            "1. Prune and destroy all dead/infected wood.\n"
            "2. Apply Captan or Thiophanate-methyl fungicide.\n"
            "3. Remove mummified fruits from tree and ground.\n"
            "4. Protect wounds from insects (borers).\n"
            "5. Spray at 10-14 day intervals during wet weather."
        ),
        "treatment_hi": (
            "1. सभी मृत/संक्रमित लकड़ी की छंटाई करें।\n"
            "2. Captan या Thiophanate-methyl फफूंदनाशक लगाएं।\n"
            "3. पेड़ और जमीन से सूखे फल हटाएं।"
        ),
        "treatment_mr": (
            "1. सर्व मृत/संक्रमित लाकूड छाटून नष्ट करा.\n"
            "2. Captan किंवा Thiophanate-methyl बुरशीनाशक फवारा.\n"
            "3. झाड आणि जमिनीवरील सुकलेली फळे काढा."
        )
    },
    "Apple___Cedar_apple_rust": {
        "name": "Cedar Apple Rust",
        "name_hi": "सेब सीडर रस्ट",
        "name_mr": "सफरचंद सेडर रस्ट",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Myclobutanil (Rally) or Triadimefon fungicide.\n"
            "2. Remove nearby Eastern red cedar/juniper trees if possible.\n"
            "3. Plant rust-resistant apple varieties.\n"
            "4. Spray at 7-10 day intervals during spring infection period."
        ),
        "treatment_hi": (
            "1. Myclobutanil (Rally) या Triadimefon फफूंदनाशक लगाएं।\n"
            "2. पास के सीडर/जुनिपर पेड़ हटाएं।\n"
            "3. रस्ट-प्रतिरोधी किस्में लगाएं।"
        ),
        "treatment_mr": (
            "1. Myclobutanil (Rally) किंवा Triadimefon बुरशीनाशक फवारा.\n"
            "2. जवळचे सीडर/जुनिपर झाडे काढा.\n"
            "3. रस्ट-प्रतिरोधक वाण लावा."
        )
    },
    "Apple___healthy": {
        "name": "Apple — Healthy",
        "name_hi": "सेब — स्वस्थ",
        "name_mr": "सफरचंद — निरोगी",
        "severity": "none",
        "treatment_en": "✅ Apple tree looks healthy! Continue regular scouting and preventive fungicide schedule.",
        "treatment_hi": "✅ सेब का पेड़ स्वस्थ है!",
        "treatment_mr": "✅ सफरचंदाचे झाड निरोगी आहे!"
    },

    # ── Grape ──────────────────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "name": "Grape Black Rot",
        "name_hi": "अंगूर ब्लैक रॉट",
        "name_mr": "द्राक्ष काळी कूज",
        "severity": "high",
        "treatment_en": (
            "1. Apply Myclobutanil or Mancozeb from early season.\n"
            "2. Remove all mummified berries and infected canes.\n"
            "3. Improve canopy airflow through pruning.\n"
            "4. Spray at 7-10 day intervals — critical at fruit set."
        ),
        "treatment_hi": (
            "1. मौसम की शुरुआत से Myclobutanil या Mancozeb लगाएं।\n"
            "2. सभी सूखे फल और संक्रमित टहनियां हटाएं।\n"
            "3. छंटाई से वायु प्रवाह बढ़ाएं।"
        ),
        "treatment_mr": (
            "1. हंगामाच्या सुरुवातीपासून Myclobutanil किंवा Mancozeb फवारा.\n"
            "2. सर्व सुकलेली फळे आणि संक्रमित फांद्या काढा.\n"
            "3. छाटणीद्वारे हवा खेळती ठेवा."
        )
    },
    "Grape___healthy": {
        "name": "Grape — Healthy",
        "name_hi": "अंगूर — स्वस्थ",
        "name_mr": "द्राक्ष — निरोगी",
        "severity": "none",
        "treatment_en": "✅ Grapevine looks healthy!",
        "treatment_hi": "✅ अंगूर का पौधा स्वस्थ है!",
        "treatment_mr": "✅ द्राक्षाचे झाड निरोगी आहे!"
    },

    # ── Corn (Maize) ───────────────────────────────────────────────────────────
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "name": "Corn Gray Leaf Spot",
        "name_hi": "मक्का ग्रे लीफ स्पॉट",
        "name_mr": "मका राखाडी पान ठिपके",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Azoxystrobin or Propiconazole fungicide.\n"
            "2. Use resistant hybrid varieties.\n"
            "3. Rotate corn with non-host crops for 1-2 years.\n"
            "4. Till infected residue to reduce inoculum."
        ),
        "treatment_hi": (
            "1. Azoxystrobin या Propiconazole फफूंदनाशक लगाएं।\n"
            "2. प्रतिरोधी संकर किस्में उपयोग करें।\n"
            "3. 1-2 साल के लिए फसल चक्र अपनाएं।"
        ),
        "treatment_mr": (
            "1. Azoxystrobin किंवा Propiconazole बुरशीनाशक फवारा.\n"
            "2. प्रतिरोधक संकर वाण वापरा.\n"
            "3. 1-2 वर्षे पीक फेरपालट करा."
        )
    },
    "Corn_(maize)___Common_rust_": {
        "name": "Corn Common Rust",
        "name_hi": "मक्का सामान्य रस्ट",
        "name_mr": "मका सामान्य गंज",
        "severity": "medium",
        "treatment_en": (
            "1. Apply Propiconazole or Mancozeb at first sign.\n"
            "2. Plant resistant varieties — most modern hybrids have tolerance.\n"
            "3. Early planting avoids peak rust season.\n"
            "4. Severe cases: spray twice at 10-day intervals."
        ),
        "treatment_hi": (
            "1. पहले लक्षण पर Propiconazole या Mancozeb लगाएं।\n"
            "2. प्रतिरोधी किस्में लगाएं।\n"
            "3. जल्दी बुवाई से रस्ट मौसम से बचें।"
        ),
        "treatment_mr": (
            "1. पहिल्या लक्षणावर Propiconazole किंवा Mancozeb फवारा.\n"
            "2. प्रतिरोधक वाण लावा.\n"
            "3. लवकर पेरणी करा."
        )
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "name": "Corn Northern Leaf Blight",
        "name_hi": "मक्का नॉर्दर्न लीफ ब्लाइट",
        "name_mr": "मका उत्तरी पान करपा",
        "severity": "high",
        "treatment_en": (
            "1. Apply Propiconazole or Azoxystrobin at tasseling.\n"
            "2. Use resistant hybrids (most critical solution).\n"
            "3. Crop rotation — reduce infected residue.\n"
            "4. Till soil after harvest to bury infected debris."
        ),
        "treatment_hi": (
            "1. फूल आने पर Propiconazole या Azoxystrobin लगाएं।\n"
            "2. प्रतिरोधी संकर का उपयोग करें।\n"
            "3. फसल चक्र अपनाएं।"
        ),
        "treatment_mr": (
            "1. फुलोरा येताना Propiconazole किंवा Azoxystrobin फवारा.\n"
            "2. प्रतिरोधक संकर वापरा.\n"
            "3. पीक फेरपालट करा."
        )
    },
    "Corn_(maize)___healthy": {
        "name": "Corn — Healthy",
        "name_hi": "मक्का — स्वस्थ",
        "name_mr": "मका — निरोगी",
        "severity": "none",
        "treatment_en": "✅ Corn plant looks healthy!",
        "treatment_hi": "✅ मक्के का पौधा स्वस्थ है!",
        "treatment_mr": "✅ मक्याचे झाड निरोगी आहे!"
    },
}

# Fallback for classes not in the database
DEFAULT_INFO = {
    "name": "Unknown Disease",
    "name_hi": "अज्ञात रोग",
    "name_mr": "अज्ञात रोग",
    "severity": "unknown",
    "treatment_en": "Disease identified but detailed treatment not in database yet. Consult your local agricultural extension officer (Krishi Vibhag).",
    "treatment_hi": "रोग की पहचान हुई लेकिन विस्तृत उपचार डेटाबेस में नहीं है। अपने स्थानीय कृषि अधिकारी से संपर्क करें।",
    "treatment_mr": "रोग ओळखला गेला परंतु तपशीलवार उपचार डेटाबेसमध्ये नाही. स्थानिक कृषी अधिकाऱ्याशी संपर्क करा."
}

SEVERITY_COLORS = {
    "none":    "#22c55e",   # green
    "low":     "#84cc16",   # lime
    "medium":  "#f59e0b",   # amber
    "high":    "#ef4444",   # red
    "unknown": "#6b7280",   # gray
}

SEVERITY_LABELS = {
    "none":    {"en": "No Disease", "hi": "कोई रोग नहीं", "mr": "रोग नाही"},
    "low":     {"en": "Low Risk",   "hi": "कम जोखिम",    "mr": "कमी धोका"},
    "medium":  {"en": "Moderate",   "hi": "मध्यम",        "mr": "मध्यम"},
    "high":    {"en": "Urgent",     "hi": "तत्काल",       "mr": "तातडीचे"},
    "unknown": {"en": "Unknown",    "hi": "अज्ञात",        "mr": "अज्ञात"},
}


def get_disease_info(class_name: str) -> dict:
    """Return disease info dict for a given PlantVillage class name."""
    return DISEASE_INFO.get(class_name, {**DEFAULT_INFO, "name": class_name})
