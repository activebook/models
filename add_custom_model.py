import json
import os
import argparse
from sync_models import update_index

def add_custom_model(provider, model_name, context_length, max_tokens):
    """Create a custom model JSON file and update the index."""
    template_path = 'template.json'
    if not os.path.exists(template_path):
        print(f"Error: {template_path} not found.")
        return

    with open(template_path, 'r') as f:
        data = json.load(f)

    # Sanitize and set IDs
    model_id = f"{provider}/{model_name}"
    filename = f"{provider}_{model_name}.json"
    output_dir = 'models'
    filepath = os.path.join(output_dir, filename)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Update template data
    data['id'] = model_id
    data['name'] = f"{provider.capitalize()}: {model_name}"
    data['context_length'] = int(context_length)
    data['top_provider']['context_length'] = int(context_length)
    data['top_provider']['max_completion_tokens'] = int(max_tokens) if max_tokens else None

    with open(filepath, 'w') as f_out:
        json.dump(data, f_out, indent=2)

    print(f"Successfully created custom model: {filepath}")
    
    # Refresh list.json
    update_index()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a custom model to the registry.")
    parser.add_argument("provider", help="Provider name (e.g., openai, custom)")
    parser.add_argument("model", help="Model name (e.g., gpt-5, my-model)")
    parser.add_argument("context", type=int, help="Context length (tokens)")
    parser.add_argument("max_tokens", type=int, help="Max completion tokens")

    args = parser.parse_args()
    add_custom_model(args.provider, args.model, args.context, args.max_tokens)
