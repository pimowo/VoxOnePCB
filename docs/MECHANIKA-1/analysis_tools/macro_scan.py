from pathlib import Path
import json, math, itertools, collections
R=Path(__file__).resolve().parents[3]
D=R/'docs/MECHANIKA-1'
def wr(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def dist(a,b):return math.hypot(max(a[0]-b[2],b[0]-a[2],0),max(a[1]-b[3],b[1]-a[3],0))
def hit(a,b,g=0):return a[0]<b[2]+g and a[2]>b[0]-g and a[1]<b[3]+g and a[3]>b[1]-g
def rect(x,y,w,h):return (x,y,x+w,y+h)
def basic(H,mx,dt,bx,bt,ry=0):
 # coordinates relative to PCB top-left. DAC exact reference body and source jack union retained.
 body={'MAIN':rect(mx,.5,28,63.4),'DAC':rect(81.5,dt,18.5,31.9),'BT':rect(bx,bt,30.48,36.83)}
 ant={'MAIN':rect(mx+5,.5,18,6.4),'BT':rect(bx,bt,30.48,6.35)}
 for n,q in body.items():
  if q[0]<0 or q[2]>100 or q[1]<0 or q[3]>H:return None
  for m,z in body.items():
   if n<m and hit(q,z,1):return None
  for m,z in ant.items():
   if n!=m and dist(q,z)<15-1e-6:return None
 # USB MAIN and BT plug corridors; source BT housing included in plug reserve.
 cables={'MAIN1':rect(mx+5,63.9,9,18),'MAIN2':rect(mx+18,63.9,9,18),'MAIN1_CABLE':rect(mx+7.5,81.9,4,max(0,H+5-81.9)),'MAIN2_CABLE':rect(mx+20.5,81.9,4,max(0,H+5-81.9)),'BT':rect(bx+10.24,bt+36.83,10,24.35),'JACK':rect(100,dt+5.4,18,9)}
 for n,q in body.items():
  for m,z in cables.items():
   if m.startswith(n) or n==m:continue
   if hit(q,z):return None
 for (n,q),(m,z) in itertools.combinations(cables.items(),2):
  if hit(q,z):return None
 return {'H':H,'MAIN_x':mx,'DAC_top':dt,'BT_x':bx,'BT_top':bt,'body':body,'ant':ant,'cables':cables}
def macro():
 # Exhaustive explicit discrete family, NOT a proof of general impossibility.
 # Explore stacked and lateral/staggered BT, preserving module orientation and 15mm RF.
 results={}
 for H in [75,80,85,90,95]:
  pool=[];count=0;near=[];rejects=collections.Counter()
  for mx in [12,14,16,16.5,17,18,20]:
   for dt in [x*.5 for x in range(1,int(H-31.9)*2+1)]:
    for bx in [46,48,50,52,54,56,58,59.5,60,62,64,66,68]:
     for bt in [x for x in range(1,int(H-36.83)+1)]:
      s=basic(H,mx,dt,bx,bt)
      if not s:continue
      count+=1
      # rank upper-right DAC, exterior-friendly MAIN/BT, free RTC space.
      # Check four M3 in corner windows 3.5..12mm, circular 7mm heads, 15mm antenna distance.
      holes=[];missing=[]
      for corner in range(4):
       best=None
       for dx in [3.5,5,7,9,11.5]:
        for dy in [3.5,5,7,9,11.5]:
         x=dx if corner%2==0 else 100-dx;y=dy if corner<2 else H-dy;q=(x,y,x,y)
         if any(dist(q,z)<3.7 for z in s['body'].values()):continue
         if any(dist(q,z)<18.5-1e-6 for z in s['ant'].values()):continue
         if any(dist(q,z)<3.5 for z in s['cables'].values()):continue
         v=dx+dy
         if best is None or v<best[0]:best=(v,x,y)
       if best is None:missing.append(corner)
       else:holes.append(best[1:])
      if len(holes)!=4:
       rejects['M3']+=1
       near.append({'placement':s,'reason':'No 4 M3 with circular 7mm heads in tested corner windows 3.5..11.5mm and 15mm RF reserve','found_holes':holes,'missing_corners':missing})
       near.sort(key=lambda v:(-len(v['found_holes']),v['placement']['DAC_top']*3+abs(v['placement']['MAIN_x']-17)));near=near[:3]
       continue
      s['holes']=holes
      # RTC full 13.4square +2mm clearance and RF. Search central regions.
      rtc=None
      for y in range(18,int(H-14)):
       for x in range(42,76):
        q=rect(x,y,13.4,13.4)
        if any(dist(q,z)<2 for z in s['body'].values()):continue
        if any(dist(q,z)<15 for z in s['ant'].values()):continue
        if any(hit(q,z,1) for z in s['cables'].values()):continue
        if any(dist((a,b,a,b),q)<3.5 for a,b in holes):continue
        score=abs(x+6.7-54)+abs(y+6.7-H*.52)
        if rtc is None or score<rtc[0]:rtc=(score,q)
      if rtc is None:
       rejects['RTC']+=1
       if len(near)<10:near.append({'placement':s,'reason':'No RTC in tested central grid with 2mm body clearance and 15mm RF'})
       continue
      s['body']['RTC']=rtc[1]
      score=dt*3+abs(mx-17)+abs(bx-60)*.15+rtc[0]*.2
      pool.append((score,s))
  pool.sort(key=lambda x:x[0]);best=[s for _,s in pool[:3]]
  results[str(H)]={'macro_solutions_before_M3_RTC':count,'macro_solutions_after_M3_RTC':len(pool),'best':best,'near_misses':near,'rejection_counts':dict(rejects),'search_is_not_continuous_impossibility_proof':True}
  print(H,count,len(pool),best[:1],flush=True)
 wr(D/'MACRO_SEARCH.json',results)

if __name__=='__main__':macro()
