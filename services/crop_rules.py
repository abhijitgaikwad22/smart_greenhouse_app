"""
Crop rules module.
Stores ideal environmental ranges for different crops in Maharashtra.
"""

CROP_RANGES = {
    # Kharif Crops (Monsoon Season - June to October)
    'Tomato': {
        'name': 'Tomato (टोमॅटो)',
        'marathi_name': 'टोमॅटो',
        'region': 'Nashik, Pune, Satara',
        'season': 'Kharif & Rabi',
        'temp': (18, 30),
        'humidity': (60, 80),
        'soil_moisture': (40, 100),
        'light': (50, 90),
        'soil_type': 'Well-drained loamy soil',
        'description': 'Nashik is famous for tomato production. Requires consistent moisture.',
        'local_tips': 'नाशिक मध्ये मोठ्या प्रमाणात उत्पादन. नियमित पाणी द्या.'
    },
    
    'Lettuce': {
        'name': 'Lettuce (लेट्यूस)',
        'marathi_name': 'लेट्यूस',
        'region': 'Pune, Mahabaleshwar',
        'season': 'Rabi & Summer',
        'temp': (10, 24),
        'humidity': (65, 85),
        'soil_moisture': (50, 100),
        'light': (40, 70),
        'soil_type': 'Rich organic soil',
        'description': 'Cool-season crop, grown in Mahabaleshwar hills.',
        'local_tips': 'महाबळेश्वर परिसरात चांगले उत्पादन. जास्त उन्हापासून संरक्षण करा.'
    },
    
    'Capsicum': {
        'name': 'Capsicum (ढोबळी मिरची)',
        'marathi_name': 'ढोबळी मिरची',
        'region': 'Nashik, Pune, Satara',
        'season': 'Kharif & Rabi',
        'temp': (16, 28),
        'humidity': (50, 75),
        'soil_moisture': (45, 100),
        'light': (50, 85),
        'soil_type': 'Well-drained sandy loam',
        'description': 'High-value crop in Maharashtra. Requires good ventilation.',
        'local_tips': 'नाशिक मधील प्रसिद्ध पीक. हवा खेळती राहील याची काळजी घ्या.'
    },
    
    'Brinjal': {
        'name': 'Brinjal (वांगी)',
        'marathi_name': 'वांगी',
        'region': 'Kolhapur, Pune, Ahmednagar',
        'season': 'Throughout year',
        'temp': (20, 32),
        'humidity': (55, 75),
        'soil_moisture': (45, 100),
        'light': (60, 90),
        'soil_type': 'Well-drained fertile soil',
        'description': 'Kolhapuri vangi is famous variety. Heat-tolerant crop.',
        'local_tips': 'कोल्हापुरी वांगी प्रसिद्ध. उन्हाळ्यात पाणी व्यवस्थापन महत्त्वाचे.'
    },
    
    'Okra': {
        'name': 'Okra (भेंडी)',
        'marathi_name': 'भेंडी',
        'region': 'Ahmednagar, Jalna, Parbhani',
        'season': 'Kharif & Summer',
        'temp': (22, 35),
        'humidity': (50, 70),
        'soil_moisture': (40, 100),
        'light': (70, 100),
        'soil_type': 'Well-drained loamy soil',
        'description': 'Drought-tolerant crop, good for Marathwada region.',
        'local_tips': 'मराठवाड्यासाठी योग्य. कमी पाण्यात चालते.'
    },
    
    'Cauliflower': {
        'name': 'Cauliflower (फ्लॉवर)',
        'marathi_name': 'फ्लॉवर',
        'region': 'Pune, Nasik, Satara',
        'season': 'Rabi',
        'temp': (15, 25),
        'humidity': (60, 80),
        'soil_moisture': (50, 100),
        'light': (50, 80),
        'soil_type': 'Rich well-drained soil',
        'description': 'Winter crop, requires cool climate.',
        'local_tips': 'हिवाळी पीक. पुणे जिल्ह्यात मोठ्या प्रमाणात उत्पादन.'
    },
    
    'Cabbage': {
        'name': 'Cabbage (कोबी)',
        'marathi_name': 'कोबी',
        'region': 'Pune, Satara, Kolhapur',
        'season': 'Rabi',
        'temp': (12, 26),
        'humidity': (60, 80),
        'soil_moisture': (50, 100),
        'light': (45, 75),
        'soil_type': 'Fertile well-drained soil',
        'description': 'Cool season crop, good for Western Maharashtra.',
        'local_tips': 'थंड हवामान आवश्यक. सातारा जिल्ह्यात चांगले उत्पादन.'
    },
    
    # Cereals & Grains
    'Sugarcane': {
        'name': 'Sugarcane (ऊस)',
        'marathi_name': 'ऊस',
        'region': 'Kolhapur, Sangli, Solapur, Ahmednagar',
        'season': 'Annual (12-18 months)',
        'temp': (20, 35),
        'humidity': (60, 85),
        'soil_moisture': (60, 100),
        'light': (80, 100),
        'soil_type': 'Deep well-drained loamy soil',
        'description': 'Major cash crop of Western Maharashtra. High water requirement.',
        'local_tips': 'कोल्हापूर, सांगली मधील मुख्य पीक. भरपूर पाणी लागते.'
    },
    
    'Soybean': {
        'name': 'Soybean (सोयाबीन)',
        'marathi_name': 'सोयाबीन',
        'region': 'Latur, Nanded, Parbhani, Hingoli',
        'season': 'Kharif',
        'temp': (20, 32),
        'humidity': (50, 75),
        'soil_moisture': (40, 85),
        'light': (60, 90),
        'soil_type': 'Black cotton soil',
        'description': 'Main oilseed crop of Marathwada. Rainfed crop.',
        'local_tips': 'मराठवाड्यातील मुख्य पीक. पावसावर अवलंबून.'
    },
    
    'Cotton': {
        'name': 'Cotton (कापूस)',
        'marathi_name': 'कापूस',
        'region': 'Yavatmal, Akola, Amravati, Wardha',
        'season': 'Kharif',
        'temp': (22, 36),
        'humidity': (40, 65),
        'soil_moisture': (35, 80),
        'light': (70, 100),
        'soil_type': 'Black cotton soil',
        'description': 'Vidarbha region is famous for cotton. Drought-tolerant.',
        'local_tips': 'विदर्भातील मुख्य पीक. काळी माती योग्य.'
    },
    
    'Groundnut': {
        'name': 'Groundnut (भुईमूग)',
        'marathi_name': 'भुईमूग',
        'region': 'Solapur, Ahmednagar, Nashik',
        'season': 'Kharif & Summer',
        'temp': (22, 34),
        'humidity': (45, 70),
        'soil_moisture': (35, 75),
        'light': (75, 100),
        'soil_type': 'Sandy loam soil',
        'description': 'Important oilseed crop. Grows well in light soil.',
        'local_tips': 'हलकी जमीन योग्य. सोलापूर जिल्ह्यात मोठ्या प्रमाणात.'
    },
    
    'Bajra': {
        'name': 'Bajra (बाजरी)',
        'marathi_name': 'बाजरी',
        'region': 'Solapur, Ahmednagar, Dhule, Jalgaon',
        'season': 'Kharif',
        'temp': (25, 38),
        'humidity': (35, 60),
        'soil_moisture': (25, 65),
        'light': (80, 100),
        'soil_type': 'Light sandy soil',
        'description': 'Millet crop, drought-resistant. Good for dry areas.',
        'local_tips': 'कोरडवाहू भागासाठी योग्य. कमी पाण्यात चांगले उत्पादन.'
    },
    
    'Jowar': {
        'name': 'Jowar (ज्वारी)',
        'marathi_name': 'ज्वारी',
        'region': 'Solapur, Pune, Satara, Sangli',
        'season': 'Kharif & Rabi',
        'temp': (20, 35),
        'humidity': (40, 65),
        'soil_moisture': (30, 70),
        'light': (70, 100),
        'soil_type': 'Black soil',
        'description': 'Staple food grain of Maharashtra. Rabi jowar is famous.',
        'local_tips': 'रब्बी ज्वारी प्रसिद्ध. सोलापूर मध्ये मोठ्या प्रमाणात.'
    },
    
    'Wheat': {
        'name': 'Wheat (गहू)',
        'marathi_name': 'गहू',
        'region': 'Nashik, Ahmednagar, Pune, Satara',
        'season': 'Rabi',
        'temp': (12, 25),
        'humidity': (40, 65),
        'soil_moisture': (45, 85),
        'light': (60, 90),
        'soil_type': 'Well-drained loamy soil',
        'description': 'Winter crop, requires cool climate during growing.',
        'local_tips': 'हिवाळी पीक. नाशिक मध्ये चांगले उत्पादन.'
    },
    
    # Pulses
    'Tur': {
        'name': 'Tur (तूर)',
        'marathi_name': 'तूर',
        'region': 'Latur, Nanded, Parbhani, Jalna',
        'season': 'Kharif',
        'temp': (20, 34),
        'humidity': (45, 70),
        'soil_moisture': (30, 75),
        'light': (70, 100),
        'soil_type': 'Well-drained soil',
        'description': 'Main pulse crop of Marathwada. Rainfed cultivation.',
        'local_tips': 'मराठवाड्यातील मुख्य कडधान्य पीक.'
    },
    
    'Moong': {
        'name': 'Moong (मूग)',
        'marathi_name': 'मूग',
        'region': 'Jalgaon, Dhule, Nashik',
        'season': 'Kharif & Summer',
        'temp': (20, 32),
        'humidity': (50, 75),
        'soil_moisture': (35, 80),
        'light': (65, 95),
        'soil_type': 'Well-drained soil',
        'description': 'Short duration pulse crop. Good for intercropping.',
        'local_tips': 'कमी कालावधीत तयार होते. आंतरपीक म्हणून चांगले.'
    },
    
    # Fruits
    'Grapes': {
        'name': 'Grapes (द्राक्षे)',
        'marathi_name': 'द्राक्षे',
        'region': 'Nashik, Sangli, Solapur',
        'season': 'Rabi & Summer',
        'temp': (15, 35),
        'humidity': (45, 65),
        'soil_moisture': (50, 85),
        'light': (70, 100),
        'soil_type': 'Well-drained loamy soil',
        'description': 'Nashik is the grape capital of India. Export quality.',
        'local_tips': 'नाशिक मधील द्राक्षे प्रसिद्ध. बागायती पीक.'
    },
    
    'Pomegranate': {
        'name': 'Pomegranate (डाळिंब)',
        'marathi_name': 'डाळिंब',
        'region': 'Solapur, Sangli, Ahmednagar, Nashik',
        'season': 'Throughout year',
        'temp': (15, 38),
        'humidity': (35, 55),
        'soil_moisture': (40, 75),
        'light': (80, 100),
        'soil_type': 'Well-drained medium black soil',
        'description': 'Solapur pomegranate has GI tag. Drought-tolerant.',
        'local_tips': 'सोलापूरचे डाळिंब प्रसिद्ध. कमी पाण्यात चालते.'
    },
    
    'Banana': {
        'name': 'Banana (केळी)',
        'marathi_name': 'केळी',
        'region': 'Jalgaon, Dhule, Nandurbar',
        'season': 'Throughout year',
        'temp': (20, 35),
        'humidity': (60, 85),
        'soil_moisture': (55, 100),
        'light': (70, 100),
        'soil_type': 'Deep rich soil',
        'description': 'Jalgaon banana is famous. High water requirement.',
        'local_tips': 'जळगाव केळी प्रसिद्ध. भरपूर पाणी लागते.'
    },
    
    'Orange': {
        'name': 'Orange (संत्रे)',
        'marathi_name': 'संत्रे',
        'region': 'Nagpur, Amravati, Wardha',
        'season': 'Rabi',
        'temp': (10, 35),
        'humidity': (40, 70),
        'soil_moisture': (45, 85),
        'light': (70, 95),
        'soil_type': 'Well-drained loamy soil',
        'description': 'Nagpur orange has GI tag. Needs distinct winter.',
        'local_tips': 'नागपूरची संत्री प्रसिद्ध. थंड हवामान आवश्यक.'
    }
}

def get_crop_ranges(crop_name):
    """Get ideal ranges for a specific crop"""
    return CROP_RANGES.get(crop_name)

def get_all_crops():
    """Get list of all available crops"""
    return list(CROP_RANGES.keys())

def get_crops_by_region(region):
    """Get crops suitable for specific Maharashtra region"""
    region_crops = []
    for crop_name, crop_data in CROP_RANGES.items():
        if region.lower() in crop_data['region'].lower():
            region_crops.append({
                'name': crop_name,
                'marathi_name': crop_data['marathi_name'],
                'season': crop_data['season']
            })
    return region_crops

def get_seasonal_crops(season):
    """Get crops for specific season (Kharif/Rabi/Summer)"""
    seasonal_crops = []
    for crop_name, crop_data in CROP_RANGES.items():
        if season.lower() in crop_data['season'].lower():
            seasonal_crops.append(crop_name)
    return seasonal_crops