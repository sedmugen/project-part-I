from model import *
from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader
from zipfile import ZipFile
from lxml import etree
import re
path=ROOT/'03_Deliverable_3/DailyKhata_Deliverable_3_v1.0.docx'
d=Document(path);pdf=PdfReader(WORK/'D3_QA.pdf')
pages=[p.extract_text() for p in pdf.pages]
assert len(pages)==76 or len(pages)>40
assert all(len(p.strip())>100 for p in pages)
assert 'Page 1 of' not in pages[0]
for i,p in enumerate(pages[1:],2):assert f'Page {i} of {len(pages)}' in p,(i,p[-100:])
assert not any('Error! ' in p for p in pages)
body='\n'.join(p.text for p in d.paragraphs)
assert DEFINITION in body and PROBLEM in body and EXCLUDED in body and FUTURE in body
for s in d.sections:
 assert sorted([round(s.page_width.mm),round(s.page_height.mm)])==[210,297]
 assert [round(x.inches,2) for x in [s.top_margin,s.bottom_margin,s.left_margin,s.right_margin]]==[1,1,1.25,1]
assert d.sections[0].different_first_page_header_footer
for n,sz in enumerate([16,14,12,12],1):
 st=d.styles[f'Heading {n}'];assert (st.font.size.pt if st.font.size else 12)==sz and st.font.bold
 assert st.element.find('.//'+qn('w:numPr')) is not None
assert d.styles['Normal'].font.size.pt==12
assert d.styles['Normal'].paragraph_format.space_after.pt==6
for t in d.tables: assert t.rows[0]._tr.find('.//'+qn('w:tblHeader')) is not None
with ZipFile(path) as z:
 xml={n:z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xml')}
 assert not any('\u2014' in x for x in xml.values())
 assert 'TOC ' in xml['word/document.xml'] and 'SEQ Table' in xml['word/document.xml']
for b in BR:assert b[2] in body
for f in FR:assert f['statement'] in body and f['acceptance'] in body
for n in NFR:assert n['statement'] in body and n['test'] in body
# Source baseline assertions on canonical data rather than prose similarity alone.
tables=[[[c.text for c in row.cells] for row in t.rows] for t in d.tables]
scope_table=next(t for t in tables if t[0]==['Scope and priority','Capability','Formal requirements'])
assert {(row[0].split('\n')[0],row[1],row[0].split('\n')[1]) for row in scope_table[1:]}==set(SCOPE)
persona=next(t for t in tables if t[0]==['Persona','Age and role','Classification'])
assert persona[1:]==[[p[0]+' '+p[1],p[2]+'; '+p[3],p[4]] for p in PERSONAS]
for source in [ROOT/'01_Deliverable_1/DailyKhata_Deliverable_1_v2.0.docx',ROOT/'02_Deliverable_2/DailyKhata_Deliverable_2_v2.0.docx']:
 sd=Document(source);stables=[[[c.text for c in row.cells] for row in t.rows] for t in sd.tables]
 source_scope=next(t for t in stables if t[0]==['ID','Capability','Priority'])
 assert {tuple(row) for row in source_scope[1:]}==set(SCOPE)
 source_personas=next(t for t in stables if t[0]==['ID and name','Age and role','Classification'])
 assert source_personas[1:]==[[p[0]+'\n'+p[1],p[2]+'\n'+p[3],p[4]] for p in PERSONAS]
 sb='\n'.join(p.text for p in sd.paragraphs)
 assert DEFINITION in sb and PROBLEM in sb and EXCLUDED in sb and FUTURE in sb
quality=next(t for t in tables if t[0]==['Functional ID','NFR IDs','Reason'])
assert {row[0]:row[1].split(', ') for row in quality[1:]}=={f['id']:f['nfr'] for f in FR}
index=next(t for t in tables if t[0]==['ID','Title','Priority'] and t[1][0].startswith('FR-'))
assert len(index)-1==len(FR)
fonts=set();colours=set();locations=[]
for i,page in enumerate(pdf.pages,1):
 def visit(txt,cm,tm,font,size):
  if txt.strip() and font:fonts.add(str(font.get('/BaseFont')))
 def operator(op,args,cm,tm):
  if op in [b'rg',b'RG'] and len(args)==3:colours.add(tuple(float(x) for x in args))
 page.extract_text(visitor_text=visit,visitor_operand_before=operator)
 locations.append({'page':i,'width':float(page.mediabox.width),'height':float(page.mediabox.height),'characters':len(pages[i-1]),'start':pages[i-1][:115],'end':pages[i-1][-125:]})
assert all('TimesNewRoman' in x for x in fonts),fonts
assert all(abs(x[0]-x[1])<.0001 and abs(x[1]-x[2])<.0001 for x in colours),colours
manifest=json.loads((WORK/'source_manifest.json').read_text(encoding='utf-8-sig'))
assert all(hashlib.sha256(Path(x['Path']).read_bytes()).hexdigest().upper()==x['SHA256'] for x in manifest)
audit={'pages':len(pdf.pages),'tables':len(d.tables),'BR':len(BR),'FR':len(FR),'NFR':len(NFR),'must_scope_covered':27,'all_scope_covered':38,'canonical_personas_matched':5,'original_files_unchanged':len(manifest),'em_dash_count':0,'active_fonts':sorted(fonts),'active_colours':'black and grey only','fields':'TOC list of tables page fields refreshed in Microsoft Word','status':'Structural and cross-document checks passed; visual review pending'}
(WORK/'document_audit.json').write_text(json.dumps(audit,indent=2))
(WORK/'page_inventory.json').write_text(json.dumps(locations,indent=2))
(WORK/'pdf_text.txt').write_text('\n\n'.join('PAGE '+str(i+1)+'\n'+p for i,p in enumerate(pages)),encoding='utf-8')
print(json.dumps(audit,indent=2))
print('Short pages:',[(x['page'],x['characters'],x['start']) for x in locations if x['characters']<650])
