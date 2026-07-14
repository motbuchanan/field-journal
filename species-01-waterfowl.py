"""
Field Journal — North American species database.

ONE entry per species. Regions are declared per-species with a status,
because the same bird is "common" in one region and "rare" in another.

Region codes:
  NE = Northeast          SE = Southeast        MW = Midwest
  NW = Northwest          SW = Southwest        CA = California
  TX = Texas & Oklahoma

Status shorthand in `reg`:  "NE:c90"  =  common in Northeast, freq 90
  c = common   u = uncommon   r = rare
"""

# (name, sci, order, emoji, tags, size, weight, wingspan, lifespan, reg,
#  about, male, female, diet, habitat)

SPECIES = []

def S(name, sci, order, emoji, tags, size, weight, wingspan, lifespan, reg,
      about, male, female, diet, habitat):
    SPECIES.append(dict(
        name=name, sci=sci, order=order, emoji=emoji, tags=tags,
        size=size, weight=weight, wingspan=wingspan, lifespan=lifespan,
        reg=reg, about=about, male=male, female=female, diet=diet, habitat=habitat))


# ══════════════════════════════════════════════════════════════════
# WATERFOWL — geese, swans, ducks
# ══════════════════════════════════════════════════════════════════

S("Canada Goose", "Branta canadensis", "Anseriformes", "🪿", ["waterfowl"],
  "76–110 cm", "3.5–6.5 kg", "127–185 cm", "10–24 yr",
  "NE:c95 SE:c85 MW:c95 NW:c90 SW:u55 CA:c85 TX:c80",
  "Once purely migratory, urban populations are now year-round residents across most of the continent. Highly social, fiercely territorial when nesting, and famous for the V-formation flight.",
  "Black head and neck with a bold white chinstrap. Brown body, pale breast. Ganders are larger but plumage is identical.",
  "Identical to the male but noticeably smaller. She does the incubating while he stands guard nearby.",
  ["Grass", "Aquatic plants", "Grain", "Corn"],
  "Lakes, ponds, rivers, golf courses, park lawns, and farm fields. Needs open water beside short grass for grazing."),

S("Snow Goose", "Anser caerulescens", "Anseriformes", "🪿", ["waterfowl"],
  "64–79 cm", "2–3.3 kg", "135–165 cm", "~15 yr",
  "NE:u50 SE:u55 MW:c70 NW:u50 SW:u45 CA:u60 TX:c75",
  "Migrates in enormous, noisy flocks that can darken the sky. Populations have exploded to the point of damaging their Arctic breeding grounds. Comes in a white morph and a dark 'Blue Goose' morph.",
  "White morph: all white with black wingtips and a pink bill with a dark 'grinning patch'. Blue morph: dark grey-brown body with a white head.",
  "Identical to the male in both morphs, slightly smaller on average.",
  ["Grasses", "Sedges", "Grain", "Roots", "Waste corn"],
  "Marshes, wet grasslands, and agricultural fields on migration. Winters on coastal marsh and farmland."),

S("Trumpeter Swan", "Cygnus buccinator", "Anseriformes", "🦢", ["waterfowl"],
  "138–165 cm", "7–14 kg", "185–250 cm", "20–30 yr",
  "NE:r25 MW:u35 NW:u45 CA:r20",
  "North America's largest native waterfowl and one of the heaviest flying birds on Earth. Hunted nearly to extinction, it has recovered through intensive reintroduction — a genuine conservation success.",
  "All white with a black bill and black lores. Cobs are slightly larger than pens but otherwise identical.",
  "Identical plumage. The pen incubates while the cob defends the territory. Both give the resonant trumpet call.",
  ["Aquatic vegetation", "Pondweed", "Sedges", "Tubers"],
  "Large clear lakes, slow rivers, and marshes with abundant submerged plants. Needs a long runway of open water to take off."),

S("Tundra Swan", "Cygnus columbianus", "Anseriformes", "🦢", ["waterfowl"],
  "120–150 cm", "3.4–9.6 kg", "168–211 cm", "~20 yr",
  "NE:u40 SE:u35 MW:u45 NW:u50 CA:u45",
  "The most numerous swan in North America, migrating in long lines between the Arctic and coastal wintering grounds. Smaller and shorter-necked than the Trumpeter, with a higher, yelping call.",
  "All white with a black bill, usually showing a small yellow teardrop at the base in front of the eye.",
  "Identical to the male, slightly smaller. Pairs mate for life and migrate as family groups.",
  ["Aquatic plants", "Waste grain", "Tubers", "Corn"],
  "Shallow lakes, estuaries, flooded fields, and coastal bays in winter. Breeds on Arctic tundra."),

S("Wood Duck", "Aix sponsa", "Anseriformes", "🦆", ["waterfowl"],
  "47–54 cm", "454–862 g", "66–73 cm", "~4 yr",
  "NE:c70 SE:c75 MW:c70 NW:u55 CA:u50 TX:c65",
  "Often called the most beautiful duck in North America. Unique among waterfowl for nesting in tree cavities — ducklings leap from the nest hole to the ground on their first day. Nest boxes rescued it from near-extinction.",
  "Iridescent green and purple crested head with intricate white face striping, chestnut breast, and a red eye.",
  "Grey-brown with a distinctive white teardrop eye-ring on a grey face, and a white throat.",
  ["Acorns", "Seeds", "Berries", "Insects", "Aquatic plants"],
  "Wooded swamps, beaver ponds, and tree-lined rivers. One of very few ducks that can perch in trees."),

S("Mallard", "Anas platyrhynchos", "Anseriformes", "🦆", ["waterfowl"],
  "50–65 cm", "1–1.6 kg", "81–98 cm", "5–10 yr",
  "NE:c98 SE:c90 MW:c98 NW:c95 SW:c85 CA:c95 TX:c92",
  "The world's most abundant dabbling duck and the ancestor of nearly every domestic duck breed. Thrives in almost any watery habitat, from wilderness marsh to city retention pond.",
  "Iridescent green head, yellow bill, chestnut breast set off by a white neck ring, grey body, curled black tail feathers.",
  "Mottled brown with an orange bill blotched in black. Both sexes show a blue speculum bordered in white.",
  ["Seeds", "Aquatic plants", "Grain", "Invertebrates"],
  "Extraordinarily adaptable — ponds, lakes, rivers, marshes, flooded fields, and urban parks."),

S("American Black Duck", "Anas rubripes", "Anseriformes", "🦆", ["waterfowl"],
  "54–59 cm", "0.7–1.6 kg", "88–95 cm", "~15 yr",
  "NE:c65 SE:u50 MW:u40",
  "A dark, wary duck of the eastern marshes. Declining, in part because it hybridizes readily with the expanding Mallard, blurring the species line.",
  "Very dark sooty-brown body contrasting with a paler grey-brown head. Olive-yellow bill. Violet speculum without white borders.",
  "Similar to the male but with a duller olive bill. In flight both sexes flash brilliant white wing linings against the dark body.",
  ["Aquatic plants", "Seeds", "Snails", "Insects"],
  "Salt marsh, coastal bays, wooded swamps, and beaver ponds. Prefers quieter, wilder water than Mallards."),

S("Northern Pintail", "Anas acuta", "Anseriformes", "🦆", ["waterfowl"],
  "51–76 cm", "0.45–1.4 kg", "80–95 cm", "~20 yr",
  "NE:u45 SE:u50 MW:u60 NW:c65 SW:u55 CA:c75 TX:c70",
  "An elegant, long-necked dabbler and one of the earliest spring migrants. The drake's needle-thin tail streamers are unmistakable in flight.",
  "Chocolate-brown head, a white breast stripe running up the neck, grey body, and long black central tail feathers.",
  "Mottled buff-brown, plainer than most female ducks, with a slender neck and grey bill. Elegant even in drab plumage.",
  ["Seeds", "Waste grain", "Aquatic invertebrates", "Snails"],
  "Shallow wetlands, flooded fields, and prairie potholes. Winters on coastal marsh and rice fields."),

S("Green-winged Teal", "Anas crecca", "Anseriformes", "🦆", ["waterfowl"],
  "34–38 cm", "250–400 g", "53–59 cm", "~5 yr",
  "NE:u45 SE:c60 MW:u55 NW:c60 SW:u55 CA:c70 TX:c70",
  "The smallest dabbling duck on the continent — fast, agile, and given to twisting, shorebird-like flock flight.",
  "Chestnut head with a sweeping iridescent green patch from the eye to the nape, a vertical white bar on the side, and a spotted breast.",
  "Mottled brown and easy to overlook, but the tiny size and bright green speculum give her away.",
  ["Seeds", "Aquatic invertebrates", "Algae"],
  "Shallow marshes, mudflats, and flooded fields. Feeds in water barely deep enough to float in."),

S("Blue-winged Teal", "Spatula discors", "Anseriformes", "🦆", ["waterfowl"],
  "37–41 cm", "280–420 g", "58–62 cm", "~6 yr",
  "NE:u55 SE:u55 MW:c70 NW:u50 SW:u45 CA:u45 TX:c65",
  "A long-distance migrant that arrives late in spring and leaves early in fall — some winter as far south as Peru. Travels in small, fast, low-flying flocks.",
  "Slate-grey head with a bold white crescent in front of the eye, and a warm spotted brown body.",
  "Mottled brown with a pale patch at the base of the bill. Both sexes flash a chalky blue forewing in flight.",
  ["Seeds", "Aquatic invertebrates", "Snails", "Insects"],
  "Shallow marshes, prairie potholes, and pond edges with plenty of emergent vegetation."),

S("Northern Shoveler", "Spatula clypeata", "Anseriformes", "🦆", ["waterfowl"],
  "43–53 cm", "470–1000 g", "70–84 cm", "~15 yr",
  "NE:u50 SE:u55 MW:c65 NW:c65 SW:c60 CA:c80 TX:c70",
  "Instantly told by its enormous spatulate bill, which it uses to strain tiny invertebrates from the water. Groups sometimes swim in tight circles to stir food to the surface.",
  "Green head, white breast, chestnut flanks, and a huge black bill — a striking, almost cartoonish combination.",
  "Mottled brown with the same oversized bill, which is orange-tinged along the edges.",
  ["Aquatic invertebrates", "Seeds", "Plankton", "Snails"],
  "Shallow, mucky wetlands and marshes rich in invertebrates. Also uses sewage lagoons and flooded fields."),

S("Gadwall", "Mareca strepera", "Anseriformes", "🦆", ["waterfowl"],
  "46–57 cm", "0.5–1.3 kg", "78–90 cm", "~19 yr",
  "NE:u55 SE:u55 MW:c65 NW:c60 SW:u55 CA:c70 TX:c70",
  "A subtly beautiful duck that rewards a second look — what seems plain grey at a distance is finely vermiculated up close. Often steals food from diving ducks as they surface.",
  "Intricately patterned grey body, black rear end, and a small white speculum patch visible at rest.",
  "Mottled brown, very like a small female Mallard, but with an orange-sided bill and that white wing patch.",
  ["Aquatic plants", "Seeds", "Invertebrates"],
  "Marshes, ponds, and reservoirs with plenty of submerged vegetation."),

S("American Wigeon", "Mareca americana", "Anseriformes", "🦆", ["waterfowl"],
  "42–59 cm", "0.5–1.3 kg", "76–91 cm", "~21 yr",
  "NE:u50 SE:u55 MW:u55 NW:c70 SW:u55 CA:c75 TX:c65",
  "A grazing duck as likely to be found on a wet lawn or golf course as on water. Gives a distinctive three-note whistle that carries across a marsh.",
  "Green swoosh behind the eye on a grey head, with a creamy-white crown — hence the old name 'baldpate'. Pinkish-brown breast.",
  "Warm grey-brown with a plain greyish head and a small blue-grey bill tipped in black.",
  ["Grasses", "Aquatic plants", "Waste grain"],
  "Marshes, lakes, and flooded fields. Frequently grazes on shortgrass well away from water."),

S("Canvasback", "Aythya valisineria", "Anseriformes", "🦆", ["waterfowl"],
  "48–56 cm", "0.9–1.6 kg", "79–89 cm", "~22 yr",
  "NE:u40 SE:u40 MW:u50 NW:u45 SW:u40 CA:u55 TX:u50",
  "The aristocrat of diving ducks, with a long sloping forehead that makes the head and bill look like one continuous wedge. Flies fast and high in long lines.",
  "Chestnut-red head, black breast, and a strikingly pale white-grey body that gleams at distance.",
  "Soft brown head and breast with a pale grey body. The distinctive sloped head profile identifies her at any range.",
  ["Aquatic plants", "Wild celery", "Tubers", "Mollusks"],
  "Large lakes, reservoirs, and coastal bays in winter. Breeds on prairie marshes."),

S("Redhead", "Aythya americana", "Anseriformes", "🦆", ["waterfowl"],
  "42–54 cm", "0.9–1.1 kg", "75–84 cm", "~21 yr",
  "NE:u40 SE:u45 MW:u55 NW:u45 SW:u50 CA:u50 TX:c60",
  "A diving duck that frequently lays its eggs in other ducks' nests, letting the host raise its young. Winters in huge rafts, especially on the Texas Gulf coast.",
  "Rounded coppery-red head, black breast, and grey body — like a Canvasback but with a rounder head and a shorter blue-grey bill.",
  "Warm brown overall with a slightly paler face and a dark-tipped grey bill. Rounded head shape is the key.",
  ["Aquatic plants", "Seeds", "Mollusks", "Insects"],
  "Marshes and prairie potholes for breeding; large lakes and coastal bays in winter."),

S("Ring-necked Duck", "Aythya collaris", "Anseriformes", "🦆", ["waterfowl"],
  "39–46 cm", "490–910 g", "62–63 cm", "~20 yr",
  "NE:c60 SE:c65 MW:c60 NW:c60 SW:u55 CA:c65 TX:c60",
  "Badly named — the chestnut neck ring is nearly invisible in the field, while the bold white bill ring is obvious. Prefers smaller, wooded ponds than most diving ducks.",
  "Glossy black head with a peaked crown, black back, grey sides with a white spur at the shoulder, and a white-ringed grey bill.",
  "Brown with a paler face, a white eye-ring, and the same distinctive bill pattern. Peaked head shape is diagnostic.",
  ["Aquatic plants", "Seeds", "Snails", "Insects"],
  "Wooded ponds, beaver ponds, marshes, and small lakes — smaller waters than most diving ducks use."),

S("Lesser Scaup", "Aythya affinis", "Anseriformes", "🦆", ["waterfowl"],
  "38–48 cm", "0.45–1.1 kg", "68–78 cm", "~18 yr",
  "NE:c60 SE:c60 MW:c65 NW:c60 SW:u55 CA:c65 TX:c65",
  "The most abundant diving duck in North America, gathering in rafts that can number in the thousands. Told from Greater Scaup by a peaked, not rounded, crown.",
  "Black head glossed purple, black breast, white sides, and a grey vermiculated back. Yellow eye.",
  "Dark brown with a crisp white patch at the base of the bill. Yellow eye and peaked crown.",
  ["Aquatic invertebrates", "Mollusks", "Seeds", "Aquatic plants"],
  "Large lakes, reservoirs, and coastal bays. Breeds on northern prairie and boreal wetlands."),

S("Bufflehead", "Bucephala albeola", "Anseriformes", "🦆", ["waterfowl"],
  "32–40 cm", "270–550 g", "55 cm", "~18 yr",
  "NE:c65 SE:c65 MW:c60 NW:c70 SW:u55 CA:c75 TX:c60",
  "A tiny, buoyant diving duck that pops to the surface like a cork. Nests almost exclusively in old flicker cavities, which limits it to where big woodpeckers live.",
  "Puffy black head with an enormous white wedge from eye to nape, glossed green and purple. Bright white body.",
  "Dusky grey-brown with a small, neat white cheek patch. Much smaller and plainer than the male.",
  ["Aquatic invertebrates", "Snails", "Crustaceans", "Seeds"],
  "Small lakes, ponds, rivers, and sheltered coastal bays in winter."),

S("Common Goldeneye", "Bucephala clangula", "Anseriformes", "🦆", ["waterfowl"],
  "40–51 cm", "0.5–1.3 kg", "77–83 cm", "~15 yr",
  "NE:c60 SE:u45 MW:c60 NW:c65 SW:u40 CA:u50",
  "Nicknamed 'whistler' for the loud whirring hum its wings make in flight — audible long before the bird is seen. Winters on cold, open water, often the last duck to leave a freezing lake.",
  "Glossy green-black head with a round white spot before the eye, bright white body, and a striking golden eye.",
  "Chocolate-brown head with a grey body and a dark bill usually tipped in yellow. Golden eye.",
  ["Aquatic invertebrates", "Crustaceans", "Mollusks", "Small fish"],
  "Large lakes, rivers, and coastal bays. Breeds in tree cavities in northern forests."),

S("Hooded Merganser", "Lophodytes cucullatus", "Anseriformes", "🦆", ["waterfowl"],
  "40–49 cm", "450–880 g", "56–70 cm", "~14 yr",
  "NE:c60 SE:c60 MW:c55 NW:u55 CA:u45 TX:u50",
  "A small, spectacular fish-eating duck with a fan-shaped crest it can raise and lower. Has a third eyelid that acts as built-in goggles for underwater hunting.",
  "Black head with a huge white fan-shaped crest, chestnut flanks, and bold black-and-white breast stripes.",
  "Grey-brown with a shaggy cinnamon crest. Subtle but unmistakable once you know the shape.",
  ["Small fish", "Crayfish", "Aquatic insects", "Amphibians"],
  "Wooded ponds, swamps, and slow rivers. Nests in tree cavities, often alongside Wood Ducks."),

S("Common Merganser", "Mergus merganser", "Anseriformes", "🦆", ["waterfowl"],
  "58–72 cm", "0.9–2.1 kg", "78–97 cm", "~13 yr",
  "NE:c60 SE:u40 MW:u55 NW:c70 SW:u40 CA:u55",
  "A large, streamlined fish hunter with a serrated 'sawbill' for gripping slippery prey. Broods of ducklings often ride on the mother's back.",
  "Clean white body, glossy dark green head with no crest, and a slender red bill.",
  "Grey body with a sharply demarcated rusty-cinnamon head, a shaggy crest, and a crisp white chin.",
  ["Fish", "Aquatic invertebrates", "Crustaceans"],
  "Clear rivers, large lakes, and reservoirs. Prefers clean water where it can hunt fish by sight."),

S("Red-breasted Merganser", "Mergus serrator", "Anseriformes", "🦆", ["waterfowl"],
  "51–64 cm", "0.8–1.3 kg", "70–86 cm", "~9 yr",
  "NE:c55 SE:c55 MW:u45 NW:c55 CA:c55 TX:u50",
  "The saltwater merganser, wintering mostly on coasts and the Great Lakes. Holds the record for the fastest level flight of any duck, clocked over 130 km/h.",
  "Shaggy double crest, dark green head, white neck ring, and a speckled rusty breast.",
  "Grey-brown with a shaggy rufous head that blends gradually into the neck — no crisp border like the Common Merganser.",
  ["Small fish", "Crustaceans", "Aquatic insects"],
  "Coastal bays, estuaries, and the Great Lakes in winter. Breeds on northern lakes and tundra ponds."),

S("Ruddy Duck", "Oxyura jamaicensis", "Anseriformes", "🦆", ["waterfowl"],
  "35–43 cm", "310–790 g", "56–62 cm", "~13 yr",
  "NE:u40 SE:u50 MW:u55 NW:u55 SW:c60 CA:c70 TX:c60",
  "A compact stiff-tailed diver with an outsized attitude. The courting male drums his blue bill against his chest fast enough to froth the water with bubbles.",
  "Breeding: bright chestnut body, black cap, bold white cheek, and an electric sky-blue bill. Tail often cocked straight up.",
  "Grey-brown with a dark cap and a single dark line crossing the pale cheek. Also cocks the stiff tail.",
  ["Midge larvae", "Aquatic invertebrates", "Seeds"],
  "Marshes and prairie potholes for breeding; open lakes, reservoirs, and coastal bays in winter."),
