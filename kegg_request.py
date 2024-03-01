import requests

# Define a function to query the KEGG API for pathway information
def query_kegg_pathway(pathway_id):
    """
    Fetches details for a given pathway ID from the KEGG API.

    Args:
    - pathway_id (str): The ID of the pathway to retrieve, e.g., "hsa00010".

    Returns:
    - dict: Parsed pathway information if successful, None otherwise.
    """
    base_url = "http://rest.kegg.jp/get/"
    response = requests.get(f"{base_url}{pathway_id}")

    if response.status_code == 200:
        return parse_kegg_response(response.text)
    else:
        print(f"Failed to retrieve data for pathway {pathway_id}. Status code: {response.status_code}")
        return None

def parse_kegg_response(response_text):
    """
    Parses the plain text response from KEGG into a structured dictionary.

    Args:
    - response_text (str): The plain text response from KEGG.

    Returns:
    - dict: A dictionary with parsed pathway information.
    """
    # Example parsing logic; this should be adapted based on your specific needs
    pathway_info = {}
    lines = response_text.split('\n')
    current_section = None
    
    for line in lines:
        # Check for a new section
        if line.startswith("ENTRY") or line.startswith("NAME") or line.startswith("DESCRIPTION"):
            current_section = line.split()[0]
            pathway_info[current_section] = " ".join(line.split()[1:])
        elif current_section in pathway_info:
            # Continue appending information to the current section
            pathway_info[current_section] += " " + line.strip()
        else:
            # Handle other cases as needed
            continue
    
    return pathway_info

# Example usage
# pathway_id = "hsa00010"  # Example pathway ID for Glycolysis / Gluconeogenesis
# pathway_info = query_kegg_pathway(pathway_id)
# print(pathway_info)

pathway_id = "path:map00010"  # Glycolysis / Gluconeogenesis pathway
pathway_info = query_kegg_pathway(pathway_id)
print(pathway_info)

# # Mock response (simplified for demonstration)
# mock_response = """ENTRY       map00010
# NAME        Glycolysis / Gluconeogenesis
# GENE        HK1; Hexokinase 1
#             PFKL; Phosphofructokinase, liver type
# """

# # Parse the mock response
# parsed_response = parse_kegg_response(mock_response)

# # Check the results
# print(parsed_response)