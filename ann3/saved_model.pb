՚
??
B
AssignVariableOp
resource
value"dtype"
dtypetype?
~
BiasAdd

value"T	
bias"T
output"T" 
Ttype:
2	"-
data_formatstringNHWC:
NHWCNCHW
8
Const
output"dtype"
valuetensor"
dtypetype
.
Identity

input"T
output"T"	
Ttype
q
MatMul
a"T
b"T
product"T"
transpose_abool( "
transpose_bbool( "
Ttype:

2	
e
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool(?

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
@
ReadVariableOp
resource
value"dtype"
dtypetype?
E
Relu
features"T
activations"T"
Ttype:
2	
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0?
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0?
?
Select
	condition

t"T
e"T
output"T"	
Ttype
H
ShardedFilename
basename	
shard

num_shards
filename
?
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ??
@
StaticRegexFullMatch	
input

output
"
patternstring
N

StringJoin
inputs*N

output"
Nint(0"
	separatorstring 
?
VarHandleOp
resource"
	containerstring "
shared_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 ?"serve*2.7.02v2.7.0-rc1-69-gc256c071bb28??
?
inputlayer/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape:
??*"
shared_nameinputlayer/kernel
y
%inputlayer/kernel/Read/ReadVariableOpReadVariableOpinputlayer/kernel* 
_output_shapes
:
??*
dtype0
w
inputlayer/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:?* 
shared_nameinputlayer/bias
p
#inputlayer/bias/Read/ReadVariableOpReadVariableOpinputlayer/bias*
_output_shapes	
:?*
dtype0
?
hiddenlayer/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape:	?8*#
shared_namehiddenlayer/kernel
z
&hiddenlayer/kernel/Read/ReadVariableOpReadVariableOphiddenlayer/kernel*
_output_shapes
:	?8*
dtype0
x
hiddenlayer/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:8*!
shared_namehiddenlayer/bias
q
$hiddenlayer/bias/Read/ReadVariableOpReadVariableOphiddenlayer/bias*
_output_shapes
:8*
dtype0
?
outputlayer/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
:8*#
shared_nameoutputlayer/kernel
y
&outputlayer/kernel/Read/ReadVariableOpReadVariableOpoutputlayer/kernel*
_output_shapes

:8*
dtype0
x
outputlayer/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:*!
shared_nameoutputlayer/bias
q
$outputlayer/bias/Read/ReadVariableOpReadVariableOpoutputlayer/bias*
_output_shapes
:*
dtype0
f
	Adam/iterVarHandleOp*
_output_shapes
: *
dtype0	*
shape: *
shared_name	Adam/iter
_
Adam/iter/Read/ReadVariableOpReadVariableOp	Adam/iter*
_output_shapes
: *
dtype0	
j
Adam/beta_1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nameAdam/beta_1
c
Adam/beta_1/Read/ReadVariableOpReadVariableOpAdam/beta_1*
_output_shapes
: *
dtype0
j
Adam/beta_2VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nameAdam/beta_2
c
Adam/beta_2/Read/ReadVariableOpReadVariableOpAdam/beta_2*
_output_shapes
: *
dtype0
h

Adam/decayVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name
Adam/decay
a
Adam/decay/Read/ReadVariableOpReadVariableOp
Adam/decay*
_output_shapes
: *
dtype0
x
Adam/learning_rateVarHandleOp*
_output_shapes
: *
dtype0*
shape: *#
shared_nameAdam/learning_rate
q
&Adam/learning_rate/Read/ReadVariableOpReadVariableOpAdam/learning_rate*
_output_shapes
: *
dtype0
^
totalVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nametotal
W
total/Read/ReadVariableOpReadVariableOptotal*
_output_shapes
: *
dtype0
^
countVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_namecount
W
count/Read/ReadVariableOpReadVariableOpcount*
_output_shapes
: *
dtype0
b
total_1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name	total_1
[
total_1/Read/ReadVariableOpReadVariableOptotal_1*
_output_shapes
: *
dtype0
b
count_1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name	count_1
[
count_1/Read/ReadVariableOpReadVariableOpcount_1*
_output_shapes
: *
dtype0
?
Adam/inputlayer/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:
??*)
shared_nameAdam/inputlayer/kernel/m
?
,Adam/inputlayer/kernel/m/Read/ReadVariableOpReadVariableOpAdam/inputlayer/kernel/m* 
_output_shapes
:
??*
dtype0
?
Adam/inputlayer/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:?*'
shared_nameAdam/inputlayer/bias/m
~
*Adam/inputlayer/bias/m/Read/ReadVariableOpReadVariableOpAdam/inputlayer/bias/m*
_output_shapes	
:?*
dtype0
?
Adam/hiddenlayer/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:	?8**
shared_nameAdam/hiddenlayer/kernel/m
?
-Adam/hiddenlayer/kernel/m/Read/ReadVariableOpReadVariableOpAdam/hiddenlayer/kernel/m*
_output_shapes
:	?8*
dtype0
?
Adam/hiddenlayer/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:8*(
shared_nameAdam/hiddenlayer/bias/m

+Adam/hiddenlayer/bias/m/Read/ReadVariableOpReadVariableOpAdam/hiddenlayer/bias/m*
_output_shapes
:8*
dtype0
?
Adam/outputlayer/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape
:8**
shared_nameAdam/outputlayer/kernel/m
?
-Adam/outputlayer/kernel/m/Read/ReadVariableOpReadVariableOpAdam/outputlayer/kernel/m*
_output_shapes

:8*
dtype0
?
Adam/outputlayer/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:*(
shared_nameAdam/outputlayer/bias/m

+Adam/outputlayer/bias/m/Read/ReadVariableOpReadVariableOpAdam/outputlayer/bias/m*
_output_shapes
:*
dtype0
?
Adam/inputlayer/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:
??*)
shared_nameAdam/inputlayer/kernel/v
?
,Adam/inputlayer/kernel/v/Read/ReadVariableOpReadVariableOpAdam/inputlayer/kernel/v* 
_output_shapes
:
??*
dtype0
?
Adam/inputlayer/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:?*'
shared_nameAdam/inputlayer/bias/v
~
*Adam/inputlayer/bias/v/Read/ReadVariableOpReadVariableOpAdam/inputlayer/bias/v*
_output_shapes	
:?*
dtype0
?
Adam/hiddenlayer/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:	?8**
shared_nameAdam/hiddenlayer/kernel/v
?
-Adam/hiddenlayer/kernel/v/Read/ReadVariableOpReadVariableOpAdam/hiddenlayer/kernel/v*
_output_shapes
:	?8*
dtype0
?
Adam/hiddenlayer/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:8*(
shared_nameAdam/hiddenlayer/bias/v

+Adam/hiddenlayer/bias/v/Read/ReadVariableOpReadVariableOpAdam/hiddenlayer/bias/v*
_output_shapes
:8*
dtype0
?
Adam/outputlayer/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape
:8**
shared_nameAdam/outputlayer/kernel/v
?
-Adam/outputlayer/kernel/v/Read/ReadVariableOpReadVariableOpAdam/outputlayer/kernel/v*
_output_shapes

:8*
dtype0
?
Adam/outputlayer/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:*(
shared_nameAdam/outputlayer/bias/v

+Adam/outputlayer/bias/v/Read/ReadVariableOpReadVariableOpAdam/outputlayer/bias/v*
_output_shapes
:*
dtype0

NoOpNoOp
?&
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*?&
value?&B?& B?&
?
layer_with_weights-0
layer-0
layer_with_weights-1
layer-1
layer_with_weights-2
layer-2
	optimizer

signatures
#_self_saveable_object_factories
	variables
trainable_variables
	regularization_losses

	keras_api
?

kernel
bias
#_self_saveable_object_factories
	variables
trainable_variables
regularization_losses
	keras_api
?

kernel
bias
#_self_saveable_object_factories
	variables
trainable_variables
regularization_losses
	keras_api
?

kernel
bias
#_self_saveable_object_factories
	variables
trainable_variables
regularization_losses
	keras_api
?
 iter

!beta_1

"beta_2
	#decay
$learning_ratemDmEmFmGmHmIvJvKvLvMvNvO
 
 
*
0
1
2
3
4
5
*
0
1
2
3
4
5
 
?
%non_trainable_variables

&layers
'metrics
(layer_regularization_losses
)layer_metrics
	variables
trainable_variables
	regularization_losses
][
VARIABLE_VALUEinputlayer/kernel6layer_with_weights-0/kernel/.ATTRIBUTES/VARIABLE_VALUE
YW
VARIABLE_VALUEinputlayer/bias4layer_with_weights-0/bias/.ATTRIBUTES/VARIABLE_VALUE
 

0
1

0
1
 
?
*non_trainable_variables

+layers
,metrics
-layer_regularization_losses
.layer_metrics
	variables
trainable_variables
regularization_losses
^\
VARIABLE_VALUEhiddenlayer/kernel6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUE
ZX
VARIABLE_VALUEhiddenlayer/bias4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUE
 

0
1

0
1
 
?
/non_trainable_variables

0layers
1metrics
2layer_regularization_losses
3layer_metrics
	variables
trainable_variables
regularization_losses
^\
VARIABLE_VALUEoutputlayer/kernel6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUE
ZX
VARIABLE_VALUEoutputlayer/bias4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUE
 

0
1

0
1
 
?
4non_trainable_variables

5layers
6metrics
7layer_regularization_losses
8layer_metrics
	variables
trainable_variables
regularization_losses
HF
VARIABLE_VALUE	Adam/iter)optimizer/iter/.ATTRIBUTES/VARIABLE_VALUE
LJ
VARIABLE_VALUEAdam/beta_1+optimizer/beta_1/.ATTRIBUTES/VARIABLE_VALUE
LJ
VARIABLE_VALUEAdam/beta_2+optimizer/beta_2/.ATTRIBUTES/VARIABLE_VALUE
JH
VARIABLE_VALUE
Adam/decay*optimizer/decay/.ATTRIBUTES/VARIABLE_VALUE
ZX
VARIABLE_VALUEAdam/learning_rate2optimizer/learning_rate/.ATTRIBUTES/VARIABLE_VALUE
 

0
1
2

90
:1
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
4
	;total
	<count
=	variables
>	keras_api
D
	?total
	@count
A
_fn_kwargs
B	variables
C	keras_api
OM
VARIABLE_VALUEtotal4keras_api/metrics/0/total/.ATTRIBUTES/VARIABLE_VALUE
OM
VARIABLE_VALUEcount4keras_api/metrics/0/count/.ATTRIBUTES/VARIABLE_VALUE

;0
<1

=	variables
QO
VARIABLE_VALUEtotal_14keras_api/metrics/1/total/.ATTRIBUTES/VARIABLE_VALUE
QO
VARIABLE_VALUEcount_14keras_api/metrics/1/count/.ATTRIBUTES/VARIABLE_VALUE
 

?0
@1

B	variables
?~
VARIABLE_VALUEAdam/inputlayer/kernel/mRlayer_with_weights-0/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
|z
VARIABLE_VALUEAdam/inputlayer/bias/mPlayer_with_weights-0/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
?
VARIABLE_VALUEAdam/hiddenlayer/kernel/mRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
}{
VARIABLE_VALUEAdam/hiddenlayer/bias/mPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
?
VARIABLE_VALUEAdam/outputlayer/kernel/mRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
}{
VARIABLE_VALUEAdam/outputlayer/bias/mPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
?~
VARIABLE_VALUEAdam/inputlayer/kernel/vRlayer_with_weights-0/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
|z
VARIABLE_VALUEAdam/inputlayer/bias/vPlayer_with_weights-0/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
?
VARIABLE_VALUEAdam/hiddenlayer/kernel/vRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
}{
VARIABLE_VALUEAdam/hiddenlayer/bias/vPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
?
VARIABLE_VALUEAdam/outputlayer/kernel/vRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
}{
VARIABLE_VALUEAdam/outputlayer/bias/vPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
s
 serving_default_inputlayer_inputPlaceholder*
_output_shapes
:	?*
dtype0*
shape:	?
?
StatefulPartitionedCallStatefulPartitionedCall serving_default_inputlayer_inputinputlayer/kernelinputlayer/biashiddenlayer/kernelhiddenlayer/biasoutputlayer/kerneloutputlayer/bias*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8? *-
f(R&
$__inference_signature_wrapper_913935
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
?

StatefulPartitionedCall_1StatefulPartitionedCallsaver_filename%inputlayer/kernel/Read/ReadVariableOp#inputlayer/bias/Read/ReadVariableOp&hiddenlayer/kernel/Read/ReadVariableOp$hiddenlayer/bias/Read/ReadVariableOp&outputlayer/kernel/Read/ReadVariableOp$outputlayer/bias/Read/ReadVariableOpAdam/iter/Read/ReadVariableOpAdam/beta_1/Read/ReadVariableOpAdam/beta_2/Read/ReadVariableOpAdam/decay/Read/ReadVariableOp&Adam/learning_rate/Read/ReadVariableOptotal/Read/ReadVariableOpcount/Read/ReadVariableOptotal_1/Read/ReadVariableOpcount_1/Read/ReadVariableOp,Adam/inputlayer/kernel/m/Read/ReadVariableOp*Adam/inputlayer/bias/m/Read/ReadVariableOp-Adam/hiddenlayer/kernel/m/Read/ReadVariableOp+Adam/hiddenlayer/bias/m/Read/ReadVariableOp-Adam/outputlayer/kernel/m/Read/ReadVariableOp+Adam/outputlayer/bias/m/Read/ReadVariableOp,Adam/inputlayer/kernel/v/Read/ReadVariableOp*Adam/inputlayer/bias/v/Read/ReadVariableOp-Adam/hiddenlayer/kernel/v/Read/ReadVariableOp+Adam/hiddenlayer/bias/v/Read/ReadVariableOp-Adam/outputlayer/kernel/v/Read/ReadVariableOp+Adam/outputlayer/bias/v/Read/ReadVariableOpConst*(
Tin!
2	*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *(
f#R!
__inference__traced_save_914180
?
StatefulPartitionedCall_2StatefulPartitionedCallsaver_filenameinputlayer/kernelinputlayer/biashiddenlayer/kernelhiddenlayer/biasoutputlayer/kerneloutputlayer/bias	Adam/iterAdam/beta_1Adam/beta_2
Adam/decayAdam/learning_ratetotalcounttotal_1count_1Adam/inputlayer/kernel/mAdam/inputlayer/bias/mAdam/hiddenlayer/kernel/mAdam/hiddenlayer/bias/mAdam/outputlayer/kernel/mAdam/outputlayer/bias/mAdam/inputlayer/kernel/vAdam/inputlayer/bias/vAdam/hiddenlayer/kernel/vAdam/hiddenlayer/bias/vAdam/outputlayer/kernel/vAdam/outputlayer/bias/v*'
Tin 
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *+
f&R$
"__inference__traced_restore_914271??
?!
?
!__inference__wrapped_model_913699
inputlayer_inputH
4sequential_inputlayer_matmul_readvariableop_resource:
??D
5sequential_inputlayer_biasadd_readvariableop_resource:	?H
5sequential_hiddenlayer_matmul_readvariableop_resource:	?8D
6sequential_hiddenlayer_biasadd_readvariableop_resource:8G
5sequential_outputlayer_matmul_readvariableop_resource:8D
6sequential_outputlayer_biasadd_readvariableop_resource:
identity??-sequential/hiddenlayer/BiasAdd/ReadVariableOp?,sequential/hiddenlayer/MatMul/ReadVariableOp?,sequential/inputlayer/BiasAdd/ReadVariableOp?+sequential/inputlayer/MatMul/ReadVariableOp?-sequential/outputlayer/BiasAdd/ReadVariableOp?,sequential/outputlayer/MatMul/ReadVariableOp?
+sequential/inputlayer/MatMul/ReadVariableOpReadVariableOp4sequential_inputlayer_matmul_readvariableop_resource* 
_output_shapes
:
??*
dtype0?
sequential/inputlayer/MatMulMatMulinputlayer_input3sequential/inputlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes
:	??
,sequential/inputlayer/BiasAdd/ReadVariableOpReadVariableOp5sequential_inputlayer_biasadd_readvariableop_resource*
_output_shapes	
:?*
dtype0?
sequential/inputlayer/BiasAddBiasAdd&sequential/inputlayer/MatMul:product:04sequential/inputlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes
:	??
,sequential/hiddenlayer/MatMul/ReadVariableOpReadVariableOp5sequential_hiddenlayer_matmul_readvariableop_resource*
_output_shapes
:	?8*
dtype0?
sequential/hiddenlayer/MatMulMatMul&sequential/inputlayer/BiasAdd:output:04sequential/hiddenlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:8?
-sequential/hiddenlayer/BiasAdd/ReadVariableOpReadVariableOp6sequential_hiddenlayer_biasadd_readvariableop_resource*
_output_shapes
:8*
dtype0?
sequential/hiddenlayer/BiasAddBiasAdd'sequential/hiddenlayer/MatMul:product:05sequential/hiddenlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:8u
sequential/hiddenlayer/ReluRelu'sequential/hiddenlayer/BiasAdd:output:0*
T0*
_output_shapes

:8?
,sequential/outputlayer/MatMul/ReadVariableOpReadVariableOp5sequential_outputlayer_matmul_readvariableop_resource*
_output_shapes

:8*
dtype0?
sequential/outputlayer/MatMulMatMul)sequential/hiddenlayer/Relu:activations:04sequential/outputlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:?
-sequential/outputlayer/BiasAdd/ReadVariableOpReadVariableOp6sequential_outputlayer_biasadd_readvariableop_resource*
_output_shapes
:*
dtype0?
sequential/outputlayer/BiasAddBiasAdd'sequential/outputlayer/MatMul:product:05sequential/outputlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:u
sequential/outputlayer/ReluRelu'sequential/outputlayer/BiasAdd:output:0*
T0*
_output_shapes

:o
IdentityIdentity)sequential/outputlayer/Relu:activations:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp.^sequential/hiddenlayer/BiasAdd/ReadVariableOp-^sequential/hiddenlayer/MatMul/ReadVariableOp-^sequential/inputlayer/BiasAdd/ReadVariableOp,^sequential/inputlayer/MatMul/ReadVariableOp.^sequential/outputlayer/BiasAdd/ReadVariableOp-^sequential/outputlayer/MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2^
-sequential/hiddenlayer/BiasAdd/ReadVariableOp-sequential/hiddenlayer/BiasAdd/ReadVariableOp2\
,sequential/hiddenlayer/MatMul/ReadVariableOp,sequential/hiddenlayer/MatMul/ReadVariableOp2\
,sequential/inputlayer/BiasAdd/ReadVariableOp,sequential/inputlayer/BiasAdd/ReadVariableOp2Z
+sequential/inputlayer/MatMul/ReadVariableOp+sequential/inputlayer/MatMul/ReadVariableOp2^
-sequential/outputlayer/BiasAdd/ReadVariableOp-sequential/outputlayer/BiasAdd/ReadVariableOp2\
,sequential/outputlayer/MatMul/ReadVariableOp,sequential/outputlayer/MatMul/ReadVariableOp:Q M

_output_shapes
:	?
*
_user_specified_nameinputlayer_input
?	
?
F__inference_inputlayer_layer_call_and_return_conditional_losses_914036

inputs2
matmul_readvariableop_resource:
??.
biasadd_readvariableop_resource:	?
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOpv
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource* 
_output_shapes
:
??*
dtype0a
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*
_output_shapes
:	?s
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes	
:?*
dtype0n
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes
:	?W
IdentityIdentityBiasAdd:output:0^NoOp*
T0*
_output_shapes
:	?w
NoOpNoOp^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*"
_input_shapes
:	?: : 20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
+__inference_sequential_layer_call_fn_913772
inputlayer_input
unknown:
??
	unknown_0:	?
	unknown_1:	?8
	unknown_2:8
	unknown_3:8
	unknown_4:
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputlayer_inputunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_sequential_layer_call_and_return_conditional_losses_913757f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:Q M

_output_shapes
:	?
*
_user_specified_nameinputlayer_input
?	
?
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_914056

inputs1
matmul_readvariableop_resource:	?8-
biasadd_readvariableop_resource:8
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOpu
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes
:	?8*
dtype0`
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:8r
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:8*
dtype0m
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:8G
ReluReluBiasAdd:output:0*
T0*
_output_shapes

:8X
IdentityIdentityRelu:activations:0^NoOp*
T0*
_output_shapes

:8w
NoOpNoOp^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*"
_input_shapes
:	?: : 20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?	
?
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_913733

inputs1
matmul_readvariableop_resource:	?8-
biasadd_readvariableop_resource:8
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOpu
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes
:	?8*
dtype0`
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:8r
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:8*
dtype0m
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:8G
ReluReluBiasAdd:output:0*
T0*
_output_shapes

:8X
IdentityIdentityRelu:activations:0^NoOp*
T0*
_output_shapes

:8w
NoOpNoOp^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*"
_input_shapes
:	?: : 20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
F__inference_sequential_layer_call_and_return_conditional_losses_913993

inputs=
)inputlayer_matmul_readvariableop_resource:
??9
*inputlayer_biasadd_readvariableop_resource:	?=
*hiddenlayer_matmul_readvariableop_resource:	?89
+hiddenlayer_biasadd_readvariableop_resource:8<
*outputlayer_matmul_readvariableop_resource:89
+outputlayer_biasadd_readvariableop_resource:
identity??"hiddenlayer/BiasAdd/ReadVariableOp?!hiddenlayer/MatMul/ReadVariableOp?!inputlayer/BiasAdd/ReadVariableOp? inputlayer/MatMul/ReadVariableOp?"outputlayer/BiasAdd/ReadVariableOp?!outputlayer/MatMul/ReadVariableOp?
 inputlayer/MatMul/ReadVariableOpReadVariableOp)inputlayer_matmul_readvariableop_resource* 
_output_shapes
:
??*
dtype0w
inputlayer/MatMulMatMulinputs(inputlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes
:	??
!inputlayer/BiasAdd/ReadVariableOpReadVariableOp*inputlayer_biasadd_readvariableop_resource*
_output_shapes	
:?*
dtype0?
inputlayer/BiasAddBiasAddinputlayer/MatMul:product:0)inputlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes
:	??
!hiddenlayer/MatMul/ReadVariableOpReadVariableOp*hiddenlayer_matmul_readvariableop_resource*
_output_shapes
:	?8*
dtype0?
hiddenlayer/MatMulMatMulinputlayer/BiasAdd:output:0)hiddenlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:8?
"hiddenlayer/BiasAdd/ReadVariableOpReadVariableOp+hiddenlayer_biasadd_readvariableop_resource*
_output_shapes
:8*
dtype0?
hiddenlayer/BiasAddBiasAddhiddenlayer/MatMul:product:0*hiddenlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:8_
hiddenlayer/ReluReluhiddenlayer/BiasAdd:output:0*
T0*
_output_shapes

:8?
!outputlayer/MatMul/ReadVariableOpReadVariableOp*outputlayer_matmul_readvariableop_resource*
_output_shapes

:8*
dtype0?
outputlayer/MatMulMatMulhiddenlayer/Relu:activations:0)outputlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:?
"outputlayer/BiasAdd/ReadVariableOpReadVariableOp+outputlayer_biasadd_readvariableop_resource*
_output_shapes
:*
dtype0?
outputlayer/BiasAddBiasAddoutputlayer/MatMul:product:0*outputlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:_
outputlayer/ReluReluoutputlayer/BiasAdd:output:0*
T0*
_output_shapes

:d
IdentityIdentityoutputlayer/Relu:activations:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp#^hiddenlayer/BiasAdd/ReadVariableOp"^hiddenlayer/MatMul/ReadVariableOp"^inputlayer/BiasAdd/ReadVariableOp!^inputlayer/MatMul/ReadVariableOp#^outputlayer/BiasAdd/ReadVariableOp"^outputlayer/MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2H
"hiddenlayer/BiasAdd/ReadVariableOp"hiddenlayer/BiasAdd/ReadVariableOp2F
!hiddenlayer/MatMul/ReadVariableOp!hiddenlayer/MatMul/ReadVariableOp2F
!inputlayer/BiasAdd/ReadVariableOp!inputlayer/BiasAdd/ReadVariableOp2D
 inputlayer/MatMul/ReadVariableOp inputlayer/MatMul/ReadVariableOp2H
"outputlayer/BiasAdd/ReadVariableOp"outputlayer/BiasAdd/ReadVariableOp2F
!outputlayer/MatMul/ReadVariableOp!outputlayer/MatMul/ReadVariableOp:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
,__inference_hiddenlayer_layer_call_fn_914045

inputs
unknown:	?8
	unknown_0:8
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:8*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_913733f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:8`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*"
_input_shapes
:	?: : 22
StatefulPartitionedCallStatefulPartitionedCall:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
+__inference_sequential_layer_call_fn_913952

inputs
unknown:
??
	unknown_0:	?
	unknown_1:	?8
	unknown_2:8
	unknown_3:8
	unknown_4:
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_sequential_layer_call_and_return_conditional_losses_913757f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
F__inference_sequential_layer_call_and_return_conditional_losses_914017

inputs=
)inputlayer_matmul_readvariableop_resource:
??9
*inputlayer_biasadd_readvariableop_resource:	?=
*hiddenlayer_matmul_readvariableop_resource:	?89
+hiddenlayer_biasadd_readvariableop_resource:8<
*outputlayer_matmul_readvariableop_resource:89
+outputlayer_biasadd_readvariableop_resource:
identity??"hiddenlayer/BiasAdd/ReadVariableOp?!hiddenlayer/MatMul/ReadVariableOp?!inputlayer/BiasAdd/ReadVariableOp? inputlayer/MatMul/ReadVariableOp?"outputlayer/BiasAdd/ReadVariableOp?!outputlayer/MatMul/ReadVariableOp?
 inputlayer/MatMul/ReadVariableOpReadVariableOp)inputlayer_matmul_readvariableop_resource* 
_output_shapes
:
??*
dtype0w
inputlayer/MatMulMatMulinputs(inputlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes
:	??
!inputlayer/BiasAdd/ReadVariableOpReadVariableOp*inputlayer_biasadd_readvariableop_resource*
_output_shapes	
:?*
dtype0?
inputlayer/BiasAddBiasAddinputlayer/MatMul:product:0)inputlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes
:	??
!hiddenlayer/MatMul/ReadVariableOpReadVariableOp*hiddenlayer_matmul_readvariableop_resource*
_output_shapes
:	?8*
dtype0?
hiddenlayer/MatMulMatMulinputlayer/BiasAdd:output:0)hiddenlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:8?
"hiddenlayer/BiasAdd/ReadVariableOpReadVariableOp+hiddenlayer_biasadd_readvariableop_resource*
_output_shapes
:8*
dtype0?
hiddenlayer/BiasAddBiasAddhiddenlayer/MatMul:product:0*hiddenlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:8_
hiddenlayer/ReluReluhiddenlayer/BiasAdd:output:0*
T0*
_output_shapes

:8?
!outputlayer/MatMul/ReadVariableOpReadVariableOp*outputlayer_matmul_readvariableop_resource*
_output_shapes

:8*
dtype0?
outputlayer/MatMulMatMulhiddenlayer/Relu:activations:0)outputlayer/MatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:?
"outputlayer/BiasAdd/ReadVariableOpReadVariableOp+outputlayer_biasadd_readvariableop_resource*
_output_shapes
:*
dtype0?
outputlayer/BiasAddBiasAddoutputlayer/MatMul:product:0*outputlayer/BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:_
outputlayer/ReluReluoutputlayer/BiasAdd:output:0*
T0*
_output_shapes

:d
IdentityIdentityoutputlayer/Relu:activations:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp#^hiddenlayer/BiasAdd/ReadVariableOp"^hiddenlayer/MatMul/ReadVariableOp"^inputlayer/BiasAdd/ReadVariableOp!^inputlayer/MatMul/ReadVariableOp#^outputlayer/BiasAdd/ReadVariableOp"^outputlayer/MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2H
"hiddenlayer/BiasAdd/ReadVariableOp"hiddenlayer/BiasAdd/ReadVariableOp2F
!hiddenlayer/MatMul/ReadVariableOp!hiddenlayer/MatMul/ReadVariableOp2F
!inputlayer/BiasAdd/ReadVariableOp!inputlayer/BiasAdd/ReadVariableOp2D
 inputlayer/MatMul/ReadVariableOp inputlayer/MatMul/ReadVariableOp2H
"outputlayer/BiasAdd/ReadVariableOp"outputlayer/BiasAdd/ReadVariableOp2F
!outputlayer/MatMul/ReadVariableOp!outputlayer/MatMul/ReadVariableOp:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?	
?
G__inference_outputlayer_layer_call_and_return_conditional_losses_913750

inputs0
matmul_readvariableop_resource:8-
biasadd_readvariableop_resource:
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOpt
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

:8*
dtype0`
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:r
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype0m
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:G
ReluReluBiasAdd:output:0*
T0*
_output_shapes

:X
IdentityIdentityRelu:activations:0^NoOp*
T0*
_output_shapes

:w
NoOpNoOp^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*!
_input_shapes
:8: : 20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:F B

_output_shapes

:8
 
_user_specified_nameinputs
?
?
+__inference_sequential_layer_call_fn_913969

inputs
unknown:
??
	unknown_0:	?
	unknown_1:	?8
	unknown_2:8
	unknown_3:8
	unknown_4:
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_sequential_layer_call_and_return_conditional_losses_913840f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
+__inference_inputlayer_layer_call_fn_914026

inputs
unknown:
??
	unknown_0:	?
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
:	?*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_inputlayer_layer_call_and_return_conditional_losses_913716g
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes
:	?`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*"
_input_shapes
:	?: : 22
StatefulPartitionedCallStatefulPartitionedCall:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
F__inference_sequential_layer_call_and_return_conditional_losses_913891
inputlayer_input%
inputlayer_913875:
?? 
inputlayer_913877:	?%
hiddenlayer_913880:	?8 
hiddenlayer_913882:8$
outputlayer_913885:8 
outputlayer_913887:
identity??#hiddenlayer/StatefulPartitionedCall?"inputlayer/StatefulPartitionedCall?#outputlayer/StatefulPartitionedCall?
"inputlayer/StatefulPartitionedCallStatefulPartitionedCallinputlayer_inputinputlayer_913875inputlayer_913877*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
:	?*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_inputlayer_layer_call_and_return_conditional_losses_913716?
#hiddenlayer/StatefulPartitionedCallStatefulPartitionedCall+inputlayer/StatefulPartitionedCall:output:0hiddenlayer_913880hiddenlayer_913882*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:8*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_913733?
#outputlayer/StatefulPartitionedCallStatefulPartitionedCall,hiddenlayer/StatefulPartitionedCall:output:0outputlayer_913885outputlayer_913887*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_outputlayer_layer_call_and_return_conditional_losses_913750r
IdentityIdentity,outputlayer/StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp$^hiddenlayer/StatefulPartitionedCall#^inputlayer/StatefulPartitionedCall$^outputlayer/StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2J
#hiddenlayer/StatefulPartitionedCall#hiddenlayer/StatefulPartitionedCall2H
"inputlayer/StatefulPartitionedCall"inputlayer/StatefulPartitionedCall2J
#outputlayer/StatefulPartitionedCall#outputlayer/StatefulPartitionedCall:Q M

_output_shapes
:	?
*
_user_specified_nameinputlayer_input
?
?
F__inference_sequential_layer_call_and_return_conditional_losses_913910
inputlayer_input%
inputlayer_913894:
?? 
inputlayer_913896:	?%
hiddenlayer_913899:	?8 
hiddenlayer_913901:8$
outputlayer_913904:8 
outputlayer_913906:
identity??#hiddenlayer/StatefulPartitionedCall?"inputlayer/StatefulPartitionedCall?#outputlayer/StatefulPartitionedCall?
"inputlayer/StatefulPartitionedCallStatefulPartitionedCallinputlayer_inputinputlayer_913894inputlayer_913896*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
:	?*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_inputlayer_layer_call_and_return_conditional_losses_913716?
#hiddenlayer/StatefulPartitionedCallStatefulPartitionedCall+inputlayer/StatefulPartitionedCall:output:0hiddenlayer_913899hiddenlayer_913901*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:8*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_913733?
#outputlayer/StatefulPartitionedCallStatefulPartitionedCall,hiddenlayer/StatefulPartitionedCall:output:0outputlayer_913904outputlayer_913906*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_outputlayer_layer_call_and_return_conditional_losses_913750r
IdentityIdentity,outputlayer/StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp$^hiddenlayer/StatefulPartitionedCall#^inputlayer/StatefulPartitionedCall$^outputlayer/StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2J
#hiddenlayer/StatefulPartitionedCall#hiddenlayer/StatefulPartitionedCall2H
"inputlayer/StatefulPartitionedCall"inputlayer/StatefulPartitionedCall2J
#outputlayer/StatefulPartitionedCall#outputlayer/StatefulPartitionedCall:Q M

_output_shapes
:	?
*
_user_specified_nameinputlayer_input
?
?
,__inference_outputlayer_layer_call_fn_914065

inputs
unknown:8
	unknown_0:
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_outputlayer_layer_call_and_return_conditional_losses_913750f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*!
_input_shapes
:8: : 22
StatefulPartitionedCallStatefulPartitionedCall:F B

_output_shapes

:8
 
_user_specified_nameinputs
?m
?
"__inference__traced_restore_914271
file_prefix6
"assignvariableop_inputlayer_kernel:
??1
"assignvariableop_1_inputlayer_bias:	?8
%assignvariableop_2_hiddenlayer_kernel:	?81
#assignvariableop_3_hiddenlayer_bias:87
%assignvariableop_4_outputlayer_kernel:81
#assignvariableop_5_outputlayer_bias:&
assignvariableop_6_adam_iter:	 (
assignvariableop_7_adam_beta_1: (
assignvariableop_8_adam_beta_2: '
assignvariableop_9_adam_decay: 0
&assignvariableop_10_adam_learning_rate: #
assignvariableop_11_total: #
assignvariableop_12_count: %
assignvariableop_13_total_1: %
assignvariableop_14_count_1: @
,assignvariableop_15_adam_inputlayer_kernel_m:
??9
*assignvariableop_16_adam_inputlayer_bias_m:	?@
-assignvariableop_17_adam_hiddenlayer_kernel_m:	?89
+assignvariableop_18_adam_hiddenlayer_bias_m:8?
-assignvariableop_19_adam_outputlayer_kernel_m:89
+assignvariableop_20_adam_outputlayer_bias_m:@
,assignvariableop_21_adam_inputlayer_kernel_v:
??9
*assignvariableop_22_adam_inputlayer_bias_v:	?@
-assignvariableop_23_adam_hiddenlayer_kernel_v:	?89
+assignvariableop_24_adam_hiddenlayer_bias_v:8?
-assignvariableop_25_adam_outputlayer_kernel_v:89
+assignvariableop_26_adam_outputlayer_bias_v:
identity_28??AssignVariableOp?AssignVariableOp_1?AssignVariableOp_10?AssignVariableOp_11?AssignVariableOp_12?AssignVariableOp_13?AssignVariableOp_14?AssignVariableOp_15?AssignVariableOp_16?AssignVariableOp_17?AssignVariableOp_18?AssignVariableOp_19?AssignVariableOp_2?AssignVariableOp_20?AssignVariableOp_21?AssignVariableOp_22?AssignVariableOp_23?AssignVariableOp_24?AssignVariableOp_25?AssignVariableOp_26?AssignVariableOp_3?AssignVariableOp_4?AssignVariableOp_5?AssignVariableOp_6?AssignVariableOp_7?AssignVariableOp_8?AssignVariableOp_9?
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*?
value?B?B6layer_with_weights-0/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-0/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUEB)optimizer/iter/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_1/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_2/.ATTRIBUTES/VARIABLE_VALUEB*optimizer/decay/.ATTRIBUTES/VARIABLE_VALUEB2optimizer/learning_rate/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/count/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/count/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-0/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-0/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-0/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-0/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH?
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*K
valueBB@B B B B B B B B B B B B B B B B B B B B B B B B B B B B ?
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*?
_output_shapesr
p::::::::::::::::::::::::::::**
dtypes 
2	[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOpAssignVariableOp"assignvariableop_inputlayer_kernelIdentity:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_1AssignVariableOp"assignvariableop_1_inputlayer_biasIdentity_1:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_2AssignVariableOp%assignvariableop_2_hiddenlayer_kernelIdentity_2:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_3IdentityRestoreV2:tensors:3"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_3AssignVariableOp#assignvariableop_3_hiddenlayer_biasIdentity_3:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_4IdentityRestoreV2:tensors:4"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_4AssignVariableOp%assignvariableop_4_outputlayer_kernelIdentity_4:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_5IdentityRestoreV2:tensors:5"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_5AssignVariableOp#assignvariableop_5_outputlayer_biasIdentity_5:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_6IdentityRestoreV2:tensors:6"/device:CPU:0*
T0	*
_output_shapes
:?
AssignVariableOp_6AssignVariableOpassignvariableop_6_adam_iterIdentity_6:output:0"/device:CPU:0*
_output_shapes
 *
dtype0	]

Identity_7IdentityRestoreV2:tensors:7"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_7AssignVariableOpassignvariableop_7_adam_beta_1Identity_7:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_8IdentityRestoreV2:tensors:8"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_8AssignVariableOpassignvariableop_8_adam_beta_2Identity_8:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_9IdentityRestoreV2:tensors:9"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_9AssignVariableOpassignvariableop_9_adam_decayIdentity_9:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_10IdentityRestoreV2:tensors:10"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_10AssignVariableOp&assignvariableop_10_adam_learning_rateIdentity_10:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_11IdentityRestoreV2:tensors:11"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_11AssignVariableOpassignvariableop_11_totalIdentity_11:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_12IdentityRestoreV2:tensors:12"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_12AssignVariableOpassignvariableop_12_countIdentity_12:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_13IdentityRestoreV2:tensors:13"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_13AssignVariableOpassignvariableop_13_total_1Identity_13:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_14IdentityRestoreV2:tensors:14"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_14AssignVariableOpassignvariableop_14_count_1Identity_14:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_15IdentityRestoreV2:tensors:15"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_15AssignVariableOp,assignvariableop_15_adam_inputlayer_kernel_mIdentity_15:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_16IdentityRestoreV2:tensors:16"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_16AssignVariableOp*assignvariableop_16_adam_inputlayer_bias_mIdentity_16:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_17IdentityRestoreV2:tensors:17"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_17AssignVariableOp-assignvariableop_17_adam_hiddenlayer_kernel_mIdentity_17:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_18IdentityRestoreV2:tensors:18"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_18AssignVariableOp+assignvariableop_18_adam_hiddenlayer_bias_mIdentity_18:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_19IdentityRestoreV2:tensors:19"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_19AssignVariableOp-assignvariableop_19_adam_outputlayer_kernel_mIdentity_19:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_20IdentityRestoreV2:tensors:20"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_20AssignVariableOp+assignvariableop_20_adam_outputlayer_bias_mIdentity_20:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_21IdentityRestoreV2:tensors:21"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_21AssignVariableOp,assignvariableop_21_adam_inputlayer_kernel_vIdentity_21:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_22IdentityRestoreV2:tensors:22"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_22AssignVariableOp*assignvariableop_22_adam_inputlayer_bias_vIdentity_22:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_23IdentityRestoreV2:tensors:23"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_23AssignVariableOp-assignvariableop_23_adam_hiddenlayer_kernel_vIdentity_23:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_24IdentityRestoreV2:tensors:24"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_24AssignVariableOp+assignvariableop_24_adam_hiddenlayer_bias_vIdentity_24:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_25IdentityRestoreV2:tensors:25"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_25AssignVariableOp-assignvariableop_25_adam_outputlayer_kernel_vIdentity_25:output:0"/device:CPU:0*
_output_shapes
 *
dtype0_
Identity_26IdentityRestoreV2:tensors:26"/device:CPU:0*
T0*
_output_shapes
:?
AssignVariableOp_26AssignVariableOp+assignvariableop_26_adam_outputlayer_bias_vIdentity_26:output:0"/device:CPU:0*
_output_shapes
 *
dtype01
NoOpNoOp"/device:CPU:0*
_output_shapes
 ?
Identity_27Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_11^AssignVariableOp_12^AssignVariableOp_13^AssignVariableOp_14^AssignVariableOp_15^AssignVariableOp_16^AssignVariableOp_17^AssignVariableOp_18^AssignVariableOp_19^AssignVariableOp_2^AssignVariableOp_20^AssignVariableOp_21^AssignVariableOp_22^AssignVariableOp_23^AssignVariableOp_24^AssignVariableOp_25^AssignVariableOp_26^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9^NoOp"/device:CPU:0*
T0*
_output_shapes
: W
Identity_28IdentityIdentity_27:output:0^NoOp_1*
T0*
_output_shapes
: ?
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_11^AssignVariableOp_12^AssignVariableOp_13^AssignVariableOp_14^AssignVariableOp_15^AssignVariableOp_16^AssignVariableOp_17^AssignVariableOp_18^AssignVariableOp_19^AssignVariableOp_2^AssignVariableOp_20^AssignVariableOp_21^AssignVariableOp_22^AssignVariableOp_23^AssignVariableOp_24^AssignVariableOp_25^AssignVariableOp_26^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9*"
_acd_function_control_output(*
_output_shapes
 "#
identity_28Identity_28:output:0*K
_input_shapes:
8: : : : : : : : : : : : : : : : : : : : : : : : : : : : 2$
AssignVariableOpAssignVariableOp2(
AssignVariableOp_1AssignVariableOp_12*
AssignVariableOp_10AssignVariableOp_102*
AssignVariableOp_11AssignVariableOp_112*
AssignVariableOp_12AssignVariableOp_122*
AssignVariableOp_13AssignVariableOp_132*
AssignVariableOp_14AssignVariableOp_142*
AssignVariableOp_15AssignVariableOp_152*
AssignVariableOp_16AssignVariableOp_162*
AssignVariableOp_17AssignVariableOp_172*
AssignVariableOp_18AssignVariableOp_182*
AssignVariableOp_19AssignVariableOp_192(
AssignVariableOp_2AssignVariableOp_22*
AssignVariableOp_20AssignVariableOp_202*
AssignVariableOp_21AssignVariableOp_212*
AssignVariableOp_22AssignVariableOp_222*
AssignVariableOp_23AssignVariableOp_232*
AssignVariableOp_24AssignVariableOp_242*
AssignVariableOp_25AssignVariableOp_252*
AssignVariableOp_26AssignVariableOp_262(
AssignVariableOp_3AssignVariableOp_32(
AssignVariableOp_4AssignVariableOp_42(
AssignVariableOp_5AssignVariableOp_52(
AssignVariableOp_6AssignVariableOp_62(
AssignVariableOp_7AssignVariableOp_72(
AssignVariableOp_8AssignVariableOp_82(
AssignVariableOp_9AssignVariableOp_9:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
?
?
F__inference_sequential_layer_call_and_return_conditional_losses_913840

inputs%
inputlayer_913824:
?? 
inputlayer_913826:	?%
hiddenlayer_913829:	?8 
hiddenlayer_913831:8$
outputlayer_913834:8 
outputlayer_913836:
identity??#hiddenlayer/StatefulPartitionedCall?"inputlayer/StatefulPartitionedCall?#outputlayer/StatefulPartitionedCall?
"inputlayer/StatefulPartitionedCallStatefulPartitionedCallinputsinputlayer_913824inputlayer_913826*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
:	?*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_inputlayer_layer_call_and_return_conditional_losses_913716?
#hiddenlayer/StatefulPartitionedCallStatefulPartitionedCall+inputlayer/StatefulPartitionedCall:output:0hiddenlayer_913829hiddenlayer_913831*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:8*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_913733?
#outputlayer/StatefulPartitionedCallStatefulPartitionedCall,hiddenlayer/StatefulPartitionedCall:output:0outputlayer_913834outputlayer_913836*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_outputlayer_layer_call_and_return_conditional_losses_913750r
IdentityIdentity,outputlayer/StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp$^hiddenlayer/StatefulPartitionedCall#^inputlayer/StatefulPartitionedCall$^outputlayer/StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2J
#hiddenlayer/StatefulPartitionedCall#hiddenlayer/StatefulPartitionedCall2H
"inputlayer/StatefulPartitionedCall"inputlayer/StatefulPartitionedCall2J
#outputlayer/StatefulPartitionedCall#outputlayer/StatefulPartitionedCall:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?
?
+__inference_sequential_layer_call_fn_913872
inputlayer_input
unknown:
??
	unknown_0:	?
	unknown_1:	?8
	unknown_2:8
	unknown_3:8
	unknown_4:
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputlayer_inputunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_sequential_layer_call_and_return_conditional_losses_913840f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:Q M

_output_shapes
:	?
*
_user_specified_nameinputlayer_input
?	
?
G__inference_outputlayer_layer_call_and_return_conditional_losses_914076

inputs0
matmul_readvariableop_resource:8-
biasadd_readvariableop_resource:
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOpt
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

:8*
dtype0`
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*
_output_shapes

:r
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype0m
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes

:G
ReluReluBiasAdd:output:0*
T0*
_output_shapes

:X
IdentityIdentityRelu:activations:0^NoOp*
T0*
_output_shapes

:w
NoOpNoOp^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*!
_input_shapes
:8: : 20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:F B

_output_shapes

:8
 
_user_specified_nameinputs
?
?
$__inference_signature_wrapper_913935
inputlayer_input
unknown:
??
	unknown_0:	?
	unknown_1:	?8
	unknown_2:8
	unknown_3:8
	unknown_4:
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputlayer_inputunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8? **
f%R#
!__inference__wrapped_model_913699f
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:Q M

_output_shapes
:	?
*
_user_specified_nameinputlayer_input
?
?
F__inference_sequential_layer_call_and_return_conditional_losses_913757

inputs%
inputlayer_913717:
?? 
inputlayer_913719:	?%
hiddenlayer_913734:	?8 
hiddenlayer_913736:8$
outputlayer_913751:8 
outputlayer_913753:
identity??#hiddenlayer/StatefulPartitionedCall?"inputlayer/StatefulPartitionedCall?#outputlayer/StatefulPartitionedCall?
"inputlayer/StatefulPartitionedCallStatefulPartitionedCallinputsinputlayer_913717inputlayer_913719*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
:	?*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *O
fJRH
F__inference_inputlayer_layer_call_and_return_conditional_losses_913716?
#hiddenlayer/StatefulPartitionedCallStatefulPartitionedCall+inputlayer/StatefulPartitionedCall:output:0hiddenlayer_913734hiddenlayer_913736*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:8*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_913733?
#outputlayer/StatefulPartitionedCallStatefulPartitionedCall,hiddenlayer/StatefulPartitionedCall:output:0outputlayer_913751outputlayer_913753*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes

:*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *P
fKRI
G__inference_outputlayer_layer_call_and_return_conditional_losses_913750r
IdentityIdentity,outputlayer/StatefulPartitionedCall:output:0^NoOp*
T0*
_output_shapes

:?
NoOpNoOp$^hiddenlayer/StatefulPartitionedCall#^inputlayer/StatefulPartitionedCall$^outputlayer/StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:	?: : : : : : 2J
#hiddenlayer/StatefulPartitionedCall#hiddenlayer/StatefulPartitionedCall2H
"inputlayer/StatefulPartitionedCall"inputlayer/StatefulPartitionedCall2J
#outputlayer/StatefulPartitionedCall#outputlayer/StatefulPartitionedCall:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?	
?
F__inference_inputlayer_layer_call_and_return_conditional_losses_913716

inputs2
matmul_readvariableop_resource:
??.
biasadd_readvariableop_resource:	?
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOpv
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource* 
_output_shapes
:
??*
dtype0a
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*
_output_shapes
:	?s
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes	
:?*
dtype0n
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*
_output_shapes
:	?W
IdentityIdentityBiasAdd:output:0^NoOp*
T0*
_output_shapes
:	?w
NoOpNoOp^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*"
_input_shapes
:	?: : 20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:G C

_output_shapes
:	?
 
_user_specified_nameinputs
?<
?
__inference__traced_save_914180
file_prefix0
,savev2_inputlayer_kernel_read_readvariableop.
*savev2_inputlayer_bias_read_readvariableop1
-savev2_hiddenlayer_kernel_read_readvariableop/
+savev2_hiddenlayer_bias_read_readvariableop1
-savev2_outputlayer_kernel_read_readvariableop/
+savev2_outputlayer_bias_read_readvariableop(
$savev2_adam_iter_read_readvariableop	*
&savev2_adam_beta_1_read_readvariableop*
&savev2_adam_beta_2_read_readvariableop)
%savev2_adam_decay_read_readvariableop1
-savev2_adam_learning_rate_read_readvariableop$
 savev2_total_read_readvariableop$
 savev2_count_read_readvariableop&
"savev2_total_1_read_readvariableop&
"savev2_count_1_read_readvariableop7
3savev2_adam_inputlayer_kernel_m_read_readvariableop5
1savev2_adam_inputlayer_bias_m_read_readvariableop8
4savev2_adam_hiddenlayer_kernel_m_read_readvariableop6
2savev2_adam_hiddenlayer_bias_m_read_readvariableop8
4savev2_adam_outputlayer_kernel_m_read_readvariableop6
2savev2_adam_outputlayer_bias_m_read_readvariableop7
3savev2_adam_inputlayer_kernel_v_read_readvariableop5
1savev2_adam_inputlayer_bias_v_read_readvariableop8
4savev2_adam_hiddenlayer_kernel_v_read_readvariableop6
2savev2_adam_hiddenlayer_bias_v_read_readvariableop8
4savev2_adam_outputlayer_kernel_v_read_readvariableop6
2savev2_adam_outputlayer_bias_v_read_readvariableop
savev2_const

identity_1??MergeV2Checkpointsw
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*Z
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.parta
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part?
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: f

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: L

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :f
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : ?
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: ?
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*?
value?B?B6layer_with_weights-0/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-0/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUEB)optimizer/iter/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_1/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_2/.ATTRIBUTES/VARIABLE_VALUEB*optimizer/decay/.ATTRIBUTES/VARIABLE_VALUEB2optimizer/learning_rate/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/count/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/count/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-0/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-0/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-0/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-0/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH?
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*K
valueBB@B B B B B B B B B B B B B B B B B B B B B B B B B B B B ?
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0,savev2_inputlayer_kernel_read_readvariableop*savev2_inputlayer_bias_read_readvariableop-savev2_hiddenlayer_kernel_read_readvariableop+savev2_hiddenlayer_bias_read_readvariableop-savev2_outputlayer_kernel_read_readvariableop+savev2_outputlayer_bias_read_readvariableop$savev2_adam_iter_read_readvariableop&savev2_adam_beta_1_read_readvariableop&savev2_adam_beta_2_read_readvariableop%savev2_adam_decay_read_readvariableop-savev2_adam_learning_rate_read_readvariableop savev2_total_read_readvariableop savev2_count_read_readvariableop"savev2_total_1_read_readvariableop"savev2_count_1_read_readvariableop3savev2_adam_inputlayer_kernel_m_read_readvariableop1savev2_adam_inputlayer_bias_m_read_readvariableop4savev2_adam_hiddenlayer_kernel_m_read_readvariableop2savev2_adam_hiddenlayer_bias_m_read_readvariableop4savev2_adam_outputlayer_kernel_m_read_readvariableop2savev2_adam_outputlayer_bias_m_read_readvariableop3savev2_adam_inputlayer_kernel_v_read_readvariableop1savev2_adam_inputlayer_bias_v_read_readvariableop4savev2_adam_hiddenlayer_kernel_v_read_readvariableop2savev2_adam_hiddenlayer_bias_v_read_readvariableop4savev2_adam_outputlayer_kernel_v_read_readvariableop2savev2_adam_outputlayer_bias_v_read_readvariableopsavev2_const"/device:CPU:0*
_output_shapes
 **
dtypes 
2	?
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:?
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*
_output_shapes
 f
IdentityIdentityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: Q

Identity_1IdentityIdentity:output:0^NoOp*
T0*
_output_shapes
: [
NoOpNoOp^MergeV2Checkpoints*"
_acd_function_control_output(*
_output_shapes
 "!

identity_1Identity_1:output:0*?
_input_shapes?
?: :
??:?:	?8:8:8:: : : : : : : : : :
??:?:	?8:8:8::
??:?:	?8:8:8:: 2(
MergeV2CheckpointsMergeV2Checkpoints:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix:&"
 
_output_shapes
:
??:!

_output_shapes	
:?:%!

_output_shapes
:	?8: 

_output_shapes
:8:$ 

_output_shapes

:8: 

_output_shapes
::

_output_shapes
: :

_output_shapes
: :	

_output_shapes
: :


_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :&"
 
_output_shapes
:
??:!

_output_shapes	
:?:%!

_output_shapes
:	?8: 

_output_shapes
:8:$ 

_output_shapes

:8: 

_output_shapes
::&"
 
_output_shapes
:
??:!

_output_shapes	
:?:%!

_output_shapes
:	?8: 

_output_shapes
:8:$ 

_output_shapes

:8: 

_output_shapes
::

_output_shapes
: "?L
saver_filename:0StatefulPartitionedCall_1:0StatefulPartitionedCall_28"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp*?
serving_default?
E
inputlayer_input1
"serving_default_inputlayer_input:0	?6
outputlayer'
StatefulPartitionedCall:0tensorflow/serving/predict:?P
?
layer_with_weights-0
layer-0
layer_with_weights-1
layer-1
layer_with_weights-2
layer-2
	optimizer

signatures
#_self_saveable_object_factories
	variables
trainable_variables
	regularization_losses

	keras_api
P__call__
*Q&call_and_return_all_conditional_losses
R_default_save_signature"
_tf_keras_sequential
?

kernel
bias
#_self_saveable_object_factories
	variables
trainable_variables
regularization_losses
	keras_api
S__call__
*T&call_and_return_all_conditional_losses"
_tf_keras_layer
?

kernel
bias
#_self_saveable_object_factories
	variables
trainable_variables
regularization_losses
	keras_api
U__call__
*V&call_and_return_all_conditional_losses"
_tf_keras_layer
?

kernel
bias
#_self_saveable_object_factories
	variables
trainable_variables
regularization_losses
	keras_api
W__call__
*X&call_and_return_all_conditional_losses"
_tf_keras_layer
?
 iter

!beta_1

"beta_2
	#decay
$learning_ratemDmEmFmGmHmIvJvKvLvMvNvO"
	optimizer
,
Yserving_default"
signature_map
 "
trackable_dict_wrapper
J
0
1
2
3
4
5"
trackable_list_wrapper
J
0
1
2
3
4
5"
trackable_list_wrapper
 "
trackable_list_wrapper
?
%non_trainable_variables

&layers
'metrics
(layer_regularization_losses
)layer_metrics
	variables
trainable_variables
	regularization_losses
P__call__
R_default_save_signature
*Q&call_and_return_all_conditional_losses
&Q"call_and_return_conditional_losses"
_generic_user_object
%:#
??2inputlayer/kernel
:?2inputlayer/bias
 "
trackable_dict_wrapper
.
0
1"
trackable_list_wrapper
.
0
1"
trackable_list_wrapper
 "
trackable_list_wrapper
?
*non_trainable_variables

+layers
,metrics
-layer_regularization_losses
.layer_metrics
	variables
trainable_variables
regularization_losses
S__call__
*T&call_and_return_all_conditional_losses
&T"call_and_return_conditional_losses"
_generic_user_object
%:#	?82hiddenlayer/kernel
:82hiddenlayer/bias
 "
trackable_dict_wrapper
.
0
1"
trackable_list_wrapper
.
0
1"
trackable_list_wrapper
 "
trackable_list_wrapper
?
/non_trainable_variables

0layers
1metrics
2layer_regularization_losses
3layer_metrics
	variables
trainable_variables
regularization_losses
U__call__
*V&call_and_return_all_conditional_losses
&V"call_and_return_conditional_losses"
_generic_user_object
$:"82outputlayer/kernel
:2outputlayer/bias
 "
trackable_dict_wrapper
.
0
1"
trackable_list_wrapper
.
0
1"
trackable_list_wrapper
 "
trackable_list_wrapper
?
4non_trainable_variables

5layers
6metrics
7layer_regularization_losses
8layer_metrics
	variables
trainable_variables
regularization_losses
W__call__
*X&call_and_return_all_conditional_losses
&X"call_and_return_conditional_losses"
_generic_user_object
:	 (2	Adam/iter
: (2Adam/beta_1
: (2Adam/beta_2
: (2
Adam/decay
: (2Adam/learning_rate
 "
trackable_list_wrapper
5
0
1
2"
trackable_list_wrapper
.
90
:1"
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
N
	;total
	<count
=	variables
>	keras_api"
_tf_keras_metric
^
	?total
	@count
A
_fn_kwargs
B	variables
C	keras_api"
_tf_keras_metric
:  (2total
:  (2count
.
;0
<1"
trackable_list_wrapper
-
=	variables"
_generic_user_object
:  (2total
:  (2count
 "
trackable_dict_wrapper
.
?0
@1"
trackable_list_wrapper
-
B	variables"
_generic_user_object
*:(
??2Adam/inputlayer/kernel/m
#:!?2Adam/inputlayer/bias/m
*:(	?82Adam/hiddenlayer/kernel/m
#:!82Adam/hiddenlayer/bias/m
):'82Adam/outputlayer/kernel/m
#:!2Adam/outputlayer/bias/m
*:(
??2Adam/inputlayer/kernel/v
#:!?2Adam/inputlayer/bias/v
*:(	?82Adam/hiddenlayer/kernel/v
#:!82Adam/hiddenlayer/bias/v
):'82Adam/outputlayer/kernel/v
#:!2Adam/outputlayer/bias/v
?2?
+__inference_sequential_layer_call_fn_913772
+__inference_sequential_layer_call_fn_913952
+__inference_sequential_layer_call_fn_913969
+__inference_sequential_layer_call_fn_913872?
???
FullArgSpec1
args)?&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults?
p 

 

kwonlyargs? 
kwonlydefaults? 
annotations? *
 
?2?
F__inference_sequential_layer_call_and_return_conditional_losses_913993
F__inference_sequential_layer_call_and_return_conditional_losses_914017
F__inference_sequential_layer_call_and_return_conditional_losses_913891
F__inference_sequential_layer_call_and_return_conditional_losses_913910?
???
FullArgSpec1
args)?&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults?
p 

 

kwonlyargs? 
kwonlydefaults? 
annotations? *
 
?B?
!__inference__wrapped_model_913699inputlayer_input"?
???
FullArgSpec
args? 
varargsjargs
varkwjkwargs
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
+__inference_inputlayer_layer_call_fn_914026?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
F__inference_inputlayer_layer_call_and_return_conditional_losses_914036?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
,__inference_hiddenlayer_layer_call_fn_914045?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_914056?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
,__inference_outputlayer_layer_call_fn_914065?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
G__inference_outputlayer_layer_call_and_return_conditional_losses_914076?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?B?
$__inference_signature_wrapper_913935inputlayer_input"?
???
FullArgSpec
args? 
varargs
 
varkwjkwargs
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 ?
!__inference__wrapped_model_913699m1?.
'?$
"?
inputlayer_input	?
? "0?-
+
outputlayer?
outputlayer?
G__inference_hiddenlayer_layer_call_and_return_conditional_losses_914056K'?$
?
?
inputs	?
? "?
?
08
? n
,__inference_hiddenlayer_layer_call_fn_914045>'?$
?
?
inputs	?
? "?8?
F__inference_inputlayer_layer_call_and_return_conditional_losses_914036L'?$
?
?
inputs	?
? "?
?
0	?
? n
+__inference_inputlayer_layer_call_fn_914026?'?$
?
?
inputs	?
? "?	??
G__inference_outputlayer_layer_call_and_return_conditional_losses_914076J&?#
?
?
inputs8
? "?
?
0
? m
,__inference_outputlayer_layer_call_fn_914065=&?#
?
?
inputs8
? "??
F__inference_sequential_layer_call_and_return_conditional_losses_913891a9?6
/?,
"?
inputlayer_input	?
p 

 
? "?
?
0
? ?
F__inference_sequential_layer_call_and_return_conditional_losses_913910a9?6
/?,
"?
inputlayer_input	?
p

 
? "?
?
0
? ?
F__inference_sequential_layer_call_and_return_conditional_losses_913993W/?,
%?"
?
inputs	?
p 

 
? "?
?
0
? ?
F__inference_sequential_layer_call_and_return_conditional_losses_914017W/?,
%?"
?
inputs	?
p

 
? "?
?
0
? ?
+__inference_sequential_layer_call_fn_913772T9?6
/?,
"?
inputlayer_input	?
p 

 
? "??
+__inference_sequential_layer_call_fn_913872T9?6
/?,
"?
inputlayer_input	?
p

 
? "?y
+__inference_sequential_layer_call_fn_913952J/?,
%?"
?
inputs	?
p 

 
? "?y
+__inference_sequential_layer_call_fn_913969J/?,
%?"
?
inputs	?
p

 
? "??
$__inference_signature_wrapper_913935?E?B
? 
;?8
6
inputlayer_input"?
inputlayer_input	?"0?-
+
outputlayer?
outputlayer