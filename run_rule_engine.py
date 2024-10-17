from rule_engine.api import create_rule, combine_rules
from rule_engine.evaluator import evaluate_rule

def main():
    # Example rule
    rule1 = create_rule("age > 30 AND department = 'Sales'")
    rule2 = create_rule("salary > 50000 OR experience > 5")

    # Evaluate the first rule
    data1 = {"age": 35, "department": "Sales"}
    result1 = evaluate_rule(rule1, data1)
    print(f"Evaluation of rule1: {result1}")  # Expected output: True

    # Evaluate the second rule
    data2 = {"salary": 60000, "experience": 4}
    result2 = evaluate_rule(rule2, data2)
    print(f"Evaluation of rule2: {result2}")  # Expected output: True

    # Combine rules
    combined_rule = combine_rules([rule1, rule2])
    print("Combined rule created.")

if _name_ == "_main_":
    main()
