from django.db import migrations


def clear_and_reseed(apps, schema_editor):
    Threat = apps.get_model('farming', 'Threat')
    CropTip = apps.get_model('farming', 'CropTip')

    # Clear all existing data
    Threat.objects.all().delete()
    CropTip.objects.all().delete()

    # =========================================================
    # WILDLIFE — 20 entries, Pan India
    # =========================================================
    wildlife = [
        {
            'name': 'Wild Boar',
            'category': 'wildlife',
            'icon': '🐗',
            'severity': 'critical',
            'season': 'Year-round; most active October–March',
            'affected_crops': 'Wheat, Rice, Sugarcane, Maize, Potato, Groundnut, Cassava, Sweet Potato',
            'description': (
                'Wild boars cause severe damage by uprooting crops and trampling fields across nearly every '
                'Indian state. They dig up roots, eat tubers, and trample standing crops. Most active at night, '
                'a single sounder can devastate an entire field within hours. Highly prevalent in UP, MP, '
                'Jharkhand, Odisha, Karnataka, and Kerala.'
            ),
            'prevention_methods': (
                '1. Install solar-powered electric fencing around field boundaries\n'
                '2. Dig V-shaped trenches (3 ft wide, 3 ft deep) along borders\n'
                '3. Set up motion-activated alarm lights at night\n'
                '4. Spray chili-garlic repellent solution on crop borders\n'
                '5. Community night-watch programs with searchlights and drums\n'
                '6. Plant thorny hedges (babool, keekar) as natural barriers'
            ),
            'treatment': (
                'Contact local Forest Department for trap-and-relocate operations. Apply chili-garlic paste '
                'on field edges. Coordinate with neighboring farmers for community-level control drives.'
            ),
        },
        {
            'name': 'Nilgai (Blue Bull)',
            'category': 'wildlife',
            'icon': '🦌',
            'severity': 'critical',
            'season': 'Rabi season (October–March)',
            'affected_crops': 'Wheat, Mustard, Barley, Vegetables, Sugarcane, Peas, Lentils',
            'description': (
                'Nilgai are the largest Asian antelopes and a top crop pest in North and Central India — UP, '
                'Bihar, Rajasthan, Haryana, MP. A herd can consume or trample an entire wheat or mustard field '
                'overnight. Protected under the Wildlife Protection Act, so lethal control requires permits.'
            ),
            'prevention_methods': (
                '1. Erect tall fencing (minimum 6–8 feet) with barbed-wire top\n'
                '2. Hang human hair bundles or lion/tiger dung sachets around borders\n'
                '3. Use scarecrows fitted with shiny reflective strips and wind-chimes\n'
                '4. Apply bitter neem oil spray on crop foliage\n'
                '5. Community watch patrols with drums and lanterns\n'
                '6. Plant unpalatable border crops like lemongrass or mint'
            ),
            'treatment': (
                'Apply neem-based repellents on crop borders regularly. Some states now allow culling permits — '
                'contact District Collector. Coordinate community Nilgai drives at night during critical crop periods.'
            ),
        },
        {
            'name': 'Indian Elephant',
            'category': 'wildlife',
            'icon': '🐘',
            'severity': 'critical',
            'season': 'Year-round; peaks June–November (Kharif season)',
            'affected_crops': 'Rice, Sugarcane, Banana, Maize, Jackfruit, Mango, Coconut, Finger Millet',
            'description': (
                'Elephants raid crops in forest-fringe areas of Assam, West Bengal, Odisha, Kerala, Tamil Nadu, '
                'Karnataka, and Jharkhand. A single herd can destroy hectares of crops in one night. One of the '
                'most destructive wildlife threats in India, causing both enormous crop loss and human casualties.'
            ),
            'prevention_methods': (
                '1. Install bee-fence barriers — elephants fear bees, proven highly effective in South India\n'
                '2. Use chili-smoke fires and chili-dung briquettes along field borders\n'
                '3. Dig wide deep trenches (1.5 m deep × 2 m wide) on migration corridors\n'
                '4. Solar-powered electric fences certified for elephant deterrence\n'
                '5. Early-warning mobile alert systems using trip-wires and sensors\n'
                '6. Form community Rapid Response Teams with drums and torches'
            ),
            'treatment': (
                'Immediately contact local Forest Department or Wildlife Division. NEVER confront elephants '
                'directly. Apply for crop loss compensation under state government schemes. Document all losses '
                'with photographs and a revenue panchnama for claim filing.'
            ),
        },
        {
            'name': 'Monkeys (Rhesus & Bonnet Macaque)',
            'category': 'wildlife',
            'icon': '🐒',
            'severity': 'high',
            'season': 'Year-round; worst during fruit-ripening season',
            'affected_crops': 'Mango, Guava, Banana, Apple, Vegetables, Maize, Sunflower, Groundnut',
            'description': (
                'Monkeys are a serious threat to orchards, vegetable gardens, and grain crops across India. '
                'They steal ripe fruits, break branches, and contaminate produce. Particularly severe in '
                'Himachal Pradesh, Uttarakhand, UP, Maharashtra, and Tamil Nadu. Troop raids can strip '
                'orchards bare within hours.'
            ),
            'prevention_methods': (
                '1. Employ langur (hanuman monkey) deterrence — their presence naturally repels macaques\n'
                '2. Install stainless steel wire mesh nets over orchards\n'
                '3. Use rubber snake or owl effigies placed at field entry points\n'
                '4. Stretch taut wire lines above orchards to block aerial travel routes\n'
                '5. Scare with loud firecrackers or recorded predator distress calls\n'
                '6. Smear bitter neem paste on tree trunks'
            ),
            'treatment': (
                'Motion-sensor water sprinklers and community monkey brigades during harvest are most effective. '
                'Report to Animal Husbandry Department for sterilization programs where available.'
            ),
        },
        {
            'name': 'Wild Gaur (Indian Bison)',
            'category': 'wildlife',
            'icon': '🐂',
            'severity': 'critical',
            'season': 'Year-round; peaks in dry season when forest food is scarce',
            'affected_crops': 'Rice, Sugarcane, Maize, Banana, Coconut, Coffee, Cardamom, Tea',
            'description': (
                'The world\'s largest bovine, wild gaur raid crops in forest-fringe areas of South India, '
                'Northeast India, and Central India. A single animal can destroy a large field area by '
                'trampling alone. Common threat in coffee and tea estates of Karnataka, Kerala, and Tamil Nadu.'
            ),
            'prevention_methods': (
                '1. Deep wide trench barriers (1.5 m deep × 2 m wide) around fields\n'
                '2. Solar electric fencing with a 5–7 joule energizer rated for large animals\n'
                '3. Bright motion-sensor floodlights covering all approach paths\n'
                '4. Controlled fire-lines at estate boundaries at night\n'
                '5. Loud alarm systems triggered by motion sensors'
            ),
            'treatment': (
                'Contact State Forest Department immediately. Do not attempt to scare large animals alone. '
                'File compensation claims with full revenue documentation and photographs.'
            ),
        },
        {
            'name': 'Spotted Deer (Chital)',
            'category': 'wildlife',
            'icon': '🦌',
            'severity': 'medium',
            'season': 'Year-round; peak during early crop growth stages',
            'affected_crops': 'Rice, Wheat, Vegetables, Groundnut, Soybean, Pulses, Sugarcane',
            'description': (
                'Spotted deer graze on young crop seedlings and tender shoots in fields adjoining forests and '
                'protected areas. Common in forest-fringe states including MP, Maharashtra, Odisha, AP, '
                'Telangana, and Karnataka. Most active at dawn and dusk.'
            ),
            'prevention_methods': (
                '1. Install 5–6 ft fencing with barbed wire top layer around fields\n'
                '2. Place thorny branches along field boundaries as low-cost barrier\n'
                '3. Motion-sensor lights at night covering all field edges\n'
                '4. Apply predator urine or dung near field borders\n'
                '5. Community patrol at dawn and dusk when deer are most active'
            ),
            'treatment': (
                'Contact Forest Department for population management in high-density areas. '
                'Apply for damage compensation under state wildlife compensation schemes with documentation.'
            ),
        },
        {
            'name': 'Porcupine (Indian Crested)',
            'category': 'wildlife',
            'icon': '🦔',
            'severity': 'medium',
            'season': 'Year-round; most active at night during dry months',
            'affected_crops': 'Potato, Sweet Potato, Cassava, Onion, Carrot, Groundnut, Sugarcane roots',
            'description': (
                'Porcupines dig up roots, tubers, bulbs, and root vegetables at night causing extensive '
                'underground damage that is often invisible until the plant wilts. Widespread across India. '
                'Their burrows also destabilize field bunds and irrigation channels.'
            ),
            'prevention_methods': (
                '1. Lay wire mesh just below soil surface around root crop beds\n'
                '2. Install buried metal sheet barriers 2 ft deep around field perimeter\n'
                '3. Set cage traps at burrow entrances at dusk\n'
                '4. Maintain clean field borders without shrub cover for hiding\n'
                '5. Smoke out burrows with sulfur sticks (keep away from crops)'
            ),
            'treatment': (
                'Cage trap and relocate with Forest Department permission. Fill and compact burrow '
                'entrances to block re-entry. Apply repellent granules near active burrow sites.'
            ),
        },
        {
            'name': 'Indian Hare & Wild Rabbit',
            'category': 'wildlife',
            'icon': '🐇',
            'severity': 'low',
            'season': 'Year-round; most damaging during seedling establishment stage',
            'affected_crops': 'Vegetables, Wheat seedlings, Groundnut, Pulses, Carrot, Cabbage, Cauliflower',
            'description': (
                'Hares and rabbits are widespread in agricultural areas across India. They damage young '
                'seedlings, vegetable leaves, and tender shoots. Common in dryland areas of Rajasthan, '
                'Gujarat, and Central India. Damage is heaviest at the seedling stage before canopy closure.'
            ),
            'prevention_methods': (
                '1. Install fine mesh wire (chicken wire) fencing around vegetable plots\n'
                '2. Apply blood meal or predator urine spray around field edges\n'
                '3. Use live cage traps along known animal runways\n'
                '4. Remove brush piles and tall grass cover near fields\n'
                '5. Intercrop with strong-smelling herbs like garlic and onion as border'
            ),
            'treatment': (
                'Live cage traps and relocation is the most humane method. Community hunting drives with '
                'Forest Department permission. Protect seedling areas with physical mesh barriers until canopy closes.'
            ),
        },
        {
            'name': 'Peafowl & Jungle Fowl',
            'category': 'wildlife',
            'icon': '🦚',
            'severity': 'medium',
            'season': 'Year-round; peaks at sowing and harvest time',
            'affected_crops': 'Groundnut, Pulses, Sunflower, Maize, Sorghum, Vegetables, newly sown seeds',
            'description': (
                'Peacocks and jungle fowl scratch the soil, eat newly sown seeds, young seedlings, and '
                'ripening grain. Peacocks are fully protected under Indian law and cannot be harmed. '
                'Particularly severe in Rajasthan, Gujarat, MP, Maharashtra, and UP — states with large '
                'peacock populations.'
            ),
            'prevention_methods': (
                '1. Use gas-powered automatic bird banger guns on programmable timers\n'
                '2. Stretch shiny reflective aluminium tape over crop rows in parallel lines\n'
                '3. Hang old CDs or foil strips on strings above crop canopy\n'
                '4. Set up motion-triggered audio systems playing predator calls\n'
                '5. Cover newly sown fields with fine shade net until germination is complete'
            ),
            'treatment': (
                'Only non-lethal deterrents are legal for peacocks — any harm is a criminal offence. '
                'Coordinate with Forest Department for management guidance. Cover seeds after sowing to prevent feeding.'
            ),
        },
        {
            'name': 'Jackals & Foxes',
            'category': 'wildlife',
            'icon': '🦊',
            'severity': 'low',
            'season': 'Year-round; most active December–March (breeding season)',
            'affected_crops': 'Watermelon, Muskmelon, Grapes, Guava, Vegetables, Poultry',
            'description': (
                'Jackals and foxes raid vegetable gardens, fruit orchards, and small livestock farms across '
                'India. They are skilled at digging under fences and attack soft fruits on the ground. '
                'Common nuisance in peri-urban farming areas and dryland regions.'
            ),
            'prevention_methods': (
                '1. Bury wire mesh fencing at least 1.5 ft below ground to prevent digging under\n'
                '2. Motion-triggered alarm lights covering all night entry points\n'
                '3. Install audio deterrent devices along field edges\n'
                '4. Eliminate hiding spots — tall grass and brush near fields\n'
                '5. Large guard dogs (Bully Kutta, Gaddi breed) are highly effective deterrents'
            ),
            'treatment': (
                'Cage traps and relocation with Forest Department approval. '
                'Regular patrol during evening and early morning hours.'
            ),
        },
        {
            'name': 'Birds (Parrots, Munias & Sparrows)',
            'category': 'wildlife',
            'icon': '🦜',
            'severity': 'high',
            'season': 'Ripening and harvest season: September–November and March–May',
            'affected_crops': 'Sunflower, Jowar, Bajra, Rice, Grapes, Guava, Pomegranate, Maize',
            'description': (
                'Flocks of rose-ringed parakeets, munias, baya weavers, and house sparrows attack ripening '
                'grain and fruits causing massive losses. A large flock can strip a sunflower or bajra field '
                'bare within days. Present across all of India in both irrigated and dryland crop areas.'
            ),
            'prevention_methods': (
                '1. Stretch bird exclusion netting over the entire crop canopy area\n'
                '2. Hang reflective tape and old CDs on strings at 3 ft intervals across field\n'
                '3. Set up automatic gas-powered bird bangers on programmable timers\n'
                '4. Use kite-shaped hawk effigies mounted on long poles to scare small birds\n'
                '5. Employ bird scarers (persons) during ripening season, especially mornings\n'
                '6. Play recorded predator calls through timed speakers'
            ),
            'treatment': (
                'Bird netting remains the most reliable and permanent solution. Community action needed for '
                'large infestations across multiple fields. Early harvest is advisable if bird pressure is severe.'
            ),
        },
        {
            'name': 'Rats & Field Rodents',
            'category': 'wildlife',
            'icon': '🐀',
            'severity': 'high',
            'season': 'Year-round; critical at harvest and storage periods',
            'affected_crops': 'Rice, Wheat, Sugarcane, Groundnut, Stored Grains, Potato',
            'description': (
                'The bandicoot rat, Indian field rat, and house rat cause enormous pre- and post-harvest losses '
                'across India. Rats cut plant stems, dig up seeds, attack stored grain, and burrow into bunds '
                'causing irrigation water loss. Estimated to destroy 15–20% of stored grain in some states annually.'
            ),
            'prevention_methods': (
                '1. Deep plowing after harvest to destroy burrows and expose stored food\n'
                '2. Community rat control drives before each sowing season\n'
                '3. Install zinc phosphide or bromodiolone bait stations at burrow entrances\n'
                '4. Encourage natural predators — erect barn owl nest boxes in fields\n'
                '5. Maintain clean field bunds — remove tall grass that provides cover\n'
                '6. Store grain only in metal or concrete rat-proof containers'
            ),
            'treatment': (
                'Zinc phosphide (2%) bait in T-shaped bait stations along all field bunds. Fumigation of '
                'active burrows. Snap traps at burrow entrances overnight. Install barn owl boxes to '
                'encourage natural predation — one pair of barn owls kills 1,000+ rats per year.'
            ),
        },
        {
            'name': 'Sloth Bear',
            'category': 'wildlife',
            'icon': '🐻',
            'severity': 'critical',
            'season': 'Year-round; peaks March–May (mango season) and post-monsoon',
            'affected_crops': 'Sugarcane, Maize, Mango, Jackfruit, Honey Bee colonies',
            'description': (
                'Sloth bears raid sugarcane, maize, and fruit orchards in forest-fringe areas of Jharkhand, '
                'Odisha, Chhattisgarh, MP, Maharashtra, and Karnataka. They also destroy beehives in orchards. '
                'Highly dangerous to farm workers — approach without warning and attack unpredictably.'
            ),
            'prevention_methods': (
                '1. Solar electric fencing — the single most effective deterrent for bears\n'
                '2. Beehive fences on field edges (bears fear bee stings intensely)\n'
                '3. Motion-sensor floodlights covering all approach paths from forest edge\n'
                '4. Community watch groups with noise-making equipment and searchlights\n'
                '5. Never leave harvested fruits or sugarcane in the field overnight'
            ),
            'treatment': (
                'Contact Forest Department immediately — bears are Schedule I protected species. No lethal '
                'control is legal under any circumstances. Apply for crop loss compensation under state '
                'wildlife damage compensation schemes with full documentation.'
            ),
        },
        {
            'name': 'Leopard',
            'category': 'wildlife',
            'icon': '🐆',
            'severity': 'high',
            'season': 'Year-round; peaks when natural prey is scarce',
            'affected_crops': 'Indirect impact — livestock loss leads to farmland abandonment',
            'description': (
                'Leopards increasingly raid livestock near forest edges across India — from the Himalayas to '
                'South India and Western Ghats. Though they rarely attack crops directly, their presence '
                'disrupts farming operations, forces farmers to abandon night field work, and causes heavy '
                'livestock losses that affect farm income and draught power.'
            ),
            'prevention_methods': (
                '1. Secure all livestock in reinforced enclosures with a solid roof at night\n'
                '2. Motion-triggered alarms around farm boundaries and livestock sheds\n'
                '3. Keep large guard dogs (Bully Kutta, Gaddi) for livestock protection\n'
                '4. Bright security lighting around the entire farmstead and shed area\n'
                '5. Coordinate with Forest Department for camera trapping and population monitoring'
            ),
            'treatment': (
                'Contact Forest Department immediately for any leopard sightings near habitation. '
                'Apply for livestock loss compensation under state schemes. '
                'Never attempt to trap, harm, or confront — Schedule I protected species.'
            ),
        },
        {
            'name': 'Sambhar & Barking Deer',
            'category': 'wildlife',
            'icon': '🦌',
            'severity': 'high',
            'season': 'Year-round; peaks during spring planting and autumn harvest',
            'affected_crops': 'Apple, Pear, Plum, Maize, Potato, Vegetables, Rice (terrace fields)',
            'description': (
                'Sambhar and barking deer cause significant crop damage in hilly states — Himachal Pradesh, '
                'Uttarakhand, J&K, all Northeastern states, and Western Ghats regions. They are most damaging '
                'to high-value horticultural crops cultivated on terraced hillside farms.'
            ),
            'prevention_methods': (
                '1. Install 6–8 ft high chain-link or welded mesh wire fencing\n'
                '2. Solar electric fence with multiple strands at 30, 60, 90, 120 cm heights\n'
                '3. Motion-sensor lights and alarm systems covering all field approaches\n'
                '4. Grow thorny hedges (wild rose, berberis) on exposed field borders\n'
                '5. Community watch especially at dawn, dusk, and through the night'
            ),
            'treatment': (
                'Contact State Wildlife Department. Compensation available under state schemes for '
                'horticultural crop losses. Document all losses with dated photo evidence and revenue records.'
            ),
        },
        {
            'name': 'Wild Pig (Sus scrofa — Forest Areas)',
            'category': 'wildlife',
            'icon': '🐖',
            'severity': 'high',
            'season': 'Post-monsoon and winter: August–February',
            'affected_crops': 'Maize, Potato, Cassava, Groundnut, Vegetables, Pulses',
            'description': (
                'Forest-dwelling wild pigs (distinct from feral domestic pigs) are a major problem in '
                'Northeast India, Jharkhand, Chhattisgarh, Odisha, and Andaman Islands. They move in '
                'sounders of 6–20 animals and can root up entire field sections overnight. '
                'Tribal and forest-edge communities are most severely affected.'
            ),
            'prevention_methods': (
                '1. Communal electric fence enclosing entire village farm cluster is most effective\n'
                '2. Deep bund trenches around individual fields\n'
                '3. Chili-dung smoke fires lit at forest edge at dusk\n'
                '4. Acoustic deterrents — radios or alarm systems left running through the night\n'
                '5. Guard dogs posted at field boundaries overnight'
            ),
            'treatment': (
                'Traditional community pig drives with forest department knowledge. '
                'Contact Tribal Welfare Department or Forest Department for support and compensation. '
                'Some states permit licensed hunting in designated areas.'
            ),
        },
        {
            'name': 'Mongoose & Civets',
            'category': 'wildlife',
            'icon': '🦡',
            'severity': 'low',
            'season': 'Year-round; mainly nocturnal',
            'affected_crops': 'Poultry, Eggs, Watermelon, Muskmelon, Papaya',
            'description': (
                'Mongooses and civets raid poultry houses, destroy melons, and damage papaya on the ground. '
                'While less damaging than large mammals, they can cause significant losses in poultry-integrated '
                'farming systems and kitchen gardens. Common across peninsular India.'
            ),
            'prevention_methods': (
                '1. Secure poultry houses with fine wire mesh including on the floor\n'
                '2. Collect ground-fallen fruits daily before nightfall\n'
                '3. Cage traps baited with eggs near known entry points\n'
                '4. Remove brush piles and dense vegetation near farm buildings'
            ),
            'treatment': (
                'Live cage traps and relocation. Both species are protected wildlife — no lethal action is legal. '
                'Strengthen poultry enclosures as primary prevention strategy.'
            ),
        },
        {
            'name': 'Flamingos & Water Birds (Rice Paddies)',
            'category': 'wildlife',
            'icon': '🦩',
            'severity': 'medium',
            'season': 'Monsoon and post-monsoon: July–November',
            'affected_crops': 'Transplanted Rice, Fish Ponds, Shrimp Farms',
            'description': (
                'Large flocks of flamingos, cranes, egrets, and other water birds land in flooded rice paddies '
                'and fish ponds causing direct crop and fish damage. Problem areas include coastal Odisha, '
                'Kerala backwaters, coastal Tamil Nadu, and Gujarat (Rann region). '
                'All water birds are legally protected in India.'
            ),
            'prevention_methods': (
                '1. Install bird netting over fish pond surfaces\n'
                '2. Stretch nylon lines criss-cross above paddy nurseries\n'
                '3. Use scarecrow effigies and reflective windmills in paddy fields\n'
                '4. Employ field watchmen with noise-making devices during peak migration\n'
                '5. Coordinate with local bird sanctuary authorities for management advice'
            ),
            'treatment': (
                'All actions must be non-lethal — all water birds are protected under the Wildlife Protection Act. '
                'Contact State Wetland Authority or Forest Department for guidance and compensation claims.'
            ),
        },
        {
            'name': 'Nilgai & Sambar in Tea Gardens (Northeast)',
            'category': 'wildlife',
            'icon': '🦌',
            'severity': 'high',
            'season': 'Year-round in Assam, West Bengal, and Arunachal Pradesh',
            'affected_crops': 'Tea, Rubber, Cardamom, Orange (Nagpur variety in NE)',
            'description': (
                'In Northeast India, large deer species including sambar and hog deer browse on tea bushes '
                'and young rubber trees inside estates adjoining forest reserves. They cause significant '
                'pruning damage to young tea plants set back by 6–12 months of growth.'
            ),
            'prevention_methods': (
                '1. Perimeter fencing of entire estate block with 7 ft deer fencing\n'
                '2. Night patrolling by anti-poaching and wildlife watch teams\n'
                '3. Motion-sensor lights along estate-forest boundary\n'
                '4. Collaboration with Forest Department on corridor management'
            ),
            'treatment': (
                'Document damage thoroughly with GPS coordinates and dated photos. '
                'File compensation claims with State Tea Board and Forest Department. '
                'Engage with Wildlife Institute of India for long-term corridor planning.'
            ),
        },
        {
            'name': 'One-Horned Rhinoceros (Assam)',
            'category': 'wildlife',
            'icon': '🦏',
            'severity': 'critical',
            'season': 'Year-round; peaks post-flood when rhinos leave Kaziranga National Park',
            'affected_crops': 'Rice, Mustard, Wheat, Lentil, Vegetables',
            'description': (
                'The Indian one-horned rhinoceros is a major crop raider in Assam, particularly in villages '
                'bordering Kaziranga National Park. After monsoon floods, rhinos move into agricultural land '
                'in large numbers. Their sheer size causes enormous trampling damage beyond what they eat. '
                'Also highly dangerous to human life.'
            ),
            'prevention_methods': (
                '1. Multi-strand high-voltage electric fence (forest department assisted)\n'
                '2. Deep wide trenches along village-forest boundary\n'
                '3. Community watch towers with searchlights and warning bells\n'
                '4. Coordinated early warning system with Kaziranga park authorities\n'
                '5. Avoid walking to fields at night during post-flood rhino movement season'
            ),
            'treatment': (
                'Contact Kaziranga National Park authority immediately. Assam government has a dedicated '
                'Human-Wildlife Conflict compensation scheme — file within 72 hours with documentation. '
                'NEVER attempt to drive away rhinos personally — extremely dangerous.'
            ),
        },
        {
            'name': 'Feral Cattle & Stray Animals',
            'category': 'wildlife',
            'icon': '🐄',
            'severity': 'high',
            'season': 'Year-round; worst during Kharif crop ripening (September–November)',
            'affected_crops': 'Wheat, Rice, Vegetables, Sugarcane, Soybean, Pulses',
            'description': (
                'Abandoned and feral cattle have become a massive agricultural problem across North and '
                'Central India following state-level bans on cattle slaughter. UP, MP, Rajasthan, and '
                'Bihar are most severely affected. Large herds of stray cattle destroy crops with no '
                'legal mechanism for lethal control, devastating small and marginal farmers most severely.'
            ),
            'prevention_methods': (
                '1. Strong fencing with barbed wire around all agricultural fields\n'
                '2. Community "go-shala" (cattle shelter) maintenance to contain strays\n'
                '3. Night watchmen posted during standing crop period\n'
                '4. Report repeated damage to District Magistrate for cattle pound action\n'
                '5. Thorny hedge planting for long-term low-cost fencing'
            ),
            'treatment': (
                'Lodge formal complaint with local police or district administration. State governments '
                'have designated Gaushala facilities — file for cattle removal and compensation. '
                'Approach gram panchayat for community-level cattle management resolution.'
            ),
        },
    ]

    # =========================================================
    # PESTS & INSECTS — 22 entries, Pan India
    # =========================================================
    pests = [
        {
            'name': 'Aphids (Multiple Species)',
            'category': 'pest',
            'icon': '🦗',
            'severity': 'high',
            'season': 'February–April (Rabi crops); October–December (vegetables)',
            'affected_crops': 'Wheat, Mustard, Cotton, Potato, Okra, Chilli, Citrus, Pulses, Vegetables',
            'description': (
                'Aphids are tiny soft-bodied sucking insects that colonize growing tips and leaf undersides. '
                'They secrete honeydew causing black sooty mold. More importantly, they vector devastating '
                'viral diseases — wheat streak mosaic, mustard mosaic, potato leaf roll, and citrus tristeza. '
                'Found in all states on virtually every crop.'
            ),
            'prevention_methods': (
                '1. Spray neem oil solution (5 ml/L water + 2 ml liquid soap) every 10 days\n'
                '2. Release natural predators — ladybird beetles, lacewings, syrphid fly larvae\n'
                '3. Install yellow sticky traps for monitoring and mass trapping (25 per ha)\n'
                '4. Avoid excess nitrogen fertilization — promotes soft growth aphids prefer\n'
                '5. Intercrop with coriander, fennel, or marigold to attract beneficial insects\n'
                '6. Remove and destroy heavily infested plant parts immediately'
            ),
            'treatment': (
                'Spray imidacloprid 17.8 SL (0.5 ml/L) or dimethoate 30 EC (1 ml/L). '
                'For organic farming: Azadirachtin-based neem pesticide. '
                'Rotate insecticide classes with every spray to prevent resistance build-up.'
            ),
        },
        {
            'name': 'Fall Army Worm (Spodoptera frugiperda)',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'critical',
            'season': 'June–November (Kharif); spreading to Rabi maize areas',
            'affected_crops': 'Maize (primary), Sorghum, Sugarcane, Rice, Wheat, Cotton',
            'description': (
                'Invasive pest that entered India in 2018 and spread to all states within 2 years. FAW '
                'caterpillars bore into the whorl and developing cob of maize causing 30–70% losses. '
                'Identified by a characteristic inverted Y on the head capsule and 4 black dots on the last '
                'abdominal segment. One of the most dangerous new threats to Indian agriculture.'
            ),
            'prevention_methods': (
                '1. Scout plant whorls weekly from emergence stage — look for feeding damage\n'
                '2. Install pheromone traps (8–10 per hectare) for adult moth monitoring\n'
                '3. Apply Bt (Bacillus thuringiensis var. kurstaki) spray against early-instar larvae\n'
                '4. Conserve parasitoid wasps — avoid unnecessary broad-spectrum insecticide use\n'
                '5. Use FAW-resistant maize varieties wherever available in your state\n'
                '6. Timely sowing to avoid peak infestation window (July–August)'
            ),
            'treatment': (
                'Apply spinetoram 11.7% SC (0.5 ml/L), chlorantraniliprole 18.5 SC (0.4 ml/L), or '
                'emamectin benzoate 5 SG (0.4 g/L). Target early-instar larvae in whorls. '
                'Evening application is most effective when larvae are most active.'
            ),
        },
        {
            'name': 'Whitefly & Cotton Leaf Curl Virus',
            'category': 'pest',
            'icon': '🦟',
            'severity': 'critical',
            'season': 'May–October; critical peak August–September',
            'affected_crops': 'Cotton, Tomato, Chilli, Okra, Brinjal, Cucurbits, Cassava, Tobacco',
            'description': (
                'Whitefly (Bemisia tabaci) is among India\'s most damaging vector pests. It transmits '
                'Cotton Leaf Curl Virus (CLCuV), Tomato Yellow Leaf Curl Virus, and other geminiviruses '
                'that have no cure. Even 1–2 whiteflies per leaf can transmit virus. Present across all '
                'states; most devastating in Punjab, Haryana, Rajasthan, and AP cotton belts.'
            ),
            'prevention_methods': (
                '1. Install yellow sticky traps (25–30 per ha) for monitoring and mass trapping\n'
                '2. Use UV-blocking silver reflective mulches — physically repels whitefly\n'
                '3. Spray neem oil (5 ml/L) or NSKE 5% preventively every 15 days\n'
                '4. Remove and destroy virus-infected plants immediately — no chemical cure exists\n'
                '5. Avoid planting cotton or tomato near older infested crops\n'
                '6. Use resistant varieties wherever available in your state'
            ),
            'treatment': (
                'Spray thiamethoxam 25 WG (0.3 g/L) or spiromesifen 22.9 SC (0.9 ml/L). '
                'Strictly rotate insecticide classes every single spray. '
                'For virus-infected plants: uproot and burn — no chemical treatment reverses infection.'
            ),
        },
        {
            'name': 'Brown Plant Hopper (BPH)',
            'category': 'pest',
            'icon': '🦗',
            'severity': 'critical',
            'season': 'Kharif rice season: July–November',
            'affected_crops': 'Rice (all varieties; resistant varieties exist)',
            'description': (
                'BPH is the most devastating insect pest of rice in India, causing "hopper burn" — '
                'circular dead patches visible from a distance. It vectors Grassy Stunt and Ragged Stunt '
                'viruses. Insecticide-induced resurgence is a serious problem — killing natural enemies '
                'makes BPH outbreaks far worse. Most damaging in WB, Odisha, Tamil Nadu, and Andhra Pradesh.'
            ),
            'prevention_methods': (
                '1. Use BPH-resistant varieties: IR64, Swarna Sub1, Samba Mahsuri, MTU 7029\n'
                '2. Avoid excessive nitrogen — promotes lush growth BPH prefers\n'
                '3. Maintain proper plant spacing for air circulation and natural enemy activity\n'
                '4. Practice alternate wetting and drying irrigation\n'
                '5. Conserve spiders, mirid bugs, and other natural enemies\n'
                '6. Install light traps for population monitoring from July'
            ),
            'treatment': (
                'Spray buprofezin 25 SC (1.25 ml/L) or pymetrozine 50 WG (0.6 g/L) directed at plant base. '
                'NEVER spray synthetic pyrethroids — they eliminate natural enemies and cause severe BPH resurgence.'
            ),
        },
        {
            'name': 'Rice & Sugarcane Stem Borer',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'high',
            'season': 'Kharif: July–October; Sugarcane: year-round',
            'affected_crops': 'Rice, Sugarcane, Maize, Sorghum, Bajra',
            'description': (
                'Stem borers are the most widespread and consistently damaging pests of rice and sugarcane. '
                'Larvae bore into stems causing "dead heart" in vegetative stage and "white ear" at booting '
                'in rice — both result in complete tiller loss with no grain production. Multiple generations '
                'occur each season, making continuous monitoring essential.'
            ),
            'prevention_methods': (
                '1. Use light traps to catch adult moths and monitor population build-up\n'
                '2. Clip and destroy egg masses found on leaves during regular scouting\n'
                '3. Release Trichogramma japonicum egg parasitoid (50,000 per ha, twice)\n'
                '4. Avoid dense planting — maintain recommended spacing for air movement\n'
                '5. Remove and burn all stubble after harvest — destroys overwintering larvae\n'
                '6. Synchronize planting across village to break continuous pest cycle'
            ),
            'treatment': (
                'Apply cartap hydrochloride 4G (18 kg/ha) or chlorantraniliprole 0.4G (10 kg/ha) granules '
                'into whorls or irrigation water. Spray chlorpyrifos or monocrotophos at early borer stage detection.'
            ),
        },
        {
            'name': 'Thrips (Chilli & Onion Thrips)',
            'category': 'pest',
            'icon': '🦟',
            'severity': 'high',
            'season': 'February–May and September–December; year-round in South India',
            'affected_crops': 'Chilli, Cotton, Onion, Potato, Grapes, Mango, Cucumber, Banana, Rose',
            'description': (
                'Thrips rasp and suck plant cell contents causing silvery streaks, leaf curl, and '
                'deformed fruits and flowers. They vector Tomato Spotted Wilt Virus (TSWV) and '
                'Iris Yellow Spot Virus (IYSV in onion) — both incurable. Thrive in hot, dry '
                'conditions. Major economic pest of chilli, onion, and mango across India.'
            ),
            'prevention_methods': (
                '1. Install blue sticky traps for monitoring — 25 per ha from planting\n'
                '2. Spray neem oil 3000 ppm (5 ml/L) preventively every 15 days\n'
                '3. Maintain soil moisture — thrips populations explode in drought stress conditions\n'
                '4. Remove and destroy infested growing tips showing silvering or curling\n'
                '5. Install reflective silver mulch to repel thrips from leaf undersides\n'
                '6. Avoid planting near old onion or chilli crop residue'
            ),
            'treatment': (
                'Spray spinosad 45 SC (0.3 ml/L) or imidacloprid 70 WG (0.3 g/L). '
                'Rotate chemical groups with every spray — thrips develop resistance rapidly. '
                'TSWV-infected plants must be removed and destroyed immediately.'
            ),
        },
        {
            'name': 'Subterranean Termites',
            'category': 'pest',
            'icon': '🐜',
            'severity': 'high',
            'season': 'Year-round; most damaging during dry periods',
            'affected_crops': 'Wheat, Maize, Sugarcane, Cotton, Groundnut, Jowar, Fruit trees',
            'description': (
                'Subterranean termites (Odontotermes spp.) attack crop roots and stems from below, '
                'causing sudden plant wilting and death. Damage is invisible until the plant collapses '
                'from below. Most destructive in sandy soils and dry regions of Rajasthan, Gujarat, '
                'Madhya Pradesh, and the Deccan plateau dryland areas.'
            ),
            'prevention_methods': (
                '1. Deep summer plowing (grishm jotai) to expose and destroy termite colonies\n'
                '2. Avoid incorporating undecomposed organic matter into soil\n'
                '3. Treat seeds with chlorpyrifos 20 EC (5 ml/kg seed) before sowing\n'
                '4. Apply only well-composted FYM — raw manure actively attracts termites\n'
                '5. Maintain proper field hygiene — remove dead wood, roots, and stumps\n'
                '6. Flood irrigation when termite activity is first detected'
            ),
            'treatment': (
                'Drench soil with chlorpyrifos 20 EC (3 ml/L) around affected plant bases. '
                'Treat seeds with imidacloprid 600 FS (3 ml/kg). '
                'Apply phorate 10G (5 kg/ha) in soil at sowing in high-risk fields.'
            ),
        },
        {
            'name': 'Desert & Migratory Locust',
            'category': 'pest',
            'icon': '🦗',
            'severity': 'critical',
            'season': 'June–November; outbreak years are irregular',
            'affected_crops': 'All crops — wheat, rice, cotton, vegetables, orchards, fodder — nothing is spared',
            'description': (
                'Locusts form swarms covering hundreds of square km. A 1 km² swarm contains 40 million '
                'insects that can consume 35,000 people\'s daily food. The 2020 outbreak was India\'s '
                'worst in nearly 30 years, affecting Rajasthan, Gujarat, UP, and MP with losses of thousands '
                'of crores. No individual farmer can combat a swarm alone.'
            ),
            'prevention_methods': (
                '1. Register for NCIPM and FAO Desert Locust Information Service alert system\n'
                '2. Monitor FAO locust forecasts and IMD weather bulletins during outbreak years\n'
                '3. Coordinate with District Agriculture Officer for community response planning\n'
                '4. Report any unusual grasshopper or locust sightings to Agriculture Department immediately\n'
                '5. Maintain barrier spraying infrastructure along desert borders (Rajasthan, Gujarat)'
            ),
            'treatment': (
                'Government-led aerial and ground spraying with malathion ULV or chlorpyrifos. '
                'Do not attempt individual control of swarms — contact District Agriculture Officer '
                'and State Locust Control Unit immediately upon any sighting.'
            ),
        },
        {
            'name': 'Helicoverpa (American Bollworm)',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'critical',
            'season': 'Kharif: August–November; Rabi chickpea: January–March',
            'affected_crops': 'Cotton, Chickpea, Pigeonpea, Tomato, Sunflower, Maize, Sorghum, Groundnut',
            'description': (
                'One of India\'s most economically destructive pests. Larvae bore into cotton bolls, '
                'chickpea pods, tomato fruits, and sunflower heads. Has developed resistance to '
                'organophosphates and pyrethroids. Causes thousands of crores in losses annually. '
                'Polyphagous — attacks over 180 host plant species across India.'
            ),
            'prevention_methods': (
                '1. Install pheromone traps (5 per ha) for adult moth population monitoring\n'
                '2. Apply Helicoverpa NPV spray (250 LE/ha) — highly specific biological control\n'
                '3. Release Trichogramma chilonis (1.5 lakh per ha) for egg parasitism\n'
                '4. Install light traps (1 per ha) to attract and kill adults at night\n'
                '5. Use Bt cotton varieties for built-in bollworm resistance in cotton\n'
                '6. Practice strict crop rotation — never plant host crops back-to-back'
            ),
            'treatment': (
                'Apply emamectin benzoate 5 SG (0.4 g/L), indoxacarb 14.5 SC (0.5 ml/L), or '
                'spinosad 45 SC (0.3 ml/L). Rotate chemical groups with every spray — '
                'resistance management is critical for this pest.'
            ),
        },
        {
            'name': 'Red Spider Mite',
            'category': 'pest',
            'icon': '🕷️',
            'severity': 'high',
            'season': 'February–May and September–November; worst in drought years',
            'affected_crops': 'Cotton, Brinjal, Okra, Beans, Strawberry, Rose, Papaya, Cucurbits, Tea, Groundnut',
            'description': (
                'Spider mites are arachnids — not insects — causing silvery stippling on leaves, '
                'fine webbing on the underside, and rapid leaf drop. One female produces 200 offspring '
                'in just 3 weeks. They multiply explosively in hot dry weather and develop acaricide '
                'resistance very quickly. A major problem in cotton, vegetables, and tea gardens across India.'
            ),
            'prevention_methods': (
                '1. Maintain adequate soil moisture — mites explode under drought stress\n'
                '2. Forcefully spray plain water on leaf undersides to physically dislodge mite colonies\n'
                '3. Apply neem oil spray (5 ml/L + 2 ml soap) — disrupts mite reproduction cycle\n'
                '4. Release predatory mites (Phytoseiidae family) as biological control agents\n'
                '5. Avoid broad-spectrum insecticides that destroy natural predators\n'
                '6. Scout with a 10x hand lens weekly — detect early before population explosion'
            ),
            'treatment': (
                'Apply spiromesifen 22.9 SC (0.9 ml/L), abamectin 1.8 EC (0.5 ml/L), or '
                'propargite 57 EC (2 ml/L). Strictly rotate acaricide groups with every application — '
                'never use the same product twice in a season.'
            ),
        },
        {
            'name': 'Diamondback Moth',
            'category': 'pest',
            'icon': '🦋',
            'severity': 'high',
            'season': 'October–March (Rabi vegetables)',
            'affected_crops': 'Cabbage, Cauliflower, Mustard, Radish, Knol-Khol, Broccoli, Chinese Cabbage',
            'description': (
                'Diamondback moth (DBM) is the most destructive pest of cruciferous vegetables globally. '
                'Tiny larvae scrape leaves from the underside creating a "windowpane" effect, then bore '
                'into heads and curds. It was the world\'s first insect proven to develop pesticide '
                'resistance and has now developed resistance to over 100 insecticides. Found in all Indian states.'
            ),
            'prevention_methods': (
                '1. Install pheromone traps (10 per ha) for monitoring — replace lures monthly\n'
                '2. Use Bt (Bacillus thuringiensis var. kurstaki) spray against early-instar larvae\n'
                '3. Cover young transplants with 40-mesh insect-proof net for first 3 weeks\n'
                '4. Plant yellow mustard as sacrifice trap crop border — destroy when infested\n'
                '5. Maintain a crop-free break between consecutive brassica crop cycles'
            ),
            'treatment': (
                'Apply emamectin benzoate 5 SG (0.4 g/L), chlorfenapyr 10 SC (1 ml/L), or '
                'spinosad 45 SC (0.3 ml/L). Chemical rotation is mandatory — '
                'DBM develops resistance within 2–3 generations without rotation.'
            ),
        },
        {
            'name': 'Tobacco Caterpillar (Spodoptera litura)',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'high',
            'season': 'Kharif: July–November; also in Rabi vegetable season',
            'affected_crops': 'Groundnut, Cotton, Tobacco, Soybean, Vegetables, Pulses, Ornamentals',
            'description': (
                'A highly polyphagous pest that attacks over 100 crop species. Young caterpillars '
                'feed gregariously and skeletonize entire leaves. Older solitary larvae devour complete '
                'leaves and tender fruits causing severe defoliation. Particularly damaging to groundnut, '
                'soybean, and vegetables in Central, West, and South India.'
            ),
            'prevention_methods': (
                '1. Collect and destroy egg masses and gregarious young larvae clusters by hand\n'
                '2. Apply Spodoptera litura NPV (SlNPV) spray — specific and highly effective biological control\n'
                '3. Set pheromone traps to monitor and mass-trap adult moths\n'
                '4. Install light traps (1 per ha) to attract and kill adult moths\n'
                '5. Deep plowing after crop harvest to expose pupae in soil to sun and predators'
            ),
            'treatment': (
                'Apply chlorpyrifos 20 EC (2 ml/L) or indoxacarb 14.5 SC (1 ml/L). '
                'Spray in the evening when larvae are actively feeding. '
                'For early instars, use SlNPV or Bt biological sprays for resistance management.'
            ),
        },
        {
            'name': 'Mango Mealybug',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'high',
            'season': 'December–March (nymph emergence and tree-climbing phase)',
            'affected_crops': 'Mango, Litchi, Ber, Peach, Plum, Jamun',
            'description': (
                'Mango mealybug (Drosicha mangiferae) nymphs emerge from soil in January, climb tree '
                'trunks, and suck sap from young shoots, flowers, and developing fruits. Heavy infestations '
                'cause complete flower and fruit drop. Sooty mold on honeydew further reduces fruit quality. '
                'Major pest in UP, Bihar, MP, and Maharashtra mango growing belts.'
            ),
            'prevention_methods': (
                '1. Apply sticky alkathene band (25 cm wide with petroleum grease) around trunk in December\n'
                '2. Spray chlorpyrifos 20 EC (3 ml/L) on soil around tree base in January\n'
                '3. Till soil under tree canopy in October–November to expose eggs to sun and birds\n'
                '4. Scrape bark around trunk base to remove overwintering egg masses in November\n'
                '5. Community-level action — treat all trees in the orchard/village area together'
            ),
            'treatment': (
                'Remove alkathene bands with trapped insects and destroy. '
                'Spray dimethoate 30 EC (2 ml/L) on nymphs before tree ascent. '
                'Apply profenofos if population is very high.'
            ),
        },
        {
            'name': 'Citrus Psylla & Huanglongbing (HLB)',
            'category': 'pest',
            'icon': '🦟',
            'severity': 'critical',
            'season': 'Active whenever citrus produces new leaf flush (3–4 times per year)',
            'affected_crops': 'Sweet Lime, Mandarin, Lemon, Orange, Grapefruit, Curry Leaf',
            'description': (
                'Citrus psylla (Diaphorina citri) vectors Huanglongbing — the most destructive citrus disease '
                'worldwide. Infected trees produce small, misshapen, bitter fruits and die within 5–10 years. '
                'No cure for HLB exists. Once a tree is infected, it must be removed. Now detected in several '
                'Indian citrus-growing states including Maharashtra, AP, Karnataka, and Tamil Nadu.'
            ),
            'prevention_methods': (
                '1. Source certified psylla-free planting material only from registered nurseries\n'
                '2. Spray imidacloprid or dimethoate before every new flush emergence (4–5 times per year)\n'
                '3. Quarantine all new plant material for 3 months before planting in main orchard\n'
                '4. Remove and destroy HLB-infected trees immediately — they are source of disease\n'
                '5. Release Tamarixia radiata parasitoid for biological psylla control'
            ),
            'treatment': (
                'If HLB detected: NO CURE — remove and destroy infected tree entirely, roots and all. '
                'For psylla: spray imidacloprid 17.8 SL (0.3 ml/L) or thiamethoxam 25 WG (0.3 g/L) '
                'targeting all new leaf flush emergence precisely.'
            ),
        },
        {
            'name': 'Legume Pod Borer (Maruca vitrata)',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'high',
            'season': 'August–November (Kharif pulses)',
            'affected_crops': 'Pigeonpea, Cowpea, Moth Bean, French Bean, Yardlong Bean',
            'description': (
                'Pod borer is the most damaging pest of tropical legumes in India. Larvae web together '
                'flowers and developing pods, then feed inside, destroying seeds before harvest. '
                'Causes 30–80% yield loss in susceptible varieties. Major problem in Maharashtra, AP, '
                'Karnataka, Tamil Nadu, and UP pigeonpea and cowpea growing regions.'
            ),
            'prevention_methods': (
                '1. Use resistant or tolerant legume varieties documented by ICRISAT\n'
                '2. Timely and early planting to escape peak borer pressure window\n'
                '3. Apply Maruca NPV spray at first egg hatching for biological control\n'
                '4. Install pheromone traps (5 per ha) for adult moth monitoring\n'
                '5. Intercrop with sorghum or maize as barrier rows to reduce infestation\n'
                '6. Remove and destroy webbed flower clusters and infested young pods daily'
            ),
            'treatment': (
                'Apply chlorantraniliprole 18.5 SC (0.3 ml/L) or indoxacarb 14.5 SC (0.5 ml/L). '
                'Begin spray at 50% flowering stage. Repeat at 15-day intervals until pod maturity.'
            ),
        },
        {
            'name': 'Rice Gall Midge',
            'category': 'pest',
            'icon': '🦟',
            'severity': 'high',
            'season': 'Kharif: July–September',
            'affected_crops': 'Rice (all varieties except resistant ones)',
            'description': (
                'Gall midge larvae attack the growing point of rice plants causing the characteristic '
                '"silver shoot" or "onion leaf" — a hollow tubular leaf that produces no grain. '
                'Affected tillers are completely and permanently lost. Major endemic pest in Odisha, '
                'Chhattisgarh, West Bengal, and coastal Andhra Pradesh and Tamil Nadu.'
            ),
            'prevention_methods': (
                '1. Use gall midge resistant varieties: GMR-6, Shakti, Dhanrasi, Rambha\n'
                '2. Avoid late planting — synchronize transplanting with all neighboring fields\n'
                '3. Drain and re-flood field to kill larvae at soil surface interface\n'
                '4. Install light traps to catch adult midges and monitor population build-up\n'
                '5. Apply nitrogen in split doses — avoid heavy early dose that promotes lush growth'
            ),
            'treatment': (
                'Apply carbofuran 3G granules (20 kg/ha) into flooded field water at tillering stage. '
                'Spray monocrotophos 36 SL (1.5 ml/L) when silver shoots are first noticed.'
            ),
        },
        {
            'name': 'Banana Stem Weevil',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'high',
            'season': 'Year-round in tropical banana growing regions',
            'affected_crops': 'Banana, Plantain, Ensete',
            'description': (
                'The banana rhizome weevil (Cosmopolites sordidus) is the most serious pest of banana '
                'plantations worldwide and in India. Larvae tunnel through rhizome and pseudostem causing '
                'plant lodging, reduced bunch size, and 30–60% production loss. Present in all '
                'banana-growing states: Tamil Nadu, AP, Kerala, Maharashtra, Karnataka, Bihar, and WB.'
            ),
            'prevention_methods': (
                '1. Use tissue culture banana planting material — completely free of weevil infestation\n'
                '2. Place split-stem traps near infested banana stools to attract and trap adult weevils\n'
                '3. Remove and destroy all dead pseudostems and decaying rhizome material promptly\n'
                '4. Apply carbofuran 3G in the planting hole at time of transplanting\n'
                '5. Treat rhizomes with chlorpyrifos solution before planting in new area'
            ),
            'treatment': (
                'Drench soil around banana stools with chlorpyrifos 20 EC (5 ml/L). '
                'Apply carbofuran 3G (40 g per plant) near corm. '
                'Mass trapping with lure-baited intercept traps along all field borders.'
            ),
        },
        {
            'name': 'Coffee Berry Borer',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'high',
            'season': 'Post-monsoon: October–February',
            'affected_crops': 'Arabica Coffee, Robusta Coffee',
            'description': (
                'The coffee berry borer (Hypothenemus hampei) is the world\'s most economically damaging '
                'coffee pest. Female beetles bore into berries and lay eggs inside. Infested berries drop '
                'prematurely or produce defective beans with visible borer holes. A major economic problem '
                'in all coffee estates of Karnataka, Kerala, and Tamil Nadu.'
            ),
            'prevention_methods': (
                '1. Strip-harvest promptly — never leave overripe berries on tree or fallen on ground\n'
                '2. Collect and destroy all fallen berries from ground — they harbor pupating beetles\n'
                '3. Apply Beauveria bassiana fungal biocontrol spray — approved and highly effective\n'
                '4. Install BROCAP lure traps with methanol/ethanol mixture (1 per 20 trees)\n'
                '5. Maintain 30–40% shade canopy to moderate temperature that favors borer'
            ),
            'treatment': (
                'Apply endosulfan 35 EC (1.5 ml/L) or chlorpyrifos during post-harvest critical period. '
                'Beauveria bassiana (1×10⁸ spores/ml) is the approved biopesticide of choice. '
                'Submerge harvested berries before pulping to kill larvae inside.'
            ),
        },
        {
            'name': 'Cutworm (Agrotis ipsilon)',
            'category': 'pest',
            'icon': '🐛',
            'severity': 'medium',
            'season': 'October–February (Rabi); Kharif seedling establishment stage',
            'affected_crops': 'Tomato, Brinjal, Cabbage, Tobacco, Groundnut, Sunflower, Maize, Sugarcane',
            'description': (
                'Cutworm larvae spend daytime hidden in soil and emerge at night to cut plant stems '
                'at or just below soil level. They cause sudden death of rows of seedlings, creating '
                'large gaps in fields. Damage appears seemingly random and is often discovered at '
                'morning inspection. Common across all Indian states in Rabi vegetable crops.'
            ),
            'prevention_methods': (
                '1. Deep summer plowing to expose and kill pupae in soil through sun and bird predation\n'
                '2. Install light traps to attract and kill adult cutworm moths at night\n'
                '3. Place poison bait (bran + jaggery + chlorpyrifos) near damaged plant rows each evening\n'
                '4. Use protective collars around transplanted seedlings to block larval access\n'
                '5. Flood irrigation forces larvae to soil surface where birds predate them'
            ),
            'treatment': (
                'Apply chlorpyrifos 20 EC as soil drench (3 ml/L) around stem bases in the evening. '
                'Broadcast poison bait in the evening for immediate control of active populations.'
            ),
        },
        {
            'name': 'Groundnut Leaf Miner',
            'category': 'pest',
            'icon': '🦟',
            'severity': 'medium',
            'season': 'August–November (Kharif groundnut)',
            'affected_crops': 'Groundnut (primary host), Soybean',
            'description': (
                'Groundnut leaf miner (Aproaerema modicella) larvae create serpentine mines inside '
                'leaves, then fold and web leaves together. Heavy infestation causes complete defoliation '
                'and drastic yield loss. Very common in Gujarat, AP, Tamil Nadu, Karnataka, and '
                'Rajasthan groundnut belts from August to November.'
            ),
            'prevention_methods': (
                '1. Deep summer plowing to destroy overwintering pupae in soil before new season\n'
                '2. Timely sowing to avoid peak infestation period in September–October\n'
                '3. Apply neem seed kernel extract (NSKE) 5% spray preventively\n'
                '4. Conserve parasitoid wasps by avoiding unnecessary broad-spectrum insecticide sprays\n'
                '5. Install light traps to catch adult moths at night'
            ),
            'treatment': (
                'Spray dimethoate 30 EC (1.5 ml/L) or quinalphos 25 EC (2 ml/L) at first sign of leaf '
                'folding. Repeat after 15 days if population remains above economic threshold.'
            ),
        },
        {
            'name': 'Whitefly on Cassava (CBSD Vector)',
            'category': 'pest',
            'icon': '🦟',
            'severity': 'high',
            'season': 'Year-round in South India and Northeast India',
            'affected_crops': 'Cassava, Sweet Potato, Yam, Colocasia',
            'description': (
                'Cassava whitefly vectors Cassava Brown Streak Disease (CBSD) and Cassava Mosaic Disease '
                '(CMD), both of which have devastated cassava production in Africa and are an emerging '
                'risk in India. Heavy whitefly populations also cause direct feeding damage and sooty '
                'mold on leaves of root crops in Kerala, Tamil Nadu, and Northeast states.'
            ),
            'prevention_methods': (
                '1. Use virus-free, certified planting material and clean stem cuttings\n'
                '2. Install yellow sticky traps for monitoring (20 per ha)\n'
                '3. Apply neem oil (5 ml/L) as preventive spray throughout the crop season\n'
                '4. Remove and destroy plants showing mosaic or chlorotic symptoms immediately\n'
                '5. Avoid planting near tomato, chilli, or other whitefly-hosting crops'
            ),
            'treatment': (
                'Spray imidacloprid 17.8 SL (0.3 ml/L) or thiamethoxam 25 WG (0.3 g/L). '
                'For virus-infected plants: uproot and destroy — no chemical treatment cures viral infection.'
            ),
        },
    ]

    # =========================================================
    # WEEDS — 16 entries, Pan India
    # =========================================================
    weeds = [
        {
            'name': 'Wild Oat (Phalaris minor)',
            'category': 'weed',
            'icon': '🌾',
            'severity': 'critical',
            'season': 'November–March (Rabi wheat season)',
            'affected_crops': 'Wheat, Barley',
            'description': (
                'The most economically damaging weed of wheat fields in North India. Phalaris minor '
                'resembles wheat in early growth stages, making identification and hand weeding extremely '
                'difficult. It has evolved resistance to multiple widely used herbicides. A single plant '
                'produces 2,000–5,000 seeds that persist in soil for several years.'
            ),
            'prevention_methods': (
                '1. Use certified, weed-free seeds from registered dealers only\n'
                '2. Practice zero or minimum tillage sowing to reduce germination stimulation\n'
                '3. Crop rotation with non-cereal crops — rotate rice-wheat to rice-sugarcane\n'
                '4. Apply pre-emergence herbicide within 3 days of sowing\n'
                '5. Hand weed at the 2–3 leaf stage before seed formation\n'
                '6. Never allow weed to set seeds — seeds persist for many years'
            ),
            'treatment': (
                'Apply clodinafop-propargyl 15 WP (400 g/ha) or fenoxaprop-p-ethyl 10 EC (750 ml/ha) '
                'at 3–4 weeks after sowing. For herbicide-resistant populations: '
                'use mesosulfuron + iodosulfuron combination products.'
            ),
        },
        {
            'name': 'Barnyard Grass (Echinochloa crus-galli)',
            'category': 'weed',
            'icon': '🌾',
            'severity': 'critical',
            'season': 'Kharif rice season: June–October',
            'affected_crops': 'Rice (primary host), Maize, Vegetables',
            'description': (
                'The most serious weed of rice paddies across India. Barnyard grass mimics rice in early '
                'growth stages, making hand weeding very difficult without experience. Competes extremely '
                'aggressively and can reduce rice yield by 50–80% in severe infestations in both '
                'transplanted and direct-seeded rice systems.'
            ),
            'prevention_methods': (
                '1. Transplant rice at recommended age to give crop a competitive head start\n'
                '2. Maintain 5–7 cm floodwater as long as possible — suppresses barnyard grass\n'
                '3. Hand weed thoroughly at 20–25 days after transplanting\n'
                '4. Use rice varieties with strong early-season canopy closure\n'
                '5. Line transplanting enables mechanical intercultural operations between rows'
            ),
            'treatment': (
                'Apply butachlor 50 EC (2 L/ha) pre-emergence at 2–5 days after transplanting. '
                'Or bispyribac sodium 10 SC (200 ml/ha) at 3–4 leaf stage of weed. '
                'Maintain 2–3 cm water level after herbicide application for 3 days.'
            ),
        },
        {
            'name': 'Nut Grass (Cyperus rotundus)',
            'category': 'weed',
            'icon': '🌾',
            'severity': 'critical',
            'season': 'Kharif and Rabi both; year-round in warm climates',
            'affected_crops': 'Sugarcane, Potato, Cotton, Vegetables, Rice, Groundnut, Onion',
            'description': (
                'Listed by scientists as the world\'s most troublesome weed. Nut grass spreads through '
                'underground nutlets (tubers) that survive extremes of heat, cold, and drought. One plant '
                'produces up to 40,000 tubers in a single season. Found in every Indian state — nearly '
                'impossible to fully eradicate once established.'
            ),
            'prevention_methods': (
                '1. Deep summer plowing to expose and desiccate tubers under hot summer sun\n'
                '2. Solarize soil with black polythene for 6–8 weeks in peak summer\n'
                '3. Dense-canopy crops suppress nut grass through shading\n'
                '4. Repeated shallow cultivation over 2–3 seasons to exhaust tuber food reserves\n'
                '5. Never deep-till once established — spreads tubers throughout the soil profile'
            ),
            'treatment': (
                'Apply halosulfuron-methyl 75 WP (67 g/ha) in sugarcane or vegetable crops. '
                'Use sulfentrazone in potato. '
                'In rice: bensulfuron-methyl + pretilachlor combination product.'
            ),
        },
        {
            'name': 'Parthenium (Congress Grass)',
            'category': 'weed',
            'icon': '🌿',
            'severity': 'high',
            'season': 'Kharif: June–October; also present in Rabi months in South India',
            'affected_crops': 'Maize, Sorghum, Vegetables, Pulses, Sugarcane; invades pastures and roadsides',
            'description': (
                'One of India\'s most invasive and hazardous weeds. Parthenium causes severe allergic '
                'reactions — contact dermatitis, hay fever, and asthma — in humans and livestock. '
                'It releases allelopathic chemicals that suppress crop growth by up to 40%. Spread '
                'to all states from J&K to Tamil Nadu since its accidental introduction in the 1950s.'
            ),
            'prevention_methods': (
                '1. Uproot by hand before flowering — always wear gloves and face mask\n'
                '2. Never allow seeds to form — one plant produces 25,000+ seeds\n'
                '3. Use biological control: Zygogramma bicolorata beetle (NBPGR approved)\n'
                '4. Promote competitive smother crops: sunflower and sorghum suppress parthenium\n'
                '5. Community village-level eradication drives with public awareness campaigns'
            ),
            'treatment': (
                'Spray glyphosate 41% SL (2 ml/L) on non-crop areas. '
                'Atrazine 50 WP (1.5 kg/ha) in maize fields. '
                'Biological control with Zygogramma beetle is the preferred long-term strategy.'
            ),
        },
        {
            'name': 'Bathua (Chenopodium album)',
            'category': 'weed',
            'icon': '🌱',
            'severity': 'medium',
            'season': 'October–February (Rabi season)',
            'affected_crops': 'Wheat, Mustard, Potato, Onion, Vegetables',
            'description': (
                'Bathua or Lamb\'s Quarters is a fast-emerging broadleaf weed that rapidly outcompetes '
                'Rabi crops for light, nutrients, and water. A single plant produces up to 75,000 seeds '
                'that remain viable in soil for decades. Widespread across all North and Central India '
                'in winter crop fields — familiar to every farmer.'
            ),
            'prevention_methods': (
                '1. Hand weed at 2–3 weeks after crop emergence before weed establishes\n'
                '2. Intercultural operations with hoe or cultivator between crop rows\n'
                '3. Pre-emergence herbicide within 3 days of sowing\n'
                '4. Mulching to suppress germination in vegetable crops\n'
                '5. Dense-canopy crop rotation to shade out seed germination'
            ),
            'treatment': (
                'Apply 2,4-D sodium salt 80 WP (500 g/ha) at 3–4 weeks after wheat sowing. '
                'Or metsulfuron-methyl 20 WP (20 g/ha). '
                'For vegetables: use pendimethalin pre-emergence.'
            ),
        },
        {
            'name': 'Johnson Grass (Sorghum halepense)',
            'category': 'weed',
            'icon': '🌿',
            'severity': 'high',
            'season': 'Kharif: June–October; re-emerges from rhizomes in Rabi',
            'affected_crops': 'Sugarcane, Cotton, Maize, Sorghum, Soybean, Vegetables',
            'description': (
                'Perennial grass weed that spreads by both seeds and vigorous underground rhizomes. '
                'Once established, it is extremely difficult to eradicate without multi-season effort. '
                'Competes strongly for water, nutrients, and light. Also harbors several crop disease '
                'pathogens. Present across all Indian states in a wide range of crop types.'
            ),
            'prevention_methods': (
                '1. Deep repeated tillage to bring rhizomes to surface and desiccate in summer\n'
                '2. Soil solarization with transparent polythene for 6–8 weeks in peak summer\n'
                '3. Never allow plants to set seed — one plant produces thousands of viable seeds\n'
                '4. Use certified weed-free irrigation water and imported farm inputs\n'
                '5. Clean all farm equipment between fields to prevent rhizome spread'
            ),
            'treatment': (
                'Apply glyphosate 41% SL (3 ml/L) as directed spray on weed foliage, keeping away from crops. '
                'For in-crop control in maize: nicosulfuron 4 SC (1.5 L/ha). '
                'Multiple treatments over 2–3 seasons required for effective control.'
            ),
        },
        {
            'name': 'Striga (Witchweed)',
            'category': 'weed',
            'icon': '🌸',
            'severity': 'critical',
            'season': 'Kharif: appears July–September after onset of monsoon rains',
            'affected_crops': 'Sorghum, Maize, Sugarcane, Pearl Millet, Upland Rice, Cowpea',
            'description': (
                'Striga is a root-parasitic weed with no chlorophyll. It attaches to crop roots '
                'underground and drains nutrients before it even emerges above soil. By the time '
                'it is visible, 40–70% of yield loss has already occurred with no recovery possible. '
                'Major threat in tribal belt areas of Maharashtra, AP, Telangana, MP, and Chhattisgarh.'
            ),
            'prevention_methods': (
                '1. Use Striga-resistant sorghum and maize varieties documented by ICRISAT\n'
                '2. Apply Fusarium oxysporum f. sp. strigae biocontrol — attacks striga roots underground\n'
                '3. Nitrogen-fixing legume intercropping suppresses striga germination through high N\n'
                '4. Pull and burn all striga plants before seed set — one plant makes 200,000 seeds\n'
                '5. Apply fertilizer (N and P) to boost crop competitive ability against parasitism'
            ),
            'treatment': (
                'Seed treatment with Fusarium-based biocontrol agent. '
                'Apply 2,4-D at early post-emergence striga stage. '
                'Community eradication programs are essential — individual field control alone is insufficient.'
            ),
        },
        {
            'name': 'Water Hyacinth',
            'category': 'weed',
            'icon': '🌊',
            'severity': 'high',
            'season': 'Year-round in standing water; explosive growth March–September',
            'affected_crops': 'Irrigated Rice, Aquaculture Ponds, Irrigation Channels',
            'description': (
                'Water hyacinth is the world\'s worst aquatic weed. It blocks irrigation canals, reduces '
                'water flow to fields, depletes oxygen in water bodies (killing fish), and harbors '
                'mosquitoes and crop pests. Population doubles every 2 weeks under ideal conditions. '
                'A major problem in canal-irrigated areas of Bihar, WB, Assam, Odisha, and Kerala.'
            ),
            'prevention_methods': (
                '1. Manual removal before seed set — compost harvested biomass for biogas\n'
                '2. Biological control: Neochetina eichhorniae weevil (approved in some states)\n'
                '3. Dewater and desilting of canals before irrigation season\n'
                '4. Maintain water velocity in channels — stagnant water promotes explosive growth\n'
                '5. Community cooperative canal cleaning before each irrigation season'
            ),
            'treatment': (
                'Apply 2,4-D amine 58% SL (2 L/ha) on water bodies where legally permitted. '
                'Mechanical harvesting with slashers in larger canals. '
                'Use harvested biomass for biogas production for economic recovery.'
            ),
        },
        {
            'name': 'Lantana (Lantana camara)',
            'category': 'weed',
            'icon': '🌸',
            'severity': 'high',
            'season': 'Year-round; seeds throughout the year after monsoon establishment',
            'affected_crops': 'Plantation crops, Pastures, Forest margins adjacent to farm land',
            'description': (
                'Lantana is one of India\'s most widespread invasive shrub weeds. It forms impenetrable '
                'dense thickets that prevent crop establishment, harbor pests and snakes, and is toxic '
                'to livestock. Spreads rapidly from forest margins and roadsides into agricultural land. '
                'Present in every Indian state — removal requires sustained multi-year effort.'
            ),
            'prevention_methods': (
                '1. Uproot young plants before they become woody — most effective when caught early\n'
                '2. Controlled burning of cut material in non-crop areas\n'
                '3. Release approved biocontrol: Teleonemia scrupulosa lace bug\n'
                '4. Immediately replace cleared areas with competitive grass cover\n'
                '5. Prevent bird feeding on berries in farm area — birds disperse seeds widely'
            ),
            'treatment': (
                'Cut stems at soil level and immediately paint freshly cut stumps with undiluted '
                'glyphosate or triclopyr ester. Foliar spray triclopyr on young regrowth. '
                'Requires multi-year persistence — one treatment is never sufficient.'
            ),
        },
        {
            'name': 'Mikania (Mile-a-Minute)',
            'category': 'weed',
            'icon': '🌿',
            'severity': 'critical',
            'season': 'Most aggressive during monsoon: June–September',
            'affected_crops': 'Tea, Rubber, Banana, Young Plantation Trees, Vegetable Gardens',
            'description': (
                'Mikania micrantha is one of the world\'s most aggressive climbing weeds, growing up to '
                '8 cm per day. It smothers tea bushes, rubber saplings, and plantation trees by covering '
                'them completely within weeks. A major problem in Northeast India, West Bengal, Assam, '
                'and Kerala estates where it causes enormous productivity losses annually.'
            ),
            'prevention_methods': (
                '1. Manual weeding every 2–3 weeks during monsoon season without fail\n'
                '2. Black polythene mulching to prevent germination in plantation beds\n'
                '3. Biological control: Puccinia spegazzinii rust fungus (approved in some regions)\n'
                '4. Shade management in plantations — mikania thrives in open canopy gaps\n'
                '5. Early detection and prevention of seed formation before spread occurs'
            ),
            'treatment': (
                'Spray glyphosate 41% SL (5 ml/L) as directed spray on mikania foliage only. '
                'Or metribuzin 70 WP (1 g/L) in tea gardens. '
                'Manual cutting and burning of cut material. Multiple treatments every season required.'
            ),
        },
        {
            'name': 'Spiny Amaranth (Amaranthus spinosus)',
            'category': 'weed',
            'icon': '🌱',
            'severity': 'medium',
            'season': 'Kharif: June–October; also in summer crops',
            'affected_crops': 'Cotton, Groundnut, Maize, Soybean, Vegetables, Pulses, Okra',
            'description': (
                'Spiny amaranth is a prickly broadleaf weed that competes aggressively with Kharif crops. '
                'Its sharp spines make hand weeding dangerous to workers without gloves. One plant '
                'produces over 100,000 seeds. Widespread across all Indian states in summer and '
                'Kharif cropping systems — a common sight in cotton and groundnut fields.'
            ),
            'prevention_methods': (
                '1. Apply pre-emergence herbicide immediately after sowing\n'
                '2. Shallow cultivation at 2–3 weeks to cut seedlings before spines harden\n'
                '3. Always wear protective gloves and shoes when hand weeding in infested fields\n'
                '4. Prevent seed formation — remove plants before flowering begins\n'
                '5. Dense crop canopy establishment suppresses germination of new weed seeds'
            ),
            'treatment': (
                'Apply pendimethalin 30 EC (3.3 L/ha) pre-emergence. '
                'Post-emergence in maize: atrazine 50 WP (1.5 kg/ha). '
                'Hand weed when plants are still small and before spines fully develop.'
            ),
        },
        {
            'name': 'Orobanche (Broomrape)',
            'category': 'weed',
            'icon': '🌸',
            'severity': 'high',
            'season': 'Rabi: October–March; emerges after host crop root development',
            'affected_crops': 'Tomato, Carrot, Potato, Mustard, Sunflower, Faba Bean, Lentil',
            'description': (
                'Orobanche is a rootless, leafless parasitic weed that attaches to host crop roots and '
                'drains water and nutrients. A single plant produces 100,000+ tiny seeds that remain '
                'viable in soil for 20+ years — making eradication extremely long-term. '
                'Major problem in UP, Bihar, Rajasthan, and Punjab on tomato, vegetables, and sunflower.'
            ),
            'prevention_methods': (
                '1. Practice long crop rotations — minimum 7 years away from susceptible hosts\n'
                '2. Use resistant or tolerant crop varieties where commercially available\n'
                '3. Apply ethylene gas as suicidal germination stimulant before main crop planting\n'
                '4. Deep summer plowing exposes seeds to lethal surface soil temperatures\n'
                '5. Incorporate Trichoderma harzianum to suppress seed viability over time'
            ),
            'treatment': (
                'Apply glyphosate at suicidal germination dose before main crop planting. '
                'Use imazethapyr in sunflower (tolerant varieties only). '
                'Hand-remove all parasite plants before they flower and shed seeds.'
            ),
        },
        {
            'name': 'Dodder (Cuscuta spp.)',
            'category': 'weed',
            'icon': '🌱',
            'severity': 'high',
            'season': 'Kharif and Rabi both; depends on host crop planted',
            'affected_crops': 'Alfalfa, Lentil, Coriander, Tomato, Potato, Flax, Onion, Clover',
            'description': (
                'Dodder is a leafless, rootless, parasitic weed with no chlorophyll. Orange or yellow '
                'thread-like strands twine around crops and extract water and nutrients directly through '
                'haustoria embedded in host tissue. Can spread from plant to plant and devastate entire '
                'patches of legumes and vegetables. Enters fields as seed contaminant.'
            ),
            'prevention_methods': (
                '1. Inspect planting material — dodder seeds enter as contaminant in crop seeds\n'
                '2. Use only certified cleaned seeds screened to remove dodder contamination\n'
                '3. Destroy infested patches including all surrounding soil — do not compost\n'
                '4. Crop rotation with grasses — dodder cannot parasitize monocot grasses\n'
                '5. Deep plow after detection to bury seed bank deeper'
            ),
            'treatment': (
                'Remove and burn all dodder and attached host plants in infested patches without delay. '
                'Apply pendimethalin pre-emergence in next crop cycle. '
                'No selective post-emergence herbicide works in established crops with active dodder.'
            ),
        },
        {
            'name': 'Imperata Grass (Cogon Grass)',
            'category': 'weed',
            'icon': '🌾',
            'severity': 'high',
            'season': 'Year-round; most aggressive during monsoon season',
            'affected_crops': 'Plantation Crops, Jhum Crops, Young Orchards, Pastures, Rubber Estates',
            'description': (
                'Imperata cylindrica is a perennial grass weed spreading through underground rhizomes and '
                'wind-dispersed seeds. It forms dense mats that exclude all other vegetation. Common in '
                'degraded lands, jhum (shifting cultivation) fields, and forest edges in Northeast India, '
                'Odisha, and parts of South India including rubber estates.'
            ),
            'prevention_methods': (
                '1. Repeated tillage to fragment and desiccate rhizomes over multiple seasons\n'
                '2. Soil solarization with clear polythene for 6–8 weeks in peak summer\n'
                '3. Establish smother crops (Mucuna, Desmodium) after initial chemical control\n'
                '4. Never burn Imperata — burning stimulates vigorous rhizome regeneration\n'
                '5. Promote fast-growing plantation trees that quickly shade the area'
            ),
            'treatment': (
                'Apply glyphosate 41% SL (7 ml/L) when grass is actively growing with '
                'new shoots at 30–40 cm height. Re-treat regrowth after 4–6 weeks. '
                'Multiple applications over 2 full seasons required for effective control.'
            ),
        },
        {
            'name': 'Morning Glory (Ipomoea spp.)',
            'category': 'weed',
            'icon': '🌺',
            'severity': 'medium',
            'season': 'Kharif: June–October (warm moist conditions)',
            'affected_crops': 'Cotton, Soybean, Maize, Groundnut, Sugarcane',
            'description': (
                'Morning glory is a fast-climbing broadleaf weed that twines around crop plants, '
                'competing for light and ultimately causing lodging. Very common in cotton, soybean, '
                'and maize fields across Central and Western India. Spreads rapidly under warm, '
                'moist Kharif season conditions — can overwhelm a crop within 3–4 weeks.'
            ),
            'prevention_methods': (
                '1. Apply pre-emergence herbicide immediately after sowing\n'
                '2. Intercultural cultivation at 20 and 40 days after sowing to cut seedlings\n'
                '3. Remove climbing vines manually before they set seed\n'
                '4. Dense crop spacing to shade out germinating seeds from below\n'
                '5. Crop rotation to break the soil seed bank cycle over seasons'
            ),
            'treatment': (
                'Apply pendimethalin 30 EC (3.3 L/ha) pre-emergence. '
                'Post-emergence in soybean: lactofen 21.3 EC (1 L/ha). '
                'In cotton: directed spray of oxyfluorfen on inter-rows, avoiding crop foliage.'
            ),
        },
        {
            'name': 'Gokhru / Puncture Vine (Tribulus terrestris)',
            'category': 'weed',
            'icon': '🌱',
            'severity': 'medium',
            'season': 'Kharif: June–September in dryland areas',
            'affected_crops': 'Groundnut, Moth Bean, Mung Bean, Pearl Millet, Sesame, Cotton',
            'description': (
                'Gokhru is a prostrate dryland weed with extremely sharp spiny fruits that cause '
                'tyre punctures, injure feet, and harm livestock hooves. Thrives in sandy, nutrient-poor '
                'soils. Seeds remain viable for 3–7 years. Common in dryland areas of Rajasthan, '
                'Gujarat, Deccan plateau, and dryland crop regions of Karnataka and Andhra Pradesh.'
            ),
            'prevention_methods': (
                '1. Deep tillage before sowing to bring seeds to surface and expose to hot sun\n'
                '2. Maintain adequate soil fertility — thrives in nutrient-depleted degraded soils\n'
                '3. Hand weed before fruit formation when spines are still soft\n'
                '4. Intercultural operations at 20–25 days after sowing\n'
                '5. Wear sturdy closed-toe boots in all infested fields at all times'
            ),
            'treatment': (
                'Apply pendimethalin pre-emergence after sowing. '
                '2,4-D spray at 3–4 leaf stage of weed. '
                'Hand removal before spiny fruits mature and disperse is essential. '
                'Community-level control in village common lands is necessary.'
            ),
        },
    ]

    # Bulk insert all three categories
    all_threats = wildlife + pests + weeds
    for data in all_threats:
        Threat.objects.create(**data)

    # =========================================================
    # CROP TIPS — 22 entries, Pan India
    # =========================================================
    tips = [
        {
            'title': 'IPM for Wheat — North India Rabi Season',
            'content': (
                'Apply Integrated Pest Management: use certified seeds treated with carboxin + thiram. '
                'Monitor weekly from January for aphids using yellow sticky traps. Spray imidacloprid '
                'ONLY when aphid population crosses 26 per tiller — spraying below this threshold is '
                'waste of money. Practice crop rotation with mustard or sugarcane every 3 years. Apply '
                '2,4-D for broadleaf weeds and clodinafop for wild oat at 3–4 weeks after sowing. '
                'Proper IPM reduces pesticide use by 40–60% while protecting yield.'
            ),
            'crop_type': 'Wheat', 'season': 'Rabi',
        },
        {
            'title': 'SRI Method for Rice — Maximum Yield with Less Water',
            'content': (
                'System of Rice Intensification (SRI) boosts yield by 20–50%. Transplant 8–12 day old '
                'seedlings (single seedling per hill, 25×25 cm spacing). Practice alternate wetting and '
                'drying irrigation instead of continuous flooding — saves 30% water. Apply compost or FYM '
                '(5 t/ha). Use rotary weeder at 10-day intervals. SRI produces larger root systems, '
                'more tillers, and better grain filling. Proven in WB, Tamil Nadu, Karnataka, and Odisha.'
            ),
            'crop_type': 'Rice', 'season': 'Kharif',
        },
        {
            'title': 'Cotton Bollworm & Whitefly Management — Central India',
            'content': (
                'Plant Bt cotton to reduce bollworm pressure by 80%. Install 5 pheromone traps per ha for '
                'army worm and bollworm monitoring. Apply Trichoderma soil treatment before planting for '
                'fusarium and root rot control. Monitor whitefly from August with yellow sticky traps. '
                'Never spray during early morning flowering hours — protects pollinators. Use at least 3 '
                'different chemical groups per season to prevent resistance development.'
            ),
            'crop_type': 'Cotton', 'season': 'Kharif',
        },
        {
            'title': 'Groundnut Yield Improvement — South India',
            'content': (
                'Use bold-seeded, rosette-resistant varieties: TG 37A, ICGV 91114. Treat seeds with '
                'Rhizobium culture for nitrogen fixation — saves 25 kg N/ha. Apply gypsum (500 kg/ha) '
                'at flowering — essential for pod filling and preventing hollow hearts. Monitor for leaf '
                'miner and tikka leaf spot from August. Ensure good drainage — groundnut cannot tolerate '
                'even 24 hours of waterlogging. Deep summer plowing controls soil-borne diseases.'
            ),
            'crop_type': 'Groundnut', 'season': 'Kharif',
        },
        {
            'title': 'Sugarcane Management — UP, Maharashtra, Tamil Nadu',
            'content': (
                'Choose zone-recommended variety: Co 0238 for UP; Co 86032 for Maharashtra; Co 86032 or '
                'CoC 671 for Tamil Nadu. Treat setts with carbendazim 0.1% for smut and wilt control. '
                'First ratoon yields 80% of plant crop at only 40% of cost — manage ratoons well. '
                'Install pheromone traps for early shoot borer detection from May. Apply trash mulching '
                'between rows to conserve moisture and suppress weeds.'
            ),
            'crop_type': 'Sugarcane', 'season': 'All seasons',
        },
        {
            'title': 'Tomato Disease & Pest Management — All States',
            'content': (
                'Raise nursery on elevated beds covered with 50-mesh insect-proof net — prevents whitefly '
                'and thrips from day one. Apply Trichoderma harzianum + Pseudomonas fluorescens soil drench '
                'for fusarium wilt protection. Install yellow sticky traps at transplanting. Stake '
                'indeterminate varieties for better air circulation. Monitor for early blight from fruit '
                'set — spray mancozeb 0.2% every 10 days preventively. Remove and burn any plant showing '
                'leaf curl virus symptoms immediately.'
            ),
            'crop_type': 'Tomato', 'season': 'All seasons',
        },
        {
            'title': 'Mustard Production — Rajasthan, MP, UP, Haryana',
            'content': (
                'Sow on time (1–15 October) to avoid peak January aphid season. Maintain 30 cm × 10–15 cm '
                'spacing. Apply 80 kg N/ha in two splits: basal and top dressing at branching. Monitor for '
                'Alternaria blight from rosette stage — spray mancozeb 0.2% preventively. Install yellow '
                'sticky traps from January for aphid monitoring. Spray thiamethoxam when aphid count '
                'exceeds 26 per plant. Harvest when 75% of pods turn yellow-brown.'
            ),
            'crop_type': 'Mustard', 'season': 'Rabi',
        },
        {
            'title': 'Banana Bunch Management — Maharashtra, Tamil Nadu, AP',
            'content': (
                'Cover banana bunches with blue polythene bags 2–3 weeks after emergence — protects '
                'from sunburn, birds, and insect pests. Desuck to maintain one ratoon per mother plant. '
                'Remove male bud (bell) after the last hand is fully developed to prevent Sigatoka spread. '
                'Apply MOP (500 g/plant) regularly — bananas are the heaviest potassium feeders among '
                'all crops. Drip irrigation with fertigation improves yield by 30–40%.'
            ),
            'crop_type': 'Banana', 'season': 'All seasons',
        },
        {
            'title': 'Soybean IPM — MP, Maharashtra, Rajasthan',
            'content': (
                'Treat seeds with Rhizobium japonicum + Bradyrhizobium culture (saves 25 kg N/ha). Use '
                'recommended varieties: JS 335, MACS 1281, or NRC 86. Monitor for girdle beetle at 30 '
                'DAS — spray carbaryl if incidence exceeds 5%. Scout for yellow mosaic virus from July — '
                'remove infected plants immediately as whitefly transmits this incurable virus. Never grow '
                'back-to-back soybean — rotate with wheat to break disease and pest cycles.'
            ),
            'crop_type': 'Soybean', 'season': 'Kharif',
        },
        {
            'title': 'Chilli Crop Protection — AP, Telangana, Karnataka',
            'content': (
                'Source certified, virus-indexed seedlings from registered nurseries only. Install 50-mesh '
                'nylon net in nursery to block thrips and whitefly from day one. Apply blue sticky traps '
                '(25/ha) specifically for thrips monitoring from transplanting. Remove plants showing leaf '
                'curl symptoms immediately — no chemical cure for this virus exists. Spray imidacloprid at '
                'transplanting as preventive against virus vectors. Monitor for powdery mildew in cool '
                'weather — spray wettable sulphur 80 WP (2 g/L) preventively.'
            ),
            'crop_type': 'Chilli', 'season': 'Kharif and Rabi',
        },
        {
            'title': 'Potato Disease Management — UP, West Bengal, Gujarat',
            'content': (
                'Use certified seed potatoes free from late blight and viruses. Disinfect cutting knives '
                'between cuts with KMnO4 solution. Spray mancozeb 0.2% or cymoxanil + mancozeb '
                'preventively from 30 days after planting. Haulm kill (cut vines) 10 days before harvest '
                'to prevent tuber blight infection. Store at 3–4°C with 90% relative humidity. Never plant '
                'in waterlogged fields — Phytophthora rot kills tubers immediately.'
            ),
            'crop_type': 'Potato', 'season': 'Rabi',
        },
        {
            'title': 'Onion Bulb Yield Improvement — Maharashtra, Gujarat, Karnataka',
            'content': (
                'Grow nursery on 1 m wide raised beds for good drainage. Transplant at 4–5 leaf stage '
                'at 15×10 cm spacing. Apply gypsum (250 kg/ha) for better bulb size, shelf life, and '
                'flavor. Drip irrigation with fertigation improves size uniformity significantly. Remove '
                'bolted (flowering) plants immediately — they never form marketable bulbs. Withhold water '
                '10 days before harvest for natural curing. Cure in shade 3–5 days before storage.'
            ),
            'crop_type': 'Onion', 'season': 'Rabi',
        },
        {
            'title': 'Apple Orchard Management — HP, J&K, Uttarakhand',
            'content': (
                'Spray dormant oil (4%) before bud burst to control San Jose scale and overwintering '
                'spider mites. Apply captan fungicide at green tip, pink bud, petal fall, and fruit set '
                'to control apple scab. Install codling moth pheromone traps (4–5/ha) to time sprays. '
                'Thin fruitlets at 6–7 mm for improved fruit size and quality. Apply reflective mulch '
                'under tree canopy to improve red color. Spray calcium at regular intervals to prevent '
                'bitter pit disorder in storage.'
            ),
            'crop_type': 'Apple', 'season': 'Rabi and Spring',
        },
        {
            'title': 'Tea Estate Pest Management — Assam, WB, Nilgiris',
            'content': (
                'Monitor for Helopeltis bug (tea mosquito bug) from April — spray thiamethoxam at first '
                'sign of tip damage characteristic. Apply zinc and boron micronutrients every 6 months '
                'for quality leaf growth. Follow skiffing and pruning schedule to maintain bush vigour. '
                'Maintain 30–40% shade — full sun reduces quality while full shade reduces yield. '
                'During flush periods, increase hand-plucking rounds to every 7 days for '
                'two-leaf-and-bud standard.'
            ),
            'crop_type': 'Tea', 'season': 'All seasons',
        },
        {
            'title': 'Chickpea & Pigeonpea — MP, Maharashtra, Karnataka',
            'content': (
                'Treat seeds with Rhizobium + PSB (Phosphate Solubilizing Bacteria) before sowing. '
                'Install 5 pheromone traps/ha for Helicoverpa monitoring from October. Apply Helicoverpa '
                'NPV (250 LE/ha) at first larval appearance for biological control. Spray '
                'chlorantraniliprole at 5% pod damage threshold. Avoid excess irrigation and nitrogen — '
                'promotes lush vegetative growth that increases Helicoverpa infestation while '
                'reducing pod set ratio.'
            ),
            'crop_type': 'Chickpea and Pigeonpea', 'season': 'Rabi',
        },
        {
            'title': 'Mango Orchard Care — UP, Bihar, AP, Maharashtra',
            'content': (
                'Apply alkathene sticky bands (25 cm wide, greased) on trunks in December to intercept '
                'mealybug nymphs. Spray Bordeaux mixture 1% on trunk and branches after pruning to '
                'prevent stem end rot. Apply copper hydroxide at bud emergence for powdery mildew control. '
                'Thin flower clusters when more than 50% of branches are flowering. Install fruit fly '
                'monitoring traps (methyl eugenol lure) from March — bait-spray at fly threshold.'
            ),
            'crop_type': 'Mango', 'season': 'Rabi and Summer',
        },
        {
            'title': 'Coconut Nutrition & Pest Management — Kerala, TN, Karnataka',
            'content': (
                'Apply 1.3 kg urea + 2 kg SSP + 2 kg MOP per palm per year in 2 splits (June and December). '
                'Green manure basin with Mucuna between palms. Monitor for eriophyid mite under button nut '
                'perianth — spray fenazaquin if detected. Install red palm weevil pheromone traps (1/10 '
                'trees). Apply neem cake (2 kg/palm) in basin. Inject monocrotophos into leaf axils '
                'for rhinoceros beetle control.'
            ),
            'crop_type': 'Coconut', 'season': 'All seasons',
        },
        {
            'title': 'Soil Health & Organic Matter — Pan India',
            'content': (
                'Test soil every 3 years for pH, NPK, and micronutrients at nearest KVK (Krishi Vigyan '
                'Kendra). Apply FYM 10–15 t/ha or vermicompost 3–5 t/ha before sowing. Green manure with '
                'dhaincha (Sesbania) or sunhemp in summer — adds 100–120 kg N/ha equivalent. Never burn '
                'crop residue — destroys beneficial soil organisms. Use subsoil plowing every 3–4 years '
                'to break hardpan compaction. Target soil organic carbon above 0.75% for sustainable yield.'
            ),
            'crop_type': 'All Crops', 'season': 'All seasons',
        },
        {
            'title': 'Drip & Sprinkler Irrigation — Save Water, Boost Yield',
            'content': (
                'Drip irrigation saves 40–60% water versus flood irrigation and improves yield by 20–40% '
                'through precise fertigation. Eligible under PM Krishi Sinchayee Yojana subsidy — up to '
                '55% for general farmers, 90% for SC/ST and small farmers. Drip is ideal for vegetables, '
                'orchards, sugarcane, and cotton. Sprinkler suits wheat, pulses, and oilseeds. '
                'Tensiometer-based monitoring prevents costly over- or under-watering.'
            ),
            'crop_type': 'All Crops', 'season': 'All seasons',
        },
        {
            'title': 'Post-Harvest Grain Storage — Eliminate Losses',
            'content': (
                'Dry grain to safe moisture before storage: wheat <12%, rice <14%, maize <12%, pulses <10%. '
                'Use hermetic PICS bags — eliminates insects without chemicals in 3–4 weeks. Treat storage '
                'bins with malathion dust on walls and floor. Use aluminum phosphide (Celphos) tablets only '
                'in fully sealed storage by trained persons — highly toxic, follow safety strictly. '
                'Check stored grain weekly for heating, mold, and insects. Never store freshly '
                'harvested moist grain under any circumstances.'
            ),
            'crop_type': 'All Crops', 'season': 'Post-harvest',
        },
        {
            'title': 'Zero Budget Natural Farming (ZBNF) — Pan India',
            'content': (
                'ZBNF uses only local cow-based inputs. Jeevamrit: ferment 10 kg cow dung + 10 L cow urine '
                '+ 2 kg jaggery + 2 kg pulse flour in 200 L water for 48 hours — apply 200 L/acre as soil '
                'drench or foliar spray. Bijamrit for seed treatment. Mulch with crop residue to retain '
                'moisture and feed earthworms. Proven results in Karnataka, AP, and Himachal Pradesh on '
                'rice, cotton, and vegetables. State governments of AP and Gujarat actively promote ZBNF '
                'with farmer training support.'
            ),
            'crop_type': 'All Crops', 'season': 'All seasons',
        },
        {
            'title': 'PM Fasal Bima Yojana — Crop Insurance Guide',
            'content': (
                'Enroll in PMFBY before state-prescribed last date. Premium: only 2% for Kharif, 1.5% '
                'for Rabi, 5% for commercial crops — government pays the rest. Coverage: prevented sowing, '
                'mid-season adversity (drought, flood, pest), and post-harvest losses up to 14 days. '
                'Notify bank or insurance company within 72 hours of any crop damage. Document all losses '
                'with dated photos, field area, and revenue records. Visit nearest CSC (Common Service '
                'Centre) for enrollment assistance.'
            ),
            'crop_type': 'All Crops', 'season': 'All seasons',
        },
    ]

    for tip in tips:
        CropTip.objects.create(**tip)


def reverse_migration(apps, schema_editor):
    Threat = apps.get_model('farming', 'Threat')
    CropTip = apps.get_model('farming', 'CropTip')
    Threat.objects.all().delete()
    CropTip.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('farming', '0002_seed_data'),
    ]

    operations = [
        migrations.RunPython(clear_and_reseed, reverse_migration),
    ]
