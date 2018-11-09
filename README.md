1. [Ontology Smart Contract](https://github.com/ontio/ontology-smartcontract) 了解。

2. [Ontology 本地环境搭建与节点启动](https://github.com/ontio/ontology)

3. [Ontology Cli使用教程](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide_CN.md)

4. SmartX是一种在线合约开发、编译、布署[网站](https://smartx.ont.io/)。[这里](https://ontio.github.io/documentation/SmartX_Tutorial_en.html)是SmartX使用教程。

5. 一些简单基础的Python版Ontology[智能合约模版](https://github.com/ONT-Avocados/python-template)。

6. Pytho合约的本地编译器[neo-boa](https://github.com/ontio/neo-boa)；即将替代neo-boa的[Python编译器](https://github.com/ontio/ontology-python-compiler)。


感兴趣且有时间的话，也可以看一下我们的Dapp开发框架[punica-python](https://github.com/ontio-community/punica-python), 类型于Ethereum的truffle工具。

Notes:

合约开发：
```
1. 智能合约中使用的函数可以在[neo-boa](https://github.com/ontio/neo-boa)找到引用接口。

2. 可以使用的函数也可以在SmartX上面得到指示。
```

合约编译：
```
1. 通过SmartX

2. 本地通过neo-boa编译
```

合约布署
```
1. 可以通过SmartX,连上cyano wallet(ONT的cyano wallet是一种chrome plugin，可以用Ethereum的MetaMask来类比)指定网络(与IP地址)，可将合约布署到本地网、或测试网、或主网。

2. 在启动节点的情况下，可以通过Cli，将合约布署到本地、测试网或主网。
```

合约测试：
```
1. SmartX上可以进行运行、调试合约内的函数。

2. 可以通过Cli运行、调试合约函数。

3. 我们也有Python测试框架，可测试合约功能，建议：在上述内容有了大致了解之后，再去接触测试框架。
```