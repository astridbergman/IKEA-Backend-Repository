import json
from FairSource.services.score_service import calculate_region_scores

def load_sources():
    with open("FairSource/data/database.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    return data

def get_baseInfo():
    sources = load_sources()
    regions = {}

     #This what ever will be sent to score_service
    for source in sources["sources"]:
         region = source["region"]

         if region not in regions:
              regions[region] = []
        
         regions[region].append(source)
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
          



           
