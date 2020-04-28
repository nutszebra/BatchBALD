store = {}
store['args']={'num_inference_samples': 10, 'available_sample_k': 10, 'seed': 1017036, 'type': 'AcquisitionFunction.mean_stddev', 'acquisition_method': 'AcquisitionMethod.independent', 'experiment_description': 'RMNIST with noise k100 var ratios and mean stddev', 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 3072, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 5056, 'target_accuracy': 0.95, 'target_num_acquired_samples': 300, 'initial_percentage': 100, 'reduce_percentage': 0, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'dataset': 'DatasetEnum.repeated_mnist_w_noise', 'experiment_task_id': 'rmnist_w_noise_independent_mean_stddev_k10_b10_1017036', 'experiments_laaos': './experiment_configs/rmnist_w_noise_other_methods/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'balanced_validation_set': False}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=rmnist_w_noise_independent_mean_stddev_k10_b10_1017036', '--experiments_laaos=./experiment_configs/rmnist_w_noise_other_methods/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6676, 'nll': 2.3925228869336848}, 'chosen_samples': [74189, 14189, 134189, 34721, 154721, 41578, 94453, 15775, 94721, 161578], 'chosen_samples_score': [0.18954742483085815, 0.18768185912634655, 0.1874513447889616, 0.1863848238863056, 0.18521513847274207, 0.1851780519150225, 0.18471315709927927, 0.18433082837831513, 0.18430500767038466, 0.18422806135948971], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.582735714000592, 'batch_acquisition_elapsed_time': 40.566623769002035})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.722, 'nll': 2.721927648277283}, 'chosen_samples': [59343, 134913, 179343, 14913, 119343, 74913, 51544, 111544, 31396, 171544], 'chosen_samples_score': [0.20023531450295892, 0.19857925052422762, 0.19684860832195364, 0.19678440295543953, 0.19576580886922237, 0.1953408764215607, 0.1943144330686644, 0.19428743962167527, 0.19353124179578315, 0.1934363582683062], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.492606892999902, 'batch_acquisition_elapsed_time': 40.19898240099428})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.6661, 'nll': 2.814146482491493}, 'chosen_samples': [48417, 108417, 71380, 11380, 144468, 24468, 131380, 167260, 2840, 165749], 'chosen_samples_score': [0.2069982618098337, 0.20493384460443204, 0.1875520867338272, 0.18742974683698854, 0.187248919330985, 0.18722086524652898, 0.18710538051252174, 0.18691854446610678, 0.18402850480113253, 0.18383279574511072], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.969819236997864, 'batch_acquisition_elapsed_time': 40.10190903199691})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.7384, 'nll': 2.0433847817969317}, 'chosen_samples': [62702, 122702, 2702, 35841, 5295, 179449, 155841, 59449, 65295, 119449], 'chosen_samples_score': [0.2147517750576097, 0.21391858467111394, 0.21242701957260746, 0.19824128265391933, 0.19699808664070032, 0.19582295959966914, 0.19526225216376888, 0.19507677452146835, 0.1948046947366731, 0.1945544605222089], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.639546662998328, 'batch_acquisition_elapsed_time': 40.45385495300434})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.7343, 'nll': 2.231456471930146}, 'chosen_samples': [28455, 88455, 148455, 27153, 136043, 1276, 61276, 76043, 87153, 121276], 'chosen_samples_score': [0.1999946674845742, 0.1991848360235642, 0.19895431163302804, 0.19099123336381613, 0.1909014498631202, 0.18997521293199224, 0.18986576298825486, 0.18908944878107292, 0.18900038624520055, 0.18815604087394414], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.86818312000105, 'batch_acquisition_elapsed_time': 40.607142920001934})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.772, 'nll': 1.9493147648292783}, 'chosen_samples': [73014, 23997, 19638, 83997, 143997, 139638, 134065, 79638, 14065, 74065], 'chosen_samples_score': [0.19500512736083386, 0.19473593854041105, 0.1941037178407925, 0.19359683972851024, 0.19300311751689744, 0.19287497111354876, 0.19273488438897896, 0.19270862605162903, 0.1914646578708989, 0.19112386643657975], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.306941325994558, 'batch_acquisition_elapsed_time': 40.18226175699965})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.7885, 'nll': 1.4792896883702278}, 'chosen_samples': [104961, 23746, 44961, 123734, 83746, 164961, 143746, 115905, 113522, 55905], 'chosen_samples_score': [0.18892956435391572, 0.1876126381244583, 0.18758501844679903, 0.18679136835375015, 0.18634759569179005, 0.18534028505155237, 0.18389203181958097, 0.18327243722407824, 0.18310334378217005, 0.18305847050790947], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.768793708004523, 'batch_acquisition_elapsed_time': 40.460955086004105})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.7733, 'nll': 1.8778433200025557}, 'chosen_samples': [40702, 160702, 100702, 72937, 126962, 66962, 132937, 794, 60794, 12937], 'chosen_samples_score': [0.1916028313843529, 0.19102887414153358, 0.18776510317092635, 0.18745760462932792, 0.18700457994106431, 0.18692068900607522, 0.18647663072928863, 0.18641081259697032, 0.1859195510235393, 0.1852989878421861], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.514175846998114, 'batch_acquisition_elapsed_time': 40.46038129099907})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.8335, 'nll': 1.3624482080090048}, 'chosen_samples': [121299, 61299, 1299, 81947, 134273, 52661, 112661, 172661, 14273, 140567], 'chosen_samples_score': [0.19648116626745815, 0.1944397612576241, 0.1901907741730419, 0.1870867200674694, 0.18649537446134032, 0.18610490418189538, 0.185551242773088, 0.1854610470697276, 0.1853465650913259, 0.18516915885168914], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.23123241000576, 'batch_acquisition_elapsed_time': 40.79361660799623})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8141, 'nll': 1.3789637615400556}, 'chosen_samples': [153714, 93714, 33714, 102413, 149002, 89002, 116819, 140206, 165611, 119562], 'chosen_samples_score': [0.19687928988658718, 0.1961044795964679, 0.19564910305422728, 0.18782373594704607, 0.18675226896305494, 0.18668259287021394, 0.18632406230510054, 0.18583034751848584, 0.18545697501792036, 0.18532908521048372], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.517106653001974, 'batch_acquisition_elapsed_time': 40.54407694099791})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.8628, 'nll': 1.3198776089888808}, 'chosen_samples': [64514, 90925, 150925, 4514, 30925, 90386, 30386, 124514, 11693, 131693], 'chosen_samples_score': [0.2073017925554189, 0.20668998731219457, 0.20547736739340067, 0.20490891790157376, 0.20396053914122994, 0.20321865925356933, 0.202890003361393, 0.2028087964432055, 0.20268494736864592, 0.20266507035475756], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 26.61304754199955, 'batch_acquisition_elapsed_time': 40.55144769999606})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8414, 'nll': 1.2205579189258813}, 'chosen_samples': [92070, 152070, 32070, 132391, 72391, 12391, 105535, 74125, 61437, 165535], 'chosen_samples_score': [0.1872411101860659, 0.1869513617925164, 0.18654477329540775, 0.18440523116500757, 0.18407643121937997, 0.1827825157200646, 0.1774365577583649, 0.17695440892748648, 0.17612218226131515, 0.1761128005552758], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.242418079003983, 'batch_acquisition_elapsed_time': 40.508441043995845})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8716, 'nll': 0.9486334999012949}, 'chosen_samples': [86511, 125113, 65113, 26511, 5113, 146511, 33185, 93185, 153185, 124909], 'chosen_samples_score': [0.1989897095146083, 0.19832412475753305, 0.197056554222822, 0.19693794948849944, 0.19630019278534683, 0.19504922402135705, 0.1934908232894882, 0.19331921539582883, 0.19279422570874885, 0.19024720448605795], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.05576603499503, 'batch_acquisition_elapsed_time': 40.8520729380034})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.8736, 'nll': 1.0450745592349768}, 'chosen_samples': [147939, 151777, 164502, 104502, 91777, 31777, 44502, 138846, 78846, 27939], 'chosen_samples_score': [0.19963936106592245, 0.19334313320908558, 0.1932256298371193, 0.1927542558025518, 0.19265802403842652, 0.19214139573104927, 0.19139877608050257, 0.18821993539805393, 0.18815661525568111, 0.18798368621001715], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.989570174999244, 'batch_acquisition_elapsed_time': 40.84944151400123})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8801, 'nll': 0.9269397158908842}, 'chosen_samples': [162672, 102672, 42672, 158974, 38974, 98974, 89186, 29186, 149186, 19648], 'chosen_samples_score': [0.18475819597103627, 0.18387788328408053, 0.18330088359552746, 0.1780236942520595, 0.17800021408514843, 0.17791002033934003, 0.1773945598408069, 0.1772933218757185, 0.17728197415013455, 0.17653425197318115], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.243492538000282, 'batch_acquisition_elapsed_time': 40.501357847999316})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8905, 'nll': 0.9330024329280854}, 'chosen_samples': [68691, 8691, 52971, 172971, 112971, 91335, 57882, 142491, 117882, 79042], 'chosen_samples_score': [0.1896863874050001, 0.18946251767904582, 0.186892798299145, 0.18464606353218696, 0.18342116901824623, 0.1821633665753833, 0.18192129286443065, 0.18082066831732452, 0.17936418977803809, 0.17895970290718274], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 20.19807982599741, 'batch_acquisition_elapsed_time': 40.38126641699637})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9011, 'nll': 0.7814113507223129}, 'chosen_samples': [57474, 177474, 117474, 148512, 88512, 20763, 28512, 80763, 140763, 43126], 'chosen_samples_score': [0.21022546463328695, 0.21019580473979838, 0.2100165101583394, 0.2018830948117032, 0.2017462157184397, 0.2005040374318252, 0.20013261261144324, 0.19793129825500008, 0.19638815099109524, 0.1943804871285655], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.23538286799885, 'batch_acquisition_elapsed_time': 40.719989762001205})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9025, 'nll': 0.7742098332953454}, 'chosen_samples': [170370, 110370, 50370, 109064, 169064, 51736, 111736, 49064, 33222, 171736], 'chosen_samples_score': [0.19238417534203536, 0.19166730669928786, 0.18887538709540208, 0.186937954061024, 0.18626548723468214, 0.185452871344478, 0.18523924556706217, 0.18491210680101278, 0.18386975952461698, 0.18361453699306152], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.949718376003148, 'batch_acquisition_elapsed_time': 40.750134038004035})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9081, 'nll': 0.7227777544510364}, 'chosen_samples': [86850, 26850, 146850, 135618, 15618, 75618, 80859, 2406, 152918, 140859], 'chosen_samples_score': [0.1854976723918773, 0.1839363046244873, 0.18250875882233633, 0.17800334701943796, 0.1775548026881916, 0.17748281207302233, 0.17372594711418027, 0.1733496159089182, 0.17319463257805048, 0.17239738387235434], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.225061125995126, 'batch_acquisition_elapsed_time': 40.613482927001314})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8992, 'nll': 0.7662688177168369}, 'chosen_samples': [79576, 19576, 80792, 139576, 140792, 20792, 107365, 123810, 3810, 47365], 'chosen_samples_score': [0.1978379899411585, 0.1900099118496492, 0.18911921672949394, 0.18832616077521552, 0.18775080169939448, 0.18654337347593922, 0.1837863727193602, 0.1837487809990556, 0.18236498788138927, 0.17975944231051572], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.729550817995914, 'batch_acquisition_elapsed_time': 40.69963050200022})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8903, 'nll': 0.7431522360652687}, 'chosen_samples': [167741, 47741, 107741, 94678, 154678, 34678, 71878, 131878, 22453, 88137], 'chosen_samples_score': [0.18806073299622458, 0.18785295481737668, 0.1857938717857348, 0.17738186151062552, 0.17697635133906442, 0.17690187688254783, 0.16964522411820543, 0.169499538217963, 0.16790142313230327, 0.16773123134152298], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.82667544099968, 'batch_acquisition_elapsed_time': 40.234003263001796})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9016, 'nll': 0.696607432088852}, 'chosen_samples': [140171, 29725, 20171, 59390, 179390, 89725, 776, 18376, 120776, 78376], 'chosen_samples_score': [0.18393291205871537, 0.1822182616362993, 0.18200725362986955, 0.1817982654797441, 0.18154903977736334, 0.1811397721790663, 0.18110259204154874, 0.18096000786849972, 0.18092888602008603, 0.18039485158422613], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.21428643300169, 'batch_acquisition_elapsed_time': 40.28557343200373})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9084, 'nll': 0.8011177816963196}, 'chosen_samples': [145384, 85384, 25384, 169890, 1840, 61840, 56464, 109890, 116464, 176464], 'chosen_samples_score': [0.19331211202966214, 0.1924017069583352, 0.19186989032874102, 0.19141647520920263, 0.18942296287878413, 0.18817870078974108, 0.18808020750665963, 0.1878768129679415, 0.1873416073735626, 0.1871005177692463], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 25.8871699339943, 'batch_acquisition_elapsed_time': 40.09537601000193})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9162, 'nll': 0.6990035228359699}, 'chosen_samples': [100456, 40456, 16036, 160456, 87883, 85132, 25986, 136036, 24424, 144424], 'chosen_samples_score': [0.18166971909986682, 0.18151913242740864, 0.18050348114815504, 0.18031675990529586, 0.17983190996638995, 0.1783709827720725, 0.17813925794188, 0.17798981760966318, 0.17757123645985465, 0.17744596861903286], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.67036934600037, 'batch_acquisition_elapsed_time': 40.322904594002466})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9101, 'nll': 0.8043909895485639}, 'chosen_samples': [90980, 266, 120266, 843, 60266, 126291, 6291, 150980, 24107, 144107], 'chosen_samples_score': [0.1929447532588282, 0.19110028575027901, 0.18987108137169487, 0.18904304212100626, 0.18862388358801216, 0.18819719317822425, 0.18778046272287496, 0.1876206461681139, 0.18743788844222822, 0.18739135218813527], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 23.99255551600072, 'batch_acquisition_elapsed_time': 40.40196395500243})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8904, 'nll': 0.7163068781828881}, 'chosen_samples': [166478, 82404, 106478, 46478, 22404, 138426, 115353, 43692, 103692, 18426], 'chosen_samples_score': [0.18011891649294656, 0.17994612789087283, 0.17829739921098647, 0.1779900988400522, 0.17581874491792332, 0.17536332267624827, 0.17440911843251758, 0.1742483296523783, 0.17406111041565478, 0.17302389318076508], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.343620574996748, 'batch_acquisition_elapsed_time': 40.14030625900341})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9231, 'nll': 0.6789049957311153}, 'chosen_samples': [52099, 93594, 112099, 33594, 90184, 153594, 30184, 172099, 144462, 121674], 'chosen_samples_score': [0.19355573864488032, 0.1923626106922003, 0.19115146455165816, 0.18904320667441682, 0.18883391663800614, 0.18864244850549047, 0.18788925662802372, 0.1867428873762046, 0.18542767273621005, 0.18499762349515084], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 25.420118884001567, 'batch_acquisition_elapsed_time': 40.22923427599744})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.926, 'nll': 0.5545076883912086}, 'chosen_samples': [26588, 90464, 150464, 146588, 30464, 116303, 86588, 137958, 74706, 17958], 'chosen_samples_score': [0.1805558226564064, 0.17976144999435056, 0.17951750005113803, 0.17944692072405474, 0.17787454894692364, 0.1776230280673076, 0.17653319660472694, 0.1763719443289618, 0.1755209929692483, 0.17409168484835788], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.16566045700165, 'batch_acquisition_elapsed_time': 40.02183703900664})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9254, 'nll': 0.5769265934514999}, 'chosen_samples': [153812, 33812, 93812, 98252, 63268, 158252, 161540, 123268, 38252, 101540], 'chosen_samples_score': [0.1841826592774027, 0.18269021414930772, 0.18242666030761837, 0.18115365528305705, 0.18007308073301243, 0.179621377724126, 0.17817681803811644, 0.17811441782022144, 0.17805447933281765, 0.17769790279406386], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.21511957400071, 'batch_acquisition_elapsed_time': 40.249350678001065})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9285, 'nll': 0.5959888518983127}, 'chosen_samples': [15276, 22481, 135276, 75276, 142481, 82481, 71797, 11797, 131797, 98657], 'chosen_samples_score': [0.17477000273414514, 0.17259223167207388, 0.17241211594790942, 0.172152769540597, 0.17175669404022836, 0.17175412634377293, 0.17156620664803257, 0.16970119517730559, 0.16949291609990172, 0.1692423305672422], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.130402994996984, 'batch_acquisition_elapsed_time': 39.581790254000225})