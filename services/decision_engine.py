"""
Decision engine module.
Handles environmental analysis and alert generation with regional context.
"""

from services.crop_rules import get_crop_ranges
from datetime import datetime

def get_marathi_season():
    """Get current season in Marathi"""
    month = datetime.now().month
    if 6 <= month <= 10:
        return "खरीप (Kharif)"
    elif 11 <= month <= 2:
        return "रब्बी (Rabi)"
    else:
        return "उन्हाळी (Summer)"

def analyze_environment(crop, temperature, humidity, soil_moisture, light):
    """
    Analyze environmental conditions and generate alerts and recommendations.
    Includes Maharashtra-specific recommendations.
    """
    ranges = get_crop_ranges(crop)
    
    if not ranges:
        return {
            'status': 'ERROR',
            'score': 0,
            'alerts': ['❌ चुकीचे पीक निवडले / Invalid crop selected'],
            'recommendations': ['कृपया योग्य पीक निवडा / Please select a valid crop'],
            'health_indicator': 'Unknown',
            'marathi_season': get_marathi_season()
        }
    
    alerts = []
    recommendations = []
    marathi_alerts = []
    marathi_recommendations = []
    score = 100
    parameters_checked = 0
    
    # Temperature check with regional context
    temp_min, temp_max = ranges['temp']
    if temperature < temp_min:
        alerts.append(f"❌ Low Temperature: {temperature}°C (Ideal: {temp_min}-{temp_max}°C)")
        marathi_alerts.append(f"❌ कमी तापमान: {temperature}°C (आदर्श: {temp_min}-{temp_max}°C)")
        
        if crop in ['Tomato', 'Capsicum']:
            recommendations.append(f"🌡️ Use plastic mulch or low tunnels to increase temperature")
            marathi_recommendations.append(f"🌡️ प्लास्टिक आच्छादन वापरा किंवा कमी तापमानात संरक्षण करा")
        elif crop in ['Sugarcane', 'Banana']:
            recommendations.append(f"🌡️ Provide frost protection. Use irrigation to moderate temperature")
            marathi_recommendations.append(f"🌡️ गारपीट संरक्षण करा. तापमान नियंत्रणासाठी पाणी द्या")
        else:
            recommendations.append(f"🌡️ Increase temperature using greenhouse heating or row covers")
            marathi_recommendations.append(f"🌡️ हरितगृहात तापमान वाढवा किंवा आच्छादन वापरा")
        score -= 25
        
    elif temperature > temp_max:
        alerts.append(f"❌ High Temperature: {temperature}°C (Ideal: {temp_min}-{temp_max}°C)")
        marathi_alerts.append(f"❌ जास्त तापमान: {temperature}°C (आदर्श: {temp_min}-{temp_max}°C)")
        
        if crop in ['Lettuce', 'Cauliflower']:
            recommendations.append(f"🌡️ Use shade nets (50-75%) to reduce temperature. Increase irrigation frequency")
            marathi_recommendations.append(f"🌡️ सावली जाळी वापरा. पाणी देण्याचे प्रमाण वाढवा")
        elif crop in ['Grapes', 'Pomegranate']:
            recommendations.append(f"🌡️ Apply kaolin spray on fruits to prevent sunburn. Maintain mulch")
            marathi_recommendations.append(f"🌡️ फळांना उन्हाची भाज पडू नये म्हणून काओलिन फवारणी करा")
        else:
            recommendations.append(f"🌡️ Increase ventilation, use misting system for cooling")
            marathi_recommendations.append(f"🌡️ हवा खेळती ठेवा, थंडाव्यासाठी धुके फवारणी यंत्रणा वापरा")
        score -= 25
    else:
        alerts.append(f"✅ Temperature: {temperature}°C (Optimal)")
        marathi_alerts.append(f"✅ तापमान: {temperature}°C (योग्य)")
        parameters_checked += 1
    
    # Humidity check with regional context
    hum_min, hum_max = ranges['humidity']
    if humidity < hum_min:
        alerts.append(f"❌ Low Humidity: {humidity}% (Ideal: {hum_min}-{hum_max}%)")
        marathi_alerts.append(f"❌ कमी आर्द्रता: {humidity}% (आदर्श: {hum_min}-{hum_max}%)")
        
        if crop in ['Tomato', 'Capsicum']:
            recommendations.append(f"💧 Use overhead sprinklers during hot hours. Mulch to retain moisture")
            marathi_recommendations.append(f"💧 उन्हाच्या वेळेत पाण्याची फवारणी करा. आच्छादन वापरा")
        elif crop in ['Sugarcane', 'Banana']:
            recommendations.append(f"💧 Increase irrigation frequency. Use drip irrigation with higher frequency")
            marathi_recommendations.append(f"💧 पाणी देण्याचे प्रमाण वाढवा. ठिबक सिंचन वापरा")
        else:
            recommendations.append(f"💧 Increase humidity using misting system or wet floors")
            marathi_recommendations.append(f"💧 धुके फवारणी यंत्रणा वापरून आर्द्रता वाढवा")
        score -= 25
        
    elif humidity > hum_max:
        alerts.append(f"❌ High Humidity: {humidity}% (Ideal: {hum_min}-{hum_max}%)")
        marathi_alerts.append(f"❌ जास्त आर्द्रता: {humidity}% (आदर्श: {hum_min}-{hum_max}%)")
        
        if crop in ['Grapes', 'Pomegranate']:
            recommendations.append(f"💧 Improve ventilation. Avoid overhead irrigation. Watch for fungal diseases")
            marathi_recommendations.append(f"💧 हवा खेळती ठेवा. बुरशीजन्य रोगांपासून सावधानता")
        elif crop in ['Cotton', 'Soybean']:
            recommendations.append(f"💧 Ensure proper spacing between plants. Use fungicide spray")
            marathi_recommendations.append(f"💧 झाडांमध्ये योग्य अंतर ठेवा. बुरशीनाशक फवारणी करा")
        else:
            recommendations.append(f"💧 Increase air circulation, reduce watering frequency")
            marathi_recommendations.append(f"💧 हवा खेळती ठेवा, पाणी देण्याचे प्रमाण कमी करा")
        score -= 25
    else:
        alerts.append(f"✅ Humidity: {humidity}% (Optimal)")
        marathi_alerts.append(f"✅ आर्द्रता: {humidity}% (योग्य)")
        parameters_checked += 1
    
    # Soil moisture check
    soil_min, soil_max = ranges['soil_moisture']
    if soil_moisture < soil_min:
        alerts.append(f"❌ Low Soil Moisture: {soil_moisture}% (Minimum: {soil_min}%)")
        marathi_alerts.append(f"❌ कमी जमिनीतील ओलावा: {soil_moisture}% (किमान: {soil_min}%)")
        
        if crop in ['Sugarcane', 'Banana']:
            recommendations.append(f"💦 Urgent irrigation needed. Use drip irrigation with 2-3 days interval")
            marathi_recommendations.append(f"💦 तातडीने पाणी द्या. ठिबक सिंचन वापरा")
        elif crop in ['Grapes', 'Pomegranate']:
            recommendations.append(f"💦 Apply mulch to conserve moisture. Critical stage irrigation needed")
            marathi_recommendations.append(f"💦 ओलावा टिकवण्यासाठी आच्छादन वापरा. महत्त्वाच्या टप्प्यावर पाणी द्या")
        else:
            recommendations.append(f"💦 Increase irrigation frequency. Apply organic mulch")
            marathi_recommendations.append(f"💦 पाणी देण्याचे प्रमाण वाढवा. सेंद्रिय आच्छादन वापरा")
        score -= 25
        
    elif soil_moisture > soil_max:
        alerts.append(f"⚠️ High Soil Moisture: {soil_moisture}% (Maximum: {soil_max}%)")
        marathi_alerts.append(f"⚠️ जास्त जमिनीतील ओलावा: {soil_moisture}% (कमाल: {soil_max}%)")
        
        if crop in ['Groundnut', 'Bajra']:
            recommendations.append(f"💦 Improve drainage. These crops are sensitive to waterlogging")
            marathi_recommendations.append(f"💦 निचरा व्यवस्था सुधारा. ही पिके पाणी साठण्यास संवेदनशील आहेत")
        else:
            recommendations.append(f"💦 Reduce irrigation frequency. Check drainage system")
            marathi_recommendations.append(f"💦 पाणी देण्याचे प्रमाण कमी करा. निचरा व्यवस्था तपासा")
        score -= 10
    else:
        alerts.append(f"✅ Soil Moisture: {soil_moisture}% (Optimal)")
        marathi_alerts.append(f"✅ जमिनीतील ओलावा: {soil_moisture}% (योग्य)")
        parameters_checked += 1
    
    # Light check
    light_min, light_max = ranges['light']
    if light < light_min:
        alerts.append(f"❌ Low Light: {light}% (Ideal: {light_min}-{light_max}%)")
        marathi_alerts.append(f"❌ कमी प्रकाश: {light}% (आदर्श: {light_min}-{light_max}%)")
        
        if crop in ['Tomato', 'Capsicum']:
            recommendations.append(f"☀️ Ensure proper spacing. Remove shading obstacles")
            marathi_recommendations.append(f"☀️ झाडांमध्ये योग्य अंतर ठेवा. सावली देणारे अडथळे दूर करा")
        elif crop in ['Lettuce']:
            recommendations.append(f"☀️ Partial shade is okay, but ensure at least morning sun")
            marathi_recommendations.append(f"☀️ सकाळचा सूर्यप्रकाश मिळेल याची खात्री करा")
        else:
            recommendations.append(f"☀️ Increase light exposure or clean greenhouse covering")
            marathi_recommendations.append(f"☀️ प्रकाशाचे प्रमाण वाढवा किंवा हरितगृह स्वच्छ करा")
        score -= 25
        
    elif light > light_max:
        alerts.append(f"⚠️ High Light: {light}% (Ideal: {light_min}-{light_max}%)")
        marathi_alerts.append(f"⚠️ जास्त प्रकाश: {light}% (आदर्श: {light_min}-{light_max}%)")
        
        if crop in ['Grapes', 'Pomegranate']:
            recommendations.append(f"☀️ Use shade nets during peak summer months (April-May)")
            marathi_recommendations.append(f"☀️ एप्रिल-मे मध्ये सावली जाळी वापरा")
        elif crop in ['Lettuce', 'Cauliflower']:
            recommendations.append(f"☀️ Provide 30-50% shade during afternoon hours")
            marathi_recommendations.append(f"☀️ दुपारच्या वेळेत ३०-५०% सावलीची व्यवस्था करा")
        else:
            recommendations.append(f"☀️ Provide shade during peak sunlight hours")
            marathi_recommendations.append(f"☀️ जास्त उन्हाच्या वेळेत सावलीची व्यवस्था करा")
        score -= 10
    else:
        alerts.append(f"✅ Light: {light}% (Optimal)")
        marathi_alerts.append(f"✅ प्रकाश: {light}% (योग्य)")
        parameters_checked += 1
    
    # Determine overall status
    if score >= 80:
        status = "GOOD"
        health_indicator = "उत्कृष्ट 🌟 (Excellent)"
    elif score >= 50:
        status = "ATTENTION REQUIRED"
        health_indicator = "मध्यम ⚠️ (Moderate)"
    else:
        status = "CRITICAL"
        health_indicator = "गंभीर 🔴 (Critical)"
    
    # Ensure score doesn't go below 0
    score = max(0, score)
    
    # Add region-specific recommendations
    region = ranges.get('region', 'Maharashtra')
    season = ranges.get('season', 'Kharif/Rabi')
    
    # Seasonal recommendations
    current_month = datetime.now().month
    if current_month in [4, 5] and crop in ['Tomato', 'Capsicum', 'Lettuce']:
        recommendations.append("☀️ Summer months: Increase shade and irrigation frequency")
        marathi_recommendations.append("☀️ उन्हाळ्यात: सावली आणि पाणी देण्याचे प्रमाण वाढवा")
    elif current_month in [11, 12, 1] and crop in ['Grapes', 'Pomegranate']:
        recommendations.append("❄️ Winter months: Protect from cold waves if temperature drops below 10°C")
        marathi_recommendations.append("❄️ हिवाळ्यात: तापमान १०°C पेक्षा कमी झाल्यास संरक्षण करा")
    
    return {
        'status': status,
        'score': score,
        'alerts': alerts,
        'marathi_alerts': marathi_alerts,
        'recommendations': recommendations,
        'marathi_recommendations': marathi_recommendations,
        'health_indicator': health_indicator,
        'parameters_optimal': parameters_checked,
        'total_parameters': 4,
        'crop_info': {
            'name': ranges['name'],
            'marathi_name': ranges['marathi_name'],
            'region': ranges['region'],
            'season': ranges['season'],
            'soil_type': ranges['soil_type'],
            'description': ranges['description'],
            'local_tips': ranges['local_tips']
        }
    }