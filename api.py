import re
from typing import Dict, List

def extract_data(input_string: str, patterns: Dict[str, str]) -> Dict[str, List[str]]:
    """
    Extracts data from the input string based on provided regex patterns.

    Args:
        input_string (str): The string to search for matches.
        patterns (Dict[str, str]): A dictionary where keys are data types and values are regex patterns.

    Returns:
        Dict[str, List[str]]: A dictionary containing extracted data for each data type.
    """
    results = {}
    for data_type, pattern in patterns.items():
        matches = re.findall(pattern, input_string)
        results[data_type] = matches
    return results


input_string = """
user@example.com firstname.lastname@company.co.uk invalid-email
https://www.example.com http://subdomain.example.org/page ftp://not-a-valid-url
(123) 456-7890 123-456-7890 123.456.7890 not-a-phone-number
1234 5678 9012 3456 1234-5678-9012-3456 invalid-card
14:30 2:30 PM invalid-time
<p> <div class="example"> <img src="image.jpg" alt="description">
#example #ThisIsAHashtag invalid-hashtag
$19.99 $1,234.56 invalid-currency
"""

patterns = {
    "Email Addresses": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?[^\s]*",
    "Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "Credit Card Numbers": r"(?:\d{4}[-\s]?){3}\d{4}",
    "Times": r"\b(?:\d{1,2}:\d{2}(?:\s?(?:AM|PM))?)\b",
    "HTML Tags": r"<[^>]+>",
    "Hashtags": r"#\w+",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

extracted_data = extract_data(input_string, patterns)

for data_type, matches in extracted_data.items():
    print(f"{data_type}: {matches}")
