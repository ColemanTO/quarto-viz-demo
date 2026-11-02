"""Generate a synthetic 90-day food log (nutrition.csv). Stdlib only, seeded."""
import csv
import random
from datetime import date, timedelta

random.seed(42)

# name, category, kcal, protein_g, carbs_g, fat_g, fiber_g, sodium_mg (per serving)
FOODS = {
    "breakfast": [
        ("Oatmeal with berries", "Grains", 280, 9, 50, 5, 7, 120),
        ("Scrambled eggs (2)", "Protein", 190, 13, 2, 14, 0, 340),
        ("Greek yogurt with honey", "Dairy", 220, 17, 28, 5, 0, 90),
        ("Avocado toast", "Grains", 320, 8, 32, 18, 9, 380),
        ("Banana", "Fruit", 105, 1, 27, 0, 3, 1),
        ("Cold brew with milk", "Drinks", 45, 2, 4, 2, 0, 30),
        ("Granola bar", "Snacks", 190, 4, 29, 7, 2, 105),
    ],
    "lunch": [
        ("Chicken burrito bowl", "Protein", 640, 42, 68, 20, 12, 1150),
        ("Turkey sandwich", "Grains", 460, 28, 46, 18, 4, 1280),
        ("Lentil soup", "Legumes", 330, 18, 52, 5, 16, 820),
        ("Caesar salad with chicken", "Vegetables", 480, 34, 18, 31, 4, 980),
        ("Sushi rolls (8 pc)", "Grains", 380, 14, 62, 8, 3, 920),
        ("Tuna poke bowl", "Protein", 520, 36, 58, 15, 5, 870),
        ("Veggie wrap", "Vegetables", 410, 13, 55, 15, 9, 860),
    ],
    "dinner": [
        ("Salmon with rice and broccoli", "Protein", 620, 41, 55, 25, 6, 520),
        ("Spaghetti bolognese", "Grains", 720, 32, 88, 24, 7, 880),
        ("Chicken stir-fry", "Protein", 540, 38, 46, 20, 6, 1020),
        ("Veggie curry with naan", "Vegetables", 680, 17, 92, 26, 12, 940),
        ("Steak with potatoes", "Protein", 780, 52, 48, 42, 5, 640),
        ("Margherita pizza (3 slices)", "Grains", 810, 33, 96, 31, 5, 1460),
        ("Black bean tacos (3)", "Legumes", 570, 21, 78, 19, 15, 790),
    ],
    "snack": [
        ("Apple with peanut butter", "Fruit", 270, 7, 32, 14, 6, 90),
        ("Almonds (1 oz)", "Snacks", 165, 6, 6, 14, 3, 0),
        ("Dark chocolate (2 sq)", "Snacks", 120, 1, 10, 9, 2, 5),
        ("Hummus and carrots", "Vegetables", 190, 6, 22, 9, 6, 310),
        ("Potato chips", "Snacks", 230, 3, 23, 15, 2, 340),
        ("Protein shake", "Drinks", 160, 25, 6, 3, 1, 210),
        ("Cheese and crackers", "Dairy", 250, 9, 21, 15, 1, 460),
    ],
}

START = date(2026, 8, 4)
DAYS = 90

rows = []
for i in range(DAYS):
    d = START + timedelta(days=i)
    weekend = d.weekday() >= 5
    plan = [("breakfast", 1.0 if random.random() > 0.15 else 0.0), ("lunch", 1.0), ("dinner", 1.0)]
    n_snacks = random.choice([0, 1, 1, 2]) + (1 if weekend else 0)
    plan += [("snack", 1.0)] * n_snacks
    for meal, p in plan:
        if not p:
            continue
        name, cat, kcal, pro, carb, fat, fib, na = random.choice(FOODS[meal])
        # Weekends skew toward bigger portions; add per-entry noise
        servings = round(random.choice([0.75, 1, 1, 1, 1.25, 1.5]) * (1.15 if weekend and meal != "snack" else 1), 2)
        rows.append({
            "date": d.isoformat(),
            "meal": meal,
            "food": name,
            "category": cat,
            "servings": servings,
            "calories": round(kcal * servings),
            "protein_g": round(pro * servings, 1),
            "carbs_g": round(carb * servings, 1),
            "fat_g": round(fat * servings, 1),
            "fiber_g": round(fib * servings, 1),
            "sodium_mg": round(na * servings),
        })

with open("nutrition.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

print(f"wrote {len(rows)} rows over {DAYS} days")
