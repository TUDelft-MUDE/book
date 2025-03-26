# assumes yaml.safe_load(file) object
from pathlib import Path

def summarize_toc(data, output_file):
    toc_summary = "Summary of ToC and Files\n"
    toc_summary += "Summary of Files\n"
    count_all = [0, 0, 0, 0, 0]
    Np = 0
    credited = False
    for p in data['parts']:
        Np += 1
        count_all[0] +=1
        toc_summary += f"========\n"
        toc_summary += f"Part {Np}: {p['caption']}\n"
        toc_summary += f"========\n"
        toc_summary += f"\tChapters\n"
        toc_summary += f"\t========\n"
        Nc = 0

        if 'credit' in p.keys():
            toc_summary += f"\t    credit: {p['credit']}\n"
            credited = True

        for c in p['chapters']:
            Nc += 1
            count_all[1] +=1
            toc_summary += f"\t {Nc:2}:  file: ./{c['file']}\n"
            if 'title' in c.keys():
                toc_summary += f"\t     title: {c['title']}\n"
            
            if 'credit' in c.keys() and credited:
                toc_summary += f"WARNING-----------^^^^^^^^^\n"
                toc_summary += f"     file has a credit that conflicts with a higher level in toc tree credits\n"
            elif 'credit' in c.keys():
                toc_summary += f"\tt    credit: {c['credit']}\n"
                credited = True

            if 'sections' in c.keys():
                toc_summary += f"\t\tSections in Chapter {Nc}\n"
                toc_summary += f"\t\t======================\n"
                Ns = 0
                for s in c['sections']:
                    Ns += 1
                    count_all[2] +=1
                    toc_summary += f"\t\t {Ns:2}:  file: ./{s['file']}\n"
                    if 'title' in s.keys():
                        toc_summary += f"\t\t     title: {s['title']}\n"

                    if 'sections' in s.keys():
                        toc_summary += f"\t\t\tSub-sections in Section {Ns}\n"
                        toc_summary += f"\t\t\t==========================\n"
                        Nss = 0
                        for ss in s['sections']:
                            Nss += 1
                            count_all[3] +=1
                            toc_summary += f"\t\t\t {Nss:2}:  file: ./{ss['file']}\n"
                            if 'title' in ss.keys():
                                toc_summary += f"\t\t\t     title: {ss['title']}\n"

                            if 'sections' in ss.keys():
                                toc_summary += f"\t\t\t\tSub-sub-sections in Sub-section {Nss}\n"
                                toc_summary += f"\t\t\t\t====================================\n"
                                Nsss = 0
                                for sss in ss['sections']:
                                    Nsss += 1
                                    count_all[4] +=1
                                    toc_summary += f"\t\t\t\t {Nsss:2}:  file: ./{sss['file']}\n"
                                    if 'title' in sss.keys():
                                        toc_summary += f"\t\t\t\t     title: {sss['title']}\n"

                                if 'sections' in sss.keys():
                                    toc_summary += f"WARNING-----------^^^^^^^^^ this sub-sub-section has unprocessed sub-sub-sub-sections\n"
                        else:
                            toc_summary += f"\t\t\tSection {Ns:2} has no sub-sections\n"

        credited = False
    toc_summary_header = "File Count\n==========\n"
    toc_summary_header += f"  Parts:            {count_all[0]:4}\n"
    toc_summary_header += f"  Chapters:         {count_all[1]:4}\n"
    toc_summary_header += f"  Sections:         {count_all[2]:4}\n"
    toc_summary_header += f"  Sub-sections:     {count_all[3]:4}\n"
    toc_summary_header += f"  Sub-sub-sections: {count_all[4]:4}\n"
    toc_summary_header += "  ----------------------\n"
    toc_summary_header += f"  Total files:      {sum(count_all):4}\n"
    toc_summary_header += "\n"
    with open(output_file, 'w') as f:
        f.write(toc_summary_header)
        f.write(toc_summary)
