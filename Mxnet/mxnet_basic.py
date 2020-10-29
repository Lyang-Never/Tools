'''
1、
mxnet pretrained loaded by .json/.params
'''

json = 'model-symbol.json'
params = 'model-0000.params'

# vec0,vec1 = params[:-7].split('-')
# sym,arg_params,aux_params = mx.model.load_checkpoint(vec0,int(vec1))
# all_layers = sym.get_internals()

inputs = mx.sym.var('data',dtype = 'float32')
sym = mx.sym.load(json)
all_layer = sym.get_internals()   # 得到一个symbol group,可以通过.list_outputs()转化为list获得，layer_ = all_layer.list_outputs()  
# layer = sym.list_arguments()
sym = mx.gluon.SymbolBlock(all_layer['pre_fc1_output'],inputs)  # 这个'pre_fc1_output'可通过 .list_outputs()进行查看进行截取
sym.load_parameters(params,ignore_extra=True)

# return sym
