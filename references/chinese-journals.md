# Chinese Journal Classification & Verification

## Core Journal Systems

### 北大核心 (PKU Core / 中文核心期刊要目总览)
- Publisher: Peking University Library
- Updated: every 3-4 years (latest: 2023 edition)
- Covers: all disciplines, ~1,900 journals
- Nickname: "北大核心", "中文核心"

### CSSCI (中文社会科学引文索引 / "南大核心")
- Publisher: Nanjing University
- Updated: biennially (latest: 2023-2024)
- Covers: social sciences and humanities, ~600 journals
- Nicknames: "CSSCI", "南大核心", "C刊"
- Subset: CSSCI扩展版 (extended edition) for emerging journals

### CSCD (中国科学引文数据库)
- Publisher: Chinese Academy of Sciences
- Updated: biennially
- Covers: natural sciences, engineering, medicine
- Nickname: "CSCD", "中科院核心"

### 科技核心 (中国科技核心期刊 / ST Core)
- Publisher: Institute of Scientific and Technical Information of China (ISTIC)
- Updated: annually
- Covers: science and technology

## Verification Workflow

For a Chinese journal name:

1. **CN Number Check**: Verify the journal has a valid CN number (格式: CN XX-XXXX/YY)
   - Query NPPA database: `http://www.gapp.gov.cn/zongshu/magazine.shtml`
   - If no CN number found: flag as potentially illegitimate

2. **Database Inclusion Check**:
   - CNKI: search journal at `https://navi.cnki.net/knavi/`
   - Wanfang: search at `https://www.wanfangdata.com.cn/periodical`
   - VIP: search at `http://www.cqvip.com/`
   - If not in any of the three: likely not a recognized academic journal

3. **Core Classification**:
   - CNKI journal page shows core status badges (北大核心, CSSCI, CSCD, etc.)
   - Cross-check with Wanfang for confirmation

4. **Experience Check** (optional):
   - 万维书刊网 `https://www.eshukan.com/` for user reviews
   - Note: user reviews are subjective; report sample size

## Common Core Journal Lists by Discipline

For directory-style queries ("list CSSCI journals in 教育学"), search CNKI's
journal navigation filtered by discipline. Alternatively, use known lists:

- CSSCI (2023-2024) full list: publicly available PDF from Nanjing University CSSSCI center
- 北大核心 2023: published in book form; partial lists available online

When the user asks for a discipline-specific list, prefer live CNKI queries.
If offline, acknowledge the limitation and provide what is available.
