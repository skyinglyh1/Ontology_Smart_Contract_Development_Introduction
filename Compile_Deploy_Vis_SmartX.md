此文档可作为合约的编译，布署文档。

a. 将合约中的```OWNER```改为布署者的帐号(注：以大A开头的Base58地址)。

b. 打开chrome浏览器，安装[cyano wallet](https://chrome.google.com/webstore/detail/cyano-wallet/dkdedlpgdmmkkfjabffeganieamfklkm) 一种类似于MetaMask的钱包插件。

c. [smartx](https://smartx.ont.io/#/)为Ontology提供的官方编译、调试、布署、调用网站。
    注册帐号并登录，点击创建项目，选择Python, 命名项目，将更改OWNER地址后的合约代码粘贴过去。
    
d. 编译合约

e. 打开cyano wallet 选择测试网或主网(注意：接下来会影响合约被布署到哪个网络)，确保布署帐户内至少有11个ONG，布署帐户可以跟OWNER不是同一个帐户。

f. 布署合约，布署合约上链后，需要执行```init```函数，初始化合约, 该过程会生成所有代币，并将其转入到```OWNER```帐户中。
