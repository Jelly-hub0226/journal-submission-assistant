# Journal Data Sources

## International Journals

### LetPub (Primary)
- URL: `https://www.letpub.com.cn/index.php?page=journalapp&fieldname=` + URL-encoded journal name
- Or use search: `https://www.letpub.com.cn/index.php?page=journalapp&view=search`
- Returns: IF, JCR quartile, CAS quartile, self-citation rate, review cycle, acceptance rate, Chinese author发文 ratio
- **Note**: LetPub pages are HTML; extract data from the results table.

### SJR / Scimago (Fallback)
- URL: `https://www.scimagojr.com/journalsearch.php?q=` + URL-encoded journal name
- Returns: SJR, H-index, CiteScore, quartile by subject area
- **Note**: Use for cross-validation of IF/quartile data.

### Scopus API (if available)
- Base: `https://api.elsevier.com/content/serial/title?issn=` + ISSN
- Requires API key; prefer LetPub/SJR if no key configured.

## Chinese Journals

### CNKI Journal Navigation (Primary)
- URL: `https://navi.cnki.net/knavi/`
- Search by journal name returns: composite IF, comprehensive IF, core inclusion status
- **Note**: Core status labels are displayed on the journal detail page.

### Wanfang Journal Search (Fallback)
- URL: `https://www.wanfangdata.com.cn/periodical`
- Returns similar metrics; useful as cross-check.

### 万维书刊网 (Review Experience)
- URL: `https://www.eshukan.com/`
- Search by journal name for: average review cycle, acceptance difficulty rating, page fees, user reviews
- **Note**: User-submitted data; note the sample size when reporting.

## Legitimacy Check (Chinese Journals)

### National Press and Publication Administration
- URL: `https://www.nppa.gov.cn/` → 办事服务 → 期刊/期刊社查询
- Or: `http://www.gapp.gov.cn/zongshu/magazine.shtml`
- Verify CN number and publication license.

### Database Inclusion Check
- CNKI: search journal name at `https://navi.cnki.net/knavi/`
- Wanfang: search at `https://www.wanfangdata.com.cn/periodical`
- VIP (维普): search at `http://www.cqvip.com/`

## Query Strategy

1. Start with LetPub (international) or CNKI (Chinese) as primary source
2. If primary fails, try the named fallback
3. If both fail, report: "Unable to retrieve data for [journal name]. Sources tried: LetPub, SJR."
4. Always note the retrieval date and source in output
5. Never fabricate metrics - if unknown, say "not available"

## Rate Limits

- Space queries by at least 2 seconds to avoid IP blocking
- If a source returns 403/429, wait 30 seconds before retrying
- Limit batch queries to 10 journals per session
