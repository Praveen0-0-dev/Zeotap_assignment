import unittest
from .api import create_rule, combine_rules
from .evaluator import evaluate_rule

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule = create_rule("age > 30 AND department = 'Sales'")
        self.assertIsNotNone(rule)  # Ensure rule is created

    def test_evaluate_rule(self):
        rule = create_rule("age > 30 AND department = 'Sales'")
        result = evaluate_rule(rule, {"age": 35, "department": "Sales"})
        self.assertTrue(result)  # Should return True

    def test_combine_rules(self):
        rules = [
            "age > 30 AND department = 'Sales'",
            "salary > 50000 OR experience > 5"
        ]
        combined_rule = combine_rules(rules)
        self.assertIsNotNone(combined_rule)  # Ensure combined rule is created

if _name_ == "_main_":
    unittest.main()
