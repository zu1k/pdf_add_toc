import re
from typing import List
from fitzutils import ToCEntry

def parse_toc(data: str, offset = 0) -> List[ToCEntry]:
    lines = data.strip().split('\n')
    entries = []
    
    for line in lines:
        match = re.match(r'(\d+) \(p((?:\d+-)*\d+)\): (.+)', line)
        if match:
            page = match.group(1)
            level_tuple = tuple(map(int, match.group(2).split('-')))
            title = match.group(3)
            entries.append((level_tuple, title, page))
    
    entries.sort()
    
    result = []
    for level_tuple, title, page in entries:
        toc_entry = ToCEntry(
            len(level_tuple),
            title,
            int(page) + offset
        )
        result.append(toc_entry)

    result[0].level = 1
    if entries[0][0][0] == 0:
        result[0].pagenum = result[0].pagenum - offset
    return result