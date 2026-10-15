import json
from datetime import date

def load_constraints():
    with open("FairSource/data/constraints.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def calculate_region_scores(regions):

    constraints = load_constraints()["constraints"]
    regions_factored = {}

    for region, sources in regions.items():
        regions_factored[region] = []

        for source in sources:
            factors = extract_source_data(source)
            new_score = count_factored_score(factors, constraints["source_types"][factors["source_type"]])

            regions_factored[region].append(new_score)
    print(regions_factored)
    return normalization_regionscore(regions_factored)

    


def extract_source_data(source):
    return {
        "score": source["severity"],
        "source_type": source["source_id"],
        "date_made": source["published_at"],
    }


#should return a score for a source after its type of source and date made is taken into consideration
def count_factored_score(factors, constraints):
    decay = date_factor(factors["date_made"], constraints["half_life_days"])

    return {
        "score": factors["score"] * decay,
        "weight": constraints["weight"]
    }


# Date decay, count the date "score".
def date_factor(made, half_life_days):
    date_made = date.fromisoformat(made)
    today = date.today()

    age_days = (today - date_made).days

    decay = 2 ** (-age_days / half_life_days)
    return decay



# Region score
def normalization_regionscore(regions):
    regions_scores = []
    for region, scores in regions.items():

        weighted_scores = [item["score"] for item in scores]
        weights = [item["weight"] for item in scores]
        region_score = round(sum(weighted_scores) / sum(weights), 1)

        regions_scores.append({
            "region": region,
            "score": region_score
        })
    return regions_scores