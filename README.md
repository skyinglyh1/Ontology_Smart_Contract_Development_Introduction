## 
[简介](Introduction_CN.md) | [Introduction](Introduction_EN.md)


[smartx编译布署合约指导](https://github.com/skyinglyh1/Ontology_Smart_Contract_Development_Introduction/blob/master/Compile_Deploy_Vis_SmartX.md)

1. Generate ONG from nowhere in local testmode.
```
ontology.exe asset transfer --from=1 --to=1 --amount=100000000 --asset=ont


ontology.exe asset unboundong 1


ontology.exe asset withdrawong 1

```

2. What does `CheckWitness` actually do?
```
CheckWitness有两个功能

1. 验证当前的函数调用者是不是from,若是（验证签名），则验证通过.

2. 检查当前函数调用者是不是一个合约A，若是合约A，且是从合约A发起的去执行函数，则验证通过(验证from是不是callingScriptHash)

```




3. How to get the invoker like ```msg.sender``` in Ethereum smart contract?

```
Ontology smart contract does not have built-in invoker like msg.sender, you have to pass in the invoker to the method when you invoking the contract method.
Then how can we verify that the passed in account is actually the real invoker. Here we have to use ```CheckWitness``` method within contract to verfiy the transaction has been signed by the invoker.
This leads to the previous question ``` What does `CheckWitness` actually do? ```.
```

