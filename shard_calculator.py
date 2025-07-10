import pandas as pd
import csv

# Credit to HsFearless, MaxLunar & WhatYouThing for the data
# Sheet created by @lunaynx
# Kudos to Lukasaurus11 on GitHub for helpful discussions


# Matches in game name to bazaar product id
shard_names = {
    'SHARD_GROVE': 'Grove',
    'SHARD_MIST': 'Mist',
    'SHARD_FLASH': 'Flash',
    'SHARD_PHANPYRE': 'Phanpyre',
    'SHARD_COD': 'Cod',
    'SHARD_PHANFLARE': 'Phanflare',
    'SHARD_NIGHT_SQUID': 'Night Squid',
    'SHARD_LAPIS_ZOMBIE': 'Lapis Zombie',
    'SHARD_HIDEONLEAF': 'Hideonleaf',
    'SHARD_VERDANT': 'Verdant',
    'SHARD_CHILL': 'Chill',
    'SHARD_SEA_ARCHER': 'Sea Archer',
    'SHARD_VORACIOUS_SPIDER': 'Voracious Spider',
    'SHARD_HIDEONGIFT': 'Hideongift',
    'SHARD_BIRRIES': 'Birries',
    'SHARD_TANK_ZOMBIE': 'Tank Zombie',
    'SHARD_CROW': 'Crow',
    'SHARD_TADGANG': 'Tadgang',
    'SHARD_ZEALOT': 'Zealot',
    'SHARD_CORALOT': 'Coralot',
    'SHARD_HARPY': 'Harpy',
    'SHARD_MUDWORM': 'Mudworm',
    'SHARD_GOLDEN_GHOUL': 'Golden Ghoul',
    'SHARD_AZURE': 'Azure',
    'SHARD_BEZAL': 'Bezal',
    'SHARD_YOG': 'Yog',
    'SHARD_BOREAL_OWL': 'Boreal Owl',
    'SHARD_NEWT': 'Newt',
    'SHARD_MINER_ZOMBIE': 'Miner Zombie',
    'SHARD_BRAMBLE': 'Bramble',
    'SHARD_TIDE': 'Tide',
    'SHARD_QUAKE': 'Quake',
    'SHARD_SPARROW': 'Sparrow',
    'SHARD_GOLDFIN': 'Goldfin',
    'SHARD_TROGLOBYTE': 'Troglobyte',
    'SHARD_HIDEONCAVE': 'Hideoncave',
    'SHARD_SALAMANDER': 'Salamander',
    'SHARD_CUBOA': 'Cuboa',
    'SHARD_PEST': 'Pest',
    'SHARD_MOSSYBIT': 'Mossybit',
    'SHARD_RAIN_SLIME': 'Rain Slime',
    'SHARD_SEER': 'Seer',
    'SHARD_HERON': 'Heron',
    'SHARD_OBSIDIAN_DEFENDER': 'Obsidian Defender',
    'SHARD_SALMON': 'Salmon',
    'SHARD_VIPER': 'Viper',
    'SHARD_PRAYING_MANTIS': 'Praying Mantis',
    'SHARD_ZOMBIE_SOLDIER': 'Zombie Soldier',
    'SHARD_BAMBULEAF': 'Bambuleaf',
    'SHARD_SYCOPHANT': 'Sycophant',
    'SHARD_SEAGULL': 'Seagull',
    'SHARD_ENT': 'Ent',
    'SHARD_SOUL_OF_THE_ALPHA': 'Soul of the Alpha',
    'SHARD_MOCHIBEAR': 'Mochibear',
    'SHARD_MAGMA_SLUG': 'Magma Slug',
    'SHARD_FLAMING_SPIDER': 'Flaming Spider',
    'SHARD_KIWI': 'Kiwi',
    'SHARD_BRUISER': 'Bruiser',
    'SHARD_STRIDER_SURFER': 'Stridersurfer',
    'SHARD_RANA': 'Rana',
    'SHARD_TERMITE': 'Termite',
    'SHARD_SYLVAN': 'Sylvan',
    'SHARD_CASCADE': 'Cascade',
    'SHARD_BOLT': 'Bolt',
    'SHARD_BAMBLOOM': 'Bambloom',
    'SHARD_TOAD': 'Toad',
    'SHARD_GLACITE_WALKER': 'Glacite Walker',
    'SHARD_BEACONMITE': 'Beaconmite',
    'SHARD_LIZARD_KING': 'Lizard King',
    'SHARD_PYTHON': 'Python',
    'SHARD_INVISIBUG': 'Invisibug',
    'SHARD_PIRANHA': 'Piranha',
    'SHARD_HIDEONGEON': 'Hideongeon',
    'SHARD_LAPIS_SKELETON': 'Lapis Skeleton',
    'SHARD_CROPEETLE': 'Cropeetle',
    'SHARD_DROWNED': 'Drowned',
    'SHARD_STAR_SENTRY': 'Star Sentry',
    'SHARD_HIDEONDRA': 'Hideondra',
    'SHARD_ABYSSAL_LANTERN': 'Abyssal Lanternfish',
    'SHARD_ARACHNE': 'Arachne',
    'SHARD_BITBUG': 'Bitbug',
    'SHARD_REVENANT': 'Revenant',
    'SHARD_SILENTDEPTH': 'Silentdepth',
    'SHARD_SKELETOR': 'Skeletor',
    'SHARD_THYST': 'Thyst',
    'SHARD_QUARTZFANG': 'Quartzfang',
    'SHARD_HIDEONRING': 'Hideonring',
    'SHARD_SNOWFIN': 'Snowfin',
    'SHARD_KADA_KNIGHT': 'Kada Knight',
    'SHARD_CARROT_KING': 'Carrot King',
    'SHARD_WITHER_SPECTER': 'Wither Specter',
    'SHARD_MATCHO': 'Matcho',
    'SHARD_LADYBUG': 'Ladybug',
    'SHARD_LUMISQUID': 'Lumisquid',
    'SHARD_CROCODILE': 'Crocodile',
    'SHARD_BULLFROG': 'Bullfrog',
    'SHARD_DREADWING': 'Dreadwing',
    'SHARD_JOYDIVE': 'Joydive',
    'SHARD_STALAGMIGHT': 'Stalagmight',
    'SHARD_FUNGLOOM': 'Fungloom',
    'SHARD_EEL': 'Eel',
    'SHARD_KING_COBRA': 'King Cobra',
    'SHARD_LAVA_FLAME': 'Lava Flame',
    'SHARD_DRACONIC': 'Draconic',
    'SHARD_FALCON': 'Falcon',
    'SHARD_INFERNO_KOI': 'Inferno Koi',
    'SHARD_WITHER': 'Wither',
    'SHARD_GECKO': 'Gecko',
    'SHARD_TERRA': 'Terra',
    'SHARD_CRYO': 'Cryo',
    'SHARD_AERO': 'Aero',
    'SHARD_PANDARAI': 'Pandarai',
    'SHARD_LEVIATHAN': 'Leviathan',
    'SHARD_ALLIGATOR': 'Alligator',
    'SHARD_FENLORD': 'Fenlord',
    'SHARD_BASILISK': 'Basilisk',
    'SHARD_IGUANA': 'Iguana',
    'SHARD_MORAY_EEL': 'Moray Eel',
    'SHARD_THORN': 'Thorn',
    'SHARD_LUNAR_MOTH': 'Lunar Moth',
    'SHARD_FIRE_EEL': 'Fire Eel',
    'SHARD_BAL': 'Bal',
    'SHARD_HIDEONSACK': 'Hideonsack',
    'SHARD_WATER_HYDRA': 'Water Hydra',
    'SHARD_FLARE': 'Flare',
    'SHARD_SEA_EMPEROR': 'Sea Emperor',
    'SHARD_PRINCE': 'Prince',
    'SHARD_KOMODO_DRAGON': 'Komodo Dragon',
    'SHARD_MIMIC': 'Mimic',
    'SHARD_SHELLWISE': 'Shellwise',
    'SHARD_BARBARIAN_DUKE_X': 'Barbarian Duke X',
    'SHARD_TOUCAN': 'Toucan',
    'SHARD_HELLWISP': 'Hellwisp',
    'SHARD_CAIMAN': 'Caiman',
    'SHARD_FIREFLY': 'Firefly',
    'SHARD_SEA_SERPENT': 'Sea Serpent',
    'SHARD_GHOST': 'Ghost',
    'SHARD_XYZ': 'XYZ',
    'SHARD_LEATHERBACK': 'Leatherback',
    'SHARD_CAVERNSHADE': 'Cavernshade',
    'SHARD_DRAGONFLY': 'Dragonfly',
    'SHARD_TENEBRIS': 'Tenebris',
    'SHARD_BLIZZARD': 'Blizzard',
    'SHARD_TEMPEST': 'Tempest',
    'SHARD_CHAMELEON': 'Chameleon',
    'SHARD_TIAMAT': 'Tiamat',
    'SHARD_WYVERN': 'Wyvern',
    'SHARD_TORTOISE': 'Tortoise',
    'SHARD_ENDSTONE_PROTECTOR': 'Endstone Protector',
    'SHARD_NAGA': 'Naga',
    'SHARD_LAPIS_CREEPER': 'Lapis Creeper',
    'SHARD_WARTYBUG': 'Wartybug',
    'SHARD_SPIKE': 'Spike',
    'SHARD_KRAKEN': 'Kraken',
    'SHARD_TAURUS': 'Taurus',
    'SHARD_DAEMON': 'Daemon',
    'SHARD_MOLTENFISH': 'Moltenfish',
    'SHARD_SHINYFISH': 'Shinyfish',
    'SHARD_ANANKE': 'Ananke',
    'SHARD_HIDEONBOX': 'Hideonbox',
    'SHARD_LORD_JAWBUS': 'Lord Jawbus',
    'SHARD_BURNINGSOUL': 'Burningsoul',
    'SHARD_CINDER_BAT': 'Cinderbat',
    'SHARD_MEGALITH': 'Megalith',
    'SHARD_POWER_DRAGON': 'Power Dragon',
    'SHARD_CONDOR': 'Condor',
    'SHARD_SUN_FISH': 'Sun Fish',
    'SHARD_APEX_DRAGON': 'Apex Dragon',
    'SHARD_DODO': 'Dodo',
    'SHARD_JORMUNG': 'Jormung',
    'SHARD_ETHERDRAKE': 'Etherdrake',
    'SHARD_GALAXY_FISH': 'Galaxy Fish',
    'SHARD_MOLTHORN': 'Molthorn',
    'SHARD_STARBORN': 'Starborn',
}


def fetchShardPrices(snapshot, shard_names, buy_order, sell_order):

    file_name = 'bazaar_data/' + snapshot + '.csv'
    bazaar_data = pd.read_csv(file_name)
    shard_data = bazaar_data[bazaar_data['productId'].str.startswith('SHARD_')].copy()

    if buy_order:
        shard_data['buy'] = shard_data['sellPrice']  
    else:
        shard_data['buy'] = shard_data['buyPrice']   

    if sell_order:
        shard_data['sell'] = shard_data['buyPrice']  
    else:
        shard_data['sell'] = shard_data['sellPrice'] 

    shard_data['name'] = shard_data['productId'].map(shard_names)

    return shard_data[['name', 'buy', 'sell']]



def getMaxProfit(fusion):
    input1_cost = int(fusion['Input1_Quantity']) * float(shard_buy[fusion['Input1_Name']])
    input2_cost = int(fusion['Input2_Quantity']) * float(shard_buy[fusion['Input2_Name']])

    if input1_cost == 0:
        input1_cost = float('inf')
    if input2_cost == 0:
        input2_cost = float('inf')

    input_cost = input1_cost + input2_cost
    output_costs = [
        float("-inf"),
        float("-inf"),
        float("-inf")
    ]



    if not pd.isna(fusion['Output1_Name']):
        output_costs[0] = int(fusion['Output1_Quantity']) * float(shard_sell[fusion['Output1_Name']])
        
    if not pd.isna(fusion['Output2_Name']):
        output_costs[1] = int(fusion['Output2_Quantity']) * float(shard_sell[fusion['Output2_Name']])

    if not pd.isna(fusion['Output3_Name']):
        output_costs[2] = int(fusion['Output3_Quantity']) * float(shard_sell[fusion['Output3_Name']])

    max_profit_index = int(output_costs.index(max(output_costs)))
    max_profit = output_costs[max_profit_index] - input_cost
    return pd.Series({'output_index':max_profit_index, 'profit':max_profit})


buy_order = False
sell_order = False
print(f"Buy Order: {buy_order}  Sell Order: {sell_order}")

snapshot = '2025_7_10_17_30'
shard_prices = fetchShardPrices(snapshot, shard_names, buy_order, sell_order)
shard_buy = shard_prices.set_index('name')['buy'].to_dict()
shard_sell = shard_prices.set_index('name')['sell'].to_dict()


# Fetch the shard recipes
fusion_recipes = pd.read_csv("fusion_recipes.csv")
fusion_recipes = fusion_recipes[['Input1_Quantity', 'Input1_Name', 'Input2_Quantity', 'Input2_Name', 'Output1_Quantity', 'Output1_Name', 'Output2_Quantity', 'Output2_Name', 'Output3_Quantity', 'Output3_Name',]]

fusion_recipes[['output_index', 'profit']] = fusion_recipes.apply(getMaxProfit, axis=1)
fusion_recipes = fusion_recipes.sort_values('profit', ascending=False)

fusion_recipes['profit_percent'] = 100 * fusion_recipes['profit'] / (
    fusion_recipes['Input1_Quantity'].astype(float) * shard_prices.set_index('name').loc[fusion_recipes['Input1_Name']]['buy'].values +
    fusion_recipes['Input2_Quantity'].astype(float) * shard_prices.set_index('name').loc[fusion_recipes['Input2_Name']]['buy'].values
)

print(fusion_recipes.head(50))
fusion_recipes = fusion_recipes.sort_values('profit_percent', ascending=False)
print(fusion_recipes.head(50))


