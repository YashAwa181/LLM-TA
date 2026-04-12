import json

with open(r'd:\00 My Studies\QMUL\sem 2\Large Language Models & Textual analysis\cw\ProjectA_Market_Strategy.ipynb', encoding='utf-8') as f:
    data = json.load(f)

with open('cells_output.txt', 'w', encoding='utf-8') as out:
    for i, cell in enumerate(data['cells']):
        out.write(f"\n--- Cell {i} ({cell['cell_type']}) ---\n")
        source = cell.get('source', [])
        if isinstance(source, list):
            out.write(''.join(source))
        else:
            out.write(source)
        out.write('\n')
