import json

def format_to_jsonl_with_system(input_file_path, output_file_path):
    messages_blocks = []

    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        current_block = []
        for line in lines:
            if line.startswith('система:'):
                if current_block:
                    messages_blocks.append(current_block)
                    current_block = []
                current_block.append({"role": "system", "content": line.replace('система:', '').strip()})
            elif line.startswith('вопрос:'):
                current_block.append({"role": "user", "content": line.replace('вопрос:', '').strip()})
            elif line.startswith('ответ:'):
                current_block.append({"role": "assistant", "content": line.replace('ответ:', '').strip()})

        if current_block:
            messages_blocks.append(current_block)

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for block in messages_blocks:
            json_record = {"messages": block}
            json.dump(json_record, outfile, ensure_ascii=False)
            outfile.write('\n')

input_file_path = 'raw_dataset.txt'
output_file_path = 'formatted_dataset.jsonl'
format_to_jsonl_with_system(input_file_path, output_file_path)
