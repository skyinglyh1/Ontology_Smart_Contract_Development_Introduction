## 本体智能合约简介

#### 什么是智能合约

本体智能合约是一个集多功能、轻量级、高可用、可并发、多语言、跨合约、跨虚拟机等于一体的完备体系。本体智能合约支持多种主流开发语言，如 C#, Python 等，开发者不需要学习新的语言即可很方便的开发本体智能合约，未来将支持更多主流开发语言，包括：Java, C++, Rust, Go, JavaScript 等。

本体智能合约具有确定性、高性能、扩展性的特性，包括两大模块：交互服务和虚拟机。交互服务提供了虚拟机和区块链账本之间的交互。虚拟机提供了智能合约的运行环境。交互服务包括原生服务和 NEO 虚拟机服务。原生服务提供了基础链上特殊智能合约的实现，这种合约能被快速方便地使用。NEO 虚拟机服务提供了外部访问 NEO 虚拟机的 API, 它能增强智能合约的调用功能。

了解[更多](https://github.com/ontio/ontology-smartcontract)有关本体智能合约的信息。

#### 合约类型

本体智能合约有两种类型：Native 合约和 NeoVm 合约。Native 合约是在本体底层直接编写的合约，不需要像部署普通合约那样编写合约代码，具有很高的执行效率，是对普通合约的极大优化，通用的服务包括：Oracle，DID 和权限管理，数据交易所都将采用 Native 合约实现。NeoVm 合约是采用 NeoVm 虚拟机运行的合约，需要编写相应的合约代码，现支持的语言包含：Java，C#，Python，NeoVm 本身具有轻量级、可扩展、高性能的特性，通过结合 Interop Service 层能很好的打通虚拟机与账本层间的交互。


## 合约快速入门

#### 合约开发

- [SmartX](https://smartx.ont.io/#/)是一种在线合约开发、编译、布署，[这里](https://ontio.github.io/documentation/SmartX_Tutorial_en.html)是SmartX使用教程。
- [VS Code 插件](提供教程链接地址)
- [neo-boa](https://github.com/ontio/neo-boa) / [ontology](https://github.com/ontio/ontology-python-compiler)

#### 合约编译
对于C#开发的本体智能合约，这里是一些[API接口](https://github.com/ontio/ontology-smartcontract/blob/master/smart-contract-tutorial/Smart_Contract_%20API.md)。

对于python开发的本体智能合约，有两个版本的编译器。
- 编译器1.0 [neo-boa](https://github.com/ontio/neo-boa) 
- 编译器2.0 [ontology](https://github.com/ontio/ontology-python-compiler)

同时我们也给出来[编译器1.0 API接口文档](https://github.com/ontio/neo-boa/blob/master/Ontology_smart_contract_API_for_Python.md)与[编译器2.0API接口文档](https://github.com/ontio/ontology-python-compiler/blob/master/Ontology_smart_contract_API_for_Python.md)。

此外，这里有社区提供的一些简单且基础的Python版Ontology[智能合约模版](https://github.com/ONT-Avocados/python-template)与[合约防攻击解决方案](https://github.com/tonyclarking/contract-security)

我们当前推荐您开发Python版智能合约，因为Python语言深受广大开发者的喜爱，且当前阶段我们也在大力不断完善的工作重心。

合约编译方式：
- 可在SmartX上编译合约
- 可通过VS Code插件编译合约
- 可通过编译器编译合约
- 可通过您喜爱且熟悉的任意一种SDK编译合约

#### 合约布署
- 可以通过SmartX,连上cyano wallet(ONT的cyano wallet是一种chrome plugin，可将合约布署到本地网、或测试网、或主网。
- 可通过VS Code插件布署合约
- 通过SDK，调用相关函数(给出例子)来编译布署合约
- 也可在启动节点的情况下，可以通过[Cli](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide_CN.md#51-%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6%E9%83%A8%E7%BD%B2)，将合约布署到本地、测试网或主网。

#### 合约调用
- 可通过SmartX调用(包括执行或预执行)合约
- 可通过SDK，调用合约内函数，详请参考相关SDK内关于OEP4, OEP5的例子。
- 可通过[Cli](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide_CN.md#52-%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6%E6%89%A7%E8%A1%8C)，调用合约内函数进行测试。
- 也可通过Punica，可测试合约功能。

1. 构建交易

2. 发送交易

3. 获取交易结果


###### 执行与预执行的关系
执行的含义是指在调用合约内函数时，改变合约内状态，该操作会以ONG作燃料，消耗对应的手续费。理论上，函数体内应该把改动状态的关键信息以事件(Notify)的形式广播出来。

预执行的含义是指通过合约接口去查询链上合约内信息，该操作不会改变合约状态，不会消耗手续费。

###### GAS 费用模型
GAS Limit
Gas limit 是在执行智能合约的 opcode 过程中计步时使用，理论上智能合约越复杂，需要的 GAS limit 数量越高，Ontology 交易设定最低的 GAS limit 数量是 20000。

GAS Price
GAS price 是给执行 opcode 定价，GAS price 越高，共识节点会优先打包该笔交易。

Transaction Fee
交易费用是 GAS limit 和 GAS price 的乘积，实际的交易费用分以下三种情形：

执行 opcode 步数等于 GAS limit

Transaction Fee = GAS Price * GAS limit

执行 opcode 步数大于 GAS limit

Transaction Fee = GAS Price * GAS limit

交易失败，但 GAS 不会退还。

执行 opcode 步数小于 GAS limit Transaction Fee = GAS Price * (opcode实际消耗)

多余的 GAS 会退还，但最低消费是 20000。

注意：

所有 ONT, ONG 的转账 GAS limit 消费固定都是20000。

#### 合约常见问题及解答
- 1. Generate ONG from nowhere in local testmode.
```
ontology.exe asset transfer --from=1 --to=1 --amount=100000000 --asset=ont


ontology.exe asset unboundong 1


ontology.exe asset withdrawong 1


```
- 2. What does `CheckWitness` actually do?
```

CheckWitness有两个功能

1. 验证当前的函数调用者是不是from,若是（验证签名），则验证通过

2. 检查当前函数调用者是不是一个合约A，若是合约A，且是从合约A发起的去执行函数，则验证通过(验证from是不是callingScriptHash)
