import json
import os
import requests

def fetch_models():
    """Retrieve model info from OpenRouter and save to raw_models.json."""
    url = "https://openrouter.ai/api/v1/models"
    print(f"Fetching models from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        with open('raw_models.json', 'w') as f:
            json.dump(data, f, indent=2)
        print("Successfully updated raw_models.json")
        return data
    except Exception as e:
        print(f"Error fetching models: {e}")
        return None

def split_models():
    """Fetch model data and split into individual JSON files in the models folder."""
    data = fetch_models()
    if not data or 'data' not in data:
        print("No model data to split.")
        return
    
    output_dir = 'models'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    models_list = data.get('data', [])
    for model in models_list:
        model_id = model.get('id')
        if not model_id:
            continue
        
        # Replace / with _ for filename safety
        filename = f"{model_id.replace('/', '_')}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f_out:
            json.dump(model, f_out, indent=2)
            
    print(f"Successfully processed {len(models_list)} models into '{output_dir}/' folder.")

if __name__ == "__main__":
    split_models()
