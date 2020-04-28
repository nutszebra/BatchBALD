store = {}
store['args']={'dataset': 'DatasetEnum.repeated_mnist_w_noise2', 'num_inference_samples': 10, 'available_sample_k': 10, 'seed': 420620, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.multibald', 'experiment_description': 'RMNIST with noise k10 b5 and b10 (and k100 b10), BALD, BatchBALD and heuristic', 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 3072, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 5056, 'target_accuracy': 1.0, 'target_num_acquired_samples': 300, 'initial_percentage': 100, 'reduce_percentage': 0, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'experiment_task_id': 'repeated_mnist_w_noise2_multibald_bald_k10_b10_420620', 'experiments_laaos': 'experiment_configs/rmnist_w_noise_2_5/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'balanced_validation_set': False, 'balanced_test_set': False}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=repeated_mnist_w_noise2_multibald_bald_k10_b10_420620', '--experiments_laaos=experiment_configs/rmnist_w_noise_2_5/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.6345, 'nll': 1.8903366082118023}, 'chosen_targets': [5, 8, 2, 8, 2, 4, 8, 7, 8, 8], 'chosen_samples': [116711, 49496, 71193, 8719, 9672, 111077, 36915, 28520, 62215, 69852], 'chosen_samples_score': [1.317533274263591, 2.011300008221316, 2.214075098596816, 2.273437297047165, 2.2950253552649835, 2.29987843500514, 2.309030962459417, 2.3055660983860897, 2.3033458818057535, 2.2958539068770225], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.73241082399909, 'batch_acquisition_elapsed_time': 498.5018418680047})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.7235, 'nll': 0.9967534441166191}, 'chosen_targets': [4, 0, 9, 7, 5, 0, 9, 5, 3, 9], 'chosen_samples': [22034, 22144, 109714, 65049, 51278, 87035, 60930, 113479, 7721, 49714], 'chosen_samples_score': [1.3007015827327189, 2.0182931341387205, 2.218512688007059, 2.2750931505699086, 2.2918882156220994, 2.299039290127315, 2.297986406764818, 2.3133640527268597, 2.3001465035870816, 2.3072869917830743], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 5.850204889000452, 'batch_acquisition_elapsed_time': 498.5498392399968})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.791, 'nll': 0.8110974606869638}, 'chosen_targets': [8, 8, 5, 2, 7, 0, 9, 8, 3, 4], 'chosen_samples': [64797, 36192, 68104, 19833, 49056, 114985, 26212, 90738, 85586, 48785], 'chosen_samples_score': [1.4269576119324572, 2.1359470807010488, 2.2786486391295315, 2.298202184285241, 2.301560972590522, 2.302388650835434, 2.299963453871216, 2.2940981730177725, 2.296872175254975, 2.301846226911225], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.753574898000807, 'batch_acquisition_elapsed_time': 498.44699481099815})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.7881, 'nll': 0.8221266212150855}, 'chosen_targets': [6, 3, 6, 3, 6, 2, 2, 9, 7, 5], 'chosen_samples': [95962, 41391, 119237, 34695, 101018, 67170, 106122, 82725, 32651, 32362], 'chosen_samples_score': [1.4892866796409279, 2.0842973993332663, 2.232112624502734, 2.284680190359726, 2.297866992702592, 2.3014026517676975, 2.296407435301617, 2.305207154294487, 2.307831858949363, 2.309964984687936], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.818393585999729, 'batch_acquisition_elapsed_time': 498.3859398479981})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8236, 'nll': 0.5928820185749357}, 'chosen_targets': [7, 8, 2, 8, 2, 9, 3, 6, 9, 2], 'chosen_samples': [56220, 23112, 42513, 81395, 30191, 49880, 106549, 94924, 60826, 59714], 'chosen_samples_score': [1.26553888138405, 1.882416911031671, 2.1573182682750724, 2.2510535886079666, 2.281769791564514, 2.2945197733764053, 2.304390653804587, 2.3038846712236563, 2.3090712125141994, 2.3047809448609957], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 5.857877422000456, 'batch_acquisition_elapsed_time': 498.48299780100206})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8617, 'nll': 0.4781580856284373}, 'chosen_targets': [9, 3, 3, 6, 3, 5, 9, 9, 3, 6], 'chosen_samples': [15562, 78426, 89224, 51778, 43140, 64062, 34876, 82824, 86305, 70224], 'chosen_samples_score': [1.280833310767873, 1.95571934124553, 2.1673887213503393, 2.252439573768215, 2.2816568091233838, 2.29465991175716, 2.3110543401505317, 2.3015885894470474, 2.293121432683531, 2.3101608387383923], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 5.898877204002929, 'batch_acquisition_elapsed_time': 498.40599606400065})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.885, 'nll': 0.4290670890239308}, 'chosen_targets': [7, 2, 5, 5, 2, 4, 1, 5, 9, 2], 'chosen_samples': [37984, 3719, 102428, 83567, 83652, 75207, 39818, 35287, 66368, 37861], 'chosen_samples_score': [1.3153471651616222, 2.162537943880253, 2.284220518141397, 2.2983947867022634, 2.302000638588088, 2.302480174820238, 2.304618692159892, 2.303654833576641, 2.308243062704933, 2.312416890304023], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.674520921995281, 'batch_acquisition_elapsed_time': 498.1238379659917})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8836, 'nll': 0.41193869077514417}, 'chosen_targets': [3, 7, 0, 3, 3, 3, 3, 5, 5, 2], 'chosen_samples': [81998, 43178, 80840, 116741, 60207, 70260, 67762, 49728, 79973, 73121], 'chosen_samples_score': [1.0992187789010432, 1.7249431052735968, 2.0486085712806243, 2.1883801487504044, 2.2513524322692167, 2.279802420152227, 2.287586496958888, 2.303599875265615, 2.307697414782308, 2.299274863528276], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 5.913602015993092, 'batch_acquisition_elapsed_time': 498.39619931600464})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9056, 'nll': 0.3236312556923522}, 'chosen_targets': [0, 3, 2, 8, 8, 7, 4, 3, 3, 8], 'chosen_samples': [70265, 53547, 14373, 99668, 12934, 23386, 116802, 17010, 13983, 69608], 'chosen_samples_score': [1.244733041171175, 2.003520794338346, 2.2294415499346827, 2.2806136287432905, 2.2953044458576635, 2.300537541507073, 2.302510291296831, 2.3073219213775786, 2.300343817752157, 2.2887397972510923], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.808944991003955, 'batch_acquisition_elapsed_time': 498.6662700309971})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8936, 'nll': 0.36521565652236787}, 'chosen_targets': [2, 4, 1, 3, 5, 0, 1, 3, 4, 5], 'chosen_samples': [65103, 19975, 106780, 57608, 103574, 7948, 26072, 113903, 62856, 111492], 'chosen_samples_score': [0.9575098928370724, 1.6234929511678888, 2.002926835625705, 2.159312944421754, 2.233466418378637, 2.2728294262258077, 2.2820074377223953, 2.3071153710489742, 2.2991334206727982, 2.304837003293451], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 6.866861853006412, 'batch_acquisition_elapsed_time': 498.57349698799953})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9097, 'nll': 0.3203761727430629}, 'chosen_targets': [8, 4, 9, 5, 3, 4, 8, 0, 2, 8], 'chosen_samples': [7979, 13650, 92351, 77722, 49091, 12972, 16951, 78324, 84623, 38249], 'chosen_samples_score': [1.0724978304186523, 1.7672512172526793, 2.10403303091301, 2.2136728657316134, 2.26863088907106, 2.289452247140494, 2.2938335906964533, 2.3122907194659117, 2.2949069367623487, 2.3057350253221625], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 6.862063309003133, 'batch_acquisition_elapsed_time': 497.98377304000314})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9106, 'nll': 0.31649042747568357}, 'chosen_targets': [2, 7, 6, 2, 8, 8, 8, 7, 2, 8], 'chosen_samples': [115188, 95474, 18608, 96884, 19756, 31706, 47076, 119626, 97347, 100942], 'chosen_samples_score': [1.1181887316804366, 1.8340338742764846, 2.1716731094591557, 2.251013277650854, 2.283280573487571, 2.2950171939860167, 2.3036705575208076, 2.306109580335058, 2.307788376288423, 2.3040156819339157], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.861022789991694, 'batch_acquisition_elapsed_time': 498.2446817049931})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9274, 'nll': 0.24439395727917432}, 'chosen_targets': [8, 2, 2, 7, 5, 5, 8, 2, 0, 4], 'chosen_samples': [94707, 22199, 58472, 82613, 70400, 103212, 115519, 116824, 109497, 85971], 'chosen_samples_score': [1.2321909000159685, 1.9703879884271505, 2.2171835563726123, 2.286100878903282, 2.2977750583884182, 2.3015044945671974, 2.3019504661304993, 2.3038362003836466, 2.307827667740763, 2.303823941064878], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.8299227230018, 'batch_acquisition_elapsed_time': 497.78325721700094})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9265, 'nll': 0.25367197410090614}, 'chosen_targets': [7, 2, 5, 8, 3, 8, 4, 0, 7, 2], 'chosen_samples': [61127, 119390, 85738, 46368, 114858, 87085, 45069, 101713, 98598, 59390], 'chosen_samples_score': [1.0982261512419296, 1.803578052439488, 2.1417166190570636, 2.26370994415763, 2.291729878304066, 2.2993172030659776, 2.3029634139857804, 2.3084141454278586, 2.2980464853223697, 2.3097701668315107], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.799080958997365, 'batch_acquisition_elapsed_time': 497.6764513550006})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9187, 'nll': 0.30535908064090744}, 'chosen_targets': [2, 9, 4, 3, 1, 4, 7, 4, 6, 1], 'chosen_samples': [55906, 13998, 1568, 57523, 27793, 63370, 6050, 44110, 50086, 8218], 'chosen_samples_score': [1.0182015020738093, 1.6870864366990401, 2.002188709130855, 2.163110135060916, 2.2363147097785507, 2.271117802452091, 2.283548405751877, 2.29667183026739, 2.3153261272601915, 2.2964986702139845], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 6.853808404004667, 'batch_acquisition_elapsed_time': 497.9166957490088})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9263, 'nll': 0.2890173745761722}, 'chosen_targets': [5, 0, 6, 2, 3, 5, 6, 0, 2, 2], 'chosen_samples': [79942, 51649, 108370, 5700, 71565, 19942, 69468, 34623, 51986, 67879], 'chosen_samples_score': [1.2409885288909708, 1.9077059049907177, 2.187317359788203, 2.2625719934816857, 2.285102120625613, 2.295923086293307, 2.299353864317734, 2.3005632297977807, 2.2894372056773133, 2.3177192543313803], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 6.843066029003239, 'batch_acquisition_elapsed_time': 498.0485944520042})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9391, 'nll': 0.24055979279361786}, 'chosen_targets': [5, 1, 5, 3, 7, 1, 6, 2, 9, 4], 'chosen_samples': [99208, 77540, 119726, 44969, 109829, 17540, 6474, 1573, 24998, 58390], 'chosen_samples_score': [1.0922505578413357, 1.8261843178521455, 2.1029074324880366, 2.21641731662862, 2.262312177581653, 2.2830862193907637, 2.28703263449794, 2.2890084781944813, 2.2989187997312506, 2.2890142364030757], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.899406714990619, 'batch_acquisition_elapsed_time': 498.19330672999786})
store['iterations'].append({'num_epochs': 15, 'test_metrics': {'accuracy': 0.9357, 'nll': 0.22301069498962606}, 'chosen_targets': [3, 0, 2, 6, 0, 0, 5, 0, 4, 3], 'chosen_samples': [93357, 42703, 40589, 18904, 85159, 68093, 88886, 43961, 78398, 38970], 'chosen_samples_score': [1.2690885730337769, 2.0213142035881746, 2.235476132090885, 2.2850856581737715, 2.298302089593526, 2.301568324583741, 2.294110713754677, 2.3097657557563505, 2.2913355233740242, 2.2952454278797223], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.720742684003199, 'batch_acquisition_elapsed_time': 498.1078699140053})
store['iterations'].append({'num_epochs': 16, 'test_metrics': {'accuracy': 0.9436, 'nll': 0.21044695325301763}, 'chosen_targets': [7, 5, 9, 4, 2, 0, 6, 8, 5, 3], 'chosen_samples': [36818, 71922, 52910, 18501, 93361, 49200, 5684, 59294, 99700, 43224], 'chosen_samples_score': [1.3884480081490262, 2.0680074815332037, 2.2463625246801326, 2.2894639836355446, 2.300390825461946, 2.302173342826561, 2.305676397279997, 2.2956577733835437, 2.301927260407397, 2.3054239888144195], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.696014303000993, 'batch_acquisition_elapsed_time': 497.86649559400394})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9466, 'nll': 0.2011093906133134}, 'chosen_targets': [3, 7, 5, 9, 2, 9, 8, 7, 9, 5], 'chosen_samples': [108360, 2376, 66418, 80820, 77684, 61674, 69650, 28723, 30095, 92507], 'chosen_samples_score': [1.2160753741923056, 1.962792708606986, 2.1921531316737752, 2.272709420519303, 2.2941301726078676, 2.300198305255932, 2.299529327132838, 2.299572158609524, 2.308214917908563, 2.304124530288416], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.760734055002104, 'batch_acquisition_elapsed_time': 497.5982039570081})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9412, 'nll': 0.2517020926511729}, 'chosen_targets': [8, 8, 3, 0, 8, 8, 3, 2, 2, 0], 'chosen_samples': [57335, 74896, 56228, 26258, 113854, 33089, 17634, 86577, 33364, 86258], 'chosen_samples_score': [1.2031294747999908, 1.8713152789807437, 2.13442921064157, 2.2422853743208586, 2.2833879017441, 2.2954377812861346, 2.3016904731302423, 2.3066587562527534, 2.2988565946645116, 2.2956539907761693], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.884903297992423, 'batch_acquisition_elapsed_time': 497.93462665300467})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9469, 'nll': 0.20790335769141544}, 'chosen_targets': [4, 7, 8, 3, 2, 3, 6, 3, 1, 5], 'chosen_samples': [20183, 84990, 117602, 110417, 81174, 71232, 39383, 8709, 97441, 108512], 'chosen_samples_score': [1.1752559147344648, 1.8262262626691423, 2.149489751180663, 2.2505994574905244, 2.2878945553631347, 2.29893579501778, 2.292190396942036, 2.2967414752244872, 2.299915813438604, 2.3042458281295572], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.856185044991435, 'batch_acquisition_elapsed_time': 497.5352646889951})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.939, 'nll': 0.2390610242836848}, 'chosen_targets': [5, 3, 4, 8, 3, 9, 7, 2, 3, 7], 'chosen_samples': [38698, 83724, 73942, 109543, 28536, 105784, 44853, 39561, 5748, 1376], 'chosen_samples_score': [1.2031292850290582, 1.9536718464289902, 2.2305058123058994, 2.2838327613706775, 2.296579315990447, 2.300543931275457, 2.310320518163236, 2.3263139032692393, 2.298627574171674, 2.3055069387117846], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.767932508999365, 'batch_acquisition_elapsed_time': 497.4534886600013})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.948, 'nll': 0.20459441191302136}, 'chosen_targets': [0, 8, 2, 0, 9, 3, 4, 3, 0, 5], 'chosen_samples': [46412, 79350, 24462, 49463, 33358, 22675, 42793, 22149, 72264, 82194], 'chosen_samples_score': [1.2139934850707654, 1.9582840686660064, 2.216174714049857, 2.2808268216160066, 2.2953613744370056, 2.300609979514748, 2.298299971133301, 2.307354455614266, 2.3111218555993966, 2.3109713822977227], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.818519747001119, 'batch_acquisition_elapsed_time': 497.6338852659974})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9438, 'nll': 0.20238966486397997}, 'chosen_targets': [9, 4, 0, 5, 9, 9, 4, 9, 4, 0], 'chosen_samples': [46021, 99255, 71403, 26460, 12320, 8847, 107240, 106021, 60746, 40494], 'chosen_samples_score': [1.3200154087787004, 1.9735983743280467, 2.184331592104538, 2.2562601783903338, 2.288706466467751, 2.29811374481796, 2.2952764091913624, 2.31233906773023, 2.3040153345352357, 2.2973798774787486], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.752803005991154, 'batch_acquisition_elapsed_time': 497.5876049660001})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9562, 'nll': 0.1816769666497587}, 'chosen_targets': [6, 1, 5, 8, 5, 8, 4, 2, 9, 9], 'chosen_samples': [54885, 96141, 107951, 113872, 102687, 88136, 103604, 25246, 60424, 6174], 'chosen_samples_score': [1.1433217666442013, 1.8610882270774622, 2.17472970416354, 2.2565486181379466, 2.2876175134191348, 2.297528577389744, 2.3131475837513946, 2.2970197866798916, 2.3066864681525066, 2.294936662525311], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.821804797989898, 'batch_acquisition_elapsed_time': 497.6313908989978})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9492, 'nll': 0.214598500298099}, 'chosen_targets': [1, 8, 8, 3, 2, 5, 4, 9, 9, 8], 'chosen_samples': [93383, 13677, 33338, 94660, 52456, 98408, 4822, 35804, 73742, 25657], 'chosen_samples_score': [1.0129875154250882, 1.7549260922839247, 2.095136049450637, 2.22332610236165, 2.270880737187889, 2.288983356947818, 2.296301343434075, 2.288037677932067, 2.296838035211082, 2.2978142476984305], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.834866434001015, 'batch_acquisition_elapsed_time': 497.27186369399715})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9548, 'nll': 0.20279809549617914}, 'chosen_targets': [1, 9, 6, 9, 9, 2, 5, 9, 6, 5], 'chosen_samples': [12318, 62137, 93812, 71074, 49204, 52582, 8731, 12061, 54994, 56695], 'chosen_samples_score': [1.032876605993298, 1.7387855205038243, 2.059139459811591, 2.190688991469793, 2.2532019615460204, 2.2806202876310193, 2.290904995162938, 2.29438250848416, 2.3015909558580505, 2.2960573447102055], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.903509163996205, 'batch_acquisition_elapsed_time': 497.55244936699455})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9434, 'nll': 0.21305503743045812}, 'chosen_targets': [4, 3, 9, 3, 3, 4, 2, 2, 4, 3], 'chosen_samples': [1812, 998, 42438, 84066, 115054, 828, 87898, 97469, 91817, 66430], 'chosen_samples_score': [1.1275255604387864, 1.8518089303318053, 2.1501310800381477, 2.2535146354901725, 2.2852963346890824, 2.29731315295646, 2.3020651441090827, 2.292907430295901, 2.308234440034183, 2.312542183891912], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.848414755993872, 'batch_acquisition_elapsed_time': 497.56016459999955})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9474, 'nll': 0.22688749114514467}, 'chosen_targets': [7, 5, 7, 3, 9, 8, 7, 3, 7, 9], 'chosen_samples': [114035, 88477, 98389, 73969, 24164, 93162, 42573, 42477, 71534, 84613], 'chosen_samples_score': [1.03045875998435, 1.7430118528492566, 2.0877338560018788, 2.208112482846153, 2.264262620536388, 2.2855088057083552, 2.2987083309208605, 2.3047030398413977, 2.3075796609244845, 2.3106250005673674], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.802166573994327, 'batch_acquisition_elapsed_time': 497.4895444050053})