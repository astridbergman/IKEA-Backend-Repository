import json

def load_sources():
    with open("FairSource/data/database.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    return data

def get_baseInfo():
    sources = load_sources()
    regions = {}

    for source in sources["sources"]:
         region = source["region"]
         score = source["score"]

         if region not in regions:
              regions[region] = []
        
         regions[region].append(score)
    return calculate_region_scores(regions)

#----At the moment thinks the frontend handles the region name and score
def get_regionInfo(chosenRegion):
     sources = load_sources()
     region_sources = []

     for source in sources["sources"]:
          if source["region"] == chosenRegion:
               region_sources.append({
                    "type of source": source["type_of_source"],
                    "score": source["score"],
                    "summary": source["summary"]
               }
               )
     return region_sources
          


###-----Region score is currently calcutaled as the avergare of all scores for the region.---------------
def calculate_region_scores(regions):
     return [
          {
               "region": region,
               "score": sum(scores) / len(scores)
          }
          for region, scores in regions.items()
     ]
           
