import json, pathlib, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
r=pathlib.Path(__file__).resolve().parent.parent
d=json.loads((r/'data/chart_data.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#435563','text.color':'#17323a','axes.titleweight':'bold','axes.titlesize':15,'figure.facecolor':'white','axes.facecolor':'white','svg.fonttype':'none'})
teal='#168776';gray='#b2c0c7';amber='#c57a37'
def finish(fig,name):
 fig.savefig(r/'charts'/f'{name}.png',dpi=200,bbox_inches='tight',facecolor='white');fig.savefig(r/'charts'/f'{name}.svg',bbox_inches='tight',facecolor='white');plt.close(fig)
def gantt(ax):
 rows=d['milestones'];y=np.arange(len(rows))
 ax.barh(y-.17,[t['baselineEnd']-t['baselineStart'] for t in rows],left=[t['baselineStart'] for t in rows],height=.28,color=gray,label='Baseline')
 ax.barh(y+.17,[t['revisedEnd']-t['revisedStart'] for t in rows],left=[t['revisedStart'] for t in rows],height=.28,color=teal,label='10-workday sensor delay')
 ax.set_yticks(y,[t['name'] for t in rows]);ax.invert_yaxis();ax.set_xlabel('Working-day boundary from Jan 4, 2027');ax.set_xlim(0,49);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True);ax.set_title('Supplier delay: 10 days in, 5 days at launch',loc='left',pad=20);ax.legend(loc='upper right',fontsize=9,frameon=False)
 fig=ax.figure

def risks(ax):
 rows=d['results'];y=np.arange(len(rows));values=[s['launchSlip'] for s in rows]
 ax.barh(y,values,color=[gray,teal,teal,teal,amber,amber],height=.58);ax.set_yticks(y,[s['name'] for s in rows]);ax.invert_yaxis();ax.set_xlim(0,29);ax.set_xlabel('Added working days to launch');ax.set_title('Approval gates amplify launch impact',loc='left',pad=20);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
 for i,v in enumerate(values):ax.text(v+.45,i,str(v),va='center',fontweight='bold')
def recover(ax):
 rows=d['recovery'];colors=[gray,teal,amber]
 for s,c in zip(rows,colors):
  ax.scatter(s['launchSlip'],s['directCost'],s=180,color=c,zorder=3)
  title={'Accept delay':'Accept delay\n5d / $1,500','Expedite 5 working days':'Expedite\n0d / $4,500','Qualified alternative':'Conditional alternative\n15d / $13,000'}[s['option']]
  ax.annotate(title,(s['launchSlip'],s['directCost']),xytext=(12,12 if s['launchSlip']!=15 else -35),textcoords='offset points',fontsize=10)
 ax.set_xlim(-2,24);ax.set_ylim(0,16000);ax.set_xlabel('Added working days to launch');ax.set_ylabel('Direct scenario cost (USD)');ax.set_title('Expediting preserves the modeled launch',loc='left',pad=20);ax.grid(alpha=.15);ax.set_axisbelow(True);ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('${x:,.0f}'))
def coverage(ax):
 ax.barh([1,0],[3,8],color=[gray,teal],height=.5);ax.set_yticks([1,0],['Current usable stock: 180 units','With last-time buy: 480 units']);ax.set_xlim(0,9.5);ax.set_xlabel('Months of coverage at 60 units/month');ax.set_title('Last-time buy adds 5 months of coverage',loc='left',pad=20);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
 for y,v in [(1,3),(0,8)]:ax.text(v+.15,y,f'{v} months',va='center',fontweight='bold')
 ax.text(0,-.58,'Additional inventory cash: $15,600. No launch date inferred.',fontsize=10,color='#607780')
for name,fn in [('01_launch_timeline',gantt),('02_scenario_impact',risks),('03_recovery_tradeoff',recover),('04_eol_coverage',coverage)]:
 fig,ax=plt.subplots(figsize=(12,6));fn(ax);fig.text(.01,.015,'SYNTHETIC CASE STUDY  •  Deterministic simulation; not measured customer results.',fontsize=9,color='#6e7e86');fig.subplots_adjust(left=.28,bottom=.18,top=.87,right=.96);finish(fig,name)
fig,axs=plt.subplots(2,2,figsize=(20,13));gantt(axs[0,0]);risks(axs[0,1]);recover(axs[1,0]);coverage(axs[1,1]);fig.suptitle('LaunchLens | Hardware change-impact case study',x=.04,ha='left',fontsize=27,fontweight='bold',y=.98);fig.text(.04,.935,'Fictional camera launch · Component evidence → task dependencies → customer approval → recovery decision',fontsize=13,color='#5d737d');fig.text(.04,.015,'SYNTHETIC DATA · Weekdays only, no holidays. Options depend on engineering, supplier and customer confirmation. Costs exclude revenue loss.',fontsize=11,color='#6e7e86');fig.subplots_adjust(left=.17,right=.96,bottom=.1,top=.86,wspace=.68,hspace=.55);finish(fig,'00_portfolio_overview')
print('Created five PNG and five editable SVG charts.')
