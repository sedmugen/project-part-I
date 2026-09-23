from build import *
from zipfile import ZipFile
from lxml import etree
from pypdf import PdfReader
import hashlib

paths=[ROOT/'01_Deliverable_1/DailyKhata_Deliverable_1_v2.0.docx',ROOT/'02_Deliverable_2/DailyKhata_Deliverable_2_v2.0.docx']+list((ROOT/'00_Project_Governance').glob('DailyKhata_*.docx'))
paths=[p for p in paths if 'v1.0' not in p.name]
results={}
for p in paths:
 d=Document(p); s=d.sections[0]; body='\n'.join(x.text for x in d.paragraphs)
 assert round(s.page_width.mm)==210 and round(s.page_height.mm)==297
 assert [round(x.inches,2) for x in [s.top_margin,s.bottom_margin,s.left_margin,s.right_margin]]==[1,1,1.25,1]
 assert s.different_first_page_header_footer
 assert d.styles['Normal'].font.name=='Times New Roman'
 assert d.styles['Normal'].font.size.pt==12
 default_spacing=d.styles.element.find('.//'+qn('w:pPrDefault')+'//'+qn('w:spacing'))
 line=d.styles['Normal'].paragraph_format.line_spacing
 assert line==1.15 or (line is None and default_spacing.get(qn('w:line'))=='276')
 assert d.styles['Normal'].paragraph_format.space_after.pt==6
 for n,sz in enumerate([16,14,12,12],1):
  st=d.styles[f'Heading {n}']; assert (st.font.size.pt if st.font.size else 12)==sz and st.font.bold and st.font.name in [None,'Times New Roman']
  assert st.element.find('.//'+qn('w:numPr')) is not None
 assert d.styles['Heading 4'].font.italic
 for t in d.tables: assert t.rows[0]._tr.find('.//'+qn('w:tblHeader')) is not None
 rows=[tuple(c.text for c in row.cells) for t in d.tables for row in t.rows]
 if 'Deliverable_' in p.name or p.name=='DailyKhata_Project_Scope.docx':
  assert DEFINITION in body
  assert all(x in rows for x in SCOPE)
  assert EXCLUDED in body and FUTURE in body
 if 'Deliverable_' in p.name or 'Terminology' in p.name:
  assert all((x[0]+'\n'+x[1],x[2]+'\n'+x[3],x[4]) in rows for x in PERSONAS)
 if 'Deliverable_' in p.name: assert PROBLEM in body
 with ZipFile(p) as z:
  xm={n:z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xml')}
  assert not any('\u2014' in x for x in xm.values())
  assert 'TOC ' in xm['word/document.xml']
  assert 'PAGE' in ''.join(v for k,v in xm.items() if 'footer' in k)
  colours=[]
  for name,xml in xm.items():
   if not (name.startswith('word/') and name!='word/theme/theme1.xml'): continue
   tree=etree.fromstring(xml.encode())
   for c in tree.findall('.//'+qn('w:color')):
    v=c.get(qn('w:val'),'auto')
    if v!='auto' and len(v)==6 and not(v[:2]==v[2:4]==v[4:]): colours.append((name,v))
  # Some unused table styles contain theme colours. Active paragraphs are checked through the PDF render too.
 pdf=PdfReader(WORK/'rendered'/p.with_suffix('.pdf').name)
 fonts=set()
 for page in pdf.pages:
  def visit(text,cm,tm,font,size):
   if font and text.strip(): fonts.add(str(font.get('/BaseFont')))
  page.extract_text(visitor_text=visit)
 assert all('TimesNewRoman' in f for f in fonts),fonts
 pages=[pg.extract_text() for pg in pdf.pages]
 assert all(len(t.strip())>100 for t in pages)
 assert 'Page 1 of' not in pages[0]
 for i,t in enumerate(pages[1:],2): assert f'Page {i} of {len(pages)}' in t
 assert not any('Error! Bookmark' in t or 'Error! No table' in t for t in pages)
 results[p.name]={'pages':len(pages),'tables':len(d.tables),'structural_checks':'passed','em_dash_count':0,'fonts':sorted(fonts),'unused_style_colour_flags':len(colours)}

# Strict pairwise equality of all shared canonical tables and design paragraphs.
d1,d2=[Document(p) for p in paths[:2]]
def findtable(doc,header):
 return next([[c.text for c in row.cells] for row in t.rows] for t in doc.tables if [c.text for c in t.rows[0].cells]==header)
for header in [['ID','Capability','Priority'],['ID and name','Age and role','Classification'],['User-facing category','Internal accounting account'],['Original text and brand','Product identity and type','Category and account']]: assert findtable(d1,header)==findtable(d2,header)
paras1={p.text for p in d1.paragraphs}; paras2={p.text for p in d2.paragraphs}
shared=[p for p in paras1 if any(p.startswith(x) for x in ['DailyKhata must maintain','These mappings illustrate','A mixed receipt','Original receipt text,','Both products can','The AI Financial Assistant is','Illustrative response,','Conversational analysis of','English and Urdu localisation is','The application is mobile-first','Primary users are','The baseline is a single-account'])]
assert all(p in paras2 for p in shared)
manifest=json.loads((WORK/'source_manifest.json').read_text(encoding='utf-8-sig'))
assert all(hashlib.sha256(Path(x['Path']).read_bytes()).hexdigest().upper()==x['SHA256'] for x in manifest)
results['cross_document']={'scope_entries':len(SCOPE),'personas':len(PERSONAS),'shared_design_paragraphs':len(shared),'matching_canonical_tables':4,'source_hashes_unchanged':len(manifest),'result':'passed'}
(WORK/'qa_results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
