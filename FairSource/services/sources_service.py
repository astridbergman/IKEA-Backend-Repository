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

###-----Region score is currently calcutaled as the avergare of all scores for the region.---------------
def calculate_region_scores(regions):
     return [
          {
               "region": region,
               "score": sum(scores) / len(scores)
          }
          for region, scores in regions.items()
     ]
           
