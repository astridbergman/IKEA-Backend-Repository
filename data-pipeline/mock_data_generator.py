import argparse
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

source_ids = ["news", "audit", "research","un"]

regions = [
    "Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", 
    "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei", 
    "Heilongjiang", "Henan", "Hong Kong", "Hubei", "Hunan", 
    "Inner Mongolia", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", 
    "Macau", "Ningxia", "Qinghai", "Shaanxi", "Shandong", 
    "Shanghai", "Shanxi", "Sichuan", "Taiwan", "Tianjin", 
    "Tibet", "Xinjiang", "Yunnan", "Zhejiang"
]

riskCategories = [ 
    "working_hours",
    "wages",
    "workplace_safety",
    "child_labour",
    "forced_labour",
    "freedom_of_association",
    ]

titles = ["Fictional bulletin notes a synthetic shift change", "Mock report flags a simulated payroll question", "Invented dispatch mentions a hypothetical safety review"]


def mockConnector(count: int, rng: random.Random):

    records = []
    for i in range(count):
        region = rng.choice(regions)
        category = rng.choice(riskCategories)
        source_id = rng.choice(source_ids)
        severity = rng.randint(1,10)
        if source_id == "audit":
            supplier_id = f"SYN-SUP-{rng.randint(1000, 9999)}"
        else:
            supplier_id = None
        source_record = {
        "id": i + 1,
        "source_id": source_id,
        "region": region,
        "supplier_id": supplier_id,
        "risk_category": category,
        "severity": severity,
        "observed_at": datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(days=rng.randrange(365)),
        "published_at": datetime(2025, 1, 1, tzinfo=timezone.utc) + timedelta(days=rng.randrange(365)),

        
        }
        records.append(source_record)
    return records


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate mock data records.")
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=10,
        help="number of records to create (default: 10)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=5,
        help="random seed (default: 5)",
    )
    args = parser.parse_args()

    if args.count < 0:
        parser.error("count must be zero or greater")

    records = mockConnector(args.count, random.Random(args.seed))
    output_path = Path(__file__).with_name("mock_data.json")
    output_path.write_text(
        json.dumps(records, default=lambda value: value.isoformat(), indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {len(records)} records to {output_path}")
