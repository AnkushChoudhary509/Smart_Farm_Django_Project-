from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .models import Threat, CropTip, FarmerQuery, ThreatCategory
import json
import urllib.request, urllib.parse


# ─────────────────────────────────────────────────────────────────
# ROLE HELPERS
# ─────────────────────────────────────────────────────────────────
EXPERT_USERNAME = getattr(settings, 'EXPERT_USERNAME', 'AnkushChoudhary')


def is_expert(user):
    """Returns True only for the designated expert account."""
    return user.is_authenticated and user.username == EXPERT_USERNAME


def expert_required(view_fn):
    """Decorator: redirects non-experts to home with error message."""
    from functools import wraps
    @wraps(view_fn)
    def wrapper(request, *args, **kwargs):
        if not is_expert(request.user):
            messages.error(request, '🔒 Expert access required.')
            return redirect('home')
        return view_fn(request, *args, **kwargs)
    return wrapper


# ─────────────────────────────────────────────────────────────────
# AUTH VIEWS
# ─────────────────────────────────────────────────────────────────
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            nxt = request.GET.get('next', '/')
            return redirect(nxt)
        error = 'Invalid username or password. Please try again.'
    return render(request, 'farming/auth/login.html', {'error': error})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = ''
    if request.method == 'POST':
        username  = request.POST.get('username', '').strip()
        password  = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()
        email     = request.POST.get('email', '').strip()
        fname     = request.POST.get('first_name', '').strip()
        lname     = request.POST.get('last_name', '').strip()

        if not username or not password:
            error = 'Username and password are required.'
        elif password != password2:
            error = 'Passwords do not match.'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters.'
        elif username == EXPERT_USERNAME:
            error = 'That username is reserved.'
        elif User.objects.filter(username=username).exists():
            error = 'Username already taken. Choose another.'
        else:
            user = User.objects.create_user(
                username=username, password=password,
                email=email, first_name=fname, last_name=lname
            )
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name or username}! 🌾')
            return redirect('home')
    return render(request, 'farming/auth/signup.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    threats = Threat.objects.all()
    wildlife_count = threats.filter(category='wildlife').count()
    pest_count = threats.filter(category='pest').count()
    weed_count = threats.filter(category='weed').count()
    recent_tips = CropTip.objects.all()[:3]
    context = {
        'wildlife_count': wildlife_count,
        'pest_count': pest_count,
        'weed_count': weed_count,
        'total_threats': threats.count(),
        'recent_tips': recent_tips,
    }
    return render(request, 'farming/home.html', context)


def threat_list(request):
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    severity = request.GET.get('severity', '')
    threats = Threat.objects.all()
    if category:
        threats = threats.filter(category=category)
    if search:
        threats = threats.filter(
            Q(name__icontains=search) | Q(description__icontains=search) | Q(affected_crops__icontains=search)
        )
    if severity:
        threats = threats.filter(severity=severity)
    context = {
        'threats': threats, 'category': category,
        'search': search, 'severity': severity,
        'categories': ThreatCategory.choices,
    }
    return render(request, 'farming/threat_list.html', context)


def threat_detail(request, pk):
    threat = get_object_or_404(Threat, pk=pk)
    related = Threat.objects.filter(category=threat.category).exclude(pk=pk)[:3]
    return render(request, 'farming/threat_detail.html', {'threat': threat, 'related': related})


def crop_tips(request):
    season = request.GET.get('season', '')
    crop_type = request.GET.get('crop_type', '')
    tips = CropTip.objects.all()
    if season:
        tips = tips.filter(season__icontains=season)
    if crop_type:
        tips = tips.filter(crop_type__icontains=crop_type)
    return render(request, 'farming/crop_tips.html', {'tips': tips, 'season': season, 'crop_type': crop_type})


def ask_expert(request):
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        phone = (request.POST.get('phone') or '').strip()
        crop = (request.POST.get('crop') or '').strip()
        problem = (request.POST.get('problem') or '').strip()
        category = (request.POST.get('category') or 'pest').strip()
        if category not in [c[0] for c in ThreatCategory.choices]:
            category = 'pest'
        if not name or not crop or len(problem) < 10:
            messages.error(request, '❌ Please fill all required fields (name, crop, problem description).')
        else:
            try:
                FarmerQuery.objects.create(
                    name=name, email=email, phone=phone,
                    crop=crop, problem=problem, category=category,
                )
                messages.success(request, '✅ Query submitted! Our expert will respond within 48 hours.')
                return redirect('ask_expert')
            except Exception as ex:
                messages.error(request, f'❌ Save failed: {ex}')
    return render(request, 'farming/ask_expert.html', {'categories': ThreatCategory.choices})


def wildlife(request):
    threats = Threat.objects.filter(category='wildlife')
    return render(request, 'farming/category_page.html', {
        'threats': threats, 'category_name': 'Wildlife Threats', 'category': 'wildlife',
        'description': 'Wild animals that damage crops in fields', 'icon': 'lion', 'color': 'wildlife',
    })


def pests(request):
    threats = Threat.objects.filter(category='pest')
    return render(request, 'farming/category_page.html', {
        'threats': threats, 'category_name': 'Pests and Insects', 'category': 'pest',
        'description': 'Insects and pests that destroy crops', 'icon': 'bug', 'color': 'pest',
    })


def weeds(request):
    threats = Threat.objects.filter(category='weed')
    return render(request, 'farming/category_page.html', {
        'threats': threats, 'category_name': 'Weeds', 'category': 'weed',
        'description': 'Invasive plants that compete with crops', 'icon': 'leaf', 'color': 'weed',
    })


# ─── NEW FEATURES ────────────────────────────────────────────────────────────

def weather(request):
    crop_advisories = {
        "wheat":     {"kharif": "Avoid sowing wheat in Kharif. Wheat is a Rabi crop (Oct-Mar).", "rabi": "Sow Oct 15-Nov 15. Irrigate at CRI, tillering, jointing, flowering, and grain-filling stages."},
        "rice":      {"kharif": "Sow nursery in June. Transplant 25-30 days after nursery sowing. Use SRI method for 20% more yield.", "rabi": "Not suitable for Rabi. Consider mustard, wheat, or chickpea instead."},
        "cotton":    {"kharif": "Sow after first monsoon rain (June). Use Bt cotton seed. Monitor for whitefly from August. Apply neem oil 3ml/L.", "rabi": "Cotton does not grow in Rabi season."},
        "mustard":   {"kharif": "Not suitable for Kharif.", "rabi": "Sow Oct 1-15 for best yield. Avoid late sowing - increases aphid and Alternaria blight risk."},
        "maize":     {"kharif": "Sow after monsoon onset (June-July). Monitor for Fall Army Worm from emergence. Use pheromone traps.", "rabi": "Rabi maize possible in South India (Nov-Mar). DHM-117 is a popular hybrid."},
        "soybean":   {"kharif": "Sow June 15-July 15. Ideal for Central India. Treat seed with Rhizobium culture before sowing.", "rabi": "Not a Rabi crop in India."},
        "tomato":    {"kharif": "Raise nursery in June under 50-mesh insect net. Transplant July. Monitor for leaf curl virus.", "rabi": "Oct transplanting gives best quality fruit. Use drip irrigation."},
        "onion":     {"kharif": "Nursery June. Ensure good drainage to prevent Fusarium basal rot.", "rabi": "Main season. Nursery October, transplant November."},
        "potato":    {"kharif": "Not suitable - needs cool weather.", "rabi": "Plant Oct-Nov. Use certified seed tubers. Spray mancozeb preventively for late blight."},
        "groundnut": {"kharif": "Sow June-July after first good rain. Apply gypsum at pegging stage.", "rabi": "Rabi groundnut possible in AP/TN in Nov-Dec."},
        "chickpea":  {"kharif": "Not suitable.", "rabi": "Sow Oct-Nov. Install pheromone traps for Helicoverpa pod borer from November."},
        "sugarcane": {"kharif": "Feb-March planting for autumn crop.", "rabi": "Oct-Nov planting for spring sugarcane."},
    }

    state_advisories = {
        "Punjab": {
            "main_crops": "Wheat, Rice, Cotton, Maize, Sugarcane",
            "kharif": "Paddy dominant Kharif crop. PR-126 and Pusa-44 are popular varieties. Direct seeded rice saves water. Cotton in Malwa region - monitor whitefly and pink bollworm. Avoid paddy burning - use Happy Seeder for wheat.",
            "rabi": "Wheat (HD-3086, PBW-725) sown Oct 15-Nov 10. Irrigate at CRI, tillering, jointing, flowering, and grain filling. Mustard in Bathinda. Fog and frost damage risk in Jan-Feb.",
            "alerts": "Stubble burning banned - attracts Rs 5000 penalty. Use bio-decomposer spray. Pink bollworm resistant to Bt cotton reported in Abohar - use Coragen instead.",
            "schemes": "PM-KISAN, Punjab Kisan Card, Mukhyamantri Cotton Scheme.",
        },
        "Haryana": {
            "main_crops": "Wheat, Rice, Cotton, Bajra, Mustard",
            "kharif": "Paddy in irrigated areas. Bajra (HHB-272) in sandy Hisar region. Cotton in Sirsa and Fatehabad. Monitor for Pyrilla in sugarcane.",
            "rabi": "Wheat dominant - WH-1105 variety. Mustard in non-irrigated areas. Potato in Yamunanagar.",
            "alerts": "Whitefly resistant to imidacloprid in Fatehabad cotton belt - switch to flonicamid. Yellow rust in wheat - spray propiconazole if over 5% incidence.",
            "schemes": "Meri Fasal Mera Byora scheme, Saksham Haryana crop insurance.",
        },
        "Uttar Pradesh": {
            "main_crops": "Wheat, Rice, Sugarcane, Potato, Mustard, Pulses",
            "kharif": "Paddy in eastern UP (Gorakhpur belt). Sugarcane across Terai. Maize in Bundelkhand. Arhar/tur in rainfed Bundelkhand. Monitor Pyrilla in sugarcane from July.",
            "rabi": "Wheat dominant - largest wheat producing state. GW-496 and HI-8498 varieties. Mustard in Agra-Aligarh belt. Potato in Agra and Farrukhabad.",
            "alerts": "Shoot borer in sugarcane - release Cotesia flavipes at 5000 per acre. Late blight in potato (Agra belt) - spray mancozeb 75WP preventively.",
            "schemes": "UP Kisan Kalyan Mission, Paramparagat Krishi Vikas Yojana, Sugarcane price bonuses.",
        },
        "Uttarakhand": {
            "main_crops": "Rice, Wheat, Mandua (Finger Millet), Jhingora, Lentil, Rajma",
            "kharif": "Paddy in Tarai and Bhabar zone. Mandua (finger millet) and Jhingora in hills - drought tolerant. Soybean in Almora, Nainital.",
            "rabi": "Wheat in Tarai. Lentil, Chickpea, Peas in hills. Rajma (kidney bean) in high hills. Apple and stone fruits in Uttarkashi.",
            "alerts": "Hailstorm risk in April-May in hills - protect apple blossoms with nets. Landslide risk in Kharif - terrace maintenance critical.",
            "schemes": "Parvatiya Krishi Vikas, Uttarakhand Horticulture Mission, PMFBY.",
        },
        "Himachal Pradesh": {
            "main_crops": "Apple, Wheat, Maize, Potato, Off-season vegetables",
            "kharif": "Maize is dominant Kharif crop in hills. Off-season tomato, capsicum, pea in Lahaul-Spiti. Apple harvest Aug-Oct in Shimla, Kullu, Kinnaur.",
            "rabi": "Wheat in lower hills. Potato seed crop in Kufri and Solan. Garlic in Chamba.",
            "alerts": "Apple scab (Venturia inaequalis) - spray captan at pink bud stage. Codling moth - install delta traps at 5 per acre from April.",
            "schemes": "HP Horticulture Development Project, Apple e-marketing, Mukhyamantri Kisan Jeevan Suraksha Yojana.",
        },
        "Jammu & Kashmir": {
            "main_crops": "Apple, Rice, Maize, Saffron, Walnut, Cherry",
            "kharif": "Paddy in Jammu region. Maize in Rajouri and Poonch. Apple harvest starts August in Sopore belt.",
            "rabi": "Wheat in Jammu plains. Saffron in Pampore - October planting. Mustard in Kathua and Samba.",
            "alerts": "Woolly apple aphid resistant to chlorpyrifos - use thiamethoxam. Fire blight (Erwinia) in apple - prune infected branches and apply copper spray after rain.",
            "schemes": "J&K Horticulture Scheme, Mission for Integrated Development of Horticulture (MIDH).",
        },
        "Delhi": {
            "main_crops": "Vegetables, Wheat, Paddy (Yamuna floodplain), Flowers",
            "kharif": "Vegetables dominate - tomato, gourd, brinjal along Yamuna floodplain. Paddy in some pockets. Urban farming growing.",
            "rabi": "Wheat in outer Delhi fringe. Cauliflower, cabbage, peas prominent. Cut flowers for Delhi market.",
            "alerts": "Groundwater depletion - drip irrigation mandatory for orchards. Heavy metal contamination near Yamuna - test soil before growing leafy vegetables.",
            "schemes": "Delhi Urban Farm Scheme, Zero Budget Natural Farming pilot.",
        },
        "Rajasthan": {
            "main_crops": "Bajra, Jowar, Moth Bean, Clusterbean (Guar), Wheat, Mustard",
            "kharif": "Bajra (pearl millet) is main crop - HHB-272, Kaveri Super Boss varieties. Clusterbean in Barmer and Jodhpur for gum export. Moth bean in Thar desert. Cumin in Jalore and Barmer.",
            "rabi": "Mustard dominant - Rajasthan produces 40% of India mustard. Wheat in canal-irrigated areas of Kota and Bundi. Coriander in Baran. Fennel in Sirohi.",
            "alerts": "Mealy bug on guar in Aug-Sep - spray dimethoate. Powdery mildew on mustard in cold nights - spray sulphur 80WP at 3g per litre.",
            "schemes": "Rajasthan Krishi Upaj Rahan Rin Yojana, Mukhyamantri Kisan Rin Mafi, Rajasthan Agri Processing Policy.",
        },
        "Gujarat": {
            "main_crops": "Cotton, Groundnut, Sugarcane, Wheat, Castor, Tobacco",
            "kharif": "Cotton is dominant Kharif crop in Saurashtra. Groundnut in Saurashtra and Kutch. Castor in Mehsana and Banaskantha. Monitor pink bollworm with pheromone traps.",
            "rabi": "Wheat in North Gujarat. Cumin and fennel in Unjha - world largest cumin market. Potato in Deesa. Mustard in Banaskantha.",
            "alerts": "Pink bollworm resistance to Bt cotton confirmed in Saurashtra - use Coragen (chlorantraniliprole) instead. Mites in cumin during dry weather - spray abamectin.",
            "schemes": "Ikhedut Farmer Portal, Kisan Suvidha Gujarat, Soil Health Card linked fertilizer subsidy.",
        },
        "Maharashtra": {
            "main_crops": "Cotton, Sugarcane, Soybean, Jowar, Onion, Grapes",
            "kharif": "Soybean in Vidarbha and Marathwada. Cotton across Maharashtra. Jowar in dry Marathwada. Monitor for yellow mosaic virus in soybean.",
            "rabi": "Wheat in irrigated areas. Onion dominant in Nashik and Pune. Chickpea in Latur. Grapes harvest Feb-Mar in Nashik.",
            "alerts": "Leaf hopper in grapes before harvest - spray 15 days before harvest. Pink stem borer in sugarcane - Trichogramma releases at 50000 per acre.",
            "schemes": "Nanaji Deshmukh Krishi Sanjivani, Mahadbee crop insurance, Maharashtra Shetkari Sahayata Nidhi.",
        },
        "Goa": {
            "main_crops": "Rice, Cashew, Coconut, Vegetables, Areca nut",
            "kharif": "Paddy (Jyothi, Jaya varieties) in Kharif. Cashew major plantation crop - harvest March-May. Coconut year-round.",
            "rabi": "Vegetables in laterite soils. Banana year-round.",
            "alerts": "Stem bleeding disease in coconut - apply Bordeaux paste to stem. Tea mosquito bug in cashew during flowering - spray quinalphos.",
            "schemes": "Goa State Agriculture Policy, National Horticulture Mission for cashew rejuvenation.",
        },
        "Karnataka": {
            "main_crops": "Jowar, Cotton, Ragi (Finger Millet), Coffee, Coconut, Sugarcane",
            "kharif": "Cotton in North Karnataka (Dharwad, Belagavi). Ragi in Hassan and Tumkur. Coffee harvest Nov-Jan in Coorg. Monitor stem fly and helicoverpa in cotton.",
            "rabi": "Jowar dominant rabi crop. Sunflower in Haveri. Chickpea in Gulbarga. Tomato in Kolar.",
            "alerts": "White fly resistant Bt cotton in Dharwad - use neem oil spray 5ml per litre. Coffee berry borer in Coorg - install yellow sticky traps.",
            "schemes": "Bhoomi land records, Raitha Samparka Kendras, Karnataka Krishi Ashwas Scheme.",
        },
        "Tamil Nadu": {
            "main_crops": "Rice, Banana, Sugarcane, Cotton, Groundnut, Coconut, Turmeric",
            "kharif": "Kuruvai paddy (Jun-Sep) in Thanjavur delta. Banana year-round in Theni and Salem. Monitor for Sigatoka disease in banana.",
            "rabi": "Samba paddy (Dec-Mar) is main season. Sugarcane in Erode and Tirunelveli. Coconut in Coimbatore. Turmeric in Salem and Namakkal.",
            "alerts": "Leaf blight (Helminthosporium) in paddy during Samba - spray propiconazole plus tricyclazole. Stem weevil in banana - use approved bio-alternatives.",
            "schemes": "Uzhavar Sandhai direct market, CM Kalaignar Magalir Urimai Thittam, PMFBY through TNAU.",
        },
        "Andhra Pradesh": {
            "main_crops": "Rice, Cotton, Groundnut, Chilli, Tobacco, Aquaculture",
            "kharif": "Paddy dominant in Krishna and Godavari deltas. Cotton in Guntur belt. Chilli in Guntur - world largest chilli market. Monitor leaf miner in groundnut.",
            "rabi": "Rabi paddy in delta regions. Groundnut in Anantapur. Tobacco in Guntur and Prakasam - regulated crop.",
            "alerts": "Yellow mite in chilli - spray abamectin at 0.5ml per litre. Bud necrosis virus in groundnut - control thrips with fipronil seed treatment.",
            "schemes": "YSR Rythu Bharosa (Rs 13500/year), AP Rythu Seva Kendras, Smart Pulse Hub.",
        },
        "Telangana": {
            "main_crops": "Cotton, Rice, Maize, Soybean, Chilli, Turmeric",
            "kharif": "Cotton dominant in Warangal and Adilabad. Paddy post-Kaleshwaram project. Soybean in Nizamabad. Monitor pink bollworm from August.",
            "rabi": "Rabi maize and paddy with irrigation. Turmeric in Nizamabad - GI-tagged Nizamabad Yellow variety.",
            "alerts": "Groundwater depletion in plateau - switch to drip irrigation for cotton. Stem rot in paddy in waterlogged patches - apply propiconazole.",
            "schemes": "Rythu Bandhu (Rs 10000 per acre per year), Rythu Bima life insurance, Mission Kakatiya tank restoration.",
        },
        "Kerala": {
            "main_crops": "Coconut, Rubber, Pepper, Cardamom, Rice, Banana, Ginger",
            "kharif": "Nendran and Red Banana in Thrissur and Palakkad. Pepper in Wayanad - monitor for Phytophthora foot rot. Rice (Pokkali) in Alappuzha backwaters.",
            "rabi": "Rubber tapping Nov-May. Cardamom in Idukki - harvest Sep-Nov. Ginger post-monsoon in Wayanad.",
            "alerts": "Bud rot disease in coconut (Phytophthora) - inject metalaxyl into palm trunk. Quick wilt disease in pepper - drench soil with Trichoderma 10g per litre.",
            "schemes": "Kerala Karshaka Ksheam, Subhiksha Keralam food self-sufficiency programme, Vegetable Development Programme.",
        },
        "West Bengal": {
            "main_crops": "Rice (Aman, Aus, Boro), Jute, Potato, Mustard, Vegetables",
            "kharif": "Aman paddy dominant - harvest Nov-Dec. Jute cultivation June-Sep in Nadia and Murshidabad. Aus paddy (dry season) in some districts.",
            "rabi": "Boro paddy (irrigated, Jan-May). Potato in Hooghly and Burdwan. Mustard. Large vegetable cluster near Kolkata.",
            "alerts": "Brown plant hopper (BPH) in Aman paddy Aug-Oct - avoid excess nitrogen, use BPH-resistant varieties. Late blight in potato in Hooghly belt Nov-Jan.",
            "schemes": "Bangla Shasya Bima state crop insurance, Krishak Bandhu scheme (Rs 10000 per acre annual support).",
        },
        "Bihar": {
            "main_crops": "Rice, Wheat, Maize, Lentil, Litchi, Makhana",
            "kharif": "Paddy dominant Kharif. Maize explosion in north Bihar (Supaul, Darbhanga). Makhana (fox nut) in Darbhanga - unique to Bihar.",
            "rabi": "Wheat in Kosi and Mithilanchal. Lentil (masoor) in Jehanabad. Litchi harvest May-June in Muzaffarpur - world famous. Onion in Patna belt.",
            "alerts": "Stem rot in paddy (Sclerotium) in waterlogged fields - improve drainage. Whitefly in litchi pre-harvest - avoid neonicotinoids during flowering.",
            "schemes": "Bihar Krishi Road Map, Mukhyamantri Tivra Beej Vistar, PM-KISAN, PMFBY.",
        },
        "Jharkhand": {
            "main_crops": "Rice, Maize, Arhar, Niger seed, Vegetables",
            "kharif": "Rain-fed paddy dominant. Niger seed in tribal areas (Simdega, Gumla). Arhar in uplands. Vegetables in plateau soils.",
            "rabi": "Wheat in river valleys. Mustard. Pulses: lentil, gram. Horticulture growing - papaya, banana, litchi.",
            "alerts": "Neck blast in paddy - spray tricyclazole at booting stage. Dehydration risk for crops on plateau - mulching recommended.",
            "schemes": "JSLPS tribal farmer programs, Zero Budget Natural Farming, Jharkhand Organic Mission.",
        },
        "Odisha": {
            "main_crops": "Rice, Groundnut, Sugarcane, Turmeric, Vegetables, Cashew",
            "kharif": "Paddy most dominant - Swarna and MTU-1010 popular varieties. Groundnut in coastal sandy soils. Sugarcane in Rayagada. Cyclone risk - PMFBY claims important.",
            "rabi": "Mustard, Wheat (limited). Winter vegetables in river delta. Tomato near Bhubaneswar.",
            "alerts": "Cyclone risk Oct-Nov - pre-positioning of seeds for replanting. Tungro virus in paddy - remove and burn infected plants immediately.",
            "schemes": "Odisha Kisan Assistance Yojana (OKAY), BALARAM scheme for landless farmers, Odisha Millets Mission.",
        },
        "Madhya Pradesh": {
            "main_crops": "Wheat, Soybean, Chickpea, Linseed, Maize, Garlic",
            "kharif": "Soybean in Malwa plateau (Indore, Ujjain, Dewas belt) - JS-335 and NRC-37 varieties. Maize in Chhindwara. Monitor stem fly and semilooper in soybean.",
            "rabi": "Wheat dominant. Chickpea in Sehore and Raisen. Garlic in Mandsaur - India biggest garlic market. Linseed in Bundelkhand.",
            "alerts": "Soybean yellow mosaic virus spreading in Malwa - control whitefly vector with imidacloprid seed treatment. Pink stem borer in wheat in February.",
            "schemes": "Bhavantar Bhugtan Yojana price support, MP Kisan Kalyan Yojana, Shivraj Kisan Samriddhi Yojana.",
        },
        "Chhattisgarh": {
            "main_crops": "Rice, Maize, Kodo-Kutki (millets), Linseed, Pulses",
            "kharif": "Paddy - Rice Bowl of Central India. Varieties: Swarna, Mahamaya, Indira Sona. Kodo-Kutki millets in tribal Bastar and Dantewada.",
            "rabi": "Wheat in Surguja. Linseed in Bilaspur. Pulses. Tomato in Raipur belt.",
            "alerts": "Neck blast in paddy during flowering - spray tricyclazole. Wild boar damage in Bastar - community solar fence recommended.",
            "schemes": "Rajiv Gandhi Kisan Nyay Yojana (Rs 9000 per acre income support), Chhattisgarh Organic Mission.",
        },
        "Assam": {
            "main_crops": "Rice (Sali, Boro, Ahu), Tea, Jute, Mustard, Potato",
            "kharif": "Sali paddy dominant (Aug sowing, Dec harvest). Tea harvest flush Mar-Nov - Assam tea famous globally. Jute in lower Assam.",
            "rabi": "Boro paddy (Feb-May with irrigation). Mustard in winter. Potato in Brahmaputra valley.",
            "alerts": "Stem borer in paddy - install light traps from July. Blister blight in tea - spray copper oxychloride. Flood risk Jul-Aug is severe.",
            "schemes": "Assam Adarsha Krishak model farmer scheme, Mission for Integrated Development of Horticulture.",
        },
        "Meghalaya": {
            "main_crops": "Potato, Ginger, Turmeric, Pineapple, Mandarin, Rice",
            "kharif": "Paddy on terraced fields. Ginger in East Khasi Hills. Lakadong turmeric - GI tagged. Pineapple in West Khasi Hills.",
            "rabi": "Potato in high altitude (Shillong, Nongstoin). Mandarin orange in Ri-Bhoi.",
            "alerts": "Bacterial wilt in ginger - use disease-free seed rhizomes, dip in streptocycline. Potato late blight - spray mancozeb every 7 days in cool and wet weather.",
            "schemes": "Meghalaya Agriculture Intensification Project, North East Organic Mission.",
        },
        "Manipur": {
            "main_crops": "Rice, Mustard, Vegetables, Chilli, Ginger, Lemon",
            "kharif": "Paddy in Imphal Valley rice fields. Chilli cultivation growing. King Chilli (Bhut Jolokia) in hill districts.",
            "rabi": "Mustard. Vegetables in lowland. Pea and Tomato in hills.",
            "alerts": "Neck blast in paddy - use blast-resistant varieties like Manipur Bao Dhan. Fruit borer in chilli crop.",
            "schemes": "NE PMKSY, Manipur Organic Mission.",
        },
        "Mizoram": {
            "main_crops": "Jhum Rice, Maize, Ginger, Turmeric, Banana, Rubber",
            "kharif": "Jhum (shifting) cultivation for rice and vegetables. Maize and ginger growing in permanent fields.",
            "rabi": "Rubber tapping in dry season. Banana. Seasonal vegetables.",
            "alerts": "Shifting cultivation (Jhum) degrades soil - transition to permanent farming with terracing is recommended. Mite in ginger at dry spells.",
            "schemes": "Mizoram State Farm Policy, NHM for banana and ginger, RKVY for jhum transition.",
        },
        "Nagaland": {
            "main_crops": "Rice, Maize, Millet, King Chilli, Soybean, Ginger",
            "kharif": "Paddy on terraced hillsides. King Chilli (Bhut Jolokia - GI tagged, world hottest chilli). Maize on slopes.",
            "rabi": "Oilseed crops. Pulse crops in valley areas.",
            "alerts": "Jhum cycle shortening causes soil erosion - agroforestry strongly recommended. Downy mildew in maize during wet weather.",
            "schemes": "Nagaland Organic Mission, NHM, RKVY Kisan Call Centre.",
        },
        "Arunachal Pradesh": {
            "main_crops": "Rice, Maize, Millet, Apple, Orange, Kiwi",
            "kharif": "Jhum paddy. Maize on terraces. Kiwi and apple in Tawang and Ziro Valley.",
            "rabi": "Apple and stone fruits in high altitude. Vegetables in lower hills.",
            "alerts": "Codling moth in apple - install delta traps from March. Soil erosion on steep slopes - avoid mono-cropping.",
            "schemes": "NHM Kiwi development, PMKSY watershed programme, RKVY.",
        },
        "Tripura": {
            "main_crops": "Rice, Jute, Mustard, Potato, Vegetables, Rubber, Pineapple",
            "kharif": "Aman paddy dominant. Jute in valley areas. Pineapple in Gomati and Sipahijala.",
            "rabi": "Rabi paddy. Mustard and potato. Rubber growing rapidly in West Tripura.",
            "alerts": "Rubber tapping panel necrosis - use Ethephon at recommended dosage only. Pineapple heart rot - improve drainage.",
            "schemes": "Tripura Rubber Mission, NHM for pineapple, PMKSY.",
        },
        "Sikkim": {
            "main_crops": "Cardamom, Ginger, Rice, Maize, Mandarin, Buckwheat",
            "kharif": "Large Cardamom (Amomum subulatum) - Sikkim is world largest producer, GI tagged. Ginger in South Sikkim. Paddy in valley.",
            "rabi": "Buckwheat in high altitude. Mandarin orange. Temperate vegetables.",
            "alerts": "Chirke and Foorkey diseases in cardamom - destroy infected plants, use Dimethomorph spray. 100% organic state - no synthetic pesticides allowed.",
            "schemes": "Sikkim Organic Mission (100% organic state since 2016), NHM for cardamom.",
        },
        "Chandigarh": {
            "main_crops": "Wheat, Paddy, Vegetables (peri-urban farming)",
            "kharif": "Paddy in peripheral areas. Urban vegetable farming growing. Protected cultivation (polyhouse) expanding.",
            "rabi": "Wheat. Protected cultivation - polyhouse tomato, capsicum, cucumber.",
            "alerts": "Limited farmland - focus on high-value horticulture and protected cultivation for maximum income.",
            "schemes": "UT scheme linked with Punjab state schemes, PM-KISAN.",
        },
        "Ladakh": {
            "main_crops": "Barley, Wheat, Buckwheat, Peas, Sea Buckthorn, Apple",
            "kharif": "Short growing season (May-Sep). Barley and peas on terraces. Sea buckthorn berry - high value export crop with medicinal properties.",
            "rabi": "Extreme cold - no rabi crops possible. Greenhouses for off-season vegetables.",
            "alerts": "Very short frost-free season - use cold-tolerant varieties only. Codling moth in apple orchards. Use greenhouse for extended growing season.",
            "schemes": "LAHDC Agricultural scheme, NHM for sea buckthorn, PM-KISAN.",
        },
        "Lakshadweep": {
            "main_crops": "Coconut, Breadfruit, Banana, Vegetables",
            "kharif": "Coconut dominant year-round plantation. Banana varieties. Limited vegetable cultivation.",
            "rabi": "Same as Kharif - tropical island with no distinct seasons.",
            "alerts": "Root wilt disease in coconut - no cure, remove affected palms. Eriophyid mite in coconut - spray sulphur.",
            "schemes": "NHM for coconut, PM-KISAN for small holders.",
        },
        "Daman and Diu": {
            "main_crops": "Rice, Vegetables, Coconut, Groundnut",
            "kharif": "Paddy in Kharif. Groundnut. Vegetables for local market.",
            "rabi": "Winter vegetables. Coconut year-round.",
            "alerts": "Limited fresh water availability - rainwater harvesting essential. Sea intrusion in coastal farms - use salt-tolerant varieties.",
            "schemes": "PM-KISAN, NHM, Central UT agricultural schemes.",
        },
        "Dadra and Nagar Haveli": {
            "main_crops": "Rice, Sugarcane, Groundnut, Vegetables",
            "kharif": "Paddy dominant. Sugarcane. Tribal farming communities growing vegetables.",
            "rabi": "Vegetables. Groundnut.",
            "alerts": "Leaf blast in paddy in tribal areas - spray tricyclazole. Rodent damage in standing paddy crop.",
            "schemes": "PM-KISAN, RKVY, tribal farmer welfare schemes.",
        },
        "Andaman & Nicobar Islands": {
            "main_crops": "Coconut, Rice, Arecanut, Banana, Spices, Vegetables",
            "kharif": "Paddy in Kharif. Banana and coconut year-round. Clove and nutmeg spice cultivation in islands.",
            "rabi": "Vegetables. Root crops. Arecanut year-round.",
            "alerts": "Rhinoceros beetle in coconut palms - install pheromone traps. Root wilt disease in coconut spreading.",
            "schemes": "Andaman Islands Development Corporation, NHM, PM-KISAN.",
        },
        "Puducherry": {
            "main_crops": "Paddy, Sugarcane, Groundnut, Cotton, Vegetables",
            "kharif": "Paddy dominant in both Kharif and Rabi (with irrigation). Sugarcane in Karaikal region.",
            "rabi": "Rabi paddy with irrigation. Groundnut. Vegetables near Pondicherry city.",
            "alerts": "Blast disease in paddy - spray tricyclazole. Armyworm in sugarcane - use Bt formulation.",
            "schemes": "Puducherry Agriculture Department schemes, NHM, PM-KISAN.",
        },
    }

    return render(request, "farming/weather.html", {
        "crop_advisories": json.dumps(crop_advisories),
        "state_advisories": state_advisories,
        "all_states": sorted(state_advisories.keys()),
    })


def market_prices(request):
    mandi_data = {
        'Wheat': [
            {'mandi': 'Khanna, Punjab', 'state': 'Punjab', 'price': 2275, 'min': 2200, 'max': 2300, 'trend': 'up'},
            {'mandi': 'Hapur, UP', 'state': 'Uttar Pradesh', 'price': 2180, 'min': 2100, 'max': 2250, 'trend': 'stable'},
            {'mandi': 'Indore, MP', 'state': 'Madhya Pradesh', 'price': 2220, 'min': 2150, 'max': 2280, 'trend': 'up'},
            {'mandi': 'Jodhpur, Rajasthan', 'state': 'Rajasthan', 'price': 2195, 'min': 2120, 'max': 2260, 'trend': 'down'},
            {'mandi': 'Nagpur, Maharashtra', 'state': 'Maharashtra', 'price': 2240, 'min': 2190, 'max': 2300, 'trend': 'stable'},
        ],
        'Rice': [
            {'mandi': 'Karnal, Haryana', 'state': 'Haryana', 'price': 2300, 'min': 2200, 'max': 2400, 'trend': 'up'},
            {'mandi': 'Bardhaman, WB', 'state': 'West Bengal', 'price': 2150, 'min': 2050, 'max': 2250, 'trend': 'stable'},
            {'mandi': 'Cuttack, Odisha', 'state': 'Odisha', 'price': 2080, 'min': 2000, 'max': 2160, 'trend': 'down'},
            {'mandi': 'Guntur, AP', 'state': 'Andhra Pradesh', 'price': 2190, 'min': 2100, 'max': 2280, 'trend': 'up'},
            {'mandi': 'Thanjavur, TN', 'state': 'Tamil Nadu', 'price': 2120, 'min': 2040, 'max': 2200, 'trend': 'stable'},
        ],
        'Cotton': [
            {'mandi': 'Akola, Maharashtra', 'state': 'Maharashtra', 'price': 7200, 'min': 7000, 'max': 7400, 'trend': 'up'},
            {'mandi': 'Warangal, Telangana', 'state': 'Telangana', 'price': 7150, 'min': 6950, 'max': 7350, 'trend': 'stable'},
            {'mandi': 'Rajkot, Gujarat', 'state': 'Gujarat', 'price': 7350, 'min': 7200, 'max': 7500, 'trend': 'up'},
            {'mandi': 'Sirsa, Haryana', 'state': 'Haryana', 'price': 7100, 'min': 6900, 'max': 7300, 'trend': 'down'},
            {'mandi': 'Guntur, AP', 'state': 'Andhra Pradesh', 'price': 7280, 'min': 7100, 'max': 7450, 'trend': 'up'},
        ],
        'Onion': [
            {'mandi': 'Lasalgaon, Maharashtra', 'state': 'Maharashtra', 'price': 1850, 'min': 1700, 'max': 2000, 'trend': 'up'},
            {'mandi': 'Hubli, Karnataka', 'state': 'Karnataka', 'price': 1720, 'min': 1600, 'max': 1850, 'trend': 'stable'},
            {'mandi': 'Mahuva, Gujarat', 'state': 'Gujarat', 'price': 1900, 'min': 1750, 'max': 2050, 'trend': 'up'},
            {'mandi': 'Alwar, Rajasthan', 'state': 'Rajasthan', 'price': 1680, 'min': 1550, 'max': 1800, 'trend': 'down'},
            {'mandi': 'Kurnool, AP', 'state': 'Andhra Pradesh', 'price': 1760, 'min': 1620, 'max': 1900, 'trend': 'stable'},
        ],
        'Tomato': [
            {'mandi': 'Kolar, Karnataka', 'state': 'Karnataka', 'price': 2400, 'min': 2100, 'max': 2700, 'trend': 'up'},
            {'mandi': 'Nashik, Maharashtra', 'state': 'Maharashtra', 'price': 2200, 'min': 1900, 'max': 2500, 'trend': 'stable'},
            {'mandi': 'Madanapalle, AP', 'state': 'Andhra Pradesh', 'price': 2600, 'min': 2300, 'max': 2900, 'trend': 'up'},
            {'mandi': 'Kanpur, UP', 'state': 'Uttar Pradesh', 'price': 2100, 'min': 1800, 'max': 2400, 'trend': 'down'},
            {'mandi': 'Jalandhar, Punjab', 'state': 'Punjab', 'price': 2300, 'min': 2000, 'max': 2600, 'trend': 'stable'},
        ],
        'Potato': [
            {'mandi': 'Agra, UP', 'state': 'Uttar Pradesh', 'price': 1200, 'min': 1100, 'max': 1350, 'trend': 'stable'},
            {'mandi': 'Hooghly, WB', 'state': 'West Bengal', 'price': 1150, 'min': 1050, 'max': 1280, 'trend': 'down'},
            {'mandi': 'Jalandhar, Punjab', 'state': 'Punjab', 'price': 1280, 'min': 1180, 'max': 1400, 'trend': 'up'},
            {'mandi': 'Indore, MP', 'state': 'Madhya Pradesh', 'price': 1180, 'min': 1080, 'max': 1320, 'trend': 'stable'},
            {'mandi': 'Ajmer, Rajasthan', 'state': 'Rajasthan', 'price': 1220, 'min': 1120, 'max': 1360, 'trend': 'up'},
        ],
        'Soybean': [
            {'mandi': 'Indore, MP', 'state': 'Madhya Pradesh', 'price': 4800, 'min': 4650, 'max': 4950, 'trend': 'up'},
            {'mandi': 'Latur, Maharashtra', 'state': 'Maharashtra', 'price': 4750, 'min': 4600, 'max': 4900, 'trend': 'stable'},
            {'mandi': 'Kota, Rajasthan', 'state': 'Rajasthan', 'price': 4820, 'min': 4680, 'max': 4970, 'trend': 'up'},
            {'mandi': 'Nagpur, Maharashtra', 'state': 'Maharashtra', 'price': 4700, 'min': 4550, 'max': 4850, 'trend': 'down'},
            {'mandi': 'Ujjain, MP', 'state': 'Madhya Pradesh', 'price': 4780, 'min': 4640, 'max': 4930, 'trend': 'stable'},
        ],
        'Mustard': [
            {'mandi': 'Alwar, Rajasthan', 'state': 'Rajasthan', 'price': 5400, 'min': 5200, 'max': 5600, 'trend': 'up'},
            {'mandi': 'Agra, UP', 'state': 'Uttar Pradesh', 'price': 5350, 'min': 5150, 'max': 5550, 'trend': 'up'},
            {'mandi': 'Hapur, UP', 'state': 'Uttar Pradesh', 'price': 5300, 'min': 5100, 'max': 5500, 'trend': 'stable'},
            {'mandi': 'Morena, MP', 'state': 'Madhya Pradesh', 'price': 5450, 'min': 5250, 'max': 5650, 'trend': 'up'},
            {'mandi': 'Rohtak, Haryana', 'state': 'Haryana', 'price': 5380, 'min': 5180, 'max': 5580, 'trend': 'stable'},
        ],
        'Groundnut': [
            {'mandi': 'Rajkot, Gujarat', 'state': 'Gujarat', 'price': 6800, 'min': 6600, 'max': 7000, 'trend': 'up'},
            {'mandi': 'Junagadh, Gujarat', 'state': 'Gujarat', 'price': 6750, 'min': 6550, 'max': 6950, 'trend': 'stable'},
            {'mandi': 'Kurnool, AP', 'state': 'Andhra Pradesh', 'price': 6900, 'min': 6700, 'max': 7100, 'trend': 'up'},
            {'mandi': 'Bellary, Karnataka', 'state': 'Karnataka', 'price': 6820, 'min': 6620, 'max': 7020, 'trend': 'stable'},
            {'mandi': 'Warangal, Telangana', 'state': 'Telangana', 'price': 6780, 'min': 6580, 'max': 6980, 'trend': 'down'},
        ],
    }

    msp_data = {
        'Wheat': 2275, 'Rice': 2300, 'Cotton': 7121, 'Maize': 2090,
        'Soybean': 4892, 'Mustard': 5650, 'Groundnut': 6783,
        'Chickpea': 5440, 'Sugarcane': 340, 'Onion': None,
        'Tomato': None, 'Potato': None,
    }

    crops = list(mandi_data.keys())
    selected_crop = request.GET.get('crop', 'Wheat')
    if selected_crop not in mandi_data:
        selected_crop = 'Wheat'

    current_data = mandi_data[selected_crop]
    best_market = max(current_data, key=lambda x: x['price'])
    avg_price = sum(d['price'] for d in current_data) // len(current_data)
    msp = msp_data.get(selected_crop)

    lowest_market = min(current_data, key=lambda x: x['price'])
    return render(request, 'farming/market_prices.html', {
        'crops': crops,
        'selected_crop': selected_crop,
        'mandi_data': current_data,
        'best_market': best_market,
        'lowest_market': lowest_market,
        'avg_price': avg_price,
        'msp': msp,
        'all_data': json.dumps(mandi_data),
        'msp_data': json.dumps(msp_data),
    })


def irrigation_calculator(request):
    result = None
    if request.method == 'POST':
        crop = request.POST.get('crop', 'wheat')
        soil = request.POST.get('soil', 'loam')
        area_acres = float(request.POST.get('area', 1))
        rainfall_mm = float(request.POST.get('rainfall', 0))
        growth_stage = request.POST.get('growth_stage', 'vegetative')
        temperature = request.POST.get('temperature', 'moderate')
        irrigation_method = request.POST.get('irrigation_method', 'flood')

        crop_etc = {
            'wheat':     {'initial': 2.5, 'vegetative': 4.5, 'flowering': 6.5, 'maturity': 3.5},
            'rice':      {'initial': 6.0, 'vegetative': 8.0, 'flowering': 9.0, 'maturity': 6.0},
            'cotton':    {'initial': 3.0, 'vegetative': 5.5, 'flowering': 7.5, 'maturity': 4.5},
            'maize':     {'initial': 3.0, 'vegetative': 5.5, 'flowering': 7.0, 'maturity': 4.0},
            'sugarcane': {'initial': 3.5, 'vegetative': 7.0, 'flowering': 8.5, 'maturity': 5.5},
            'tomato':    {'initial': 2.5, 'vegetative': 4.5, 'flowering': 6.0, 'maturity': 4.0},
            'potato':    {'initial': 2.0, 'vegetative': 5.0, 'flowering': 7.0, 'maturity': 4.5},
            'onion':     {'initial': 2.0, 'vegetative': 4.0, 'flowering': 5.5, 'maturity': 3.5},
            'mustard':   {'initial': 2.0, 'vegetative': 3.5, 'flowering': 5.5, 'maturity': 3.0},
            'soybean':   {'initial': 2.5, 'vegetative': 4.5, 'flowering': 6.5, 'maturity': 3.5},
            'groundnut': {'initial': 2.5, 'vegetative': 4.0, 'flowering': 6.0, 'maturity': 3.5},
            'chickpea':  {'initial': 1.5, 'vegetative': 3.0, 'flowering': 4.5, 'maturity': 2.5},
        }
        soil_whc = {'sandy': 60, 'sandy_loam': 100, 'loam': 140, 'clay_loam': 170, 'clay': 200}
        temp_factor = {'cool': 0.85, 'moderate': 1.0, 'hot': 1.20, 'very_hot': 1.35}
        efficiency = {'flood': 0.60, 'furrow': 0.70, 'sprinkler': 0.80, 'drip': 0.92}

        base_etc = crop_etc.get(crop, {}).get(growth_stage, 5.0)
        adj_etc = base_etc * temp_factor.get(temperature, 1.0)
        effective_rain = rainfall_mm * 0.75
        net_etc = max(0, adj_etc - (effective_rain / 30))
        weekly_need_mm = net_etc * 7
        litres_per_acre_week = weekly_need_mm * 4046.86
        actual_litres = litres_per_acre_week / efficiency.get(irrigation_method, 0.7)
        total_litres = actual_litres * area_acres
        whc = soil_whc.get(soil, 140)
        depletion = whc * 0.5
        irr_frequency = max(1, int(depletion / net_etc)) if net_etc > 0 else 7
        flood_litres = (weekly_need_mm * 4046.86 / 0.60) * area_acres
        savings_pct = max(0, int((1 - (total_litres / flood_litres)) * 100)) if irrigation_method != 'flood' and flood_litres > 0 else 0

        result = {
            'crop': crop.replace('_', ' ').title(),
            'area_acres': area_acres,
            'daily_etc_mm': round(adj_etc, 1),
            'weekly_need_mm': round(weekly_need_mm, 1),
            'litres_per_acre_week': round(actual_litres),
            'total_litres_week': round(total_litres),
            'total_cubic_meters': round(total_litres / 1000, 1),
            'irr_frequency_days': irr_frequency,
            'savings_pct': savings_pct,
            'irrigation_method': irrigation_method.replace('_', ' ').title(),
            'growth_stage': growth_stage.replace('_', ' ').title(),
            'soil': soil.replace('_', ' ').title(),
        }

    return render(request, 'farming/irrigation.html', {'result': result})


def govt_schemes(request):
    schemes = [
        {
            'id': 'pmkisan', 'name': 'PM-KISAN', 'icon': '💰', 'color': '#2d6a4f',
            'full_name': 'Pradhan Mantri Kisan Samman Nidhi',
            'tagline': 'Direct Income Support for Farmers',
            'benefit': 'Rs.6,000 per year paid in 3 installments of Rs.2,000 each directly into bank account',
            'eligibility': 'All small and marginal farmers with cultivable land. Excludes income tax payers, constitutional post holders, and retired government employees.',
            'documents': ['Aadhaar Card', 'Bank Account linked to Aadhaar', 'Land Records (Khasra/Khatauni)', 'Mobile Number'],
            'how_to_apply': 'Visit pmkisan.gov.in or nearest Common Service Centre (CSC). Register with Aadhaar and land documents. District Agriculture Officer can also register.',
            'helpline': '155261 / 011-23381092',
            'portal': 'https://pmkisan.gov.in',
            'status': 'Active',
            'beneficiaries': '11 crore+ farmers',
            'highlight': 'Rs.2.81 lakh crore disbursed till 2024',
        },
        {
            'id': 'pmfby', 'name': 'PM Fasal Bima', 'icon': 'shield', 'color': '#c47a1a',
            'full_name': 'Pradhan Mantri Fasal Bima Yojana',
            'tagline': 'Crop Insurance at Lowest Premium in World',
            'benefit': 'Full crop loss compensation. Premium only 2% for Kharif, 1.5% for Rabi, 5% for commercial crops. Government pays the rest.',
            'eligibility': 'All farmers growing notified crops. Loanee farmers automatically enrolled. Non-loanee farmers can voluntarily join.',
            'documents': ['Aadhaar Card', 'Bank Account', 'Land Records or Lease Agreement', 'Sowing Certificate from Patwari', 'Crop details'],
            'how_to_apply': 'Contact your bank (loanee farmers) or nearest CSC, KVK, or Co-operative. Online at pmfby.gov.in. Enroll before last date for each season.',
            'helpline': '14447 / 1800-180-1551',
            'portal': 'https://pmfby.gov.in',
            'status': 'Active',
            'beneficiaries': '5.5 crore farmers per season',
            'highlight': 'Rs.1.55 lakh crore claims paid till 2024',
        },
        {
            'id': 'kcc', 'name': 'Kisan Credit Card', 'icon': 'card', 'color': '#1a4a8a',
            'full_name': 'Kisan Credit Card Scheme',
            'tagline': 'Affordable Farm Credit at 4% Interest',
            'benefit': 'Revolving credit up to Rs.3 lakh at 4% per annum. Higher amounts at 7%. Covers crop, post-harvest, allied activities, and consumption needs.',
            'eligibility': 'All farmers, sharecroppers, tenant farmers, and self-help groups. No upper limit on credit amount.',
            'documents': ['Aadhaar Card', 'PAN Card', 'Land Records', 'Passport size photo', 'Bank account'],
            'how_to_apply': 'Apply at any nationalized bank, cooperative bank, or RRB. Simple one-page application. NABARD oversees the scheme.',
            'helpline': 'Contact nearest bank branch. NABARD: 022-26530470',
            'portal': 'https://www.nabard.org',
            'status': 'Active',
            'beneficiaries': '7.4 crore KCC holders',
            'highlight': 'Rs.8.85 lakh crore outstanding credit',
        },
        {
            'id': 'enam', 'name': 'e-NAM', 'icon': 'market', 'color': '#6a2d8a',
            'full_name': 'National Agriculture Market (e-NAM)',
            'tagline': 'Sell Nationwide — Get Best Price',
            'benefit': 'Access to pan-India buyers. Transparent online bidding. Direct payment to bank within 24 hours. No middlemen required.',
            'eligibility': 'All farmers registered at their State Agriculture Market Board (APMC). Free registration.',
            'documents': ['Aadhaar Card', 'Bank Account', 'APMC farmer registration', 'Mobile Number'],
            'how_to_apply': 'Register at enam.gov.in or local APMC office. Free mobile app available on Android and iOS.',
            'helpline': '1800-270-0224 (Toll Free)',
            'portal': 'https://enam.gov.in',
            'status': 'Active',
            'beneficiaries': '1.74 crore farmers registered',
            'highlight': 'Rs.2.73 lakh crore trade volume',
        },
        {
            'id': 'pmksy', 'name': 'PM Krishi Sinchayee', 'icon': 'water', 'color': '#1a6a7a',
            'full_name': 'Pradhan Mantri Krishi Sinchayee Yojana',
            'tagline': 'Har Khet Ko Pani — 90% Subsidy on Drip Irrigation',
            'benefit': 'Up to 90% subsidy on drip/sprinkler for SC/ST/small farmers. 55% for others. Covers equipment, installation, and maintenance.',
            'eligibility': 'All farmers owning or leasing agricultural land. Small and marginal farmers get maximum benefit.',
            'documents': ['Aadhaar Card', 'Land Records or Lease Agreement', 'Bank Account', 'Crop and water source details'],
            'how_to_apply': 'Apply at District Agriculture Office or Horticulture Department. Block Agriculture Officer provides guidance.',
            'helpline': 'Visit State Agriculture Department Portal',
            'portal': 'https://pmksy.gov.in',
            'status': 'Active',
            'beneficiaries': '70 lakh farmers with micro-irrigation',
            'highlight': 'Rs.94,000 crore allocated',
        },
        {
            'id': 'pkvy', 'name': 'PKVY — Organic Farming', 'icon': 'leaf', 'color': '#2d7a3a',
            'full_name': 'Paramparagat Krishi Vikas Yojana',
            'tagline': 'Rs.50,000/ha Support for Going Organic',
            'benefit': 'Rs.50,000 per ha over 3 years. Rs.31,000 for inputs, Rs.8,800 for certification, Rs.3,600 for labelling and packaging.',
            'eligibility': 'Clusters of 50+ farmers with 50+ acres contiguous land willing to adopt certified organic farming.',
            'documents': ['Aadhaar Card', 'Land Records', 'Group formation certificate', 'Soil test report'],
            'how_to_apply': 'Form a farmer cluster. Apply through State Agriculture Department or District Agriculture Office.',
            'helpline': 'State Agriculture Department helpline',
            'portal': 'https://pgsindia-ncof.gov.in',
            'status': 'Active',
            'beneficiaries': '6.5 lakh farmers in clusters',
            'highlight': 'Rs.2,200 crore disbursed',
        },
        {
            'id': 'soil', 'name': 'Soil Health Card', 'icon': 'soil', 'color': '#6a3a1a',
            'full_name': 'Soil Health Card Scheme',
            'tagline': 'Free Soil Test — Save 10-15% on Fertilizer',
            'benefit': 'Free soil health card with nutrient status and fertilizer recommendations. Tested every 2 years. Prevents wasteful over-application.',
            'eligibility': 'ALL farmers. No income or land restriction. Completely free of cost.',
            'documents': ['Aadhaar Card', 'Mobile Number', 'Land details (village/survey number)'],
            'how_to_apply': 'Contact Block Agriculture Officer or nearest KVK. Soil sample collected from your field. Card issued in 6 weeks.',
            'helpline': '1800-180-1551 (Toll Free)',
            'portal': 'https://soilhealth.dac.gov.in',
            'status': 'Active',
            'beneficiaries': '23 crore cards issued',
            'highlight': 'Completely free service for all farmers',
        },
        {
            'id': 'rkvy', 'name': 'RKVY', 'icon': 'build', 'color': '#5a1a7a',
            'full_name': 'Rashtriya Krishi Vikas Yojana',
            'tagline': 'Grants for Agri Infrastructure',
            'benefit': 'Grants for cold storage, warehousing, farm roads, irrigation, post-harvest units. Up to Rs.3 crore for individual projects.',
            'eligibility': 'FPOs, agri-entrepreneurs, cooperatives, state governments, and NGOs working in agriculture.',
            'documents': ['Project proposal', 'Land records', 'Bank account', 'Business plan', 'Technical feasibility report'],
            'how_to_apply': 'Submit project to State Agriculture Department or State ATMA. Reviewed by State Level Sanctioning Committee.',
            'helpline': 'Contact District Agriculture Office',
            'portal': 'https://rkvy.nic.in',
            'status': 'Active',
            'beneficiaries': 'State-level implementation',
            'highlight': 'Rs.1.07 lakh crore since 2007',
        },
    ]
    return render(request, 'farming/govt_schemes.html', {'schemes': schemes})


# ─── COMMUNITY VIEWS ─────────────────────────────────────────────────────────
from .models import CommunityPost

def community(request):
    category_filter = request.GET.get('category', '')
    crop_filter = request.GET.get('crop', '')
    state_filter = request.GET.get('state', '')

    posts = CommunityPost.objects.filter(is_approved=True)
    if category_filter:
        posts = posts.filter(category=category_filter)
    if crop_filter:
        posts = posts.filter(crop__icontains=crop_filter)
    if state_filter:
        posts = posts.filter(state__icontains=state_filter)

    # Seed some demo posts if empty
    if not CommunityPost.objects.exists():
        demo_posts = [
            {'name': 'Ramesh Patel', 'state': 'Gujarat', 'crop': 'Groundnut', 'category': 'success',
             'content': 'This year I applied gypsum at flowering stage as suggested in crop tips. My yield increased by 35%! Also used drip irrigation for first time with 80% subsidy from govt. Very happy. Sharing so others can benefit too.',
             'photo_description': 'Before/after photo of my groundnut field — left side without gypsum, right side with gypsum. Huge difference visible.', 'likes': 47},
            {'name': 'Sunita Devi', 'state': 'Uttar Pradesh', 'crop': 'Wheat', 'category': 'warning',
             'content': 'WARNING for wheat farmers in UP: Aphid attack is very heavy this year in Aligarh district. I lost 30% yield last year by not spraying on time. This year spray imidacloprid when you see more than 25-30 aphids per tiller. Do not wait. Act fast.',
             'photo_description': '', 'likes': 89},
            {'name': 'Krishnamurthy', 'state': 'Karnataka', 'crop': 'Tomato', 'category': 'question',
             'content': 'My tomato leaves are curling upward and turning yellow from edges. The plants are 45 days old. I use drip irrigation. Soil is red laterite. Applied 80:60:60 NPK. Is this a virus problem or nutrient deficiency? Please help with advice.',
             'photo_description': 'Photo shows 3 affected plants with curled yellow leaves. Plants nearby look normal.', 'likes': 12},
            {'name': 'Gurpreet Singh', 'state': 'Punjab', 'crop': 'Paddy', 'category': 'tip',
             'content': 'Pro tip for paddy farmers: Use direct seeded rice (DSR) method instead of transplanting. I saved 25 days of nursery work, ₹3,000 per acre on labour, and 30% water. My yield was same as transplanted paddy. Try it with DSR herbicide kit from agriculture department.',
             'photo_description': 'My DSR paddy field at 60 days — thick uniform stand, no transplanting gaps.', 'likes': 134},
            {'name': 'Meena Kumari', 'state': 'Rajasthan', 'crop': 'Mustard', 'category': 'question',
             'content': 'My mustard crop is 50 days old. White powdery coating is appearing on leaves. Last 3 days have been foggy and cold. Should I spray sulfur? What rate? Will rain wash it? Also is this spreading problem?',
             'photo_description': '', 'likes': 8},
            {'name': 'Babu Rao', 'state': 'Andhra Pradesh', 'crop': 'Chilli', 'category': 'success',
             'content': 'I registered on e-NAM portal last month. Sold my chilli online for ₹8,400 per qtl vs ₹7,100 I was getting at local mandi. That is ₹1,300 per qtl extra! On my 10 qtl harvest that is ₹13,000 extra income. Registration is free. Do it today.',
             'photo_description': 'Screenshot of e-NAM payment confirmation for ₹84,000 direct to my account.', 'likes': 201},
            {'name': 'Suresh Nair', 'state': 'Kerala', 'crop': 'Coconut', 'category': 'tip',
             'content': 'Kerala coconut farmers: Install red palm weevil pheromone traps urgently. This pest destroyed 40% of palms in my neighbor village without any warning. Install 1 trap per 10 trees. Check weekly. If you catch many weevils in trap — inject monocrotophos into leaf axils immediately.',
             'photo_description': 'Photo of pheromone trap installed in my garden — catches 5-10 weevils per week.', 'likes': 63},
        ]
        for p in demo_posts:
            CommunityPost.objects.create(**p)
        posts = CommunityPost.objects.filter(is_approved=True)

    indian_states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
        'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
        'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
        'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
    ]

        # Attach comments to each post
    from .models import PostComment
    for post in posts:
        post.top_comments = post.comments.filter(parent=None).prefetch_related('replies')[:50]

    return render(request, 'farming/community.html', {
        'posts': posts,
        'category_filter': category_filter,
        'crop_filter': crop_filter,
        'state_filter': state_filter,
        'total_posts': CommunityPost.objects.filter(is_approved=True).count(),
        'indian_states': indian_states,
        'categories': CommunityPost.CATEGORY_CHOICES,
    })


def community_post(request):
    if request.method == 'POST':
        name = (request.POST.get('name') or 'Anonymous Farmer').strip() or 'Anonymous Farmer'
        state = (request.POST.get('state') or '').strip()
        crop = (request.POST.get('crop') or '').strip()
        category = (request.POST.get('category') or 'question').strip()
        post_content = (request.POST.get('content') or '').strip()
        photo_description = (request.POST.get('photo_description') or '').strip()
        photo_file = request.FILES.get('photo')

        if len(post_content) < 20:
            messages.error(request, '❌ Please write at least 20 characters in your post.')
            return redirect('community')
        try:
            post = CommunityPost.objects.create(
                name=name, state=state, crop=crop,
                category=category, content=post_content,
                photo_description=photo_description,
            )
            if photo_file:
                post.photo = photo_file
                post.save()
            messages.success(request, '✅ Your post has been shared with the farming community!')
        except Exception as ex:
            messages.error(request, f'❌ Could not save post: {ex}')
    return redirect('community')


def community_like(request, pk):
    from django.http import JsonResponse
    post = get_object_or_404(CommunityPost, pk=pk)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

# ─────────────────────────────────────────────
#  NEW VIEWS  — Chat, SMS, Registration, Expert Panel, Live Mandi
# ─────────────────────────────────────────────
from datetime import datetime



def community_comment(request, post_id):
    """Add a comment or reply to a community post"""
    from .models import CommunityPost, PostComment
    if request.method != 'POST':
        return redirect('community')
    try:
        post = CommunityPost.objects.get(pk=post_id, is_approved=True)
    except CommunityPost.DoesNotExist:
        return redirect('community')

    name    = (request.POST.get('name') or 'Anonymous Farmer').strip()[:200]
    content = (request.POST.get('content') or '').strip()
    state   = (request.POST.get('state') or '').strip()[:100]
    parent_id = request.POST.get('parent_id')
    expert_code = (request.POST.get('expert_code') or '').strip()

    # Verify expert: code stored in settings / simple shared secret
    EXPERT_CODE = 'SMARTFARM2024'
    is_expert = (expert_code == EXPERT_CODE)

    if not content:
        messages.error(request, 'Comment cannot be empty.')
        return redirect(f'/community/?post={post_id}#post-{post_id}')

    parent = None
    if parent_id:
        try:
            parent = PostComment.objects.get(pk=int(parent_id), post=post)
        except (PostComment.DoesNotExist, ValueError):
            pass

    PostComment.objects.create(
        post=post, name=name, content=content,
        state=state, is_expert=is_expert, parent=parent
    )
    return redirect(request.META.get('HTTP_REFERER', '/community/') + f'#post-{post_id}')


def community_comment_like(request, comment_id):
    """Like a comment"""
    from .models import PostComment
    if request.method == 'POST':
        PostComment.objects.filter(pk=comment_id).update(likes=models.F('likes') + 1)
    return JsonResponse({'ok': True})

def farmer_register(request):
    """Farmers register their phone for SMS alerts"""
    from .models import FarmerProfile
    success = False
    error = ''
    if request.method == 'POST':
        name  = (request.POST.get('name') or '').strip()
        phone = (request.POST.get('phone') or '').strip()
        state = (request.POST.get('state') or '').strip()
        crop  = (request.POST.get('crop') or '').strip()
        village = (request.POST.get('village') or '').strip()
        phone_digits = ''.join(c for c in phone if c.isdigit())
        if not name:
            error = 'Name is required.'
        elif len(phone_digits) < 10:
            error = 'Please enter a valid 10-digit mobile number.'
        else:
            try:
                FarmerProfile.objects.get_or_create(
                    phone=phone_digits[-10:],
                    defaults=dict(name=name, state=state, crop=crop, village=village)
                )
                success = True
            except Exception as ex:
                error = f'Registration failed: {ex}'
    return render(request, 'farming/farmer_register.html', {
        'success': success, 'error': error,
        'states': ['Punjab','Haryana','Uttar Pradesh','Madhya Pradesh','Rajasthan',
                   'Maharashtra','Gujarat','Karnataka','Andhra Pradesh','Telangana',
                   'Tamil Nadu','West Bengal','Odisha','Bihar','Jharkhand','Chhattisgarh'],
    })


@login_required
def chat_list(request):
    """List of all chat rooms — for expert and farmer access"""
    from .models import ChatRoom, ChatMessage
    rooms = ChatRoom.objects.all()
    for r in rooms:
        r.last_msg = r.messages.last()
        r.unread = r.messages.count()
    return render(request, 'farming/chat_list.html', {'rooms': rooms})


@login_required
def chat_new(request):
    """Farmer starts a new chat. Expert joins with secret code."""
    from .models import ChatRoom, ChatMessage
    error = ''
    if request.method == 'POST':
        mode = request.POST.get('mode', 'farmer')

        if mode == 'expert':
            # Expert login
            code = (request.POST.get('expert_code') or '').strip()
            if code == 'SMARTFARM2024':
                request.session['is_expert'] = True
                request.session['expert_name'] = (request.POST.get('expert_name') or 'Agricultural Expert').strip()
                return redirect('chat_list')
            else:
                error = 'Invalid expert code. Please contact admin.'
        else:
            # Farmer starts new chat
            name      = (request.POST.get('name') or 'Anonymous Farmer').strip()
            phone     = (request.POST.get('phone') or '').strip()
            first_msg = (request.POST.get('message') or '').strip()
            if len(first_msg) < 5:
                error = 'Please describe your problem (at least 5 characters).'
            else:
                room = ChatRoom.objects.create(farmer_name=name, farmer_phone=phone)
                ChatMessage.objects.create(
                    room=room, sender='farmer', sender_name=name, message=first_msg
                )
                # Auto-ack
                ChatMessage.objects.create(
                    room=room, sender='expert', sender_name='Agricultural Expert',
                    message=f'Hello {name}! 🙏 Your message has been received. Our agricultural expert will respond shortly. Please provide more details if you have them.'
                )
                request.session['chat_farmer_name'] = name
                request.session['chat_room_id'] = room.id
                request.session['is_expert'] = False
                return redirect('chat_room', room_id=room.id)

    is_expert_session = request.session.get('is_expert', False)
    return render(request, 'farming/chat_new.html', {
        'error': error,
        'is_expert_session': is_expert_session,
    })

@login_required
def chat_room(request, room_id):
    """Chat room — farmer and expert, session-authenticated"""
    from .models import ChatRoom, ChatMessage
    try:
        room = ChatRoom.objects.get(pk=room_id)
    except ChatRoom.DoesNotExist:
        messages.error(request, 'Chat session not found.')
        return redirect('chat_new')

    is_expert = request.session.get('is_expert', False)
    # Allow farmer who owns this room
    owns_as_farmer = (request.session.get('chat_room_id') == room_id)

    if not is_expert and not owns_as_farmer:
        # Give them a view-only with prompt to identify
        request.session['chat_room_id'] = room_id
        request.session['chat_farmer_name'] = room.farmer_name
        request.session['is_expert'] = False
        owns_as_farmer = True

    sender_name = (request.session.get('expert_name', 'Agricultural Expert')
                   if is_expert else
                   request.session.get('chat_farmer_name', room.farmer_name))
    sender_role = 'expert' if is_expert else 'farmer'

    msgs = room.messages.all()
    return render(request, 'farming/chat_room.html', {
        'room': room,
        'msgs': msgs,
        'sender_name': sender_name,
        'sender_role': sender_role,
        'is_expert': is_expert,
    })

@login_required
def chat_send(request, room_id):
    """POST: send a chat message (AJAX)"""
    from .models import ChatRoom, ChatMessage
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        room = ChatRoom.objects.get(pk=room_id)
    except ChatRoom.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)
    try:
        data = json.loads(request.body)
    except Exception:
        data = {}
    msg_text = (data.get('message') or request.POST.get('message') or '').strip()
    sender   = data.get('sender', 'farmer')
    sender_name = data.get('sender_name', room.farmer_name)
    if not msg_text:
        return JsonResponse({'error': 'Empty message'}, status=400)
    msg = ChatMessage.objects.create(
        room=room, sender=sender,
        sender_name=sender_name, message=msg_text
    )
    return JsonResponse({
        'id': msg.id,
        'sender': msg.sender,
        'sender_name': msg.sender_name,
        'message': msg.message,
        'time': msg.created_at.strftime('%I:%M %p'),
    })


def chat_messages_api(request, room_id):
    """GET: poll for new messages since ?after=<id>"""
    from .models import ChatRoom, ChatMessage
    after_id = int(request.GET.get('after', 0))
    try:
        room = ChatRoom.objects.get(pk=room_id)
    except ChatRoom.DoesNotExist:
        return JsonResponse({'messages': []})
    msgs = room.messages.filter(id__gt=after_id)
    return JsonResponse({'messages': [
        {'id': m.id, 'sender': m.sender, 'sender_name': m.sender_name,
         'message': m.message, 'time': m.created_at.strftime('%I:%M %p')}
        for m in msgs
    ]})


@expert_required
def chat_resolve(request, room_id):
    from .models import ChatRoom
    if request.method == 'POST':
        ChatRoom.objects.filter(pk=room_id).update(is_resolved=True)
    return redirect('chat_list')


@expert_required
def expert_panel(request):
    """Expert/Admin dashboard — view queries, chats, send SMS"""
    from .models import FarmerQuery, ChatRoom, FarmerProfile, SMSAlert
    queries  = FarmerQuery.objects.filter(answered=False)[:20]
    answered = FarmerQuery.objects.filter(answered=True)[:10]
    rooms    = ChatRoom.objects.filter(is_resolved=False)[:20]
    farmers  = FarmerProfile.objects.filter(is_active=True)
    alerts   = SMSAlert.objects.all()[:10]
    states   = farmers.values_list('state', flat=True).distinct()
    sms_key_configured = bool(getattr(settings, 'FAST2SMS_API_KEY', ''))
    return render(request, 'farming/expert_panel.html', {
        'queries': queries, 'answered': answered,
        'rooms': rooms, 'farmers': farmers,
        'alerts': alerts, 'states': list(states),
        'farmer_count': farmers.count(),
        'sms_key_configured': sms_key_configured,
        'expert_name': request.user.get_full_name() or request.user.username,
    })


@expert_required
def answer_query(request, pk):
    """Expert answers a farmer query"""
    from .models import FarmerQuery
    if request.method == 'POST':
        answer = (request.POST.get('answer') or '').strip()
        if answer:
            FarmerQuery.objects.filter(pk=pk).update(answered=True, answer=answer)
            messages.success(request, '✅ Answer saved.')
    return redirect('expert_panel')


@expert_required
def _clean_phone(raw):
    """Normalise any Indian phone number to 10-digit string for Fast2SMS."""
    import re
    digits = re.sub(r'\D', '', str(raw))   # strip everything non-numeric
    if digits.startswith('91') and len(digits) == 12:
        digits = digits[2:]                 # +91XXXXXXXXXX → XXXXXXXXXX
    if digits.startswith('0') and len(digits) == 11:
        digits = digits[1:]                 # 0XXXXXXXXXX  → XXXXXXXXXX
    if len(digits) == 10:
        return digits
    return None  # invalid — skip


def _fast2sms_send(api_key, phone_list, message):
    """
    Send SMS via Fast2SMS Quick SMS route (v3).
    Returns (True, '') on success or (False, error_string) on failure.

    Fast2SMS Quick SMS API:
      POST https://www.fast2sms.com/dev/bulkV2
      Headers: authorization: <api_key>
      JSON body: { "route": "q", "numbers": "...", "message": "...", "flash": 0 }
    """
    import json as jmod

    # Clean + deduplicate phone numbers
    clean = []
    for p in phone_list:
        n = _clean_phone(p)
        if n and n not in clean:
            clean.append(n)

    if not clean:
        return False, 'No valid 10-digit Indian mobile numbers found'

    # Fast2SMS accepts max 10 numbers per call on free tier
    # Split into batches of 10
    errors = []
    any_sent = False
    for i in range(0, len(clean), 10):
        batch = clean[i:i+10]
        body = jmod.dumps({
            'route': 'q',
            'numbers': ','.join(batch),
            'message': message[:160],
            'flash': 0,
            'unicode': 0,
        }).encode('utf-8')

        req = urllib.request.Request(
            'https://www.fast2sms.com/dev/bulkV2',
            data=body,
            headers={
                'authorization': api_key,
                'Content-Type': 'application/json',
                'Cache-Control': 'no-cache',
            },
            method='POST',
        )
        try:
            resp = urllib.request.urlopen(req, timeout=15)
            result = jmod.loads(resp.read().decode('utf-8'))
            if result.get('return') is True:
                any_sent = True
            else:
                err_msg = result.get('message', [])
                if isinstance(err_msg, list):
                    err_msg = '; '.join(err_msg)
                errors.append(str(err_msg))
        except urllib.error.HTTPError as e:
            body_err = e.read().decode('utf-8', errors='replace')
            errors.append(f'HTTP {e.code}: {body_err[:200]}')
        except Exception as ex:
            errors.append(str(ex))

    if any_sent:
        return True, ''
    return False, ' | '.join(errors) if errors else 'Unknown Fast2SMS error'


@expert_required
def send_sms_alert(request):
    """
    Expert sends SMS alert to registered farmers via Fast2SMS.
    API key lives in settings.py — never exposed in the frontend.

    HOW THE EXPERT USES THIS:
    1. Go to /expert-panel/
    2. Fill in Alert Title + Message (max 160 chars)
    3. Choose: All Farmers / specific State / specific Crop / custom numbers
    4. Click Send — SMS fires immediately via Fast2SMS
    """
    from .models import FarmerProfile, SMSAlert
    from django.utils import timezone

    if request.method != 'POST':
        return redirect('expert_panel')

    title       = (request.POST.get('title')       or '').strip()
    msg_txt     = (request.POST.get('message')     or '').strip()
    target      = (request.POST.get('target')      or 'all').strip()
    custom_nums = (request.POST.get('custom_numbers') or '').strip()

    if not title or not msg_txt:
        messages.error(request, ' Title and message are required.')
        return redirect('expert_panel')

    # API key from settings — never from form input
    api_key = getattr(settings, 'FAST2SMS_API_KEY', '').strip()

    # Build phone list
    if custom_nums:
        # Expert entered specific numbers manually (comma/newline separated)
        raw_list = [x.strip() for x in custom_nums.replace('\n', ',').split(',') if x.strip()]
        phones = raw_list
        target = f'custom:{len(raw_list)} numbers'
    else:
        qs = FarmerProfile.objects.filter(is_active=True)
        if target.startswith('state:'):
            qs = qs.filter(state=target.split(':', 1)[1])
        elif target.startswith('crop:'):
            qs = qs.filter(crop__icontains=target.split(':', 1)[1])
        phones = list(qs.values_list('phone', flat=True))

    sent_by = request.user.get_full_name() or request.user.username
    full_msg = f"SmartFarm Alert: {title}. {msg_txt}"

    # Save alert record
    alert = SMSAlert.objects.create(
        title=title, message=msg_txt,
        sent_by=sent_by, target=target,
        recipients_count=len(phones), status='pending'
    )

    if not phones:
        alert.status = 'failed'
        alert.save()
        messages.warning(request, f'⚠️ No farmers found for target: {target}. Register farmers first via /register/')
        return redirect('expert_panel')

    if not api_key:
        alert.status = 'failed'
        alert.save()
        messages.error(request, '❌ FAST2SMS_API_KEY not set in settings.py. Cannot send SMS.')
        return redirect('expert_panel')

    # Send the SMS
    sms_sent, sms_error = _fast2sms_send(api_key, phones, full_msg)

    if sms_sent:
        alert.status = 'sent'
        alert.sent_at = timezone.now()
        alert.save()
        messages.success(request, f'✅ SMS sent successfully to {len(phones)} farmer(s)!')
    else:
        alert.status = 'failed'
        alert.save()
        messages.error(request, f'❌ SMS failed: {sms_error}')

    return redirect('expert_panel')


def mandi_prices_api(request):
    """Proxy live Agmarknet data from data.gov.in (free government API)"""
    commodity = request.GET.get('commodity', 'Wheat')
    state     = request.GET.get('state', '')
    API_KEY   = '579b464db66ec23bdd000001c047504291654ce964bc8dddcc5fff9d'  # data.gov.in open API key
    limit     = 50

    url = (
        f'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070'
        f'?api-key={API_KEY}&format=json&limit={limit}'
        f'&filters[commodity]={urllib.parse.quote(commodity)}'
    )
    if state:
        url += f'&filters[state]={urllib.parse.quote(state)}'

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'SmartFarm/1.0'})
        resp = urllib.request.urlopen(req, timeout=8)
        data = json.loads(resp.read())
        records = data.get('records', [])
        result = [{
            'mandi':     r.get('market', r.get('apmc', 'Unknown')),
            'state':     r.get('state', ''),
            'district':  r.get('district', ''),
            'commodity': r.get('commodity', commodity),
            'variety':   r.get('variety', ''),
            'price':     float(r.get('modal_price', r.get('modalPrice', 0)) or 0),
            'min':       float(r.get('min_price',   r.get('minPrice', 0))   or 0),
            'max':       float(r.get('max_price',   r.get('maxPrice', 0))   or 0),
            'date':      r.get('arrival_date', r.get('date', '')),
        } for r in records if r.get('modal_price') or r.get('modalPrice')]
        return JsonResponse({'status': 'live', 'data': result, 'count': len(result)})
    except Exception as ex:
        return JsonResponse({'status': 'error', 'error': str(ex), 'data': []})
