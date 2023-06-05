#!/usr/bin/env python3

from sage.all import *   
from Crypto.Util.number import *
from math import sqrt 

pubk=[1153413051608659765690966350509215244410441599304795977869609, 2649449263344909989917079612505852691099017868921045204503001, 745658406444288115599679966003279655234335830084858834237308, 1501654946090437610990754702516907678101625380332752375035668, 1731839829398712068254721510140854227151979937383544415747007, 1917601407897641951467210159479072437634885900660588177638690, 1279706235765006419446891128348418014918258703242746751774802, 1502580060849949686295755918606576574401174920193784713780905, 2625238880672952214121734023768335384083807769582181928490912, 606270761347913487563503974039985349892695737642480888692673, 1247631701502816565834505451954908666946807272758349376525460, 1562927544947712147039232078400564527346400651105722414913451, 204096614275302553698473272845405530981891754187470359119553, 1408018363672404061681568720260167530505766870069064372609687, 1514590716273119237466038973941614240250338689732745719237095, 2378692629623187882152238082542498660097457763282705253592516, 1893448995872418605597767637872034355760298442376725665221500, 1637024298884398444455002361181118258859555824359194604735915, 2719190822110427203521259100337406967675292817189502308970586, 2640870406011836531895866622802297978015773425016511436224746, 2165892993782024615017169562260093941947231862572312098360126, 243718966168901036068447727263550985619152373055872226083935, 2035400781995083294650022079235484020577386045959257768911516, 2138400566976843848333310914369509998597969306214629098228227, 112446566505736446843650023065053298590439688801621609445463, 1714002630387312920696314035459338893617306790872241960138133, 1024850412773050992775197227041922238903279669151026216857401, 2358925636863552279599329365327470285835734283277847908682469, 960291266922907753413813833147215291189556626243314954787079, 2471269462645122667857359212039928357870430231828538257093882, 2254711914646827325445684712569610067589509795259364668236116, 3152079429165479260024384396045171484908571393583704823372, 7245670391945130618733779447100310448574448728525664206342, 1983149526457025777875960503986209872411223710838977852503058, 2478783519269282209571656363015372788707598874749559775480572, 1343348424777313491462495265503752251552490742957120510636719, 696771540364873293374125391721639926054346725167043556235151, 1378786198781394641622092749054458248463201336911200937601879, 2061021991295597315833886722674966530095259597797968883012294, 2022299356352726041687770564469412023446862842882981592269287, 2103599714903473220709442681420827901041209667891008147827086, 318411403427754276460826728673462955336165520042588782589752, 215426626468659219531748316787016104062139403274288645837575, 1810672814632234704157982310036649412989583692109880020715868, 1514381356252789312341658830031933431769544487506032804303686, 701593629336714590272170031617304310014522607636754911394706, 1366393539801496516181470203059815247106762948304006271700287, 2448152175170733851656170383862433487614634519538309624376469, 1348207685418679830438595499051323725246184075503096280525585, 70307869056203425509508941958172047909143575785204200382316, 716048162378262413393444002306977733357269701046546820427233, 1579543039327077934414801734410703417448650262925810895689104, 261575250132422239529017823101514330063089023490414947560266, 2298073834787955133523836383569782771499748656944587718350271, 918734699998715338244933400142282901634195616477790962697785, 1982726185421882131804832692278501191521239007312758901721603, 2584890453270172498684967368927270137126808850953779575592179, 2622231303407390255810045713997561793019571011029869053290302, 2577578579371795996917469250652847487787210673097187661267819, 52144522625291137606092085190356852042443658323935004932658, 1416019353492624837460500845581684985017464744695269553974900, 136970671991524060358119224318550078760913486366857079847622, 834407238570805549772432172630329624434383380940991215927379, 622449476884676778937441422703209818813479141928257844680738, 75067376696273791715981861842467067761435213138416895182154, 219032040463804253458387980109524000738996399683050582926151, 439103475084696638030508995976505786583616604910062247189836, 1814202485052573717557187805902619765498642274743527729845605, 1809698821925924543769848657654790341645044302785867813389478, 360799055878429084258361181388858219414492903048758868025849, 1586166800958488919817817851585852792648429629996334111648546, 1684449894575565311005197544335614943548593903243337992651255, 2069964614705320281752099612563790595789747891496953733286554, 2383149085148417442984621113438766849202060480802298928504567, 526576610310349463764463832215907813169637952107722736362933, 2462384442192741714387155278581783095614148718252893047502032, 1061123570633350127543993385427619277887339043459642290750330, 2170337927119054739024756083589705438210829415028768430188065, 1200050666804720124511437996307551173659020227930487994985079, 2655883363845532618772372239182511478421388787749297124780670, 2400366221315751744740914435412206064709757878402509681320567, 1173657318458121971155227157097755748671613663720232863891389, 2702520926423527204458471819466137878152774358799689088058931, 1690170859505110606818345405862828775136343478978847042328275, 1534078663419643827290143498400949737327886416197686994660731, 67307923426097644994998144902520797699024298403980303434111, 105900771966130069543014590856819375500591733506963326392870, 1858315637671237418113116342617022884354114188545817840978328, 1064629001068824587104664159978412758949275255254084550523914, 2378499828514660026308510311669274507417089906258942129443532, 1437038254440508929035886831353499155523639468412138764665702, 1984789428563986128172566164401185992024372439606411478873714, 219041554944305423274893335373532788223766017073784541497174, 2258288062942706796109719679247868131726532075245958863791837, 2772281247871871850634946427392047539575130353284512078765669, 287574274087253959175794635355688561944575733972684978310059, 2506025164018419623148043296951490494501935889338095366634059, 235059835346923216758180386880687400027687902442088694735840, 1644980912717446933824947561736174848219586263634409721003675, 1572840165579931577196516350362024381905217854603697776041632, 659043619562898691459776258453697360116377910757700817074496, 1789216845698992031188821923143638138110868462297673924399671, 1619100265825813762658500374679864193297950892033415641273987, 361622554311934817224321204425771742355136985271179452404586, 1898110845159102949773873772106782968253686319372837328037927, 1968514570942060836557553492419028248475360105567872527412401, 2459217543243151143119668450477701832326870800044537134671540, 298544910182500292656435254358404317205755259496560309792209, 149906488969205922910503787131112087129095370674239599761480, 615128983633335650829480404526011441387035964724705781227149, 1077311278249221585358350663793203600568999654323339628822008, 340604959778757686208546159797366254984487404276704596265048, 2332026928038585949313502074443960101452763880940874494501577, 1739243153345581325528540737224323607202795982152905642771734, 1680538202455739744022542793687266947201505214643714877523750, 2724281269173957168495717556121364664645869091558917805784718, 269955770435536528672574267859575090488788926596254183227452, 690867554053394862659304254064387000029666479498855734237421, 432334115075872216419409402565362264792449816981222325643073, 676995838914493183476507857322088404501355459686529360459634, 1429248591704369402439595219528531969683836212824391038823312, 1017541352206082542392140501303781094306429691035385881417504, 2329844650769556101295502159924139103054143477213374150786305, 484858725227698005716951674371786913299715671869938549254945, 2019689616323100753637596042131256181018624688715434347628557, 1531241724877679796713573169951128798510990437088543573162829, 890650951428215068675080339622669325809995937765921979552973, 2085385535263634731442857611465786088907319306579156575195133, 713169162170327285267994411761813261171538088821176083933328, 2132830238580678189966853709725365975652915158636890126368754, 2553075820773697497394173548451121149981470668395232632816981, 2629967663190816381736734446344114126948186032409785237304019, 108116358838841746722808565576915423329500511368084412883493, 1834294852239160644199990545816723571619353004716348864130329, 1821434442055147592774988792496293274693309790398954022521895, 8865090478398312740523263053884430262802597528119654938777, 2675920017512301584484169753459126007770241705090918340436173, 775970259397762593874930203087656823881846996489043140104336, 2230908984261303398356523561629589786652122370089276373673822, 1563242041071359605567033922906138813920273984873554393518266, 1412706933098260353222281247078459699919952588682625174886674, 556387281158977265306446356941453288617418606345908136803395, 443407639913099340937929414918212333352927652924517508010826, 94333245228596603560696949047484359941006690420461641212581, 1666507411487482973410645185048130718079862020211812194555851, 2665722910713379936159164129832898978798026422689891199196396, 2669405938547056354829211076633313140708911016566170884850843, 202245527646294028617600062733867777929713151687456763274537, 1331317632107340377871282683312084191299890870783752240012329, 428820015026787077576128392443567174723873281867688412814441, 580822016053542720196362662419423244064692449107102822301234, 1443675785490246411043062710802186999048965372808110107659119, 2298534171326758584024691931436081584600036610807140491328791, 2719407492061457004381985636495256791796955801861767579899449, 1429136078033486101134969751145412644748324277396941228294087, 1078947633205179129710839151819627291842615570015956594682809, 475791981348384907163442694660952440388755824594198529913775, 1163466286751344872926586836930564447841921809539261826505059, 2069383431903347015918184864426942857108005221730030159796260, 135245305729701630000796486837595347226266408275246670713937, 508548307523515781106994147442038828539274755394295066068411, 2239326817114831698533142359236649886367489224488220926335634, 1484417566387325697897597844553666378698131036967802335733369, 1668923214242042014489842678366631946682280497032807887066371, 2578230169323207370277795509029631593492372061179654885236334, 1351498705692317567037267236529785140053641258658101372130807, 67344713331883772397519008348838267343026244863882333750769, 1197105587451303888458675620420382520115448483852598832335116, 1175778597436703549016514382085730407955923337312856127546676, 2444116136207088642953938608890976139838919275737893120525002, 2047067250254711126671223695230847457870829969257424934259832, 1520116617448531698215483753208803490076383825023770165172330, 2499314155373490163145661426570824684843417156213389633843574, 938680244240331032933006622695829904424986381635035490902837, 2366872519973373406463469286818707121279968786244910078616602, 1689512006863085258567872248746396733612668173694765296637902, 2522847704426437604863362214701927991957171894471788086309747, 2358706258382913178503960456525602854624615948086839221241765, 2547045358928916904668881789693079740079298224013319738904902, 1456413016015393341327945933058199232664867021676744739242308]
ct=134386949562122693902447468860044804076193605907011732452713809

k = 176

N = int(sqrt(k)//2 + 1) 
M = Matrix(QQ,k+1,k+1)

for i in range(k):
	M[i,i] = 1

for i in range(len(pubk[:k])):
	M[i,k] = N*pubk[i]

for i in range(k):
	M[k,i] = 1/2

M[k,k] = N*(ct)

sol = M.LLL()

for p in sol:
	t = []
	control = True
	for l in p:
		if int(1/2-l) < 0 or int(1/2-l) >1: 
			control = False
			break
		t.append(int(abs(1/2-l)))
	
	if control and vector(t[:-1]).dot_product(vector(pubk[:k])) == ct:
		flag = long_to_bytes(int("".join([str(x) for x in t[:-1]]),2))
		print(b"DANTE{"+flag+b"}")
