# assumes yaml.safe_load(file) object
from pathlib import Path

def summarize_toc(data, output_file):
    toc_summary = "Summary of ToC and Files\n"
    toc_summary += "\nsummarize_toc: Table of Contents Summary\n"
    count_toc_components = []
    Np = 0
    for p in data['parts']:
        Np += 1
        toc_summary += f"========\n"
        toc_summary += f"Part {Np}: {p['caption']}\n"
        toc_summary += f"========\n"
        toc_summary += f"\tChapters\n"
        toc_summary += f"\t========\n"
        Nc = 0
        for c in p['chapters']:
            Nc += 1
            toc_summary += f"\t {Nc:2}:  file: ./{c['file']}\n"
            if 'title' in c.keys():
                toc_summary += f"\t     title: {c['title']}\n"
            
            
            if 'sections' in c.keys():
                toc_summary += f"\t\tSections in Chapter {Nc}\n"
                toc_summary += f"\t\t======================\n"
                Ns = 0
                for s in c['sections']:
                    Ns += 1
                    toc_summary += f"\t\t {Ns:2}:  file: ./{s['file']}\n"
                    if 'title' in s.keys():
                        toc_summary += f"\t\t     title: {s['title']}\n"
                    if 'sections' in s.keys():
                        toc_summary += f"\t\t\tSub-sections in Section {Ns}\n"
                        toc_summary += f"\t\t\t==========================\n"
                        Nss = 0
                        for ss in s['sections']:
                            Nss += 1
                            toc_summary += f"\t\t\t {Nss:2}:  file: ./{ss['file']}\n"
                            if 'title' in ss.keys():
                                toc_summary += f"\t\t\t     title: {ss['title']}\n"
                            if 'sections' in ss.keys():
                                toc_summary += f"\t\t\t\tSub-sub-sections in Sub-section {Nss}\n"
                                toc_summary += f"\t\t\t\t====================================\n"
                                Nsss = 0
                                for sss in ss['sections']:
                                    Nsss += 1
                                    toc_summary += f"\t\t\t\t {Nsss:2}:  file: ./{sss['file']}\n"
                                    if 'title' in sss.keys():
                                        toc_summary += f"\t\t\t\t     title: {sss['title']}\n"
                                if 'sections' in sss.keys():
                                    toc_summary += f"WARNING-----------^^^^^^^^^ this sub-sub-section has unprocessed sub-sub-sub-sections\n"
                        else:
                            toc_summary += f"\t\t\tSection {Ns:2} has no sub-sections\n"

    with open(output_file, 'w') as f:
        f.write(toc_summary)
