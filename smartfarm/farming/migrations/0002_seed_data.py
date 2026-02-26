from django.db import migrations


def seed_data(apps, schema_editor):
    Threat = apps.get_model('farming', 'Threat')
    CropTip = apps.get_model('farming', 'CropTip')

    threats_data = [

        # =====================================================================
        # WILDLIFE (20 entries — Pan India)
        # =====================================================================
        {
            'name': 'Wild Boar', 'category': 'wildlife', 'icon': '🐗',
            'description': 'Wild boars cause severe damage by uprooting crops and trampling fields across nearly every state in India. They dig up roots, eat tubers, and trample standing crops. Most active at night, they can devastate an entire field within hours. Present in UP, MP, Jharkhand, Odisha, Karnataka, Kerala, and most forested states.',
            'affected_crops': 'Wheat, Rice, Sugarcane, Maize, Potato, Groundnut, Cassava, Sweet Potato',
            'prevention_methods': '1. Install electric fencing (solar-powered) around field boundaries\n2. Dig V-shaped trenches (3 ft wide, 3 ft deep) along field borders\n3. Set up motion-activated alarm lights at night\n4. Spray chili-garlic repellent solution on crop borders\n5. Community night-watch programs with searchlights\n6. Plant thorny hedges (babool, keekar) as natural barriers',
            'treatment': 'Contact local Forest Department for trap-and-relocate operations. Apply chili-garlic paste on field edges as repellent. Coordinate with neighboring farmers for community-level control.',
            'season': 'Year-round; most active October–March', 'severity': 'critical',
        },
        {
            'name': 'Nilgai (Blue Bull)', 'category': 'wildlife', 'icon': '🦌',
            'description': 'Nilgai are the largest Asian antelopes and a major crop pest in North and Central India (UP, Bihar, Rajasthan, Haryana, MP). A herd can consume or trample an entire wheat or mustard field overnight. They are protected under the Wildlife Protection Act.',
            'affected_crops': 'Wheat, Mustard, Barley, Vegetables, Sugarcane, Peas, Lentils',
            'prevention_methods': '1. Erect tall fencing (minimum 6 to 8 feet) with barbed wire top\n2. Hang human hair bundles or lion/tiger dung sachets around borders\n3. Use scarecrows with shiny reflective materials and wind-chimes\n4. Apply bitter neem oil spray on crop foliage\n5. Community watch patrols with drums and lights\n6. Plant unpalatable crops (lemongrass, mint) on field boundaries',
            'treatment': 'Apply neem-based repellents on crop borders. Some states allow culling permits — contact District Collector. Coordinate community Nilgai drives during crop season.',
            'season': 'Rabi season (October–March)', 'severity': 'critical',
        },
        {
            'name': 'Indian Elephant', 'category': 'wildlife', 'icon': '🐘',
            'description': 'Elephants raid crops in forest-fringe areas of Assam, West Bengal, Odisha, Kerala, Tamil Nadu, Karnataka, and Jharkhand. A single herd can destroy hectares of crops in one night. One of the most destructive wildlife threats in India causing both crop loss and human casualties.',
            'affected_crops': 'Rice, Sugarcane, Banana, Maize, Jackfruit, Mango, Coconut, Finger Millet',
            'prevention_methods': '1. Install bee-fence barriers (elephants fear bees) — proven highly effective in South India\n2. Use chili-smoke fires and chili-dung briquettes along borders\n3. Dig wide, deep trenches (at least 1.5 m deep, 2 m wide)\n4. Install solar-powered electric fences certified for elephant deterrence\n5. Set up early-warning systems using trip-wires and mobile alerts\n6. Form community Rapid Response Teams with drums and torches',
            'treatment': 'Immediately contact local Forest Department and Wildlife Division. Never confront elephants directly. Apply for crop loss compensation under state government schemes. Document losses with photographs and panchnama.',
            'season': 'Year-round; peaks June–November (Kharif crop season)', 'severity': 'critical',
        },
        {
            'name': 'Monkeys (Rhesus and Bonnet Macaque)', 'category': 'wildlife', 'icon': '🐒',
            'description': 'Monkeys are a serious threat to orchards, vegetable gardens, and grain crops across India. They steal ripe fruits, break branches, and contaminate produce. Particularly severe in Himachal Pradesh, Uttarakhand, UP, Maharashtra, and Tamil Nadu.',
            'affected_crops': 'Mango, Guava, Banana, Apple, Vegetables, Maize, Sunflower, Groundnut',
            'prevention_methods': '1. Employ langur (hanuman monkey) deterrence — natural predator behavior\n2. Install stainless steel wire mesh nets over orchards\n3. Use rubber snake or owl effigies placed at entry points\n4. Stretch taut wire lines above orchards to block aerial movement\n5. Scare with loud crackers or recorded distress calls\n6. Smear bitter neem paste on tree trunks',
            'treatment': 'Motion-sensor water sprinklers, community monkey brigades during harvest. Report to Animal Husbandry Department for sterilization programs where available.',
            'season': 'Year-round; worst during fruit ripening season', 'severity': 'high',
        },
        {
            'name': 'Spotted Deer (Chital)', 'category': 'wildlife', 'icon': '🦌',
            'description': 'Spotted deer graze on young crop seedlings and tender shoots in fields adjoining forests and protected areas. Common in forest-fringe states including MP, Maharashtra, Odisha, AP, Telangana, and Karnataka.',
            'affected_crops': 'Rice, Wheat, Vegetables, Groundnut, Soybean, Pulses, Sugarcane',
            'prevention_methods': '1. Install 5 to 6 ft fencing with barbed wire top layer\n2. Place thorny branches on field boundaries\n3. Use motion-sensor lights at night\n4. Apply predator urine or dung near field borders\n5. Community patrol at dawn and dusk when deer are most active',
            'treatment': 'Contact Forest Department for population management in high-density areas. Apply for damage compensation under state wildlife compensation schemes.',
            'season': 'Year-round; peak during early crop growth stages', 'severity': 'medium',
        },
        {
            'name': 'Wild Gaur (Indian Bison)', 'category': 'wildlife', 'icon': '🐂',
            'description': 'The world\'s largest bovine, wild gaur raid crops in forest fringe areas of South India, Northeast India, and Central India. A single animal can destroy a large area by trampling. Common in coffee and tea estates of South India.',
            'affected_crops': 'Rice, Sugarcane, Maize, Banana, Coconut, Coffee, Cardamom, Tea',
            'prevention_methods': '1. Deep and wide trench barriers around fields\n2. Solar electric fencing rated for large animals (5–7 joule energizer)\n3. Bright floodlights triggered by motion sensors\n4. Fire-lines (controlled burning) as deterrent at night\n5. Loud alarm systems connected to motion triggers',
            'treatment': 'Contact State Forest Department immediately. Do not attempt to scare large animals alone. File compensation claims with revenue documentation and photographs.',
            'season': 'Year-round; peaks during dry season when forest food is scarce', 'severity': 'critical',
        },
        {
            'name': 'Porcupine (Indian Crested)', 'category': 'wildlife', 'icon': '🦔',
            'description': 'Porcupines dig up roots, tubers, bulbs, and root vegetables at night. Widespread across India and cause significant damage to root crops. Their burrows also destabilize field bunds and irrigation channels.',
            'affected_crops': 'Potato, Sweet Potato, Cassava, Onion, Carrot, Groundnut, Sugarcane roots',
            'prevention_methods': '1. Lay wire mesh just below soil surface around root crop beds\n2. Install buried concrete or metal sheet barriers 2 ft deep around field\n3. Set cage traps at burrow entrances\n4. Maintain clean field borders without shrub cover that provides hiding\n5. Smoke out burrows with sulfur sticks (away from crops)',
            'treatment': 'Cage trap and relocate with forest department permission. Fill and compact burrow entrances. Apply repellent granules near burrow sites.',
            'season': 'Year-round; most active at night during dry months', 'severity': 'medium',
        },
        {
            'name': 'Wild Rabbit and Indian Hare', 'category': 'wildlife', 'icon': '🐇',
            'description': 'Hares and rabbits are widespread in agricultural areas across India and cause damage by feeding on young seedlings, vegetable leaves, and tender shoots. Common in dryland farming areas of Rajasthan, Gujarat, and Central India.',
            'affected_crops': 'Vegetables, Wheat seedlings, Groundnut, Pulses, Carrots, Cabbage, Cauliflower',
            'prevention_methods': '1. Install fine mesh wire fencing (chicken wire) around vegetable plots\n2. Apply blood meal or predator urine around field edges\n3. Use cage traps along known runways\n4. Maintain clean field boundaries — remove brush piles\n5. Intercrop with strong-smelling herbs like garlic and onion',
            'treatment': 'Live cage traps. Community hunting drives with forest department permission. Protect seedling areas with physical barriers.',
            'season': 'Year-round; most damaging during seedling stage', 'severity': 'low',
        },
        {
            'name': 'Peafowl (Peacock) and Jungle Fowl', 'category': 'wildlife', 'icon': '🦚',
            'description': 'Peacocks and jungle fowl scratch the soil, consume seeds, young seedlings, and grain. Peacocks are protected by law in India and cannot be harmed. Particularly severe in Rajasthan, Gujarat, MP, Maharashtra, UP, and across peninsular India.',
            'affected_crops': 'Groundnut, Pulses, Sunflower, Maize, Sorghum, Vegetables, newly sown seeds',
            'prevention_methods': '1. Use bird-scare gas guns (automatic bangers) on timers\n2. Stretch shiny reflective tape in parallel lines over crop rows\n3. Place CDs or aluminum foil strips on strings above crops\n4. Set up automatic motion-triggered sound systems\n5. Cover newly sown fields with fine nets until germination',
            'treatment': 'Only non-lethal deterrents are legal for peacocks. Coordinate with Forest Department. Cover seeds after sowing to prevent feeding.',
            'season': 'Year-round; peaks at sowing and harvest time', 'severity': 'medium',
        },
        {
            'name': 'Jackals and Foxes', 'category': 'wildlife', 'icon': '🦊',
            'description': 'Jackals and foxes raid vegetable gardens, fruit orchards, and small livestock farms across India. They dig under fences and attack crops and stored produce. Common nuisance in peri-urban farming areas.',
            'affected_crops': 'Watermelon, Muskmelon, Grapes, Guava, Vegetables, Poultry',
            'prevention_methods': '1. Bury wire mesh fencing 1.5 ft below ground level to prevent digging\n2. Use motion-triggered alarm lights\n3. Install audio deterrent devices at field edges\n4. Eliminate hiding spots (tall grass, brush) near fields\n5. Guard dogs are highly effective deterrents',
            'treatment': 'Cage traps and relocation with Forest Department approval. Regular patrol during evening hours.',
            'season': 'Year-round; most active December–March (breeding season)', 'severity': 'low',
        },
        {
            'name': 'Birds (Parrots, Munias, and Sparrows)', 'category': 'wildlife', 'icon': '🦜',
            'description': 'Flocks of parrots, rose-ringed parakeets, munias, and sparrows attack ripening grain and fruit crops causing massive losses. A large flock can strip a field in days. Common across all of India in both irrigated and dryland crop areas.',
            'affected_crops': 'Sunflower, Jowar, Bajra, Rice, Grapes, Guava, Pomegranate, Maize',
            'prevention_methods': '1. Stretch bird exclusion netting over entire crop canopy\n2. Hang reflective tape, old CDs on strings throughout field\n3. Set up automatic gas-powered bird bangers on timers\n4. Use kite-shaped hawk effigies on poles to scare smaller birds\n5. Employ bird scarers during ripening season\n6. Use sound systems playing predator calls',
            'treatment': 'Bird netting is the most reliable and cost-effective solution. Community action for large infestations. Time harvest slightly early if damage is severe.',
            'season': 'Ripening and harvest season: Sep–Nov and Mar–May', 'severity': 'high',
        },
        {
            'name': 'Rats and Field Rodents', 'category': 'wildlife', 'icon': '🐀',
            'description': 'The bandicoot rat, field rat, and house rat cause enormous pre-harvest and post-harvest losses across India. Rats cut plant stems, dig up seeds, attack stored grain, and burrow into bunds causing irrigation water loss. Estimated to cause 15–20% crop losses in some states.',
            'affected_crops': 'Rice, Wheat, Sugarcane, Groundnut, Stored Grains, Potato',
            'prevention_methods': '1. Deep plowing after harvest to destroy burrows and expose larvae\n2. Community rat control drives before sowing\n3. Use zinc phosphide or bromodiolone bait stations at burrow entrances\n4. Encourage natural predators — barn owls, snakes\n5. Maintain clean field bunds — remove tall grass cover\n6. Store grain in metal or concrete rat-proof containers',
            'treatment': 'Zinc phosphide 2% bait in T-shaped bait stations along bunds. Fumigation of active burrows. Snap traps at burrow entrances. Install barn owl nest boxes to encourage natural predation.',
            'season': 'Year-round; critical at harvest and storage periods', 'severity': 'high',
        },
        {
            'name': 'Sloth Bear', 'category': 'wildlife', 'icon': '🐻',
            'description': 'Sloth bears raid sugarcane, maize, and fruit orchards in forest-fringe areas of Jharkhand, Odisha, Chhattisgarh, MP, Maharashtra, and Karnataka. They also destroy beehives in orchards and are highly dangerous to farm workers.',
            'affected_crops': 'Sugarcane, Maize, Mango, Jackfruit, Honey Bee colonies',
            'prevention_methods': '1. Solar electric fencing — most effective deterrent for bears\n2. Beehive fences on field edges (bears fear bee stings)\n3. Motion-sensor floodlights covering all approach paths\n4. Community watch groups with noise-making equipment and searchlights\n5. Avoid leaving harvested fruits in field overnight',
            'treatment': 'Contact Forest Department immediately. Bears are protected under Schedule I — no lethal control is legal. Apply for compensation under state schemes. Document all losses.',
            'season': 'Active year-round; peaks March–May (mango season) and post-monsoon', 'severity': 'critical',
        },
        {
            'name': 'Leopard', 'category': 'wildlife', 'icon': '🐆',
            'description': 'Leopards increasingly raid livestock and cause farmers to abandon agriculture in some areas. Found in forest-fringe areas across India from the Himalayas to South India. Their presence disrupts farming operations, especially in plantation estates and hill farms.',
            'affected_crops': 'Indirect impact through livestock loss and farmland abandonment in peripheral areas',
            'prevention_methods': '1. Secure livestock in strong enclosures with reinforced roof at night\n2. Install motion-triggered alarms around farm boundaries\n3. Use large guard dogs (Bully Kutta, Gaddi) for livestock\n4. Bright security lighting around entire farmstead\n5. Coordinate with Forest Department for camera trapping and monitoring',
            'treatment': 'Contact Forest Department immediately for any leopard sightings near habitation. Apply for livestock loss compensation. Do not attempt to trap or harm — schedule I protected animal.',
            'season': 'Year-round; peaks when natural prey is scarce', 'severity': 'high',
        },
        {
            'name': 'Deer (Sambhar and Barking Deer)', 'category': 'wildlife', 'icon': '🦌',
            'description': 'Sambhar and barking deer cause significant crop damage in hilly states including Himachal Pradesh, Uttarakhand, J&K, Northeastern states, and Western Ghats regions. They are most damaging to high-value horticultural crops in terrace farming areas.',
            'affected_crops': 'Apple, Pear, Plum, Maize, Potato, Vegetables, Rice (terrace fields)',
            'prevention_methods': '1. Install 6 to 8 ft high chain-link or mesh wire fencing\n2. Solar electric fence with multiple strands at 30, 60, 90, 120 cm heights\n3. Motion-sensor lights and alarm systems covering all approaches\n4. Grow thorny hedges (Rosa canina, berberis) on field borders\n5. Community watch especially at dawn, dusk, and through the night',
            'treatment': 'Contact State Wildlife Department. Compensation available under state schemes for horticultural crop losses. Document losses with photo evidence and revenue records.',
            'season': 'Year-round; peaks during spring planting and autumn harvest', 'severity': 'high',
        },

        # =====================================================================
        # PESTS AND INSECTS (22 entries — Pan India)
        # =====================================================================
        {
            'name': 'Aphids (Various Species)', 'category': 'pest', 'icon': '🦗',
            'description': 'Aphids are tiny soft-bodied sucking insects that colonize growing tips and undersides of leaves. They secrete honeydew causing sooty mold. They transmit devastating viral diseases including wheat streak mosaic, potato leaf roll, and mustard mosaic. Found across all states on almost every crop.',
            'affected_crops': 'Wheat, Mustard, Cotton, Potato, Okra, Chilli, Citrus, Pulses, Vegetables',
            'prevention_methods': '1. Spray neem oil solution (5 ml/liter water + 2 ml soap) every 10 days\n2. Release natural predators — ladybird beetles, lacewings, syrphid flies\n3. Use yellow sticky traps for monitoring and mass trapping\n4. Avoid excess nitrogen fertilization which promotes soft aphid-susceptible growth\n5. Intercrop with coriander, fennel, or marigold to attract beneficial insects\n6. Remove and destroy heavily infested plant parts immediately',
            'treatment': 'Spray imidacloprid 17.8 SL (0.5 ml/liter) or dimethoate 30 EC (1 ml/liter). For organic farming use Azadirachtin-based neem pesticides. Rotate insecticide classes every spray to prevent resistance.',
            'season': 'February–April (Rabi crops); October–December (vegetables)', 'severity': 'high',
        },
        {
            'name': 'Fall Army Worm (Spodoptera frugiperda)', 'category': 'pest', 'icon': '🐛',
            'description': 'Invasive pest that entered India in 2018 and spread to nearly all states within 2 years. FAW caterpillars bore into the whorl and developing cob of maize causing massive losses of 30–70%. They have a characteristic Y-shaped suture on the head capsule and 4 black dots on the last abdominal segment.',
            'affected_crops': 'Maize (primary host), Sorghum, Sugarcane, Rice, Wheat, Cotton, Turf grasses',
            'prevention_methods': '1. Early field scouting — check plant whorls weekly from emergence\n2. Set pheromone traps (8 to 10 per hectare) for adult moth monitoring\n3. Apply Bt (Bacillus thuringiensis var. kurstaki) spray — biological control against early instars\n4. Encourage parasitoid wasps — avoid broad-spectrum insecticides unnecessarily\n5. Use FAW-resistant maize varieties wherever available\n6. Timely sowing to avoid peak infestation window',
            'treatment': 'Apply spinetoram 11.7% SC (0.5 ml/L), chlorantraniliprole 18.5 SC (0.4 ml/L), or emamectin benzoate 5 SG (0.4 g/L). Target early instar larvae in whorls. Evening application is most effective.',
            'season': 'June–November (Kharif); spreading to Rabi maize areas', 'severity': 'critical',
        },
        {
            'name': 'Whitefly (Bemisia tabaci)', 'category': 'pest', 'icon': '🦟',
            'description': 'Whitefly is one of India\'s most damaging sucking pests and virus vectors. It vectors Cotton Leaf Curl Virus (CLCuV), Tomato Yellow Leaf Curl Virus, and other deadly geminiviruses. Even low populations cause heavy losses through disease transmission alone.',
            'affected_crops': 'Cotton, Tomato, Chilli, Okra, Brinjal, Cassava, Cucurbits, Tobacco',
            'prevention_methods': '1. Use yellow sticky traps (25 to 30 per hectare) for monitoring and control\n2. Install UV-blocking reflective silver mulches — repels whitefly\n3. Spray neem oil (5 ml/L) or neem seed kernel extract (5%) preventively\n4. Remove and destroy virus-infected plants immediately — no cure exists\n5. Avoid planting cotton or tomato near older infested crop fields\n6. Use resistant varieties wherever available',
            'treatment': 'Spray thiamethoxam 25 WG (0.3 g/L) or spiromesifen 22.9 SC (0.9 ml/L). Strictly rotate between different insecticide classes. Monitor resistance levels regularly.',
            'season': 'May–October; critical peak August–September', 'severity': 'critical',
        },
        {
            'name': 'Brown Plant Hopper (Nilaparvata lugens)', 'category': 'pest', 'icon': '🦗',
            'description': 'BPH is the most devastating insect pest of rice in India causing "hopper burn" — circular patches of burned, dead rice visible from a distance. It also vectors Grassy Stunt and Ragged Stunt viruses. Insecticide-induced resurgence is a major problem.',
            'affected_crops': 'Rice (all varieties; resistant varieties exist)',
            'prevention_methods': '1. Use BPH-resistant rice varieties such as IR64, Swarna Sub1, and Samba Mahsuri\n2. Avoid excessive nitrogen application — promotes lush growth that attracts BPH\n3. Maintain proper plant spacing for air circulation\n4. Practice alternate wetting and drying irrigation\n5. Conserve natural enemies (spiders, mirid bugs) by avoiding broad-spectrum sprays\n6. Set up light traps for population monitoring',
            'treatment': 'Spray buprofezin 25 SC (1.25 ml/L) or pymetrozine 50 WG (0.6 g/L). Direct spray at base of plant. Avoid synthetic pyrethroids entirely — they cause BPH resurgence.',
            'season': 'Kharif rice season: July–November', 'severity': 'critical',
        },
        {
            'name': 'Rice and Sugarcane Stem Borer', 'category': 'pest', 'icon': '🐛',
            'description': 'Stem borers are the most widespread and damaging pests of rice and sugarcane. Larvae bore into stems causing "dead heart" in vegetative stage and "white ear" at booting in rice. Multiple generations occur per crop season.',
            'affected_crops': 'Rice, Sugarcane, Maize, Sorghum, Bajra',
            'prevention_methods': '1. Use light traps to catch adult moths and monitor population\n2. Clip and destroy egg masses on leaves during field scouting\n3. Release egg parasitoid Trichogramma japonicum (50,000 per ha twice)\n4. Avoid dense planting — maintain recommended crop spacing\n5. Remove and destroy stubble after harvest\n6. Avoid late planting which coincides with peak moth flights',
            'treatment': 'Apply cartap hydrochloride 4G (18 kg/ha) or chlorantraniliprole 0.4G (10 kg/ha) granules into whorls or irrigation water. Spray chlorpyrifos or monocrotophos at early borer detection.',
            'season': 'Kharif: July–October; Rabi sugarcane: year-round', 'severity': 'high',
        },
        {
            'name': 'Thrips (Chilli and Cotton Thrips)', 'category': 'pest', 'icon': '🦟',
            'description': 'Thrips are tiny insects that rasp and suck plant cell contents causing silvery streaks, leaf curl, and deformed fruits. They vector Tomato Spotted Wilt Virus (TSWV) which has no cure. Very active in hot dry conditions during February–May.',
            'affected_crops': 'Chilli, Cotton, Onion, Potato, Grapes, Mango, Cucumber, Rose, Banana',
            'prevention_methods': '1. Use blue sticky traps for monitoring (25 per ha)\n2. Spray neem oil 3000 ppm (5 ml/L) preventively every 15 days\n3. Maintain soil moisture — thrips prefer hot dry conditions\n4. Remove and destroy infested growing tips\n5. Use reflective silver mulches to repel thrips from undersides of leaves\n6. Avoid planting near onion or chilli stubble',
            'treatment': 'Spray spinosad 45 SC (0.3 ml/L) or imidacloprid 70 WG (0.3 g/L). Rotate chemicals every spray. For TSWV-infected plants: remove and destroy immediately.',
            'season': 'February–May and September–December; year-round in South India', 'severity': 'high',
        },
        {
            'name': 'Subterranean Termites (Odontotermes spp.)', 'category': 'pest', 'icon': '🐜',
            'description': 'Subterranean termites attack roots and stems from below causing sudden wilting and plant death. Most destructive in sandy soils and dry regions. Damage often goes unnoticed until the entire plant collapses. Severe in dryland areas of Rajasthan, Gujarat, and Deccan plateau.',
            'affected_crops': 'Wheat, Maize, Sugarcane, Cotton, Groundnut, Jowar, Fruit trees',
            'prevention_methods': '1. Deep summer plowing to expose and destroy subterranean colonies\n2. Avoid incorporating undecomposed organic matter into soil\n3. Treat seeds with chlorpyrifos 20 EC (5 ml/kg seed) before sowing\n4. Apply only well-decomposed FYM — raw manure attracts termites\n5. Maintain proper field hygiene — remove dead wood and stumps\n6. Flood irrigation if termite activity is first observed',
            'treatment': 'Drench soil with chlorpyrifos 20 EC (3 ml/L) around affected plants. Treat seeds with imidacloprid 600 FS (3 ml/kg). Apply phorate 10G (5 kg/ha) in soil at sowing in high-risk areas.',
            'season': 'Year-round; most damaging during dry periods', 'severity': 'high',
        },
        {
            'name': 'Desert and Migratory Locust', 'category': 'pest', 'icon': '🦗',
            'description': 'Locusts form devastating swarms that can cover hundreds of square km. A 1 km2 swarm contains 40 million insects consuming 35,000 people\'s food daily. Major outbreaks occur every few years. The 2020 outbreak was India\'s worst in nearly 30 years affecting Rajasthan, Gujarat, UP, and MP.',
            'affected_crops': 'All crops: wheat, rice, cotton, vegetables, orchards, fodder — no crop is spared',
            'prevention_methods': '1. Register for NCIPM (National Centre for Integrated Pest Management) alert notifications\n2. Monitor FAO Desert Locust Information Service forecasts regularly\n3. Coordinate with Agriculture Department for community response planning in advance\n4. Early detection — report unusual grasshopper activity to block level agriculture officer\n5. Maintain barrier spraying infrastructure along desert borders (Rajasthan, Gujarat)',
            'treatment': 'Government-led aerial and ground spraying with malathion ULV or chlorpyrifos. Do not attempt individual control of swarms. Contact District Agriculture Officer and State Locust Control Unit immediately.',
            'season': 'June–November; outbreak years are irregular', 'severity': 'critical',
        },
        {
            'name': 'Helicoverpa (American Bollworm)', 'category': 'pest', 'icon': '🐛',
            'description': 'One of the most polyphagous and economically destructive pests in India. Larvae bore into cotton bolls, chickpea pods, tomato fruits, and sunflower heads. Has developed resistance to organophosphate and pyrethroid insecticides. Causes thousands of crores in losses annually.',
            'affected_crops': 'Cotton, Chickpea, Pigeonpea, Tomato, Sunflower, Maize, Sorghum, Groundnut',
            'prevention_methods': '1. Set up pheromone traps (5 per ha) for adult moth monitoring\n2. Apply Helicoverpa NPV spray (250 LE/ha) — highly specific biological control\n3. Release Trichogramma chilonis (1.5 lakh per ha) for egg parasitism\n4. Install light traps to attract and kill adults at night\n5. Use Bt cotton varieties for in-built bollworm resistance\n6. Practice crop rotation — never plant host crops consecutively',
            'treatment': 'Apply emamectin benzoate 5 SG (0.4 g/L), indoxacarb 14.5 SC (0.5 ml/L), or spinosad 45 SC (0.3 ml/L). Rotate chemical groups with every spray to manage resistance.',
            'season': 'Kharif: August–November; Rabi chickpea: January–March', 'severity': 'critical',
        },
        {
            'name': 'Mango Mealybug (Drosicha mangiferae)', 'category': 'pest', 'icon': '🐛',
            'description': 'Mango mealybug is a serious orchard pest in North India. Nymphs crawl from soil to trees in January, sucking sap and producing honeydew that causes sooty mold. Can cause 20 to 70% fruit loss in untreated orchards. Particularly severe in UP, Bihar, and MP mango belts.',
            'affected_crops': 'Mango, Litchi, Ber, Peach, Plum, Jamun',
            'prevention_methods': '1. Apply sticky trap bands (alkathene sheet 25 cm wide with grease) around trunk — install in December before nymph emergence\n2. Spray chlorpyrifos 20 EC (3 ml/L) on soil around tree base in January\n3. Till soil under tree canopy in October to November to expose eggs to sun and birds\n4. Scrape bark around trunk base to remove egg masses in November\n5. Community-level action — treat all trees in the village orchard area',
            'treatment': 'Remove alkathene bands with trapped insects and destroy. Spray dimethoate 30 EC (2 ml/L) or imidacloprid on nymphs before tree ascent. Apply profenofos if population is high.',
            'season': 'December–March (nymph emergence and tree climbing phase)', 'severity': 'high',
        },
        {
            'name': 'Red Spider Mite', 'category': 'pest', 'icon': '🕷️',
            'description': 'Spider mites are arachnids that cause silvery stippling on leaves, fine webbing under leaves, and rapid leaf drop. They multiply explosively in hot dry weather and develop insecticide resistance quickly. A single female can produce 200 offspring in 3 weeks.',
            'affected_crops': 'Cotton, Brinjal, Okra, Beans, Strawberry, Rose, Papaya, Cucurbits, Tea, Groundnut',
            'prevention_methods': '1. Maintain adequate soil moisture — spider mites thrive in drought stress conditions\n2. Spray plain water forcefully on leaf undersides to physically dislodge mites\n3. Apply neem oil spray (5 ml/L + 2 ml soap) — disrupts mite reproduction\n4. Release predatory mites (Phytoseiidae family) as biological control agents\n5. Avoid broad-spectrum insecticides that kill natural mite predators\n6. Monitor with 10x hand lens weekly — detect early before explosion',
            'treatment': 'Apply spiromesifen 22.9 SC (0.9 ml/L), abamectin 1.8 EC (0.5 ml/L), or propargite 57 EC (2 ml/L). Strictly rotate chemical groups with every application.',
            'season': 'February–May and September–November; worst in dry years', 'severity': 'high',
        },
        {
            'name': 'Diamondback Moth (Plutella xylostella)', 'category': 'pest', 'icon': '🦋',
            'description': 'DBM is the most destructive pest of cruciferous vegetables globally and causes major damage in India during Rabi season. Tiny larvae scrape leaves from underside creating windowpane effect. Highly insecticide-resistant — one of the first pests to develop resistance worldwide.',
            'affected_crops': 'Cabbage, Cauliflower, Mustard, Radish, Knol-Khol, Broccoli, Chinese Cabbage',
            'prevention_methods': '1. Install pheromone traps (10 per ha) for population monitoring — replace lures monthly\n2. Use Bt spray (Bacillus thuringiensis var. kurstaki) against early instar larvae\n3. Cover young transplants with insect-proof 40-mesh net for first 3 weeks\n4. Plant mustard trap crop borders — sacrifice and destroy when infested\n5. Practice crop-free breaks between consecutive brassica crops',
            'treatment': 'Apply emamectin benzoate 5 SG (0.4 g/L), chlorfenapyr 10 SC (1 ml/L), or spinosad 45 SC (0.3 ml/L). Rotation is essential — DBM develops resistance within 2 to 3 generations without rotation.',
            'season': 'October–March (Rabi vegetables)', 'severity': 'high',
        },
        {
            'name': 'Tobacco Caterpillar (Spodoptera litura)', 'category': 'pest', 'icon': '🐛',
            'description': 'A highly polyphagous pest common across India. Young caterpillars feed gregariously and skeletonize leaves. Older larvae become solitary and devour entire leaves and tender fruits causing defoliation. Particularly damaging to groundnut, soybean, and vegetables in Central and South India.',
            'affected_crops': 'Groundnut, Cotton, Tobacco, Soybean, Vegetables, Pulses, Ornamentals',
            'prevention_methods': '1. Collect and destroy egg masses and young gregarious larvae clusters by hand\n2. Use Spodoptera litura NPV (SlNPV) spray — highly specific biological control\n3. Set up pheromone traps to monitor and mass-trap adult moths\n4. Install light traps (1 per ha) to attract and kill moths at night\n5. Deep plowing after crop to expose pupae in soil to sun and birds',
            'treatment': 'Apply chlorpyrifos 20 EC (2 ml/L) or indoxacarb 14.5 SC (1 ml/L). Spray in the evening when larvae are most active. For early instars use Bt or SlNPV biological sprays.',
            'season': 'Kharif season July–November; also in Rabi vegetables', 'severity': 'high',
        },
        {
            'name': 'Citrus Psylla (Diaphorina citri)', 'category': 'pest', 'icon': '🦟',
            'description': 'Citrus psylla vectors Huanglongbing (HLB) or Citrus Greening disease — the most destructive citrus disease worldwide. Infected trees produce small, misshapen, bitter fruits and eventually die within 5 to 10 years. No cure exists for HLB. Now detected in several Indian states.',
            'affected_crops': 'Sweet Lime, Mandarin, Lemon, Orange, Grapefruit, Curry Leaf Plant',
            'prevention_methods': '1. Use certified psylla-free planting material from registered nurseries\n2. Spray imidacloprid or dimethoate before each new flush emergence (4 to 5 times per year)\n3. Quarantine new plant material for 3 months before planting in main field\n4. Remove HLB-infected trees immediately — they are reservoir for bacteria\n5. Release parasitoid Tamarixia radiata for biological psylla control',
            'treatment': 'If HLB detected: no cure exists — remove and destroy infected trees and replant. For psylla control: spray imidacloprid 17.8 SL (0.3 ml/L) or thiamethoxam 25 WG (0.3 g/L) targeting new leaf flush.',
            'season': 'Active whenever citrus produces new leaf flush (3 to 4 times per year)', 'severity': 'critical',
        },
        {
            'name': 'Legume Pod Borer (Maruca vitrata)', 'category': 'pest', 'icon': '🐛',
            'description': 'Pod borer is the most important insect pest of tropical legumes in India. Larvae web flowers and developing pods together and feed inside pods destroying seeds before harvest. Causes 30 to 80% yield loss in susceptible varieties of pigeonpea and cowpea.',
            'affected_crops': 'Pigeonpea, Cowpea, Moth Bean, French Bean, Yardlong Bean',
            'prevention_methods': '1. Use resistant or tolerant legume varieties where available\n2. Early and timely planting to escape peak borer season\n3. Spray NPV (nuclear polyhedrosis virus) at egg hatching for biological control\n4. Install pheromone traps (5 per ha) for monitoring adult moth activity\n5. Intercrop with sorghum or maize as barrier crop\n6. Remove and destroy infested flower clusters and young pods daily during peak period',
            'treatment': 'Apply chlorantraniliprole 18.5 SC (0.3 ml/L) or indoxacarb 14.5 SC (0.5 ml/L). Begin spray at 50% flowering. Repeat at 15-day intervals.',
            'season': 'August–November (Kharif pulses)', 'severity': 'high',
        },
        {
            'name': 'Rice Gall Midge (Orseolia oryzae)', 'category': 'pest', 'icon': '🦟',
            'description': 'Gall midge larvae attack the growing point of rice plants causing the characteristic silver shoot or onion leaf — a hollow tubular leaf with no grain. Affected tillers are completely lost. Major pest in Odisha, Chhattisgarh, West Bengal, and coastal Andhra Pradesh.',
            'affected_crops': 'Rice (all varieties except gall midge resistant ones)',
            'prevention_methods': '1. Use GMR-6, Shakti, and other documented gall midge resistant varieties\n2. Avoid late planting — synchronize transplanting with neighboring fields\n3. Drain and re-flood fields to kill larvae at soil surface\n4. Set light traps to catch adult midges and monitor emergence\n5. Apply nitrogen fertilizer in split doses — avoid heavy early dose which promotes lush growth',
            'treatment': 'Apply carbofuran 3G granules (20 kg/ha) into flooded field water at tillering. Spray monocrotophos 36 SL (1.5 ml/L) when silver shoots are first noticed.',
            'season': 'Kharif: July–September', 'severity': 'high',
        },
        {
            'name': 'Banana Rhizome Weevil (Cosmopolites sordidus)', 'category': 'pest', 'icon': '🐛',
            'description': 'The banana stem weevil is the most serious pest of banana plantations worldwide and across India. Larvae tunnel through the rhizome and pseudostem causing plant lodging and 30 to 60% production loss. Present in all banana-growing states.',
            'affected_crops': 'Banana, Plantain, Ensete',
            'prevention_methods': '1. Use weevil-free tissue culture planting material (completely free from weevil)\n2. Place split-stem traps near infested stools to attract and trap adult weevils\n3. Maintain field hygiene — remove dead pseudostems and decaying rhizome matter promptly\n4. Apply carbofuran 3G in the planting hole at transplanting\n5. Treat rhizomes with chlorpyrifos solution before planting in new area',
            'treatment': 'Drench soil around banana stools with chlorpyrifos 20 EC (5 ml/L). Apply carbofuran 3G (40 g per plant) near corm. Mass trapping with lure-baited intercept traps along field borders.',
            'season': 'Year-round in all tropical banana growing regions', 'severity': 'high',
        },
        {
            'name': 'Coffee Berry Borer (Hypothenemus hampei)', 'category': 'pest', 'icon': '🐛',
            'description': 'The most economically important pest of coffee worldwide. Female beetles bore into coffee berries and lay eggs inside. Infested berries drop prematurely or produce defective beans with borer holes. Major economic problem in Karnataka, Kerala, and Tamil Nadu coffee estates.',
            'affected_crops': 'Arabica Coffee, Robusta Coffee',
            'prevention_methods': '1. Strip-harvest promptly — never leave overripe berries on tree or fallen on ground\n2. Collect and destroy fallen berries which harbor pupating beetles\n3. Use Beauveria bassiana fungal biocontrol spray — approved and effective\n4. Set BROCAP lure traps with methanol and ethanol mixture (1 per 20 trees)\n5. Maintain adequate shade canopy — reduces temperature stress that favors infestation',
            'treatment': 'Apply endosulfan 35 EC (1.5 ml/L) or chlorpyrifos during post-harvest period. Beauveria bassiana (1x10 to the 8th spores/ml) is approved as bio-pesticide. Submerge harvested berries before pulping to kill larvae inside.',
            'season': 'Post-monsoon: October–February', 'severity': 'high',
        },
        {
            'name': 'Cutworm (Agrotis ipsilon)', 'category': 'pest', 'icon': '🐛',
            'description': 'Cutworm larvae live in soil during the day and feed at the base of plant stems at night, cutting young seedlings at or below soil level. They cause sudden death of rows of seedlings creating gaps in fields. Common in Rabi vegetable crops across India.',
            'affected_crops': 'Tomato, Brinjal, Cabbage, Tobacco, Groundnut, Sunflower, Maize, Sugarcane',
            'prevention_methods': '1. Deep summer plowing to expose pupae and larvae to sun and predatory birds\n2. Install light traps to attract and kill adult moths\n3. Place poison bait (bran + jaggery + chlorpyrifos) near affected plant rows in evening\n4. Use protective collars around transplanted seedlings\n5. Flood irrigation — forces cutworm larvae to soil surface for bird predation',
            'treatment': 'Apply chlorpyrifos 20 EC as soil drench (3 ml/L) around stem bases in the evening. Broadcast poison bait in the evening when larvae are most active for immediate control.',
            'season': 'October–February (Rabi season); Kharif seedling establishment stage', 'severity': 'medium',
        },
        {
            'name': 'Groundnut Leaf Miner (Aproaerema modicella)', 'category': 'pest', 'icon': '🦟',
            'description': 'Leaf miner larvae create serpentine mines inside leaves then fold and web leaves together. Heavy infestation causes complete defoliation and severe yield loss. Very common in groundnut-growing areas of Gujarat, AP, Tamil Nadu, and Karnataka.',
            'affected_crops': 'Groundnut (primary host), Soybean',
            'prevention_methods': '1. Deep summer plowing to destroy overwintering pupae in soil\n2. Timely sowing to avoid peak infestation period\n3. Apply neem seed kernel extract (NSKE) 5% spray preventively\n4. Conserve parasitoid wasps (Sympiesis spp.) by avoiding broad-spectrum sprays\n5. Set up light traps to catch adult moths at night',
            'treatment': 'Spray dimethoate 30 EC (1.5 ml/L) or quinalphos 25 EC (2 ml/L) at first sign of leaf folding. Repeat after 15 days if population remains high.',
            'season': 'August–November (Kharif groundnut season)', 'severity': 'medium',
        },

        # =====================================================================
        # WEEDS (16 entries — Pan India)
        # =====================================================================
        {
            'name': 'Wild Oat (Phalaris minor)', 'category': 'weed', 'icon': '🌾',
            'description': 'The most problematic weed of wheat fields in North India. Phalaris minor resembles wheat in early stages making identification very difficult. It has developed resistance to multiple widely used herbicides. A single plant produces 2,000 to 5,000 seeds that remain viable in soil for many years.',
            'affected_crops': 'Wheat, Barley',
            'prevention_methods': '1. Use certified, weed-free seeds only from registered dealers\n2. Practice zero or minimum tillage sowing to reduce germination stimulation\n3. Crop rotation with non-cereal crops (rotate rice-wheat to rice-sugarcane)\n4. Apply pre-emergence herbicide within 3 days of sowing\n5. Hand weeding at 2 to 3 leaf stage before seed formation\n6. Never allow weed to set seeds — seeds persist in soil for many years',
            'treatment': 'Apply clodinafop-propargyl 15 WP (400 g/ha) or fenoxaprop-p-ethyl 10 EC (750 ml/ha) at 3 to 4 weeks after sowing. For herbicide-resistant populations: use mesosulfuron + iodosulfuron combination products.',
            'season': 'November–March (Rabi wheat season)', 'severity': 'critical',
        },
        {
            'name': 'Johnson Grass (Sorghum halepense)', 'category': 'weed', 'icon': '🌿',
            'description': 'Perennial grass weed that spreads through both seeds and underground rhizomes. Once established it is extremely difficult to eradicate without multi-season effort. Competes strongly with crops for water, nutrients, and light. Also hosts several crop disease pathogens.',
            'affected_crops': 'Sugarcane, Cotton, Maize, Sorghum, Soybean, Vegetables',
            'prevention_methods': '1. Deep repeated tillage to bring rhizomes to surface and desiccate\n2. Solarize soil with transparent plastic during summer months\n3. Never allow plants to set seed — one plant can produce thousands of seeds\n4. Use certified weed-free irrigation water and farm inputs\n5. Clean farm equipment between fields to prevent rhizome spread',
            'treatment': 'Apply glyphosate 41 SL (3 ml/L) as directed spray on weed foliage keeping away from crops. For in-crop control in maize: nicosulfuron 4 SC (1.5 L/ha). Requires multiple treatments over 2 to 3 seasons.',
            'season': 'Kharif (June–October); re-emerges from rhizomes in Rabi', 'severity': 'high',
        },
        {
            'name': 'Bathua (Chenopodium album)', 'category': 'weed', 'icon': '🌱',
            'description': 'Bathua or Lamb\'s Quarters is a broadleaf weed that emerges early and rapidly competes with Rabi crops. A single plant produces up to 75,000 seeds which remain viable in soil for decades. Widespread across all of North and Central India in winter crop fields.',
            'affected_crops': 'Wheat, Mustard, Potato, Onion, Vegetables',
            'prevention_methods': '1. Hand weeding at 2 to 3 weeks after crop emergence\n2. Intercultural operations with hoe or cultivator between crop rows\n3. Pre-emergence herbicide application within 3 days after sowing\n4. Mulching to suppress germination in vegetable crops\n5. Crop rotation with dense-canopy crops that shade out germinating seeds',
            'treatment': 'Apply 2,4-D sodium salt 80 WP (500 g/ha) at 3 to 4 weeks after wheat sowing. Or use metsulfuron-methyl 20 WP (20 g/ha). For vegetables: use pendimethalin pre-emergence.',
            'season': 'October–February (Rabi season)', 'severity': 'medium',
        },
        {
            'name': 'Parthenium (Congress Grass)', 'category': 'weed', 'icon': '🌿',
            'description': 'Parthenium is one of India\'s most invasive and harmful weeds. It causes severe allergic reactions (contact dermatitis, hay fever, asthma) in humans and livestock. It releases allelopathic chemicals that suppress crop growth. Now spread across all states from J&K to Tamil Nadu.',
            'affected_crops': 'Maize, Sorghum, Vegetables, Pulses, Sugarcane; invades pastures and roadsides',
            'prevention_methods': '1. Uproot plants by hand before flowering — always wear gloves and mask\n2. Never allow seeds to form — one plant produces 25,000 or more seeds\n3. Use biological control: Zygogramma bicolorata beetle (NBPGR approved)\n4. Promote competitive smother crops: parthenium suppressed by sunflower and sorghum\n5. Community village-level eradication drives with public education',
            'treatment': 'Spray glyphosate 41% SL (2 ml/L) on non-crop areas or atrazine 50 WP (1.5 kg/ha) in maize. Metsulfuron-methyl in pastures. Biological control with Zygogramma beetle is preferred long-term strategy.',
            'season': 'Kharif June–October; also present in warmer Rabi months in South India', 'severity': 'high',
        },
        {
            'name': 'Nut Grass (Cyperus rotundus)', 'category': 'weed', 'icon': '🌾',
            'description': 'Nut grass or purple nutsedge is listed by scientists as the world\'s most troublesome weed. It spreads through underground tubers (nutlets) that survive even extreme conditions. One plant can produce 40,000 or more tubers in a season. Found in every Indian state and almost impossible to fully eradicate.',
            'affected_crops': 'Sugarcane, Potato, Cotton, Vegetables, Rice, Groundnut, Onion',
            'prevention_methods': '1. Deep summer plowing to expose and desiccate tubers under hot sun\n2. Black polythene solarization for 6 to 8 weeks in peak summer\n3. Plant dense-canopy crops to suppress by shading\n4. Repeated shallow cultivation over 2 to 3 seasons to exhaust tuber reserves\n5. Never deep-till once established — it spreads tubers throughout the soil profile',
            'treatment': 'Apply halosulfuron-methyl 75 WP (67 g/ha) in sugarcane or vegetable crops. Use sulfentrazone in potato. In rice: bensulfuron-methyl + pretilachlor combination product.',
            'season': 'Kharif and Rabi both; year-round in warm climates of South India', 'severity': 'critical',
        },
        {
            'name': 'Barnyard Grass (Echinochloa crus-galli)', 'category': 'weed', 'icon': '🌾',
            'description': 'The most serious weed of rice fields across India. Barnyard grass mimics rice in early growth stages making identification and hand weeding very difficult. It competes aggressively and can reduce rice yield by 50 to 80% in severe infestations in transplanted and direct-seeded rice.',
            'affected_crops': 'Rice (primary host), also Maize and Vegetables',
            'prevention_methods': '1. Transplant rice at recommended age to give crop a competitive advantage\n2. Maintain flooded conditions for as long as possible — barnyard grass tolerates flooding less than rice\n3. Hand weeding 20 to 25 days after transplanting\n4. Use rice varieties with strong early-season canopy closure\n5. Line transplanting enables intercultural weeding operations between rows',
            'treatment': 'Apply butachlor 50 EC (2 L/ha) pre-emergence at 2 to 5 days after transplanting in flooded rice. Or bispyribac sodium 10 SC (200 ml/ha) at 3 to 4 leaf stage of weed. Maintain 2 to 3 cm water level after herbicide application.',
            'season': 'Kharif rice season: June–October', 'severity': 'critical',
        },
        {
            'name': 'Water Hyacinth (Eichhornia crassipes)', 'category': 'weed', 'icon': '🌊',
            'description': 'Water hyacinth is the world\'s worst aquatic weed. It blocks irrigation canals, reduces water flow, depletes oxygen in water bodies killing fish, and harbors mosquitoes and crop pests. It doubles in population every 2 weeks and can completely clog entire canal systems.',
            'affected_crops': 'Irrigated rice, Aquaculture ponds, Irrigation channel systems',
            'prevention_methods': '1. Manual removal before seed set — compost harvested biomass for biogas\n2. Biological control: introduce weevil Neochetina eichhorniae (released by some state governments)\n3. Drying of canals and desilting to remove plant root matter\n4. Maintain water flow velocity in channels — stagnant water promotes explosive growth\n5. Community cooperative clearing of canal networks before irrigation season',
            'treatment': 'Apply 2,4-D amine 58% SL (2 L/ha) on water bodies where legally permitted. Mechanical harvesting with slashers or dredgers in larger canals. Use harvested biomass for biogas production for economic benefit.',
            'season': 'Year-round in standing water; explosive growth March–September', 'severity': 'high',
        },
        {
            'name': 'Lantana (Lantana camara)', 'category': 'weed', 'icon': '🌸',
            'description': 'Lantana is one of India\'s most invasive shrub weeds. It forms dense thickets preventing crops from growing, harbors pests and snakes, and is toxic to livestock. It spreads rapidly from forest margins into agricultural land and is now present in every state.',
            'affected_crops': 'Plantation crops, Pastures, Forest edges adjacent to farm land',
            'prevention_methods': '1. Uproot young plants before they become woody — most effective when caught early\n2. Controlled burning after cutting in non-crop areas\n3. Release approved biocontrol agents: Teleonemia scrupulosa lace bug\n4. Replace cleared areas with competitive grass cover immediately\n5. Prevent bird access to fruiting plants in fields — birds are primary seed dispersers',
            'treatment': 'Cut stems at soil level and immediately paint freshly cut stumps with undiluted glyphosate or triclopyr ester. Foliar spray with triclopyr on young regrowth. Requires multi-year persistence and follow-up.',
            'season': 'Spreads year-round; flowering peaks post-monsoon', 'severity': 'high',
        },
        {
            'name': 'Mikania (Mikania micrantha) — Mile-a-Minute', 'category': 'weed', 'icon': '🌿',
            'description': 'Mikania is an extremely aggressive climbing weed that smothers crops, trees, and plantation canopies. Growing up to 8 cm per day it can completely cover a tea bush or young plantation tree in weeks. A major problem in Northeast India, West Bengal, Assam, and Kerala.',
            'affected_crops': 'Tea, Rubber, Banana, Young forest plantations, Vegetable gardens',
            'prevention_methods': '1. Regular manual weeding every 2 to 3 weeks during monsoon season\n2. Mulching with black polythene to prevent germination in plantation beds\n3. Biological control: Puccinia spegazzinii rust fungus (permitted in some regions)\n4. Shade management in plantations — mikania prefers open edges and canopy gaps\n5. Early detection and prevention of seed formation before spread occurs',
            'treatment': 'Spray glyphosate 41% SL (5 ml/L) as directed spray on mikania foliage. Or use metribuzin 70 WP (1 g/L) in tea gardens. Manual cutting followed by composting or burning of cut material. Multiple treatments required every season.',
            'season': 'Most aggressive during monsoon: June–September', 'severity': 'critical',
        },
        {
            'name': 'Spiny Amaranth (Amaranthus spinosus)', 'category': 'weed', 'icon': '🌱',
            'description': 'Spiny amaranth is a prickly broadleaf weed that competes aggressively with summer and Kharif crops. Its sharp spines make hand weeding difficult and injurious to workers. A single plant can produce over 100,000 seeds. Widespread in all states especially during Kharif season.',
            'affected_crops': 'Cotton, Groundnut, Maize, Soybean, Vegetables, Pulses, Okra',
            'prevention_methods': '1. Pre-emergence herbicide application immediately after sowing\n2. Shallow cultivation at 2 to 3 weeks to cut young seedlings before spine development\n3. Wear protective gloves and clothing when hand weeding in infested fields\n4. Prevent seed formation — remove plants before flowering begins\n5. Dense crop canopy suppresses germination of new seeds',
            'treatment': 'Apply pendimethalin 30 EC (3.3 L/ha) pre-emergence. Post-emergence: atrazine 50 WP in maize (1.5 kg/ha), or hand weeding when plants are still small and without spines.',
            'season': 'Kharif: June–October; also present in summer crops', 'severity': 'medium',
        },
        {
            'name': 'Dodder (Cuscuta chinensis) — Parasitic Weed', 'category': 'weed', 'icon': '🌱',
            'description': 'Dodder is a leafless parasitic plant with no chlorophyll. It attaches to crop plants and extracts water and nutrients directly from the host through specialized haustoria. It can spread from plant to plant and devastate entire patches of legumes or vegetables.',
            'affected_crops': 'Alfalfa, Lentil, Coriander, Tomato, Potato, Flax, Onion, Clover',
            'prevention_methods': '1. Inspect planting material carefully — dodder enters as seed contaminant\n2. Use certified, properly cleaned seeds screened for dodder contamination\n3. Destroy infested patches including surrounding soil — do not compost\n4. Crop rotation with grasses (dodder cannot parasitize grasses)\n5. Deep plowing after detection to bury seed bank deeper',
            'treatment': 'Remove and burn all dodder and attached host plants in infested patches. Apply pendimethalin pre-emergence in next crop cycle. No selective herbicide is available for use in established crops with active dodder.',
            'season': 'Kharif and Rabi both; depends on host crop planted', 'severity': 'high',
        },
        {
            'name': 'Striga (Witchweed — Striga asiatica)', 'category': 'weed', 'icon': '🌸',
            'description': 'Striga is a root-parasitic weed that attaches to crop roots underground sapping nutrients before the weed even emerges above soil. By the time it is visible, 40 to 70% of yield loss has already occurred. Major threat in Maharashtra, AP, Telangana, and tribal belt areas of Central India.',
            'affected_crops': 'Sorghum, Maize, Sugarcane, Pearl Millet, Upland Rice, Cowpea',
            'prevention_methods': '1. Use Striga-resistant sorghum and maize varieties documented by ICRISAT\n2. Apply Fusarium oxysporum f. sp. strigae as biocontrol — attacks striga roots underground\n3. Use nitrogen-fixing legume intercropping — high nitrogen suppresses striga seed germination\n4. Pull out and burn striga plants before seed set — one plant makes 200,000 seeds\n5. Apply fertilizer (N and P) to boost crop competitive ability against parasitism',
            'treatment': 'Seed treatment with Fusarium-based biocontrol agent. Apply 2,4-D at early post-emergence striga stage when striga is still small. Community eradication programs are essential for long-term control.',
            'season': 'Kharif: appears July–September after onset of rains', 'severity': 'critical',
        },
        {
            'name': 'Imperata Grass (Cogon Grass — Imperata cylindrica)', 'category': 'weed', 'icon': '🌾',
            'description': 'Imperata is a perennial grass weed spreading by underground rhizomes and wind-dispersed seeds. It forms dense mats that exclude all other plants. Common in degraded lands, jhum fields, and forest edges in Northeast India and parts of South India and Western Ghats.',
            'affected_crops': 'Plantation crops, Jhum crops, Young fruit orchards, Pastures, Rubber estates',
            'prevention_methods': '1. Repeated tillage to fragment and desiccate rhizomes over multiple seasons\n2. Soil solarization with clear polythene for 6 to 8 weeks in peak summer\n3. Plant competing smother crops (Mucuna, Desmodium) after initial control\n4. Never burn — burning stimulates vigorous rhizome regeneration\n5. Promote fast-growing plantation trees that shade the area rapidly',
            'treatment': 'Apply glyphosate 41% SL (7 ml/L) when grass is actively growing with new shoots 30 to 40 cm tall. Treat again on regrowth 4 to 6 weeks later. Multiple applications over 2 full seasons required for effective control.',
            'season': 'Year-round; most actively growing during monsoon season', 'severity': 'high',
        },
        {
            'name': 'Morning Glory (Ipomoea spp.)', 'category': 'weed', 'icon': '🌺',
            'description': 'Morning glory is a climbing broadleaf weed that twines around crop plants competing for light, water, and nutrients. Common in cotton, soybean, and maize fields across Central and Western India. Spreads rapidly under warm moist Kharif conditions.',
            'affected_crops': 'Cotton, Soybean, Maize, Groundnut, Sugarcane',
            'prevention_methods': '1. Pre-emergence herbicide immediately after sowing\n2. Intercultural cultivation at 20 and 40 days after sowing to cut seedlings\n3. Remove climbing vines manually before they set seed\n4. Dense crop spacing to shade out germinating seeds\n5. Crop rotation to break the soil seed bank cycle',
            'treatment': 'Apply pendimethalin 30 EC (3.3 L/ha) pre-emergence. Post-emergence in soybean: lactofen 21.3 EC (1 L/ha). In cotton: directed spray of oxyfluorfen on inter-rows avoiding crop foliage.',
            'season': 'Kharif: June–October (warm moist conditions)', 'severity': 'medium',
        },
        {
            'name': 'Gokhru (Tribulus terrestris) — Puncture Vine', 'category': 'weed', 'icon': '🌱',
            'description': 'Gokhru is a prostrate spreading weed with extremely sharp spiny fruits that injure feet, tyre punctures, and animal paws. Thrives in dryland crops and degraded soils. Seeds remain viable in soil for 3 to 7 years. Common in dryland areas of Rajasthan, Gujarat, and Deccan plateau.',
            'affected_crops': 'Groundnut, Moth Bean, Mung Bean, Pearl Millet, Sesame, Cotton',
            'prevention_methods': '1. Deep tillage before sowing to bring seeds to surface and expose to hot sun\n2. Maintain adequate soil fertility — gokhru thrives in nutrient-poor degraded soils\n3. Hand weeding before fruit formation when spines are not yet hardened\n4. Intercultural operations at 20 to 25 days after sowing\n5. Wear sturdy closed shoes or boots in infested fields at all times',
            'treatment': 'Apply pendimethalin pre-emergence. 2,4-D spray at 3 to 4 leaf stage of weed. Hand removal before spiny fruits mature and scatter into soil. Community-level control in village common lands is essential.',
            'season': 'Kharif: June–September in dryland areas', 'severity': 'medium',
        },
        {
            'name': 'Orobanche (Broomrape) — Root Parasite', 'category': 'weed', 'icon': '🌸',
            'description': 'Orobanche is a devastating root-parasitic weed with no chlorophyll. It attaches to host crop roots and drains water and nutrients. A single plant produces 100,000 or more tiny seeds that remain viable in soil for 20 or more years. Major problem in UP, Bihar, Rajasthan, and Punjab on tomato and vegetables.',
            'affected_crops': 'Tomato, Carrot, Potato, Mustard, Sunflower, Faba Bean, Lentil',
            'prevention_methods': '1. Practice long crop rotations (minimum 7 years) away from susceptible hosts\n2. Use resistant or tolerant crop varieties where available\n3. Apply ethylene gas as suicidal germination stimulant before planting\n4. Deep summer plowing to expose seeds to lethal surface temperatures\n5. Incorporate Trichoderma harzianum to suppress seed viability',
            'treatment': 'Apply glyphosate at suicidal germination dose before main crop planting. Use imazethapyr in sunflower (tolerant varieties). Hand remove parasite plants before they flower and seed. No chemical works well in established crops.',
            'season': 'Rabi: October–March; emergence follows host crop root development', 'severity': 'high',
        },
    ]

    for data in threats_data:
        d = {k: v for k, v in data.items() if k != 'region'}
        Threat.objects.get_or_create(name=d['name'], defaults=d)

    # =========================================================================
    # CROP TIPS (22 entries — Pan India, all major crops)
    # =========================================================================
    tips_data = [
        {
            'title': 'IPM for Wheat — North India (Rabi)',
            'content': 'Apply Integrated Pest Management (IPM): Start with certified seeds treated with carboxin + thiram. Monitor fields weekly from January for aphids. Spray imidacloprid only when aphid population crosses 26 per tiller — spraying below this threshold wastes money. Practice crop rotation with mustard or sugarcane every 3 years. Apply 2,4-D for broadleaf weeds and clodinafop for wild oat at 3 to 4 weeks. Proper IPM reduces pesticide use by 40 to 60% while maintaining yield.',
            'crop_type': 'Wheat', 'season': 'Rabi'
        },
        {
            'title': 'SRI Method for Rice — Maximum Yield with Less Water',
            'content': 'System of Rice Intensification (SRI) boosts yield by 20 to 50%. Transplant 8 to 12 day old seedlings (single seedling per hill at 25x25 cm spacing). Practice intermittent irrigation (alternate wetting and drying) instead of continuous flooding — saves 30% water. Apply compost or FYM (5 tonnes per ha). Use rotary weeder at 10-day intervals instead of hand weeding. SRI results in larger root systems, more tillers, and better grain filling. Proven in WB, Tamil Nadu, Karnataka, and Odisha.',
            'crop_type': 'Rice', 'season': 'Kharif'
        },
        {
            'title': 'Cotton Bollworm and Pest Management — Central India',
            'content': 'Plant Bt cotton varieties to reduce bollworm pressure by 80%. Set up 5 pheromone traps per hectare for army worm and bollworm monitoring. Apply Trichoderma-based soil treatment before planting to control fusarium and root rots. Monitor whitefly from August using yellow sticky traps. Never spray cotton during early morning flowering hours — protects pollinators. Practice strict insecticide rotation to prevent resistance: use at least 3 different chemical groups per season.',
            'crop_type': 'Cotton', 'season': 'Kharif'
        },
        {
            'title': 'Groundnut Yield Improvement — South India',
            'content': 'Use bold-seeded and rosette-resistant groundnut varieties (TG 37A, ICGV 91114). Treat seeds with Rhizobium culture for nitrogen fixation — saves 25 kg N per ha in fertilizer. Apply gypsum at 500 kg per ha at flowering stage — essential for pod filling and preventing empty pods. Monitor for leaf miner and tikka leaf spot from August. Ensure good drainage — groundnut cannot tolerate waterlogging even for 24 hours. Practice deep summer plowing to control soil-borne diseases.',
            'crop_type': 'Groundnut', 'season': 'Kharif'
        },
        {
            'title': 'Sugarcane Management — UP, Maharashtra, Tamil Nadu',
            'content': 'Choose recommended variety for your zone: Co 0238 for UP; Co 86032 for Maharashtra; Co 86032 or CoC 671 for Tamil Nadu. Use disease-free seed material treated with carbendazim 0.1% for smut and wilt control. Adopt ratoon crop management — first ratoon yields 80% of plant crop at only 40% of the input cost. Install pheromone traps for early shoot borer detection from May onwards. Apply trash mulching between rows to conserve moisture and suppress weed growth.',
            'crop_type': 'Sugarcane', 'season': 'All seasons'
        },
        {
            'title': 'Tomato Disease and Pest Management — All States',
            'content': 'Start with nursery hygiene — raise seedlings on raised beds covered with 50-mesh insect-proof net to prevent whitefly and thrips from day one. Apply Trichoderma harzianum + Pseudomonas fluorescens soil drench for fusarium wilt protection. Install yellow sticky traps at transplanting. Use indeterminate varieties with staking for better air circulation. Monitor for early blight (Alternaria) from fruit setting stage — spray mancozeb 0.2% as preventive every 10 days. Remove and burn plants showing leaf curl virus symptoms immediately.',
            'crop_type': 'Tomato', 'season': 'All seasons'
        },
        {
            'title': 'Mustard Production Tips — Rajasthan, MP, UP, Haryana',
            'content': 'Sow on time (1 to 15 October) to avoid peak aphid season which arrives in January. Maintain plant spacing of 30 cm between rows and 10 to 15 cm within row. Apply 80 kg N per ha in two splits: basal and top dressing at branching. Monitor for Alternaria blight from rosette stage — spray mancozeb 0.2% preventively. Install yellow sticky traps from January for aphid monitoring. Spray thiamethoxam when aphid count crosses 26 per plant. Harvest when 75% pods turn yellow-brown.',
            'crop_type': 'Mustard', 'season': 'Rabi'
        },
        {
            'title': 'Banana Bunch Management — Maharashtra, Tamil Nadu, AP',
            'content': 'Cover banana bunches with blue polythene bags 2 to 3 weeks after bunch emergence to protect from sunburn, birds, and insect pests. Desuck to maintain one ratoon per mother plant at a time. Remove the male bud (bell) after the last hand is fully developed to prevent Sigatoka spread. Apply potassium fertilizer (MOP 500 g per plant) — bananas are the heaviest potassium feeders. Use drip irrigation with fertigation for 30 to 40% better water use efficiency and uniform fruit quality.',
            'crop_type': 'Banana', 'season': 'All seasons'
        },
        {
            'title': 'Soybean IPM — Madhya Pradesh, Maharashtra, Rajasthan',
            'content': 'Treat seeds with Rhizobium japonicum + Bradyrhizobium culture for nitrogen fixation (saves 25 kg N per ha). Use recommended varieties: JS 335, MACS 1281, or NRC 86. Monitor for girdle beetle at 30 days after sowing — spray carbaryl if incidence exceeds 5%. Scout for yellow mosaic virus from July — remove infected plants immediately as whitefly transmits this viral disease. Practice crop rotation with wheat — never grow back-to-back soybean as it builds up soil pathogens.',
            'crop_type': 'Soybean', 'season': 'Kharif'
        },
        {
            'title': 'Chilli Crop Protection — AP, Telangana, Karnataka',
            'content': 'Use certified virus-indexed seedlings from reputable registered nurseries. Install 50-mesh nylon net in nursery to prevent thrips and whitefly infestation from the start. Apply blue sticky traps (25 per ha) specifically for thrips monitoring from transplanting. Rogue out plants showing leaf curl virus symptoms immediately — no chemical cure exists. Spray imidacloprid at transplanting as preventive measure against virus vector insects. Monitor for powdery mildew in cool weather — spray wettable sulphur 80 WP (2 g/L) as preventive.',
            'crop_type': 'Chilli', 'season': 'Kharif and Rabi'
        },
        {
            'title': 'Potato Disease Management — UP, West Bengal, Gujarat',
            'content': 'Use certified seed potatoes free from late blight and viruses. Cut seed pieces with clean, disinfected knives — disinfect between cuts with KMnO4 solution. Spray mancozeb 0.2% or cymoxanil + mancozeb preventively from 30 days after planting. Haulm kill (cut vines) 10 days before harvest to prevent tuber blight infection. Store potatoes at 3 to 4 degrees Celsius with 90% relative humidity in cold storage. Never plant in waterlogged fields — immediately causes Phytophthora rot.',
            'crop_type': 'Potato', 'season': 'Rabi'
        },
        {
            'title': 'Onion Bulb Yield Improvement — Maharashtra, Gujarat, Karnataka',
            'content': 'Grow nursery on 1 m wide raised beds for good drainage. Transplant at 4 to 5 leaf stage with 15x10 cm spacing. Apply sulfur through gypsum (250 kg per ha) for better bulb size, keeping quality, and flavor development. Use drip irrigation with fertigation for size uniformity. Remove bolted (flowering) plants immediately — they never form good bulbs. Withhold water 10 days before harvest to allow skin curing. Cure harvested bulbs in shade for 3 to 5 days before storage to extend shelf life.',
            'crop_type': 'Onion', 'season': 'Rabi'
        },
        {
            'title': 'Apple Orchard Management — Himachal Pradesh, J&K, Uttarakhand',
            'content': 'Spray dormant oil (4%) before bud burst to control San Jose scale and overwintering mites. Apply captan fungicide spray at green tip, pink bud, petal fall, and fruit set stages to control apple scab disease. Install codling moth pheromone traps (4 to 5 per ha) to time spray interventions precisely. Thin fruitlets at 6 to 7 mm size to improve final fruit size and quality. Apply reflective mulch under tree canopy to improve red color development before harvest. Spray calcium at regular intervals to prevent bitter pit disorder.',
            'crop_type': 'Apple', 'season': 'Rabi and Spring'
        },
        {
            'title': 'Tea Estate Pest Management — Assam, West Bengal, Nilgiris',
            'content': 'Monitor for Helopeltis bug (tea mosquito bug) from April onwards — spray thiamethoxam or imidacloprid at first sign of characteristic tip damage. Apply zinc and boron micronutrients every 6 months for high-quality leaf growth and flavor. Practice skiffing and pruning on recommended schedule to maintain bush vigour. Maintain 30 to 40% shade canopy — full sun reduces quality while full shade reduces yield. During flush periods increase hand-plucking rounds to every 7 days for two-leaf-and-bud standard.',
            'crop_type': 'Tea', 'season': 'All seasons'
        },
        {
            'title': 'Chickpea and Pigeonpea Pest Management — MP, Maharashtra',
            'content': 'Treat seeds with Rhizobium + Phosphate Solubilizing Bacteria (PSB) before sowing for improved nitrogen fixation. Install pheromone traps (5 per ha) for Helicoverpa moth monitoring from October. Apply Helicoverpa NPV spray (250 LE per ha) at first larval appearance for biological control. Spray chlorantraniliprole at 5% pod damage economic threshold. Avoid excessive vegetative growth through excess irrigation and nitrogen — it increases Helicoverpa infestation and reduces pod set.',
            'crop_type': 'Chickpea and Pigeonpea', 'season': 'Rabi'
        },
        {
            'title': 'Mango Orchard Care — UP, Bihar, AP, Maharashtra',
            'content': 'Apply alkathene sticky bands 25 cm wide on tree trunks in December to intercept mealybug nymphs climbing up. Spray Bordeaux mixture 1% on trunk and branches after pruning to prevent stem end rot and gummosis. Spray copper hydroxide for powdery mildew control at bud emergence in December. Thin flower clusters when flowering is excessive (more than 50% of branches) to improve final fruit size. Install fruit fly monitoring traps (methyl eugenol lure) from March — spray malathion bait at fly threshold.',
            'crop_type': 'Mango', 'season': 'Rabi and Summer'
        },
        {
            'title': 'Coconut Nutrition and Pest Management — Kerala, TN, Karnataka',
            'content': 'Apply recommended fertilizer mixture: 1.3 kg urea + 2 kg single super phosphate + 2 kg MOP per palm per year in 2 splits (June and December). Green manure with Mucuna in basin between palms. Monitor for eriophyid mite under perianth of button nuts — spray fenazaquin if infestation is detected. Control red palm weevil by installing pheromone lure traps (1 per 10 trees). Apply neem cake (2 kg per palm) in basin at base of tree for soil pest control. Inject monocrotophos into leaf axils for rhinoceros beetle control.',
            'crop_type': 'Coconut', 'season': 'All seasons'
        },
        {
            'title': 'Soil Health and Organic Matter — Pan India',
            'content': 'Test soil every 3 years for pH, NPK, and micronutrients at nearest Krishi Vigyan Kendra (KVK). Apply FYM 10 to 15 tonnes per ha or vermicompost 3 to 5 tonnes before sowing. Practice green manuring with dhaincha (Sesbania aculeata) or sunhemp in summer — adds 100 to 120 kg N per ha equivalent. Never burn crop residue — it destroys beneficial soil organisms and microbes. Use subsoil plowing (deep tillage) every 3 to 4 years to break compaction hardpan. Soil organic carbon above 0.75% is the target for sustainable production.',
            'crop_type': 'All Crops', 'season': 'All seasons'
        },
        {
            'title': 'Drip and Sprinkler Irrigation — Save Water and Boost Yield',
            'content': 'Drip irrigation saves 40 to 60% water compared to flood irrigation and improves yield by 20 to 40% through precise fertigation delivery. Eligible under PM Krishi Sinchayee Yojana subsidy (up to 55% for general farmers, 90% for SC/ST and small farmers). Drip is ideal for vegetables, orchards, sugarcane, and cotton. Sprinkler irrigation suits wheat, pulses, and oilseeds. Soil moisture sensors (tensiometers) prevent costly over- or under-watering. Raised bed planting further reduces water requirement by 20 to 30%.',
            'crop_type': 'All Crops', 'season': 'All seasons'
        },
        {
            'title': 'Post-Harvest Grain Storage — Eliminate Losses',
            'content': 'Dry grain to safe moisture level before storage: wheat less than 12%, rice less than 14%, maize less than 12%, pulses less than 10%. Use hermetic storage bags (PICS bags, Purdue Improved Crop Storage) — eliminates insects without chemicals within 3 to 4 weeks. Treat storage bins with malathion dust on walls and floor before filling. Use aluminum phosphide (Celphos) tablets only in sealed storage by trained persons — very dangerous, follow safety instructions strictly. Check stored grain weekly for heating, mold, and insects. Never store freshly harvested moist grain under any circumstances.',
            'crop_type': 'All Crops', 'season': 'Post-harvest'
        },
        {
            'title': 'Natural Farming — Zero Budget Natural Farming (ZBNF)',
            'content': 'ZBNF uses only cow-based local inputs at zero input cost. Jeevamrit: ferment 10 kg cow dung + 10 L cow urine + 2 kg jaggery + 2 kg pulse flour in 200 L water for 48 hours — apply 200 L per acre as soil drench or foliar spray. Bijamrit for seed treatment. Mulching with crop residue keeps soil moist and feeds earthworms. Whapasa (air-moisture balance) avoids puddling damage. Proven results in Karnataka, AP, and Himachal Pradesh on rice, cotton, vegetables. State governments of Andhra Pradesh and Gujarat actively promote ZBNF.',
            'crop_type': 'All Crops', 'season': 'All seasons'
        },
        {
            'title': 'PM Fasal Bima Yojana — Crop Insurance Guide',
            'content': 'Enroll in PMFBY before the prescribed last date for your state and season. Premium is only 2% for Kharif crops, 1.5% for Rabi crops, and 5% for commercial crops — government pays the rest. Coverage includes: prevented sowing due to unseasonal rain, mid-season adversity (drought, flood, pest), and post-harvest losses up to 14 days. Notify your bank or insurance company within 72 hours of any natural disaster or crop damage. Document all losses with dated photographs, field area, and revenue records. Visit nearest Common Service Center (CSC) for enrollment if bank is far.',
            'crop_type': 'All Crops', 'season': 'All seasons'
        },
        {
            'title': 'Vermicompost — Making Quality Organic Fertilizer on Farm',
            'content': 'Build a vermicompost pit (3m x 1m x 0.75m) in shade. Add crop residue, vegetable waste, and cow dung in layers. Maintain 60% moisture and cool temperature. Stock with Eisenia fetida or Lumbricus rubellus earthworms (2 kg per pit). Harvest finished vermicompost in 45 to 60 days — dark, crumbly, earthworm-cast material. Apply 3 to 5 tonnes per ha — provides NPK plus growth hormones, beneficial microbes, and enzymes. Regular vermicompost use improves soil structure, water holding capacity, and reduces chemical fertilizer need by 25 to 30%.',
            'crop_type': 'All Crops', 'season': 'All seasons'
        },
    ]

    for data in tips_data:
        CropTip.objects.get_or_create(title=data['title'], defaults=data)


class Migration(migrations.Migration):
    dependencies = [
        ('farming', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, migrations.RunPython.noop),
    ]
