from flask import Flask, render_template, send_from_directory
import os, random

app = Flask(__name__)

#Paths to the foldesr with all the images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COMMAND_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Command")
CUNNING_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Cunning")
AGGRESSION_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Aggression")
VIGILANCE_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Vigilance")
HEROISM_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Heroism")
VILLAINY_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Villainy")
NEUTRAL_FOLDER = os.path.join(BASE_DIR, "static", "Commons", "Neutral")

UNCOMMON_COMMAND_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Command")
UNCOMMON_CUNNING_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Cunning")
UNCOMMON_AGGRESSION_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Aggression")
UNCOMMON_VIGILANCE_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Vigilance")
UNCOMMON_HEROISM_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Heroism")
UNCOMMON_VILLAINY_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Villainy")
UNCOMMON_NEUTRAL_FOLDER = os.path.join(BASE_DIR, "static", "Uncommons", "Neutral")

RARE_COMMAND_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Command")
RARE_CUNNING_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Cunning")
RARE_AGGRESSION_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Aggression")
RARE_VIGILANCE_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Vigilance")
RARE_HEROISM_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Heroism")
RARE_VILLAINY_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Villainy")
#RARE_NEUTRAL_FOLDER = os.path.join(BASE_DIR, "static", "Rares", "Neutral")

LEGENDARY_COMMAND_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Command")
LEGENDARY_CUNNING_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Cunning")
LEGENDARY_AGGRESSION_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Aggression")
LEGENDARY_VIGILANCE_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Vigilance")
LEGENDARY_HEROISM_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Heroism")
LEGENDARY_VILLAINY_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Villainy")
LEGENDARY_NEUTRAL_FOLDER = os.path.join(BASE_DIR, "static", "Legendary", "Neutral")

#Get commons, uncommons are similar below
def GetCommons():
    command_files = [f for f in os.listdir(COMMAND_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    cunning_files = [f for f in os.listdir(CUNNING_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    aggression_files = [f for f in os.listdir(AGGRESSION_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    vigilance_files = [f for f in os.listdir(VIGILANCE_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    heroism_files = [f for f in os.listdir(HEROISM_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    villainy_files = [f for f in os.listdir(VILLAINY_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    neutral_files = [f for f in os.listdir(NEUTRAL_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    #Shuffles each color
    random.shuffle(command_files)
    random.shuffle(cunning_files)
    random.shuffle(aggression_files)
    random.shuffle(vigilance_files)
    random.shuffle(heroism_files)
    random.shuffle(villainy_files)
    random.shuffle(neutral_files)
    #Picks the first of the shuffled for each color, then removes it. This prevents duplicates in a single pack. (I know that sometimes there are foils or whatever, don't worry about it for now)
    commandselected=command_files[0]
    command_files.remove(commandselected)
    cunningselected=cunning_files[0]
    cunning_files.remove(cunningselected)
    aggressionselected=aggression_files[0]
    aggression_files.remove(aggressionselected)
    vigilanceselected=vigilance_files[0]
    vigilance_files.remove(vigilanceselected)
    all_files=[command_files,cunning_files,aggression_files,vigilance_files,heroism_files,villainy_files,neutral_files]
    otherselected=all_files[:6]
    selected = [
        ("Command", command_files.pop(0)),
        ("Cunning", cunning_files.pop(0)),
        ("Aggression", aggression_files.pop(0)),
        ("Vigilance", vigilance_files.pop(0)),
    ]
    combined_remaining = []
    for folder_name, files in [
      ("Command", command_files),
      ("Cunning", cunning_files),
      ("Aggression", aggression_files),
      ("Vigilance", vigilance_files),
      ("Heroism", heroism_files),
      ("Villainy", villainy_files),
      ("Neutral", neutral_files),
    ]:
      combined_remaining.extend([(folder_name, f) for f in files])

    random.shuffle(combined_remaining)
    additional_selected=combined_remaining[:6]
    selected.extend(additional_selected)
    return selected

def GetUncommons():
    command_files = [f for f in os.listdir(UNCOMMON_COMMAND_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    cunning_files = [f for f in os.listdir(UNCOMMON_CUNNING_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    aggression_files = [f for f in os.listdir(UNCOMMON_AGGRESSION_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    vigilance_files = [f for f in os.listdir(UNCOMMON_VIGILANCE_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    heroism_files = [f for f in os.listdir(UNCOMMON_HEROISM_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    villainy_files = [f for f in os.listdir(UNCOMMON_VILLAINY_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    neutral_files = [f for f in os.listdir(UNCOMMON_NEUTRAL_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    random.shuffle(command_files)
    random.shuffle(cunning_files)
    random.shuffle(aggression_files)
    random.shuffle(vigilance_files)
    random.shuffle(heroism_files)
    random.shuffle(villainy_files)
    random.shuffle(neutral_files)
    combined_remaining = []
    for folder_name, files in [
      ("UncommonCommand", command_files),
      ("UncommonCunning", cunning_files),
      ("UncommonAggression", aggression_files),
      ("UncommonVigilance", vigilance_files),
      ("UncommonHeroism", heroism_files),
      ("UncommonVillainy", villainy_files),
      ("UncommonNeutral", neutral_files),
    ]:
      combined_remaining.extend([(folder_name, f) for f in files])

    random.shuffle(combined_remaining)
    selected=[]
    additional_selected=combined_remaining[:3]
    selected.extend(additional_selected)
    return selected

def GetRare():
    command_files = [f for f in os.listdir(RARE_COMMAND_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    cunning_files = [f for f in os.listdir(RARE_CUNNING_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    aggression_files = [f for f in os.listdir(RARE_AGGRESSION_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    vigilance_files = [f for f in os.listdir(RARE_VIGILANCE_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    heroism_files = [f for f in os.listdir(RARE_HEROISM_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    villainy_files = [f for f in os.listdir(RARE_VILLAINY_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    #neutral_files = [f for f in os.listdir(RARE_NEUTRAL_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    random.shuffle(command_files)
    random.shuffle(cunning_files)
    random.shuffle(aggression_files)
    random.shuffle(vigilance_files)
    random.shuffle(heroism_files)
    random.shuffle(villainy_files)
    #random.shuffle(neutral_files)
    #selected = files[:15]
    combined_remaining = []
    for folder_name, files in [
      ("RareCommand", command_files),
      ("RareCunning", cunning_files),
      ("RareAggression", aggression_files),
      ("RareVigilance", vigilance_files),
      ("RareHeroism", heroism_files),
      ("RareVillainy", villainy_files),
      #("RareNeutral", neutral_files),
    ]:
      combined_remaining.extend([(folder_name, f) for f in files])

    random.shuffle(combined_remaining)
    selected=[combined_remaining[0]]

    return selected

def GetLegendary():
    command_files = [f for f in os.listdir(LEGENDARY_COMMAND_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    cunning_files = [f for f in os.listdir(LEGENDARY_CUNNING_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    aggression_files = [f for f in os.listdir(LEGENDARY_AGGRESSION_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    vigilance_files = [f for f in os.listdir(LEGENDARY_VIGILANCE_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    heroism_files = [f for f in os.listdir(LEGENDARY_HEROISM_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    villainy_files = [f for f in os.listdir(LEGENDARY_VILLAINY_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    neutral_files = [f for f in os.listdir(LEGENDARY_NEUTRAL_FOLDER) if f.lower().endswith(('png','jpg','jpeg','gif','webp'))]
    random.shuffle(command_files)
    random.shuffle(cunning_files)
    random.shuffle(aggression_files)
    random.shuffle(vigilance_files)
    random.shuffle(heroism_files)
    random.shuffle(villainy_files)
    random.shuffle(neutral_files)
    #selected = files[:15]
    combined_remaining = []
    for folder_name, files in [
      ("LegendaryCommand", command_files),
      ("LegendaryCunning", cunning_files),
      ("LegendaryAggression", aggression_files),
      ("LegendaryVigilance", vigilance_files),
      ("LegendaryHeroism", heroism_files),
      ("LegendaryVillainy", villainy_files),
      ("LegendaryNeutral", neutral_files),
    ]:
      combined_remaining.extend([(folder_name, f) for f in files])

    random.shuffle(combined_remaining)
    selected=[combined_remaining[0]]

    return selected

@app.route('/')
def index():
  #Where the magic happens (Or rather where the SWU happens)
  legendaryChance=random.randrange(1,7)
  selectedCommons=GetCommons()
  selectedUncommons=GetUncommons()
  selected=[]
  selected.extend(selectedCommons)
  selected.extend(selectedUncommons)
  if legendaryChance==6:
    selectedLegendary=GetLegendary()
    selected.extend(selectedLegendary)
  else:
     selectedRare=GetRare()
     selected.extend(selectedRare)
  return render_template("Draftsim.html", images=selected)

# Route to serve images directly from the folder. If you want to add more to this you gotta do the folder stuff at the top
@app.route('/images/<folder>/<path:filename>')
def serve_image(folder,filename):
  folder_map = {
    "Command": COMMAND_FOLDER,
    "Cunning": CUNNING_FOLDER,
    "Aggression": AGGRESSION_FOLDER,
    "Vigilance": VIGILANCE_FOLDER,
    "Heroism": HEROISM_FOLDER,
    "Villainy": VILLAINY_FOLDER,
    "Neutral": NEUTRAL_FOLDER,
    "UncommonCommand":UNCOMMON_COMMAND_FOLDER,
    "UncommonCunning":UNCOMMON_CUNNING_FOLDER,
    "UncommonAggression":UNCOMMON_AGGRESSION_FOLDER,
    "UncommonVigilance":UNCOMMON_VIGILANCE_FOLDER,
    "UncommonHeroism":UNCOMMON_HEROISM_FOLDER,
    "UncommonVillainy":UNCOMMON_VILLAINY_FOLDER,
    "UncommonNeutral":UNCOMMON_NEUTRAL_FOLDER,
    "RareCommand":RARE_COMMAND_FOLDER,
    "RareCunning":RARE_CUNNING_FOLDER,
    "RareAggression":RARE_AGGRESSION_FOLDER,
    "RareVigilance":RARE_VIGILANCE_FOLDER,
    "RareHeroism":RARE_HEROISM_FOLDER,
    "RareVillainy":RARE_VILLAINY_FOLDER,
    #"RareNeutral":RARE_NEUTRAL_FOLDER,
    "LegendaryCommand":LEGENDARY_COMMAND_FOLDER,
    "LegendaryCunning":LEGENDARY_CUNNING_FOLDER,
    "LegendaryAggression":LEGENDARY_AGGRESSION_FOLDER,
    "LegendaryVigilance":LEGENDARY_VIGILANCE_FOLDER,
    "LegendaryHeroism":LEGENDARY_HEROISM_FOLDER,
    "LegendaryVillainy":LEGENDARY_VILLAINY_FOLDER,
    "LegendaryNeutral":LEGENDARY_NEUTRAL_FOLDER

  }
  folder_path = folder_map.get(folder)
  return send_from_directory(folder_path, filename)

if __name__ == "__main__":
    app.run(debug=True)
