## 
[简介](Introduction_CN.md) | [Introduction](Introduction_EN.md)


1. Generate ONG from nowhere in local testmode.
```
ontology.exe asset transfer --from=1 --to=1 --amount=100000000 --asset=ont


ontology.exe asset unboundong 1


ontology.exe asset withdrawong 1

```

2. What does `CheckWitness` actually do?
```
CheckWitness有两个功能

1. 验证当前的函数调用者是不是from,若是（验证签名），则验证通过

2. 检查当前函数调用者是不是一个合约A，若是合约A，且是从合约A发起的去执行函数，则验证通过(验证from是不是callingScriptHash)

```




