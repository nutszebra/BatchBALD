store = {}
store['args']={'name': 'emnist_multibald_bald_k10_218487', 'available_sample_k': 5, 'num_inference_samples': 10, 'seed': 218487, 'acquisition_method': 'AcquisitionMethod.multibald', 'experiment_description': 'EMNIST with b5 and k10, k100 with both BALD and BatchBALD', 'type': 'AcquisitionFunction.bald', 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 16384, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 20224, 'target_accuracy': 0.85, 'target_num_acquired_samples': 300, 'log_interval': 20, 'dataset': 'DatasetEnum.emnist', 'initial_samples': [], 'experiment_task_id': 9, 'experiments_laaos': './experiment_configs/emnist_bbb/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=9', '--experiments_laaos=./experiment_configs/emnist_bbb/configs.py']
store['iterations']=[]
store['initial_samples']=[]
store['iterations'].append({'num_epochs': 0, 'test_metrics': {'accuracy': 0.02303191489361702, 'nll': 3.861316835119369}, 'chosen_samples': [44000, 45602, 2933, 59128, 76316], 'chosen_samples_score': [0.008420869843952072, 0.01636495369616986, 0.024158668445875442, 0.030751606817206678, 0.03899254174600841], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.06063829787234042, 'nll': 43.75167677859042}, 'chosen_samples': [45028, 54619, 86939, 41255, 6279], 'chosen_samples_score': [1.1397585442314033, 1.8273625787743426, 2.158380340570042, 2.250358099523698, 2.280659503572192], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.0973404255319149, 'nll': 48.04483991906998}, 'chosen_samples': [34015, 36189, 12586, 39419, 85314], 'chosen_samples_score': [1.4202326134964032, 2.20361232291412, 2.286180723777653, 2.2876672704686256, 2.287932778766468], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.11335106382978724, 'nll': 33.32120733058199}, 'chosen_samples': [2918, 97169, 103012, 98863, 70078], 'chosen_samples_score': [1.505445741717629, 2.2183172008243983, 2.2895102088507353, 2.295936878593367, 2.287886327327463], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.1497872340425532, 'nll': 37.20460628428358}, 'chosen_samples': [6837, 81694, 54011, 63843, 45158], 'chosen_samples_score': [1.5892625326313667, 2.2147564754047613, 2.2865467455407917, 2.312686113767761, 2.308481363007454], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.1523404255319149, 'nll': 36.180425734824325}, 'chosen_samples': [56570, 67273, 8063, 19680, 33800], 'chosen_samples_score': [1.5922964007792981, 2.1645886773813894, 2.279286582562175, 2.298157286572744, 2.3089356440194915], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.1696276595744681, 'nll': 29.192730673932015}, 'chosen_samples': [68471, 20416, 111256, 83842, 69105], 'chosen_samples_score': [1.7390849111125464, 2.210381804839998, 2.2846864717287074, 2.309249896904431, 2.306990371252213], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.18074468085106382, 'nll': 29.656835619338015}, 'chosen_samples': [42087, 39487, 22298, 86274, 25832], 'chosen_samples_score': [1.5386103032445135, 2.237942919455988, 2.290904139478499, 2.293862290749636, 2.2960108018520495], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.18925531914893617, 'nll': 24.875875443803505}, 'chosen_samples': [71975, 28492, 84293, 112029, 45975], 'chosen_samples_score': [1.6393416848000415, 2.2079711929692123, 2.285873575135307, 2.2904282197139567, 2.305413759772595], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.20893617021276595, 'nll': 23.92493075593989}, 'chosen_samples': [9089, 45939, 109256, 80673, 11930], 'chosen_samples_score': [1.7039841926882549, 2.2144926807435246, 2.282775977298548, 2.2993245458493616, 2.3136547801657645], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.22957446808510637, 'nll': 20.118213965233338}, 'chosen_samples': [26356, 93833, 110034, 69107, 30142], 'chosen_samples_score': [1.7059978012474097, 2.227534554447269, 2.2907788330445435, 2.2809798883097585, 2.310468182422582], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.24218085106382978, 'nll': 21.60280939142755}, 'chosen_samples': [98678, 95263, 68210, 62682, 60873], 'chosen_samples_score': [1.6667917579553688, 2.2412332555629444, 2.2967445343297297, 2.286766739959905, 2.311259993873777], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.25590425531914895, 'nll': 16.583754968846097}, 'chosen_samples': [6683, 87854, 12875, 82201, 75430], 'chosen_samples_score': [1.648182326502529, 2.2155466652238744, 2.290095886803276, 2.3039889332346917, 2.3282445423930027], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.26893617021276595, 'nll': 17.84725715961862}, 'chosen_samples': [58640, 1299, 31038, 78417, 36087], 'chosen_samples_score': [1.9170724141442348, 2.2707772664803643, 2.2997491206853145, 2.2780004943189054, 2.2942344931377505], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.28606382978723405, 'nll': 15.846535067456834}, 'chosen_samples': [65788, 97337, 9238, 80102, 73341], 'chosen_samples_score': [1.7185855483991463, 2.2485972296704873, 2.2967622149757823, 2.2947049208324724, 2.3268989754602742], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2785106382978723, 'nll': 15.793318233084172}, 'chosen_samples': [77941, 84041, 12256, 46696, 68594], 'chosen_samples_score': [1.8040846498657093, 2.270543985215968, 2.2977451105057165, 2.3164775102866235, 2.2981933237949175], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3072872340425532, 'nll': 14.62017266861936}, 'chosen_samples': [70638, 108254, 104973, 88120, 91382], 'chosen_samples_score': [1.5027327293540158, 2.124598660065694, 2.2684660601880777, 2.2879512148129457, 2.335434095676323], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3, 'nll': 13.48580343205878}, 'chosen_samples': [89123, 26212, 8144, 78104, 36331], 'chosen_samples_score': [1.7065475694982928, 2.2314369048018343, 2.2927666509351816, 2.28860418148747, 2.28320468106236], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.31622340425531914, 'nll': 12.34392271812926}, 'chosen_samples': [26441, 111572, 15166, 54294, 5612], 'chosen_samples_score': [1.639283290457596, 2.2009865301739766, 2.2907374319568605, 2.3280585488509367, 2.314991789997723], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.30234042553191487, 'nll': 12.294933193287951}, 'chosen_samples': [107039, 10880, 45396, 99156, 48542], 'chosen_samples_score': [1.6533393008913913, 2.1728830897784297, 2.284835052310517, 2.2818986882044143, 2.2998791989188394], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3206914893617021, 'nll': 12.216720279937094}, 'chosen_samples': [35184, 92282, 27844, 96675, 30351], 'chosen_samples_score': [1.857440954752678, 2.2458482152944144, 2.2998853677995292, 2.2966521145843592, 2.280415375508065], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3223936170212766, 'nll': 11.340651252421926}, 'chosen_samples': [23463, 54639, 33379, 102976, 78850], 'chosen_samples_score': [1.5537092482953705, 2.1587285569995194, 2.2822787754333866, 2.301099695621268, 2.2916809029762657], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.31968085106382976, 'nll': 12.173580635557784}, 'chosen_samples': [96568, 67788, 9354, 48043, 27534], 'chosen_samples_score': [1.8172590020320167, 2.273869056829471, 2.299846104810901, 2.304492928099538, 2.3003005715908698], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.31957446808510637, 'nll': 10.557250472535479}, 'chosen_samples': [55020, 79883, 86038, 110975, 54335], 'chosen_samples_score': [1.6590247845160437, 2.172698293942313, 2.277038798375785, 2.271808555733985, 2.308390051312921], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.32063829787234044, 'nll': 10.758057334575247}, 'chosen_samples': [50350, 22602, 69220, 37897, 47018], 'chosen_samples_score': [1.707396039160351, 2.2173228177945985, 2.2847742943749316, 2.3051123010300323, 2.308647552004787], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.33335106382978724, 'nll': 9.309172361657975}, 'chosen_samples': [104704, 32035, 56863, 50995, 984], 'chosen_samples_score': [1.663368649696624, 2.218908679758922, 2.291240661253317, 2.30115752683444, 2.3394698391657105], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3515957446808511, 'nll': 9.753787439224569}, 'chosen_samples': [4939, 39093, 47144, 40580, 49265], 'chosen_samples_score': [1.7117249507506793, 2.2220033155847334, 2.2889087104671395, 2.2754134209278023, 2.295151769854909], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.35638297872340424, 'nll': 9.38847083355518}, 'chosen_samples': [82560, 106651, 93750, 26835, 42580], 'chosen_samples_score': [1.6635979345558871, 2.169565071217021, 2.270196652185918, 2.279352736939404, 2.3074573131792593], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.36031914893617023, 'nll': 8.813606025208818}, 'chosen_samples': [4589, 96282, 18668, 33406, 86589], 'chosen_samples_score': [1.5933010674856467, 2.2190883600050095, 2.2925990006981753, 2.288221727143453, 2.3150793017950866], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3975, 'nll': 8.510091513369947}, 'chosen_samples': [32814, 110443, 18813, 28826, 28056], 'chosen_samples_score': [1.5751710900375655, 2.1721814001197934, 2.2805072366601356, 2.3215912348692975, 2.30453416393656], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4077659574468085, 'nll': 8.207754452482183}, 'chosen_samples': [60355, 60867, 42853, 8216, 87780], 'chosen_samples_score': [1.7268023103386405, 2.2304060613528414, 2.297359942088061, 2.283439360716008, 2.296903672846146], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3992553191489362, 'nll': 8.15065623019604}, 'chosen_samples': [86254, 56175, 42568, 34337, 4983], 'chosen_samples_score': [1.735281913432054, 2.222822329397477, 2.291786824759546, 2.312374884573961, 2.2792800142697223], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4100531914893617, 'nll': 7.481370009564339}, 'chosen_samples': [18983, 69698, 45574, 79315, 23994], 'chosen_samples_score': [1.5636831375181786, 2.172053064647976, 2.273537938158051, 2.318477266774427, 2.2956629098629118], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4103191489361702, 'nll': 8.018331776071102}, 'chosen_samples': [52038, 53847, 53180, 9339, 101260], 'chosen_samples_score': [1.6635231962641213, 2.2144414148152087, 2.2919924444279687, 2.28174349683676, 2.3032801284012736], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.40388297872340423, 'nll': 7.355077538997569}, 'chosen_samples': [89909, 85373, 79038, 94195, 99928], 'chosen_samples_score': [1.8112969730139536, 2.2517754060641204, 2.2987525561272406, 2.295059705903171, 2.2920955567632633], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.40867021276595744, 'nll': 7.503932109589273}, 'chosen_samples': [39216, 76121, 16361, 91226, 55501], 'chosen_samples_score': [1.7020995471169664, 2.229923555562115, 2.2920321496208196, 2.2948937486368104, 2.3198388568798647], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4151595744680851, 'nll': 7.052772639254306}, 'chosen_samples': [64052, 2101, 22909, 95369, 94883], 'chosen_samples_score': [1.5841139291663526, 2.1899930702928123, 2.2802155071629286, 2.295170589201038, 2.297675045765127], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4301063829787234, 'nll': 6.9326228620650925}, 'chosen_samples': [90665, 20616, 13514, 9567, 36260], 'chosen_samples_score': [1.6230769321915726, 2.2058707455454276, 2.2871277848659823, 2.2734322929122524, 2.2889969448545147], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.43303191489361703, 'nll': 6.955938620871686}, 'chosen_samples': [103986, 23211, 66290, 21642, 26277], 'chosen_samples_score': [1.4809338904044864, 2.123094220128745, 2.2527230333355357, 2.302298584784533, 2.3285469697529937], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.42638297872340425, 'nll': 7.074836414824141}, 'chosen_samples': [35098, 44545, 89125, 53022, 102171], 'chosen_samples_score': [1.7542446122073958, 2.205899951269275, 2.283605328344571, 2.315280206763302, 2.321925348186016], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.44872340425531915, 'nll': 6.531470517909273}, 'chosen_samples': [29538, 42541, 32885, 102356, 1459], 'chosen_samples_score': [1.699170070218671, 2.220342686587555, 2.287675588053842, 2.303773644782387, 2.317492499398848], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.44170212765957445, 'nll': 6.603807041898687}, 'chosen_samples': [70636, 101217, 22519, 59929, 28597], 'chosen_samples_score': [1.7484070441005388, 2.248871798725959, 2.297401905074336, 2.3024989221651433, 2.3281167528016056], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4332446808510638, 'nll': 6.608410367762789}, 'chosen_samples': [47699, 9811, 16220, 9477, 97189], 'chosen_samples_score': [1.5738439727980449, 2.1821911172762976, 2.2803819612289904, 2.311570307701511, 2.286709172730358], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4397340425531915, 'nll': 6.3588354001146685}, 'chosen_samples': [51358, 112755, 55055, 38196, 35426], 'chosen_samples_score': [1.641905729471412, 2.2136815188985386, 2.2942332042187386, 2.285357396225918, 2.2907909016672523], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4505851063829787, 'nll': 5.326562588062692}, 'chosen_samples': [107988, 23131, 90708, 9864, 79707], 'chosen_samples_score': [1.5794386235350868, 2.193635566386991, 2.2801395881917452, 2.318236058013288, 2.3070594377457656], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.47414893617021275, 'nll': 5.148639303978453}, 'chosen_samples': [110095, 30613, 45552, 65707, 104825], 'chosen_samples_score': [1.7091970314239056, 2.239398329909271, 2.2927163734995557, 2.2881517451637543, 2.305459024990687], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4677659574468085, 'nll': 5.509161911416561}, 'chosen_samples': [20248, 108655, 59045, 55016, 45274], 'chosen_samples_score': [1.5727018537983684, 2.1648316288350755, 2.2803408381407677, 2.283942617915536, 2.281415472654362], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4689893617021277, 'nll': 5.641061529200128}, 'chosen_samples': [49145, 83533, 59672, 71373, 19143], 'chosen_samples_score': [1.691183471019282, 2.2083969113315067, 2.2874649552394635, 2.2811926508478058, 2.2867129786984672], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.47175531914893615, 'nll': 5.179651263622527}, 'chosen_samples': [102979, 37877, 16630, 37151, 98190], 'chosen_samples_score': [1.6032578147971353, 2.173111935844462, 2.279801684890783, 2.2933167760276145, 2.274851819286233], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4747872340425532, 'nll': 4.940854927225316}, 'chosen_samples': [14036, 24695, 20188, 74247, 28611], 'chosen_samples_score': [1.5251173794988733, 2.1843742354873124, 2.280505173785711, 2.296196637122859, 2.295448685208162], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4742021276595745, 'nll': 4.726866995628844}, 'chosen_samples': [3159, 80397, 111911, 61035, 85673], 'chosen_samples_score': [1.595509688233043, 2.2018543297509843, 2.28212807447396, 2.293834620509365, 2.3287446894782065], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.48154255319148936, 'nll': 4.8756445373372825}, 'chosen_samples': [37203, 62634, 34661, 3495, 11940], 'chosen_samples_score': [1.5392805276591872, 2.16996641973842, 2.2768000074970987, 2.3067514101588635, 2.3103350788774697], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.47664893617021276, 'nll': 4.815562094424633}, 'chosen_samples': [40794, 50261, 55358, 44610, 76631], 'chosen_samples_score': [1.821458767242019, 2.242872273015913, 2.294273729845256, 2.319200668292494, 2.290613129996742], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4998404255319149, 'nll': 4.78972689648892}, 'chosen_samples': [27617, 83421, 89332, 75150, 65825], 'chosen_samples_score': [1.6474480464629213, 2.2051278667484424, 2.2867319308646135, 2.265758866155216, 2.2774691849640987], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.49457446808510636, 'nll': 4.547770602043639}, 'chosen_samples': [112265, 39143, 21811, 54991, 28524], 'chosen_samples_score': [1.5217220376940093, 2.1600520283195954, 2.278022324591636, 2.2920740512100934, 2.2945287162332475], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.520904255319149, 'nll': 4.251299972939998}, 'chosen_samples': [97991, 96242, 60622, 6544, 2802], 'chosen_samples_score': [1.619285857282295, 2.165615018070611, 2.27805238315727, 2.290104914511595, 2.316791338935565], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.5091489361702127, 'nll': 4.491015931799057}, 'chosen_samples': [53154, 110534, 83026, 30016, 23122], 'chosen_samples_score': [1.6847259075303873, 2.1939404678770984, 2.287032740662911, 2.348649546328251, 2.2895606085300733], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.5093085106382979, 'nll': 4.415558121863832}, 'chosen_samples': [44236, 31812, 112152, 23588, 69002], 'chosen_samples_score': [1.8468798433329048, 2.257870044962052, 2.2995507313075754, 2.3150327068440166, 2.3194734297138355], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.5095744680851064, 'nll': 4.237420169546249}, 'chosen_samples': [688, 64038, 79652, 63185, 34367], 'chosen_samples_score': [1.5492730044526846, 2.177907961941613, 2.2826195326657692, 2.310558051814466, 2.318666924863275], 'chosen_samples_orignal_score': None})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.5227659574468085, 'nll': 4.134197535210467}, 'chosen_samples': [92401, 23016, 325, 52202, 19095], 'chosen_samples_score': [1.6197226031163616, 2.1709175108802943, 2.278109014037252, 2.2983798189876783, 2.2829414042322886], 'chosen_samples_orignal_score': None})