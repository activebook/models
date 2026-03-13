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

def update_index():
    """Scan the models/ directory and generate list.json index."""
    output_dir = 'models'
    if not os.path.exists(output_dir):
        print(f"Directory '{output_dir}' does not exist.")
        return

    index_list = []
    print(f"Indexing files in {output_dir}/...")
    
    for filename in os.listdir(output_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(output_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    model_data = json.load(f)
                    model_id = model_data.get('id', '')
                    name = model_id.split('/')[-1] if '/' in model_id else model_id
                    
                    if name:
                        index_list.append({
                            "name": name,
                            "file": f"{output_dir}/{filename}"
                        })
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Sort entries by name alphabetically
    index_list.sort(key=lambda x: x['name'])
            
    # Write list.json
    with open('list.json', 'w') as f_list:
        json.dump(index_list, f_list, indent=2)
        
    print(f"Successfully indexed {len(index_list)} models in 'list.json'.")

def sync_models():
    """Fetch model data from OpenRouter and split into individual JSON files."""
    data = fetch_models()
    if not data or 'data' not in data:
        print("No model data to process.")
    else:
        output_dir = 'models'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        models_list = data.get('data', [])
        for model in models_list:
            model_id = model.get('id')
            if not model_id:
                continue
            
            # Determine filename
            filename = f"{model_id.replace('/', '_')}.json"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w') as f_out:
                json.dump(model, f_out, indent=2)
                
        print(f"Processed {len(models_list)} models from OpenRouter.")

    # Always update index from models/ folder
    update_index()

if __name__ == "__main__":
    sync_models()
