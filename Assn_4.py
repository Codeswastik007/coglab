import pandas as pd

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

categories = ["billing", "account", "general"]

def create_entry(digit, number):
    category = categories[digit % 3]

    templates = {
        "billing": {
            "question": f"how do i check my bill for account {number}",
            "answer": "You can check your bill from the Billing section.",
            "keywords": "bill payment charge amount",
            "category": category
        },
        "account": {
            "question": f"how do i update my account details {number}",
            "answer": "Go to Settings > Account to update your details.",
            "keywords": "account profile update details",
            "category": category
        },
        "general": {
            "question": f"where can i get general help {number}",
            "answer": "You can get help from the Help section.",
            "keywords": "help support information guide",
            "category": category
        }
    }

    return templates[category]

def score_query(query, entry):
    query_words = set(query.lower().split())
    text = entry["keywords"].lower().split()
    return sum(word in text for word in query_words)

def generate_hypothesis(query, df):
    scores = df.apply(lambda row: score_query(query, row), axis=1)
    max_score = scores.max()

    if max_score == 0:
        return df.iloc[0:0].copy()

    return df[scores == max_score].copy()

def same_category(category_name, df):
    return df[df["category"].str.lower() == category_name.lower()]

roll_number = input("Enter your 6-digit college roll number: ").strip()

while len(roll_number) != 6 or not roll_number.isdigit():
    roll_number = input("Enter a valid 6-digit college roll number: ").strip()

digits = [int(d) for d in roll_number[-2:]]

generated_entries = [
    create_entry(digits[0], digits[0]),
    create_entry(digits[1], digits[1])
]

df = pd.DataFrame(fixed_entries + generated_entries)

print("\nFinal 6-row DataFrame:")
print(df.to_string(index=False))

print("\nCategory Search")
category_name = input("Enter a category: ").strip()
category_result = same_category(category_name, df)
print(category_result.to_string(index=False) if not category_result.empty else "No entries found.")

print("\nQ4: Add Keyword")
entry_number = int(input(f"Pick an entry number (1-{len(df)}): ")) - 1
new_keyword = input("Enter a new keyword: ").strip().lower()

if 0 <= entry_number < len(df) and new_keyword:
    keywords = df.at[entry_number, "keywords"].split()
    if new_keyword not in keywords:
        keywords.append(new_keyword)
    df.at[entry_number, "keywords"] = " ".join(keywords)

csv_file = f"{roll_number}_faq_data.csv"
df.to_csv(csv_file, index=False)

print(f"\nUpdated DataFrame saved to {csv_file}")

print("\nQ5: Query")
query = input("Enter your query: ").strip()
matches = generate_hypothesis(query, df)

if matches.empty:
    print("No matching FAQ found.")
else:
    print(matches.to_string(index=False))

print("\nQ6: Tie Demonstration")
tie_query = "fee"
tie_matches = generate_hypothesis(tie_query, df)

print(f'Query: "{tie_query}"')
if tie_matches.empty:
    print("No matching FAQ found.")
else:
    print(tie_matches.to_string(index=False))
